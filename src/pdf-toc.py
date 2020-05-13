#!/usr/bin/env python3

import re
import fitz
import argparse
import sys
from pathlib import Path
from typing import *
from typing import Pattern, Match, Callable
import json

parserT = Dict[Union[Pattern, str], Callable[..., Any]]

scriptFolder = Path(__file__).parent


class TocJsonEncoder(json.JSONEncoder):
    def default(self, obj):
        if isinstance(obj, fitz.Point):
            return {
                '__type__': 'Point',
                'x': obj.x,
                'y': obj.y
            }
        return super(self).default(obj)


def TocJsonHook(dct):
    if isinstance(dct, dict) and dct.get('__type__', '') == 'Point':
        return fitz.Point(dct['x'], dct['y'])
    return dct


def printErr(*args, **kwargs):
    print(*args, file=sys.stderr, **kwargs)


class NoMatchException(Exception):
    """raised when no match in a parsed item"""

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)


class Attach(object):

    def __init__(self, func: Callable[[Match], Any]):
        self.func = func

    def __call__(self, match: Match):
        return self.func(match)


class Parser(object):

    def __init__(self, parserData: parserT):
        self.parserData: List[Tuple[Pattern, Callable[..., Any]]] = [
            (re.compile(p), h) for p, h in parserData.items()
        ]

    def parse(self, code: str):
        for p, h in self.parserData:
            res = re.match(p, code)
            if res is not None:
                if isinstance(h, Attach):
                    return h(res)
                else:
                    return h(*res.groups())
        else:
            raise NoMatchException(f"invalid command: '{code}'")

    __call__ = parse


class TocParser(Parser):

    def __init__(self):
        super().__init__({
            r'^\s*$': self.ignore,  # empty line
            r'^>>>>\s*(.+?)\s*$': Parser({  # commands
                r'#.+': self.ignore,  # comments
                r'([+-]\s*\d+)': self.changeOffset,
                r'offset\s*=\s*(\d+)': self.setOffset,
                r'indent\s*=\s*(\d+)': self.setIndent
            }),
            r'^( *)(.+) (\d+)\s*$': self.newTerm,
        })
        self.offset: int = 0
        self.indent: int = 4

    def ignore(self, *args):
        pass

    def changeOffset(self, newOffset):
        self.offset += int(newOffset)

    def setOffset(self, newOffset):
        self.offset = int(newOffset)

    def setIndent(self, newIndent):
        self.indent = int(newIndent)

    def newTerm(self, indent, title, page):
        page = int(page)
        return [1 + len(indent) // self.indent, title, page + self.offset, 0]


if __name__ == "__main__":
    argsParser = argparse.ArgumentParser(description='pdf ToC modifier.')
    argsParser.add_argument('source',
                            help='source pdf file directory')
    argsParser.add_argument('--show-toc', choices=['json', 'toc'], dest='show',
                            help='print the toc info of the source file and exit')
    argsParser.add_argument('-t', '--toc',
                            help='toc info used to embed in the result file')
    argsParser.add_argument('-d', '--dest',
                            help='destination directory for result file')
    argsParser.add_argument('-f', '--force', action='store_true',
                            help='overwrite dist file if it exist')
    argsParser.add_argument('-m', '--modify', action='store_true', dest='mod',
                            help='modified the original file instead of create a new one')
    args = argsParser.parse_args()

    # parse source path
    sourcePath = Path(args.source)
    if not sourcePath.exists():
        printErr('source does not exist')
        sys.exit(1)
    if not sourcePath.is_file():
        printErr('source is not a file')
        sys.exit(1)

    # source file
    source = fitz.open(str(sourcePath))

    # show file toc and exit
    if args.show is not None:
        toc = source.getToC(False)
        if args.show == 'json':
            print('[')
            print(',\n'.join(
                [f"    {json.dumps(entry, cls=TocJsonEncoder, ensure_ascii=False)}" for entry in toc]))
            print(']')
        else:
            for lvl, title, page, dest in toc:
                print(f'{"    " * (lvl - 1)}{title} {page}')
        sys.exit(0)

    # parse toc path
    if args.toc is None:
        printErr('"--toc" is required if you want to modify toc info')
        sys.exit(1)
    tocPath = Path(args.toc)
    if not tocPath.exists():
        printErr('toc does not exist')
        sys.exit(1)
    if not tocPath.is_file():
        printErr('toc is not a file')
        sys.exit(1)

    destPath = Path(args.dest) if args.dest is not None else (
        sourcePath.parent / f'{sourcePath.stem}_res.pdf')
    if destPath.exists():
        if not destPath.is_file():
            printErr('dest directory is not a file')
            sys.exit(1)
        if not args.force:
            printErr(
                'dest file exist, abort. try "-f" if you need to overwrite it.')
            sys.exit(1)

    # source = fitz.open()
    parser = TocParser()
    toc = []
    with tocPath.open('r', encoding='UTF-8') as file:
        l: str
        for l in file:
            term = parser(str(l))
            if term is not None:
                toc.append(term)
    source.setToC(toc)
    if args.mod:
        source.saveIncr()
    else:
        source.save(str(destPath))
