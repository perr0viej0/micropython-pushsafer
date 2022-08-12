#!/usr/bin/env python

from setuptools import setup

setup(
    name="micropython-pushsafer",
    version="1.0",
    description="Comprehensive bindings for the " "Pushsafer.com notification service",
    long_description=open("README.rst").read()
    + "\n"
    + open("AUTHORS.rst").read()
    + "\n"
    + open("CHANGES.rst").read(),
    url="https://github.com/perr0viej0/micropython-pushsafer",
    author="Alex Poser",
    author_email="alexposer@gmail.com",
    py_modules=["pushsafer"],
    #install_requires=["requests>=1.0"],
    use_2to3=True,
    license="GNU GPLv3",
)
