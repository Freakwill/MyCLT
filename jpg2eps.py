#! /usr/bin/env python3
# -*- coding: utf-8 -*-

''' transform jpeg to eps
example:
$ python jpg2eps.py -f {hebb}
'''

import argparse
import pathlib

from PIL import Image


parser = argparse.ArgumentParser(description='transform jpeg to eps')
parser.add_argument('-f', action='store', dest='source', metavar='FROM', type=pathlib.Path)
parser.add_argument('-t', action='store', dest='dest', metavar='TO', type=pathlib.Path)

args = parser.parse_args()

name = args.source
ext = name.suffix
if ext in {'.jpeg', '.jpg'}:
    im = Image.open(name)
elif ext in {'.png'}:
    im = Image.open(name)
    im.convert("RGB")
else:
    try:
        im = Image.open(name.with_suffix('.jepg'))
    except:
        im = Image.open(name.with_suffix('.jpg'))

if args.dest:
    im.save(args.dest.with_suffix('.eps'), 'EPS')
else:
    im.save(name.with_suffix('.eps'), 'EPS')
