# -*- coding: utf-8 -*-


import argparse
import os.path

import sh

import base

parser = argparse.ArgumentParser(description='2to3')
parser.add_argument('-n', action='store', dest='name', metavar='NAME', required=True)

args = parser.parse_args()
# name='pyswip'
path = os.path.join(base.PACKAGE_PATH, args.name)

cmd = sh.Command('2to3', search_paths=['/Library/Frameworks/Python.framework/Versions/3.6/bin'])
cmd = cmd.bake('-n')
cmd = cmd.bake('-w')
cmd(path)