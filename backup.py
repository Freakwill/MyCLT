#!/usr/bin/env python3
# -*- coding: utf-8 -*-

''' back up
save files to usb
'''

import argparse
import pathlib

import shutil

usbName = 'William-Te'

usbPath = pathlib.Path('/Volumes') / usbName

parser = argparse.ArgumentParser(description='Back up documents')
parser.add_argument('-s', action='store', dest='src', metavar='SRC', required=True, type=pathlib.Path)
parser.add_argument('-d', action='store', dest='dst', metavar='DST', default=None, type=pathlib.Path)
parser.add_argument('-i', action='store', dest='ignore', nargs='*', metavar='IGNORE')
parser.add_argument('-u', action='store', dest='usbPath', metavar='USB_PATH', default=usbPath, type=pathlib.Path)


args = parser.parse_args()
src = args.src.resolve(strict=True)
if not src.exists():
    raise OSError(f'No such path {src}')

if args.dst:
    dst = args.usbPath / args.dst
else:
    dst = args.usbPath

if dst.exists():
    print(Warning(f'{dst} has existed! It will be deleted before backup.'))
    shutil.rmtree(dst, ignore_errors=True)

if args.ignore:
    shutil.copytree(src, dst, ignore=shutil.ignore_patterns(*args.ignore))
else:
    shutil.copytree(src, dst)
