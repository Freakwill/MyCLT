#!/usr/bin/env python
# -*- coding: utf-8 -*-


''' test of argparse '''

import argparse


parser = argparse.ArgumentParser(description='test')
parser.add_argument('-o', dest='what', action='store', default='hello，你好', metavar='WHAT')

args = parser.parse_args()
print(args.what)

