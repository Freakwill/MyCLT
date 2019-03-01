#!/usr/bin/env python3
# -*- coding: utf-8 -*-

'''get info of items from wikipedia

python wiki.py -i [any item] -k [keyword]
'''

import argparse
import wikipedia as wk

parser = argparse.ArgumentParser(description='Get Information from Wikipedia')
parser.add_argument('-i', dest='item', action='store', default='', help='wanted item')
parser.add_argument('-k', dest='keyword', action='store', default='Python', help='keyword for searching an item')
args = parser.parse_args()

if args.item:
    page = wk.WikipediaPage(args.item)
    print(page.summary)

else:
    # search
    res = wk.search(args.keyword, results=10, suggestion=False)
    for x in res:
        print(x)