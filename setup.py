#!/usr/bin/env python
# -*- coding: utf-8 -*-

from distutils.core import setup

packages = [
    'dreidel'
]

setup(
    name='dreidel',
    version="1.0.0",
    author='Bernhard Mäser',
    author_email='bernhard.maeser@gmail.com',
    url='http://bmaeser.io',
    scripts=['bin/dreidel.py'],
    packages = packages,
    classifiers=(
        'Development Status :: 4 - Beta',
        'Intended Audience :: System Administrators',
        'Topic :: System :: Archiving',
        'Topic :: System :: Archiving :: Backup',
        'Operating System :: POSIX',
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python',
        'Programming Language :: Python :: 2.5',
        'Programming Language :: Python :: 2.6',
        'Programming Language :: Python :: 2.7',
    ),
)