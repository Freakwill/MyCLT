# -*- coding: utf-8 -*-

''' delete files with .xxx extension name in a path
example:
$ python delext.py -e {.txt} -p {path} [-r {False}]
'''
import os
import os.path
import argparse

_defaultPath = os.path.expanduser('~/Teaching')

parser = argparse.ArgumentParser(description='delete files with certain extension names in a path')
parser.add_argument('-e', dest='extname', nargs='+', action='store', metavar='EXT', default=[])
# parser.add_argument('-s', dest='save', nargs='+', action='store', metavar='SAVE', default=[])
parser.add_argument('-p', dest='pathname', action='store', default=_defaultPath, metavar='PATH')
parser.add_argument('-r', dest='recursive', type=bool, action='store', default=False)

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
