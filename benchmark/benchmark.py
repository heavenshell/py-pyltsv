#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
    pyltsv.benchmark.benchmark
    ~~~~~~~~~~~~~~~~~~~~~~~~~~

    Benchmark pure Python implementation and C Extension implementation.


    :copyright: (c) 2013 Shinya Ohyanagi, All rights reserved.
    :license: BSD, see LICENSE for more details.
"""
import os
import timeit
import ltsv
import pyltsv

file_path = os.path.join(os.path.dirname(os.path.abspath(__file__)),
                         'example_log.ltsv')


def bench():
    ltsv.parse_file(file_path)


def bench_c_ext():
    pyltsv.parse_file(file_path)


if __name__ == '__main__':
    t = timeit.Timer(stmt='bench()', setup='from __main__ import bench')
    ret1 = t.timeit(number=100) * 100 * 100

    t = timeit.Timer(stmt='bench_c_ext()',
                     setup='from __main__ import bench_c_ext')

    ret2 = t.timeit(number=100) * 100 * 100

    print('Pure Python: {0}'.format(ret1))
    print('C Extension: {0}'.format(ret2))
