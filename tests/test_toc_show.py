import re
from textwrap import dedent


def test_show_toc(script_runner, shared_datadir):
    ret = script_runner.run('pdf-toc',
                            "--show-toc", "toc",
                            str(shared_datadir / "Lorem Ipsum(with toc).pdf"))
    assert ret.success
    assert ret.stdout == dedent("""\
        Lorem Ipsum 1
            Preface 2
            Chapter 1 – Lorem ipsum dolor sit amet. 4
                Section 1 – Lorem ipsum dolor. 4
                Section 2 – Donec augue nulla 5
                Section 3 – Nullam placerat 5
            Chapter 2 – Cras sit amet 7
                Section 1 – Aliquam eleifend 7
                Section 2 – Ut vestibulum mauris ornare 8
            Chapter 3 – Enim vitae 9
                Section 1 – Mauris ullamcorper 9
                Section 2 – Phasellus pellentesque 10
                Section 3 – Sodales, Vivamus, Aliquam 11
            Chapter 4 – Fusce 12
                Section 1 – Fusce dictum 12
                Section 2 – Fusce egestas 13
            Chapter 5 – Aenean rhoncus 13
    """)
    assert ret.stderr == ''


def test_show_toc_json(script_runner, shared_datadir):
    ret = script_runner.run('pdf-toc',
                            "--show-toc", "json",
                            str(shared_datadir / "Lorem Ipsum(with toc).pdf"))
    assert ret.success
    assert ret.stdout == dedent("""\
        [
            [1, "Lorem Ipsum", 1, {"kind": 1, "xref": 43, "page": 0, "to": {"__type__": "Point", "x": 233.0, "y": 389.0}, "zoom": 0.0, "collapse": false}],
            [2, "Preface", 2, {"kind": 1, "xref": 45, "page": 1, "to": {"__type__": "Point", "x": 90.0, "y": 89.0}, "zoom": 0.0}],
            [2, "Chapter 1 – Lorem ipsum dolor sit amet.", 4, {"kind": 1, "xref": 60, "page": 3, "to": {"__type__": "Point", "x": 90.0, "y": 105.0}, "zoom": 0.0, "collapse": false}],
            [3, "Section 1 – Lorem ipsum dolor.", 4, {"kind": 1, "xref": 62, "page": 3, "to": {"__type__": "Point", "x": 90.0, "y": 256.0}, "zoom": 0.0}],
            [3, "Section 2 – Donec augue nulla", 5, {"kind": 1, "xref": 65, "page": 4, "to": {"__type__": "Point", "x": 90.0, "y": 152.0}, "zoom": 0.0}],
            [3, "Section 3 – Nullam placerat", 5, {"kind": 1, "xref": 63, "page": 4, "to": {"__type__": "Point", "x": 90.0, "y": 443.0}, "zoom": 0.0}],
            [2, "Chapter 2 – Cras sit amet", 7, {"kind": 1, "xref": 56, "page": 6, "to": {"__type__": "Point", "x": 90.0, "y": 76.0}, "zoom": 0.0, "collapse": false}],
            [3, "Section 1 – Aliquam eleifend", 7, {"kind": 1, "xref": 58, "page": 6, "to": {"__type__": "Point", "x": 90.0, "y": 352.0}, "zoom": 0.0}],
            [3, "Section 2 – Ut vestibulum mauris ornare", 8, {"kind": 1, "xref": 59, "page": 7, "to": {"__type__": "Point", "x": 90.0, "y": 557.0}, "zoom": 0.0}],
            [2, "Chapter 3 – Enim vitae", 9, {"kind": 1, "xref": 52, "page": 8, "to": {"__type__": "Point", "x": 90.0, "y": 370.0}, "zoom": 0.0, "collapse": false}],
            [3, "Section 1 – Mauris ullamcorper", 9, {"kind": 1, "xref": 54, "page": 8, "to": {"__type__": "Point", "x": 90.0, "y": 552.0}, "zoom": 0.0}],
            [3, "Section 2 – Phasellus pellentesque", 10, {"kind": 1, "xref": 71, "page": 9, "to": {"__type__": "Point", "x": 90.0, "y": 339.0}, "zoom": 0.0}],
            [3, "Section 3 – Sodales, Vivamus, Aliquam", 11, {"kind": 1, "xref": 55, "page": 10, "to": {"__type__": "Point", "x": 90.0, "y": 323.0}, "zoom": 0.0}],
            [2, "Chapter 4 – Fusce", 12, {"kind": 1, "xref": 48, "page": 11, "to": {"__type__": "Point", "x": 90.0, "y": 120.0}, "zoom": 0.0, "collapse": false}],
            [3, "Section 1 – Fusce dictum", 12, {"kind": 1, "xref": 50, "page": 11, "to": {"__type__": "Point", "x": 90.0, "y": 349.0}, "zoom": 0.0}],
            [3, "Section 2 – Fusce egestas", 13, {"kind": 1, "xref": 51, "page": 12, "to": {"__type__": "Point", "x": 90.0, "y": 167.0}, "zoom": 0.0}],
            [2, "Chapter 5 – Aenean rhoncus", 13, {"kind": 1, "xref": 46, "page": 12, "to": {"__type__": "Point", "x": 90.0, "y": 505.0}, "zoom": 0.0}]
        ]
    """)
    assert ret.stderr == ''
