import fitz
import re
from textwrap import dedent

expectedToc = [
    [1, "Lorem Ipsum", 1],
    [2, "Preface", 2],
    [2, "Table of Content", 3],
    [2, "Chapter 1 – Lorem ipsum dolor sit amet", 4],
    [3, "Section 1 – Lorem ipsum dolor", 4],
    [3, "Section 2 – Donec augue nulla", 5],
    [3, "Section 3 – Nullam placerat", 5],
    [2, "Chapter 2 – Cras sit amet", 7],
    [3, "Section 1 – Aliquam eleifend", 7],
    [3, "Section 2 – Ut vestibulum mauris ornare", 8],
    [2, "Chapter 3 – Enim vitae", 9],
    [3, "Section 1 – Mauris ullamcorper", 9],
    [3, "Section 2 – Phasellus pellentesque", 10],
    [3, "Section 3 – Sodales, Vivamus, Aliquam", 11],
    [2, "Chapter 4 – Fusce", 12],
    [3, "Section 1 – Fusce dictum", 12],
    [3, "Section 2 – Fusce egestas", 13],
    [2, "Chapter 5 – Aenean rhoncus", 13]
]

expectedJsonToc = [
    [1, "Lorem Ipsum", 1],
    [2, "Preface", 2],
    [2, "Chapter 1 – Lorem ipsum dolor sit amet.", 4],
    [3, "Section 1 – Lorem ipsum dolor.", 4],
    [3, "Section 2 – Donec augue nulla", 5],
    [3, "Section 3 – Nullam placerat", 5],
    [2, "Chapter 2 – Cras sit amet", 7],
    [3, "Section 1 – Aliquam eleifend", 7],
    [3, "Section 2 – Ut vestibulum mauris ornare", 8],
    [2, "Chapter 3 – Enim vitae", 9],
    [3, "Section 1 – Mauris ullamcorper", 9],
    [3, "Section 2 – Phasellus pellentesque", 10],
    [3, "Section 3 – Sodales, Vivamus, Aliquam", 11],
    [2, "Chapter 4 – Fusce", 12],
    [3, "Section 1 – Fusce dictum", 12],
    [3, "Section 2 – Fusce egestas", 13],
    [2, "Chapter 5 – Aenean rhoncus", 13]
]


def test_write_toc(script_runner, shared_datadir):
    ret = script_runner.run('pdf-toc',
                            "-t", str(shared_datadir / "Lorem Ipsum_toc.txt"),
                            str(shared_datadir / "Lorem Ipsum.pdf"))
    assert ret.success
    assert ret.stdout == ''
    assert ret.stderr == ''
    assert (shared_datadir / "Lorem Ipsum_res.pdf").exists()

    res = fitz.open(str(shared_datadir / "Lorem Ipsum_res.pdf"))
    resultToc = res.getToC()
    assert resultToc == [toc[:3] for toc in expectedToc]


def test_write_toc_with_dest(script_runner, shared_datadir):
    dest = "dest file.pdf"
    ret = script_runner.run('pdf-toc',
                            "-t", str(shared_datadir / "Lorem Ipsum_toc.txt"),
                            "-d", str(shared_datadir / dest),
                            str(shared_datadir / "Lorem Ipsum.pdf"))
    assert ret.success
    assert ret.stdout == ''
    assert ret.stderr == ''
    assert (shared_datadir / dest).exists()

    res = fitz.open(str(shared_datadir / dest))
    resultToc = res.getToC()
    res.close()
    assert resultToc == [toc[:3] for toc in expectedToc]

    # write again
    ret = script_runner.run('pdf-toc',
                            "-t", str(shared_datadir / "Lorem Ipsum_toc.txt"),
                            "-d", str(shared_datadir / dest),
                            str(shared_datadir / "Lorem Ipsum.pdf"))
    assert not ret.success
    assert ret.stdout == ''
    assert ret.stderr == 'dest file exist, abort. try "-f" if you need to overwrite it.\n'

    # write again forcefully
    ret = script_runner.run('pdf-toc',
                            '-f',
                            "-t", str(shared_datadir / "Lorem Ipsum_toc.txt"),
                            "-d", str(shared_datadir / dest),
                            str(shared_datadir / "Lorem Ipsum.pdf"))
    assert ret.success
    assert ret.stdout == ''
    assert ret.stderr == ''

    res = fitz.open(str(shared_datadir / dest))
    resultToc = res.getToC()
    res.close()
    assert resultToc == [toc[:3] for toc in expectedToc]


def test_write_toc_json(script_runner, shared_datadir):
    dest = "dest file.pdf"
    ret = script_runner.run('pdf-toc',
                            "-t", str(shared_datadir / "Lorem Ipsum_toc.json"),
                            "-d", str(shared_datadir / dest),
                            str(shared_datadir / "Lorem Ipsum.pdf"))
    assert ret.success
    assert ret.stdout == ''
    assert ret.stderr == ''
    assert (shared_datadir / dest).exists()

    res = fitz.open(str(shared_datadir / dest))
    resultToc = res.getToC()
    assert resultToc == [toc[:3] for toc in expectedJsonToc]
