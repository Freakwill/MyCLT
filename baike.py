#!/usr/bin/env python3
# -*- coding: utf-8 -*-

'''get info of items from baidu baike

python baike.py -i [any item]
'''

import argparse

from bs4 import BeautifulSoup
import requests

BAIKE_URL = 'https://baike.baidu.com'
ITEM_URL = BAIKE_URL + '/item'

parser = argparse.ArgumentParser(description='Get Information from Baidupedia')
parser.add_argument('-i', dest='item', action='store', default='百度百科', metavar='ITEM')
args = parser.parse_args()

url = ITEM_URL + '/%s'%args.item
header_dict = {'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; Trident/7.0; rv:11.0) Gecko/20100101 Firefox/57.0'}
resp = requests.get(url, headers=header_dict)
bs = BeautifulSoup(resp.content.decode('utf-8'), "lxml")
summary = bs.find('div', {'class':'lemma-summary'})
print(summary.text)