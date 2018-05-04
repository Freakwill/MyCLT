# -*- coding: utf-8 -*-

''' find path files in Math folder
grammar:
$ python findmath.py -s {text} -f {folder} [-r {True}]
example:
$ python findmath.py -s filter
'''
import os
import pathlib
import argparse

import logging
logging.propagate = False 
logging.getLogger().setLevel(logging.ERROR)

from pdfminer.pdfparser import PDFParser,PDFDocument
from pdfminer.pdfinterp import PDFResourceManager, PDFPageInterpreter
from pdfminer.converter import PDFPageAggregator
from pdfminer.layout import LTTextBoxHorizontal,LAParams
from pdfminer.pdfinterp import PDFTextExtractionNotAllowed

import base


def parse(fo):
    praser = PDFParser(fo)
    doc = PDFDocument()
    praser.set_document(doc)
    doc.set_parser(praser)
    doc.initialize()
    if not doc.is_extractable:
        raise PDFTextExtractionNotAllowed
    else:
        rsrcmgr = PDFResourceManager()
        laparams = LAParams()
        device = PDFPageAggregator(rsrcmgr, laparams=laparams)
        interpreter = PDFPageInterpreter(rsrcmgr, device)
        pages = []
        for page in doc.get_pages(): # get page list
            interpreter.process_page(page)
   
            layout = device.get_result()
   
            p = ''.join(x.get_text() for x in layout if isinstance(x, LTTextBoxHorizontal))
            pages.append(p)
    return pages

mathPath = pathlib.Path('~/Folders/Math').expanduser() # where you save math references

parser = argparse.ArgumentParser(description='find math references (.pdf files) with a certain string in a path', parents=[base.searchFiles])
# parse.set_default(path=mathPath)
parser.add_argument('-s', dest='string', action='store', metavar='STRING')
parser.add_argument('-d', dest='folder', action='store', metavar='FOLDER')

args = parser.parse_args()

path = mathPath / args.folder if args.folder else mathPath

string = args.string


def op(fname):
    if fname.suffix == '.pdf':
        with fname.open('rb') as fo:
            pages = parse(fo)
        for k, page in enumerate(pages):
            if string in page:
                try:
                    print(fname, '#page %d'%k)
                except Exception as e:
                    print(fname, ' is skipped for %s'%e)
                except:
                    print(fname, ' is skipped for some error')

base.searchx(path, op, check=None, recursive=args.recursive)
