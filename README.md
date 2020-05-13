# PDF ToC

a CLI tool to easily extract / edit ToC(Table of Content, or bookmark) of pdf file

![demo](./docs/assets/demo.gif)

## Requirements

- python 3
- PyMuPDF

## Installation

<!-- not published yet -->
<!-- install from pypi

```sh
pip install pdf-toc
``` -->

install from the repo directly

```sh
pip install git+https://github.com/HareInWeed/pdf-toc.git@master#egg=pdf-toc
```

## Usage

```plaintext
usage: pdf-toc.py [-h] [--show-toc {json,toc}] [-t TOC] [-d DEST] [-f] [-m]
                  source

pdf ToC modifier.

positional arguments:
  source                source pdf file directory

optional arguments:
  -h, --help            show this help message and exit
  --show-toc {json,toc}
                        print the toc info of the source file and exit
  -t TOC, --toc TOC     toc info used to embed in the result file
  -d DEST, --dest DEST  destination directory for result file
  -f, --force           overwrite dist file if it exist
  -m, --modify          modified the original file instead of create a new one
```

### Examples

show toc of file.pdf

```sh
pdf-toc.py --show-toc file.pdf
```

Generate a new file with content of file.pdf and toc in toc.txt

```sh
pdf-toc.py -t toc.txt -d new-file.pdf file.pdf
```

Replace the toc of file.pdf with one in toc.txt

```sh
pdf-toc.py -m -t toc.txt file.pdf
```

### ToC file

Two types of toc file are supported

One is json, which mostly follow the specification of PyMuPDF, but in json format. See [PyMuPDF docs](https://pymupdf.readthedocs.io/en/latest/document/#Document.setToC) and [toc_json.md](/docs/toc-json.md) for detail

The other is a special data format, which provides ease of modification and additional functionalities. Check out [toc.md](/docs/toc.md) for detail

## Licence

MIT
