#!/usr/bin/env python3
# -*- coding: utf-8 -*-

''' Download nltk data
'''


import argparse

import nltk
import ssl

try:
    _create_unverified_https_context = ssl._create_unverified_context
except AttributeError:
    pass
else:
    ssl._create_default_https_context = _create_unverified_https_context

parser = argparse.ArgumentParser(description='Download nltk data')
parser.add_argument('-r', dest='resource', action='store', default=None)

args = parser.parse_args()
resource = args.resource

if resource is None:
    nltk.download()
else:
    nltk.download(resource)