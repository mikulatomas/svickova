#!/usr/bin/env python

from setuptools import setup, find_packages

setup(
    name="svickova",
    packages=find_packages(),
    entry_points={
        "console_scripts": [
            "svickova = svickova.cli:cli",
        ],
    },
    install_requires=["selenium"]
)
