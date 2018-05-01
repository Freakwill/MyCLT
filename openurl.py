#!/usr/local/bin/python
# -*- coding: utf-8 -*-

import argparse

import webbrowser

browserDict = {}


parser = argparse.ArgumentParser(description='Open the Urls')
parser.add_argument('-u', dest='urls', nargs='+', action='store', default='www.baidu.com', metavar='URLs')
parser.add_argument('-e', dest='explorer', action='store', default=None, metavar='EXPLORER')

args = parser.parse_args()

if args.explorer is None:
    safariPath = '/Applications/Safari.app/Contents/MacOS/Safari'
    webbrowser.register('safari', None, webbrowser.BackgroundBrowser(safariPath))
else:
    webbrowser.register(args.explorer, None, browserDict[args.explorer])
# print(webbrowser.get('safari'))
for url in args.urls:
    webbrowser.open_new_tab(url)