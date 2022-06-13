#!/usr/bin/env python3
# -*- coding: utf-8 -*-

'''Fetch info of items from baidu baike

python baike.py -i [any item]
'''

import argparse

from bs4 import BeautifulSoup
import requests

from baidupedia import *

parser = argparse.ArgumentParser(description='Get Information of items from Baidupedia',
    formatter_class=argparse.RawDescriptionHelpFormatter,
    epilog="""
    Here is an example.
    baike.py -i 维基百科 -s 目录
    where 维基百科 is an item name and 目录 is a section name (in Chinese or English)
    Availeble section names are
    '目录/catalog', '文献/references', '摘要/summary', '内容/content', '信息/basic_info', '多义词/polysement'
    """)
parser.add_argument('-i', dest='item', action='store', default='百度百科', metavar='ITEM')
parser.add_argument('-s', dest='section', action='store', default='summary', metavar='SECTION',
    help='a section what you want to read, such as catalog(目录)、summary(摘要)')
args = parser.parse_args()

item = BaiduItem.fetch(args.item)
d = {'目录':'catalog', '文献':'references', '摘要':'summary', '内容':'content', '信息':'basic_info', '多义词':'polysement'}
args.section = d.get(args.section, args.section)
print(getattr(item, args.section))