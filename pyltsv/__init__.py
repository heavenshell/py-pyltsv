# -*- coding: utf-8 -*-
"""
    pyltsv
    ~~~~~~

    Dead simple LTSV parser written in C Extension.


    :copyright: (c) 2013 Shinya Ohyanagi, All rights reserved.
    :license: BSD, see LICENSE for more details.
"""
import argparse
from pyltsv import parse_file, parse_line


__all__ = ['parse_file', 'parse_line']


def main():
    description = 'Dead simple LTSV parser written in C Extension'
    parser = argparse.ArgumentParser(description=description, add_help=False)
    parser.add_argument('-f', '--file')

    args = parser.parse_args()
    parse_file(args.file)


if __name__ == '__main__':
    main()
