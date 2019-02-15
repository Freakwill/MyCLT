#!/usr/bin/env python3
# -*- coding: utf-8 -*-


import logging
logging.propagate = False 
logging.getLogger().setLevel(logging.ERROR)

import argparse
import pathlib


parser = argparse.ArgumentParser(description='Summarize a pdf')
parser.add_argument('-p', dest='path', action='store', type=pathlib.Path, help='the path of the file')
parser.add_argument('-n', dest='count', action='store', default=10, type=int, help='the number of sentences')
parser.add_argument('-l', dest='language', action='store', default='english', help='the language used')
args = parser.parse_args()

import pdfsummary


if args.path.suffix == '.pdf':
    pdfsummary.show_summary(args.path, args.count)
else:
    def show_summary(path, *args, **kwargs):
        print('Summary of %s' % path)
        with open(path, 'rb') as fo:
            s = fo.read()
        pdfsummary.show(pdfsummary.summarize(s, *args, **kwargs))

    show_summary(args.path, args.count, args.language)

