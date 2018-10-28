#!/usr/bin/env python3
# -*- coding: utf-8 -*-

''' start IDE spyder
'''

import pathlib
import argparse

import spyder.app.start as start



parser = argparse.ArgumentParser(description='start spyder')
parser.add_argument('-p', dest='pathname', action='store', default=pathlib.Path('~/Python/mywork').expanduser(), metavar='PATH', type=pathlib.Path)

args = parser.parse_args()
path = args.pathname

start.main()