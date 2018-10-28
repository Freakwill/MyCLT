#!/usr/bin/env python3
# -*- coding: utf-8 -*-

''' back up
save files to usb
'''

import argparse
import pathlib

import shutil

usbPath = '/Volumes/台电酷闪/'

parser = argparse.ArgumentParser(description='Back up documents')
parser.add_argument('-s', action='store', dest='src', metavar='SRC', required=True)
parser.add_argument('-d', action='store', dest='dst', metavar='DST')
parser.add_argument('-i', action='store', dest='ignore', nargs='*', metavar='IGNORE')
parser.add_argument('-u', action='store', dest='usbPath', metavar='USB_PATH', default=usbPath)


args = parser.parse_args()
src = pathlib.Path('~', args.src).expanduser()
if args.dst:
    dst = pathlib.Path(args.usbPath, args.dst)
else:
    dst = pathlib.Path(args.usbPath, args.src)

if dst.exists():
    shutil.rmtree(dst)

if args.ignore:
    shutil.copytree(src, dst, ignore=shutil.ignore_patterns(*args.ignore))
else:
    shutil.copytree(src, dst)