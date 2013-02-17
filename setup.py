#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
    pyltsv
    ~~~~~~

    Dead simple LTSV parser written in C Extension.


    :copyright: (c) 2013 Shinya Ohyanagi, All rights reserved.
    :license: BSD, see LICENSE for more details.
"""
import os
from setuptools import Extension, setup, find_packages

requires = []
try:
    import argparse
except:
    requires.append('argparse')


module = Extension('pyltsv.pyltsv',
    sources=['pyltsv/pyltsv.c'],
    #libraries=['profiler'],
    #define_macros=[('DEVELOP', None)],
)

description = file(os.path.join(os.path.dirname(__file__), 'README.rst')).read()
setup(
    name='pyltsv',
    version='0.1',
    description='Dead simple LTSV parser written in C Extension.',
    long_description=description,
    install_requires=requires,
    packages=find_packages(exclude=['tests']),
    package_dir={'': '.'},
    test_suite='tests',
    license='BSD',
    ext_modules=[module],
    platforms='Linux,Darwin',
    classifiers=[
        'Development Status :: 4 - Beta',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: BSD License',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Topic :: Text Processing'
    ]
)
