# -*- coding: utf-8 -*-
"""
    pyltsv.tests.test_lstv
    ~~~~~~~~~~~~~~~~~~~~~~

    Tests for pyltsv.


    :copyright: (c) 2013 Shinya Ohyanagi, All rights reserved.
    :license: BSD, see LICENSE for more details.
"""
import os
from unittest import TestCase
from pyltsv import parse_file, parse_line


class TestLtsv(TestCase):
    def test_parse_file(self):
        """ parse_file() should parse lstv file to dict."""
        root_path = os.path.dirname(os.path.abspath(__file__))
        test_file_path = os.path.join(root_path, 'test.ltsv')
        ret = parse_file(test_file_path)
        self.assertEqual(ret[0]['hoge'], 'foo')
        self.assertEqual(ret[0]['bar'], 'baz')
        self.assertEqual(ret[1]['perl'], '5.17.8')
        self.assertEqual(ret[2]['tennpura'].decode('utf-8'), u'天ぷら')

    def test_no_file(self):
        """ parse_file() should raise IOError if file not exits. """
        try:
            parse_file('nofile.ltsv')
        except IOError as e:
            self.assertEqual(e.message, 'LTSV file not found.')

    def test_parse_line(self):
        """ parse_file() should parse lstv line to dict."""
        line = "hoge:foo\tbar:baz\ttime:20:30:58\n"
        ret = parse_line(line)
        self.assertEqual(ret['hoge'], 'foo')
        self.assertEqual(ret['bar'], 'baz')
        self.assertEqual(ret['time'], '20:30:58')

    def test_parse_line_duplicate_key(self):
        """ Override value if label already exists in same line. """
        line = "hoge:foo\tbar:baz\ttime:20:30:58\thoge:bar\n"
        ret = parse_line(line)
        self.assertEqual(ret['hoge'], 'bar')
        self.assertEqual(ret['bar'], 'baz')
        self.assertEqual(ret['time'], '20:30:58')
