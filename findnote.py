# -*- coding: utf-8 -*-

''' delete files with .xxx extension name in a path
grammar:
$ python find.py -e {txt} -f {folder} [-r {True}]
example:
$ python find.py -e md tex
'''
import pathlib
import argparse
import codecs

import base

ROOT = pathlib.Path('~/Folders/General Note').expenduser()


parser = argparse.ArgumentParser(description='find a string in files with certain extension names in a path')
parser.add_argument('-e', dest='extname', nargs='+', action='store', metavar='EXT', default=['md','tex'])
parser.add_argument('-f', dest='folder', action='store', metavar='PATH')
parser.add_argument('-s', dest='string', action='store', metavar='STRING')
parser.add_argument('-r', dest='recursive', type=bool, action='store', default=True)

args = parser.parse_args()

names = args.extname
path = ROOT / args.folder if args.folder else ROOT
string = args.string


def condition(f):
    for name in names:
        if f.endswith('.'+name):
            return True
    return False

def op(fname):
    # Do something when find the file.
    try:
        with open(fname) as fo:
            lines = fo.readlines()
    except:
        with codecs.open(fname, encoding='gb2312') as fo:
            lines = fo.readlines()
    for k, line in enumerate(lines, 1):
        if string in line:
            print(fname, '#line %d'%k)

base.search(path, op, check, args.recursive)
