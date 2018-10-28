#!/usr/bin/env python3
# -*- coding: utf-8 -*-

''' create a file
example:
python Scripts/new.py -f hello/readme.md  # even folder hello not exists
'''

import argparse
import pathlib

heads = {'.py':'#!/usr/bin/env python3'}

parser = argparse.ArgumentParser(description='Create a file')
parser.add_argument('-f', action='store', dest='filename', default='script.txt', metavar='FILE', type=pathlib.Path)
parser.add_argument('-s', nargs='+', dest='content', action='store', default='', metavar='CONTENT')
parser.add_argument('-l', action='store', dest='head', metavar='HEAD')

args = parser.parse_args()

p = args.filename
if args.head:
    s = '%s\n\n%s'%(args.head, '\n'.join(args.content))
else:
    head = heads.get(p.suffix, '')
    s = '%s\n\n%s'%(head, '\n'.join(args.content))
try:
    p.touch()
except FileNotFoundError:
    p.parent.mkdir(parents=True)
    p.touch()
p.write_text(s)