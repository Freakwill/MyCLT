# -*- coding: utf-8 -*-

''' delete files with .xxx extension name in a path
example:
$ python delext.py -e {.txt} -p {path} [-r {False}]
'''
import os
import pathlib
import argparse

_defaultPath = pathlib.Path('~/Teaching').expanduser()

parser = argparse.ArgumentParser(description='delete files with certain extension names in a path')
parser.add_argument('-e', dest='extname', nargs='+', action='store', metavar='EXT', default=[])
# parser.add_argument('-s', dest='save', nargs='+', action='store', metavar='SAVE', default=[])
parser.add_argument('-p', dest='pathname', action='store', default=_defaultPath, metavar='PATH', type=pathlib.Path)
parser.add_argument('-r', dest='recursive', type=bool, action='store_true', default=False)

args = parser.parse_args()

names = args.extname
path = args.pathname

def check(f):
    for name in names:
        if f.endswith('.'+name):
            return True
    return False

op = os.remove

base.search(path, op, check, args.recursive)
