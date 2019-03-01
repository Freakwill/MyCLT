#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import bs4
import requests

import fire

def url2soup(url, *args, **kwargs):
    # url -> soup
    response = requests.get(url, *args, **kwargs)
    # response.encoding == 'ISO-8859-1':
    encodings = requests.utils.get_encodings_from_content(response.text)
    if encodings:
        encoding = encodings[0]
    else:
        encoding = response.apparent_encoding
    encode_content = response.content.decode(encoding, 'replace')
    return bs4.BeautifulSoup(encode_content, "lxml")


def parse(URL, name='div', prop='text', **kwargs):
    soup = url2soup(URL)
    tag = soup.body.find(name, kwargs)
    print(getattr(tag, prop))

fire.Fire(parse)