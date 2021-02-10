# setup.py
from setuptools import setup

# To use a consistent encoding
from io import open
from os import path

# The directory containing this file
HERE = path.abspath(path.dirname(__file__))

# Get the long description from the README file
with open(path.join(HERE, 'README.md'), encoding='utf-8-sig') as f:
    long_description = f.read()

setup(
    name="KSPModule",
    version="0.1.0",
    description="Library to parse KSP CFG files.",
    long_description_content_type="text/markdown",
    long_description=long_description,
    author="Gonzalo Romero",
    author_email="romero.gonzalo.h@gmail.com",
    license="MIT",
    classifiers=[
        "Intended Audience :: Developers",
        "License :: OSI Approved :: MIT License",
        "Programming Language :: Python",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
        "Operating System :: OS Independent"
    ],
    packages=["KSPModule"],
    include_package_data=True,
)
