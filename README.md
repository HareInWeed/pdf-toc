# PDF ToC

a CLI tool to easily extract / edit ToC(Table of Content, or bookmark) of pdf file

![demo](./docs/assets/demo.gif)

## Requirements

- python >= 3.6
- PyMuPDF

## Installation

install from pypi

```sh
pip install pdf-toc
```

install from the repo directly

```sh
pip install git+https://github.com/HareInWeed/pdf-toc.git@master#egg=pdf-toc
```

install a specific version

```sh
pip install git+https://github.com/HareInWeed/pdf-toc.git@v1.1.4#egg=pdf-toc
```

## Usage

```plaintext
usage: pdf-toc [-h] [--version] [--show-toc {json,toc}] [-t TOC] [-d DEST]
               [-T {json,toc}] [-f] [-m]
               source

pdf ToC modifier.

positional arguments:
  source                source pdf file directory

optional arguments:
  -h, --help            show this help message and exit
  --version             show program's version number and exit
  --show-toc {json,toc}
                        print the toc info of the source file and exit
  -t TOC, --toc TOC     toc info used to embed in the result file. leave it
                        empty to read toc from stdin
  -d DEST, --dest DEST  destination directory for result file
  -T {json,toc}, --type {json,toc}
                        specify format of ToC file. leave it empty to let the
                        tool determine the format, (from file suffix)
  -f, --force           overwrite dist file if it exist
  -m, --modify          modified the original file instead of create a new one
```

### Examples

show the toc of file.pdf in `toc` format

```sh
pdf-toc --show-toc toc file.pdf
```

Generate a new file with content of file.pdf and toc in toc.txt

```sh
pdf-toc -t toc.txt -d new-file.pdf file.pdf
```

Replace the toc of file.pdf with one in toc.txt

```sh
pdf-toc -m -t toc.txt file.pdf
```

### ToC file

Two types of toc file are supported

One is json, which mostly follow the specification of PyMuPDF, but in json format. See [PyMuPDF docs](https://pymupdf.readthedocs.io/en/latest/document.html#Document.set_toc) and [toc_json.md](/docs/toc-json.md) for detail

The other is a special data format, which provides ease of modification and additional functionalities. Check out [toc.md](/docs/toc.md) for detail

## Licence

MIT
