import fitz
import subprocess
import io
from contextlib import redirect_stdout, redirect_stderr
from textwrap import dedent


def test_show_pipe(shared_datadir):
    ToCPdfFilePath = str(shared_datadir / "Lorem Ipsum(with toc).pdf")
    pdfFilePath = str(shared_datadir / "Lorem Ipsum.pdf")
    res = subprocess.run(
        f'pdf-toc --show-toc json "{ToCPdfFilePath}" | pdf-toc -T json -m "{pdfFilePath}"',
        shell=True)
    assert res.returncode == 0
    assert res.stdout == None
    assert res.stderr == None

    ToCPdfFile = fitz.open(ToCPdfFilePath)
    pdfFile = fitz.open(pdfFilePath)
    assert ToCPdfFile.getToC() == pdfFile.getToC()
