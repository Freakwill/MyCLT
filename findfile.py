# -*- coding: utf-8 -*-

''' find a file with a fuzzy name (pattern) or a string
'''
import os
import os.path
import argparse
import re

import base

parser = argparse.ArgumentParser(description='find a file with a fuzzy name')
parser.add_argument('-e', dest='extname', nargs='+', action='store', metavar='EXT', default=[])
parser.add_argument('-p', dest='pathname', action='store', default=base.defaultPath, metavar='PATH')
parser.add_argument('-s', dest='string', action='store', metavar='STRING')
parser.add_argument('-x', dest='regex', action='store', metavar='REGEX', type=re.compile)
parser.add_argument('-r', dest='recursive', action='store_true', default=True)

args = parser.parse_args()

exts = args.extname
string = args.string
rx = args.regex


def check(f):
    if string:
        if string not in f:
            return False
    if rx:
        if not rx.match(f):
            return False
    if exts == []:
        return True
    else:
        for ext in exts:
            if f.endswith('.'+ext):
                return True
        return False


base.search(args.pathname, op=print, check=check, recursive=args.recursive)
