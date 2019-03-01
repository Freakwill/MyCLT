#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import wc
import argparse
import jieba

parser = argparse.ArgumentParser(description='generate a word could')
parser.add_argument('-s', dest='string', action='store', help='a string')
parser.add_argument('-f', dest='file', action='store', default='test.txt', help='a file')
parser.add_argument('-o', dest='wcImage', action='store', default='wc.png', help='an image to show word could')
parser.add_argument('-m', dest='mask', action='store', default=None, help='a mask image')
args = parser.parse_args()

if args.file:
    with open(args.file) as fo:
        s = fo.read()
elif args.string:
    s = args.string
else:
    raise Exception("Input the text")

wordcloud = wc.make_wordcloud(s, mask_image=args.mask)
wordcloud.to_file(args.wcImage)

