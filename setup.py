#!/usr/bin/env python
from ez_setup import use_setuptools
use_setuptools("0.7.0")

from setuptools import setup, find_packages

readme = open('README.rst').read()
history = open('CHANGES.rst').read().replace('.. :changelog:', '')

setup(
    name='timetravelpdb',
    version='0.1.0',
    author='Tom Limoncelli',
    author_email='tal@whatexit.org',
    maintainer='Thomas Grainger',
    maintainer_email = 'timetravelpdb@graingert.co.uk',
    keywords = 'time, travel, timetravel, pdb, debug',
    description = 'The Time Travel Python Debugger',
    long_description=readme + '\n\n' + history,
    url='https://github.com/graingert/timetravelpdb',
    package_dir={'': 'src'},
    packages=find_packages('src', exclude="tests"),
    zip_safe=True,
    include_package_data=False,
)
