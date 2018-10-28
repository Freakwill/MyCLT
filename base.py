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
    '''search files in the path and operate them with op

    path: path
    op: function, operate pathlib.Path
    check: pathlib.Path -> Bool, check the filename
    '''
    if recursive:
        for parent, dirnames, filenames in os.walk(path):
            for filename in filenames:
                wholename = pathlib.Path(parent, filename)
                if check is None or check(wholename):
                    op(wholename)
    else:
        for parent, dirnames, filenames in os.walk(path):
            for filename in filenames:
                wholename = pathlib.Path(parent, filename)
                if check is None or check(wholename):
                    op(wholename)
            break


def searchx(path, op, check=None, recursive=False):
    '''safe version of search in save mode
    '''
    if recursive:
        for parent, dirnames, filenames in os.walk(path):
            for filename in filenames:
                wholename = pathlib.Path(parent, filename)
                if check is None or check(wholename):
                    try:
                        op(wholename)
                    except Exception as ex:
                        print(ex)
    else:
        for parent, dirnames, filenames in os.walk(path):
            for filename in filenames:
                wholename = pathlib.Path(parent, filename)
                if check is None or check(wholename):
                    try:
                        op(wholename)
                    except Exception as ex:
                        print(ex)
            break

