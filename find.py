# -*- coding: utf-8 -*-

'''
example:
$ python find.py -s {...} -e {txt} -p {path} [-r {False}]
'''
import os
import os.path
import argparse

import base

parser = argparse.ArgumentParser(description='find a string in files with certain extension names in a path', parents=[base.searchFiles])
parser.add_argument('-e', dest='extname', nargs='+', action='store', metavar='EXT', default=[])
parser.add_argument('-s', dest='string', action='store', metavar='STRING')

args = parser.parse_args()

names = args.extname
path = args.path
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
    # Do something when finding the file.
    if string:
        try:
            with open(fname) as fo:
                lines = fo.readlines()
        except:
            try:
                import codecs
                with codecs.open(fname, encoding='gb2312') as fo:
                    lines = fo.readlines()
            except Exception as e:
                print('I just can not open %s\n'%fname, e)
                return
        if lines:
            if string in lines[0]:
                print(fname, '#line 1')
            if len(lines) > 1:
                for k, line in enumerate(lines[1:], 2):
                        if string in line:
                            print('--- #line %d'%k)
    else:
        print(fname)


base.search(path, op, check, args.recursive)
