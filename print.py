# -*- coding: utf-8 -*-

''' print a document
'''

import argparse
import os
import re
import pathlib.Path

import base

parser = argparse.ArgumentParser(description='print a document')
parser.add_argument('-p', action='store', dest='path', metavar='PATH', type=pathlib.Path)
parser.add_argument('-m', action='store', dest='printer', default='P_LaserJet_M1005_2', metavar='PRINTER')
parser.add_argument('-r', dest='recursive', type=bool, action='store_true', default=False)
parser.add_argument('-x', dest='regex', action='store', metavar='REGEX')


args = parser.parse_args()


def op(filename):
    os.system("lpr -P %s %s"%(args.printer, filename))

def check(filename):
    if args.regex:
        rx = re.compile(args.regex)
        return rx.match(filename.name)
    else:
        return True


if args.path.is_file():
    op(args.path)
else:
    base.search(args.path, op, check, args.recursive)