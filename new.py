# -*- coding: utf-8 -*-

''' print a document
'''

import argparse
import pathlib

heads = {'.py':'# -*- coding: utf-8 -*-'}

parser = argparse.ArgumentParser(description='Create a file')
parser.add_argument('-f', action='store', dest='filename', default='script.txt', metavar='FILE')
parser.add_argument('-d', action='store', dest='directory', default='~', metavar='DIRECTORY')
parser.add_argument('-s', nargs='+', dest='content', action='store', default='', metavar='CONTENT')
parser.add_argument('-l', action='store', dest='head', metavar='HEAD')

args = parser.parse_args()

p = pathlib.Path(args.directory, args.filename).expanduser()
if args.head:
    s = '%s\n\n%s'%(args.head, '\n'.join(args.content))
else:
    head = heads[p.suffix]
    s = '%s\n\n%s'%(head, '\n'.join(args.content))
p.write_text(s)