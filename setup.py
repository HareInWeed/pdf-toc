import setuptools

with open("README.md", "r", encoding='UTF-8') as fh:
    long_description = fh.read()

requirements = [
    'PyMuPDF'
]

setuptools.setup(
    name="pdf-toc",
    version="1.0.0",
    author="HareInWeed",
    description="a pdf ToC CLI tool",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="",
    install_requires=requirements,
    scripts=['src/pdf-toc.py'],
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    zip_safe=False,
    python_requires=">=3.5"
)
