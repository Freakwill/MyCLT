#!/usr/bin/env python3
# -*- coding: utf-8 -*-


import argparse

import sh

import base

parser = argparse.ArgumentParser(description='2to3')
parser.add_argument('-n', action='store', dest='name', metavar='NAME', required=True)

args = parser.parse_args()
path = base.PACKAGE_PATH / args.name

cmd = sh.Command('2to3', search_paths=[base.PATHON_PATH])
cmd = cmd.bake('-n')
cmd = cmd.bake('-w')
cmd(path)