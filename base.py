# -*- coding: utf-8 -*-

import os
import pathlib

def search(path, op, check=None, recursive=False):
    '''search files in the path and operate them with op
    path: path
    op: function
    check: check the filename
    '''
    if recursive:
        for parent, dirnames, filenames in os.walk(path):
            for filename in filenames:
                wholename = os.path.join(parent, filename)
                if check is None or check(wholename):
                    op(wholename)
    else:
        for parent, dirnames, filenames in os.walk(path):
            for filename in filenames:
                wholename = os.path.join(parent, filename)
                if check is None or check(wholename):
                    op(wholename)
            break

def searchx(path, op, check=None, recursive=False):
    '''safe version of search in save mode
    search files in the path and operate them with op
    path: path
    op: function
    check: check the filename
    '''
    if recursive:
        for parent, dirnames, filenames in os.walk(path):
            for filename in filenames:
                wholename = os.path.join(parent, filename)
                if check is None or check(wholename):
                    try:
                        op(wholename)
                    except Exception as ex:
                        print(ex)
    else:
        for parent, dirnames, filenames in os.walk(path):
            for filename in filenames:
                wholename = os.path.join(parent, filename)
                if check is None or check(wholename):
                    try:
                        op(wholename)
                    except Exception as ex:
                        print(ex)
            break



defaultPath = pathlib.Path('~/Folders').expanduser()
PATHON_PATH = "/Library/Frameworks/Python.framework/Versions/3.6/bin/"
PACKAGE_PATH = "/Library/Frameworks/Python.framework/Versions/3.6/lib/python3.6/site-packages"