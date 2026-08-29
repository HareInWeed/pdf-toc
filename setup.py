import setuptools
from pathlib import Path

with open("README.md", "r", encoding='UTF-8') as fh:
    long_description = fh.read()

requirements = [
    'PyMuPDF >= 1.19'
]


def get_version():
    with (Path(__file__).parent / 'src' / 'pdf_toc' / 'version.py').open('r') as verInfo:
        for line in verInfo:
            if line.startswith('__VERSION__'):
                delim = '"' if '"' in line else "'"
                return line.split(delim)[1]
        else:
            raise RuntimeError("Unable to find version string.")


setuptools.setup(
    name="pdf-toc",
    version=get_version(),
    author="HareInWeed",
    description="a pdf ToC CLI tool",
    long_description=long_description,
    long_description_content_type="text/markdown",
    install_requires=requirements,
    author_email="zjnvv@163.com",
    url="https://github.com/HareInWeed/pdf-toc",
    project_urls={
        "Bug Tracker": "https://github.com/HareInWeed/pdf-toc/issues",
        "Documentation": "https://github.com/HareInWeed/pdf-toc",
        "Source Code": "https://github.com/HareInWeed/pdf-toc",
    },
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    package_dir={"": "src"},
    entry_points={
        "console_scripts": [
            "pdf-toc=pdf_toc.main:main",
        ],
    },
    zip_safe=False,
    python_requires=">=3.7",
)
