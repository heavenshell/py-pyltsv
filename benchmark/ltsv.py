# -*- coding: utf-8 -*-
"""
    pyltsv.benchmark.ltsv
    ~~~~~~~~~~~~~~~~~~~~~

    Python script implementation.


    :copyright: (c) 2013 Shinya Ohyanagi, All rights reserved.
    :license: BSD, see LICENSE for more details.
"""

def parse_line(string):
    line = string.decode('utf-8').rstrip()

    return dict([x.split(':', 1) for x in line.split("\t")])


def parse_file(file_name):
    with open(file_name, 'r') as f:
        lines = f.readlines()

        return [parse_line(line) for line in lines]
