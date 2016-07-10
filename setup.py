#!/usr/bin/env python
# -*- coding: utf-8 -*-

try:
    from setuptools import setup
except ImportError:
    from distutils.core import setup

setup(
    name='pjv',
    version='0.8.2',
    description='JSON Python Validator',
    scripts=['scripts/pjv'],
    long_description=open('README.rst').read(),
    author='Viet Hung Nguyen',
    author_email='hvn@familug.org',
    url='https://github.com/hvnsweeting/pjv',
    license='MIT',
    classifiers=[
        'Environment :: Console',
        'Topic :: Terminals :: Terminal Emulators/X Terminals',
    ],
)
