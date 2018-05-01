# -*- coding: utf-8 -*-
#!/usr/bin/env python3

''' test
'''

import os.path
import argparse


parser = argparse.ArgumentParser(description='test')
parser.add_argument('-o', dest='what', action='store', default='hello', metavar='WHAT')

args = parser.parse_args()
print(args.what)