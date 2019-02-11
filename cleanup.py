#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import pathlib

import argparse

parser = argparse.ArgumentParser(description='Clean up a folder')
parser.add_argument('-p', dest='path', action='store', help='path of the folder')

args = parser.parse_args()

def cleanup(path):
    for p in path.iterdir():
        if p.is_file():
            p.unlink()
        elif p.is_dir():
            cleanup(p)
            p.rmdir()

# usb = pathlib.Path('/Volumes/XINJI1501/')

cleanup(args.path)
