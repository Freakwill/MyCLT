# -*- coding: utf-8 -*-

''' start IDE spyder
'''

import os.path
import argparse

import spyder.app.start as start



parser = argparse.ArgumentParser(description='start spyder')
parser.add_argument('-p', dest='pathname', action='store', default=os.path.expanduser('~/Python/mywork'), metavar='PATH')

args = parser.parse_args()
path = args.pathname

start.main()