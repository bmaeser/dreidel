#!/usr/bin/env python
# -*- coding: utf-8 -*-

from distutils.core import setup

packages = [
    'dreidel'
]

setup(
    name='dreidel',
    version="1.0.3",
    author='Bernhard Maeser',
    author_email='bernhard.maeser@gmail.com',
    url='https://github.com/bmaeser/dreidel',
    scripts=['dreidel/dreidel.py'],
    license="MIT",
    description="A python replacement for logrotate",
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