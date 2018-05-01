# -*- coding: utf-8 -*-

''' delete files with .xxx extension name in a path
example:
$ python find.py -s {...} -e {txt} -p {path} [-r {False}]
'''
import os
import os.path
import argparse

import base

parser = argparse.ArgumentParser(description='find a string in files with certain extension names in a path')
parser.add_argument('-e', dest='extname', nargs='+', action='store', metavar='EXT', default=[])
# parser.add_argument('-s', dest='save', nargs='+', action='store', metavar='SAVE', default=[])
parser.add_argument('-p', dest='pathname', action='store', default=base.defaultPath, metavar='PATH')
parser.add_argument('-s', dest='string', action='store', metavar='STRING')
parser.add_argument('-r', dest='recursive', action='store_true', default=False)

args = parser.parse_args()

names = args.extname
path = args.pathname
string = args.string

def check(f):
    if names == []:
        return True
    else:
        for name in names:
            if f.endswith('.'+name):
                return True
        return False

def op(fname):
    # Do something when find the file.
    if string:
        try:
            with open(fname) as fo:
                lines = fo.readlines()
        except:
            import codecs
            with codecs.open(fname, encoding='gb2312') as fo:
                lines = fo.readlines()
        for k, line in enumerate(lines, 1):
                if string in line:
                    print(fname, '#line %d'%k)
    else:
        print(fname)


base.search(path, op, check, args.recursive)
