import setuptools
from src import __VERSION__

with open("README.md", "r", encoding='UTF-8') as fh:
    long_description = fh.read()

requirements = [
    'PyMuPDF'
]

setuptools.setup(
    name="pdf-toc",
    version=__VERSION__,
    author="HareInWeed",
    description="a pdf ToC CLI tool",
    long_description=long_description,
    long_description_content_type="text/markdown",
    install_requires=requirements,
    url="",
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    packages=setuptools.find_packages(
        exclude=("docs", "tests")
    ),
    entry_points={
        "console_scripts": [
            "pdf-toc=src.main:main",
        ],
    },
    zip_safe=False,
    python_requires=">=3.2",
)
