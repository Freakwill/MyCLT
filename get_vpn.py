#!/usr/bin/env python3
# -*- coding: utf-8 -*-


import argparse

import requests
import bs4

import anytable

resp = requests.get('http://ss.weiwei.in')
table = bs4.BeautifulSoup(resp.content, 'lxml').find_all('table')[1]
df = anytable.html2dataframe(table)

parser = argparse.ArgumentParser(description='Get vpn')
parser.add_argument('-l', dest='location', default='Los Angeles', action='store', help='help')

args = parser.parse_args()

print(df[df['Location']==args.location])