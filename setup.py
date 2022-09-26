#!/usr/bin/env python

import pathlib
from setuptools import setup, find_packages


setup(
    name="svickova",
    version="0.1.0",
    author="Tomáš Mikula",
    author_email="mail@tomasmikula.cz",
    description="Simple menza.upol.cz bot for menu scrapping.",
    keywords="meal menza api bot",
    license="MIT license",
    url="https://github.com/mikulatomas/svickova",
    packages=find_packages(),
    install_requires=["python-dateutil"],
    entry_points={
        "console_scripts": [
            "svickova = svickova.cli:cli",
        ],
    },
    python_requires=">=3.10",
    long_description=pathlib.Path("README.md").read_text(encoding="utf-8"),
    long_description_content_type="text/markdown",
    classifiers=[
        "Development Status :: 3 - Alpha",
        "Intended Audience :: Developers",
        "License :: OSI Approved :: MIT License",
        "Natural Language :: English",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.7",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
        "Programming Language :: Python :: 3.10",
    ],
)
