#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import os
import pathlib
import argparse
import re

USER_PATH = pathlib.Path('~').expanduser()
defaultPath = USER_PATH / 'Folders'
PATHON_PATH = pathlib.Path("/Library/Frameworks/Python.framework/Versions/3.6/bin/")
PACKAGE_PATH = pathlib.Path("/Library/Frameworks/Python.framework/Versions/3.6/lib/python3.6/site-packages")

searchFiles = argparse.ArgumentParser(description='find a file or files with certain conditions.', add_help=False)
searchFiles.add_argument('-p', dest='path', action='store', default=USER_PATH, metavar='PATH', type=pathlib.Path, help='the folder where you search files')
searchFiles.add_argument('-x', dest='filename', action='store', metavar='FILENAME', type=re.compile, help='regex of the filenames')
searchFiles.add_argument('-r', dest='recursive', action='store_true', default=False, help='recursively search or not')


def search(path, op, check=None, recursive=False):
    """Search files in the path and operate them with op

    path: path
    op: function, operate pathlib.Path
    check: pathlib.Path -> Bool, check the filename
    """
    if recursive:
        print('Searching path %s recursively ...' % path)
        for parent, dirnames, filenames in os.walk(path):
            for filename in filenames:
                wholename = pathlib.Path(parent, filename)
                if check is None or check(wholename):
                    op(wholename)
    else:
        print('Searching path %s (not recursively) ...' % path)
        for parent, dirnames, filenames in os.walk(path):
            for filename in filenames:
                wholename = pathlib.Path(parent, filename)
                if check is None or check(wholename):
                    op(wholename)
            break


def searchx(path, op, check=None, recursive=False):
    """Safe version of search in save mode
    """

    if recursive:
        print('Searching path %s recursively ...' % path)
        for parent, dirnames, filenames in os.walk(path):
            for filename in filenames:
                wholename = pathlib.Path(parent, filename)
                if check is None or check(wholename):
                    try:
                        op(wholename)
                    except Exception as ex:
                        print(ex)
    else:
        print('Searching path %s (not recursively) ...' % path)
        for parent, dirnames, filenames in os.walk(path):
            for filename in filenames:
                wholename = pathlib.Path(parent, filename)
                if check is None or check(wholename):
                    try:
                        op(wholename)
                    except Exception as ex:
                        print(ex)
            break

# handle with pdf
from pdfminer.pdfparser import PDFParser,PDFDocument
from pdfminer.pdfinterp import PDFResourceManager, PDFPageInterpreter
from pdfminer.converter import PDFPageAggregator
from pdfminer.layout import LTTextBoxHorizontal,LAParams
from pdfminer.pdfinterp import PDFTextExtractionNotAllowed

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

# def pdf2str(fo):
#     return '\n'.join(parse(fo))

