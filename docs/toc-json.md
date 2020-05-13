# ToC in JSON

ToC in JSON format is basically same as the `toc` parameter of `fitz.Document.setToC` as [PyMuPDF docs](https://pymupdf.readthedocs.io/en/latest/document/#Document.setToC) stated. Simply rewriting the python sequence and dict into json array and object will do the trick.

However, `dest["to"]` accepts `fitz.Point` object, which cannot be serialized into or deserialized from json directly. Thus if you want to use `Point` object in toc, you have to write it as

```json
{"__type__": "Point", "x": 90.0, "y": 370.0}
```
