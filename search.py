# -*- coding: utf-8 -*-

'''
Search Engin for files
'''
import os
import argparse
import re
import pathlib

import base

parser = argparse.ArgumentParser(description='find a file or files with the names(regex) and strings in them.', parents=[base.searchFiles])
parser.add_argument('-s', dest='string', action='store', metavar='STRING', help='a string in wanted files')
parser.set_defaults(recursive=True)

args = parser.parse_args()

path = args.path
string = args.string

def check(f):
    if args.filename is None or args.filename.match(f.name):
        return True
    else:
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
