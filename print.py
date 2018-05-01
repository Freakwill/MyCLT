# -*- coding: utf-8 -*-

''' print a document
'''

import argparse
import os
import os.path
import re

import base

parser = argparse.ArgumentParser(description='print a document')
parser.add_argument('-p', action='store', dest='path', metavar='PATH')
parser.add_argument('-m', action='store', dest='printer', default='P_LaserJet_M1005_2', metavar='PRINTER')
parser.add_argument('-r', dest='recursive', type=bool, action='store', default=False)
parser.add_argument('-x', dest='regex', action='store', metavar='REGEX')


args = parser.parse_args()


def op(filename):
    os.system("lpr -P %s %s"%(args.printer, filename))

def check(filename):
    if args.regex:
        rx = re.compile(args.regex)
        return rx.match(filename)
    else:
        return True


if os.path.isfile(args.path):
    op(args.path)
else:
    base.search(args.path, op, check, args.recursive)