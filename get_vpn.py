#!/usr/bin/env python3
# -*- coding: utf-8 -*-


import argparse

import requests
import bs4

import anytable

resp = requests.get('http://ss.weiwei.in')
table = bs4.BeautifulSoup(resp.content, 'lxml').find_all('table')[1]
df = anytable.html2dataframe(table)

parser = argparse.ArgumentParser(description='Get vpn from http://ss.weiwei.in')
parser.add_argument('-l', dest='location', default=None, action='store_const', const='Los Angeles', help='Location of server')

show_keys = ['IP', 'Port', 'Method', 'Passwd', 'Location']
args = parser.parse_args()

if args.location:
    df = df[list(map(lambda x:args.location in x, df['Location']))]

print(df[show_keys])
    