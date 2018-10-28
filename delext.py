#!/usr/bin/env python3
# -*- coding: utf-8 -*-

''' delete files with .xxx extension name in a path
example:
$ python delext.py -e {.txt} -p {path} [-r {False}]
'''
import os
import pathlib
import argparse
import base

parser = argparse.ArgumentParser(description='delete files with certain extension names in a path', parents=[base.searchFiles])
parser.add_argument('-e', dest='extname', nargs='+', action='store', metavar='EXT', default=[])

args = parser.parse_args()

names = args.extname
path = args.path

def check(f):
    for name in names:
        if f.endswith('.'+name):
            return True
    return False

base.search(path, os.remove, check, args.recursive)
