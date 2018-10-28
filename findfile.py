#!/usr/bin/env python3
# -*- coding: utf-8 -*-

''' find a file with a fuzzy name (pattern) or a string
'''
import os
import argparse
import re

import base

parser = argparse.ArgumentParser(description='find a file with a fuzzy name', parents=[base.searchFiles])
parser.add_argument('-e', dest='extname', nargs='+', action='store', metavar='EXT', default=[])
parser.add_argument('-s', dest='string', action='store', metavar='STRING')
parser.set_defaults(recursive=True)

args = parser.parse_args()

exts = args.extname
string = args.string
rx = args.filename


def check(f):
    if string:
        if string not in f.name:
            return False
    if rx:
        if not rx.match(f.name):
            return False
    if exts == []:
        return True
    else:
        return f.suffix in exts


base.search(args.path, op=print, check=check, recursive=args.recursive)
