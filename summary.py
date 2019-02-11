#!/usr/bin/env python3
# -*- coding: utf-8 -*-


import logging
logging.propagate = False 
logging.getLogger().setLevel(logging.ERROR)

import argparse
import pdfsummary

parser = argparse.ArgumentParser(description='Summarize a pdf')
parser.add_argument('-p', dest='path', action='store', help='the path of the file')
parser.add_argument('-n', dest='count', action='store', default=10, type=int, help='the number of sentences')
args = parser.parse_args()


pdf.summary.show_summary(args.path, args.count)
