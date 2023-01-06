#!/usr/bin/env python3

from setuptools import setup
from english_words.version import NAME, DESCRIPTION, VERSION


# Parse readme to include in PyPI page
with open("README.md") as f:
    long_description = f.read()

setup(
    name=NAME,
    version=VERSION,
    description=DESCRIPTION.capitalize(),
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/mwiens91/english-words-py",
    author="Matt Wiens",
    author_email="mwiens91@gmail.com",
    license="MIT",
    classifiers=[
        "Development Status :: 5 - Production/Stable",
        "License :: OSI Approved :: MIT License",
        "Natural Language :: English",
        "Programming Language :: Python",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
        "Programming Language :: Python :: 3.10",
        "Programming Language :: Python :: 3 :: Only",
    ],
    packages=["english_words"],
    package_data={"english_words": ["data/*.pickle"]},
)
