#!/usr/bin/env python3

import os
from setuptools import setup, find_packages

import epoch

def read(fname):
    return open(os.path.join(os.path.dirname(__file__), fname)).read()

setup(
        name = 'pyepoch',
        version = epoch.__version__,
        author = 'Yonathan Klijnsma',
        author_email = 'admin@0x3a.com',
        url = 'https://github.com/0x3a/pyepoch',
        packages=find_packages(),
        include_package_data=True,
        description = 'A simple python-based command-line utility to convert (time|date)stamps to epoch and back.',
        long_description=read('README.md'),
        install_requires=[
            'python-dateutil',
        ],
        entry_points={
            'console_scripts': [
                'epoch=epoch:main',
            ],
        },
        zip_safe=False,
     )
