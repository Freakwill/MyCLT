#!/usr/local/bin/python
# -*- coding: utf-8 -*-
import argparse

import webbrowser

browserDict = {}

parser = argparse.ArgumentParser(description='Open the Urls recorded in a file')
parser.add_argument('-f', dest='fobj', action='store', default='urls.txt', metavar='FILE', type=argparse.FileType())
parser.add_argument('-e', dest='explorer', action='store', default=None, metavar='EXPLORER')

args = parser.parse_args()

if args.explorer is None:
    safariPath = '/Applications/Safari.app/Contents/MacOS/Safari'
    webbrowser.register('safari', None, webbrowser.BackgroundBrowser(safariPath))
else:
    webbrowser.register(args.explorer, None, browserDict[args.explorer])


webbrowser.register('safari', None, webbrowser.BackgroundBrowser(safariPath))
# print(webbrowser.get('safari'))

for url in args.fobj.readlines():
    webbrowser.open_new_tab(url.strip('\n'))
# args.fobj.close()