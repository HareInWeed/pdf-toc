# ToC in JSON

ToC in JSON format is basically same as the `toc` parameter of `fitz.Document.set_toc` as [PyMuPDF docs](https://pymupdf.readthedocs.io/en/latest/document.html#Document.set_toc) stated. Simply rewriting the python sequence and dict into json array and object respectively will do the trick.

Check out an example in [Lorem Ipsum_toc.json](/tests/data/Lorem%20Ipsum_toc.json)

However, `dest["to"]` accepts `fitz.Point` object, which cannot be serialized into or deserialized from json directly. Thus if you want to use `Point` object in toc, you have to write it as

```json
{"__type__": "Point", "x": 90.0, "y": 370.0}
```
