#!/usr/bin/env python3
# -*- coding: utf-8 -*-


import argparse

import subprocess
import collections

parser = argparse.ArgumentParser(description='install packages with pip')
parser.add_argument('-s', dest='sudo', action='store_true', default=False)
parser.set_defaults(recursive=True)

child = subprocess.Popen('pip3 list --format columns --outdate', shell=True, stdout=subprocess.PIPE)
out, err = child.communicate()
out = out.decode()

Package = collections.namedtuple('package', ['name', 'version', 'latest', 'type_'])

packages = [Package._make(package.split()) for package in out.split('\n')[2:-1] if package]
for p in packages:
    print(p.name, p.version)

args = parser.parse_args()
mode = args.sudo

print('Type names of packages wantted.')
while True:
    ps = input('>=> ')
    if ps == 'q':
        break
    elif ps == 's':
        mode = 1
        print('in sudo mode')
    elif ps == 'u':
        mode = 0
        print('not in sudo mode')
    elif ps == 'l':
        for p in packages:
            print(p.name, p.version)
    else:
        if mode:
            cmd = ['pip3', 'install', '--upgrade']
        else:
            cmd = ['sudo', 'pip3', 'install', '--upgrade']
        for p in ps.split():
            child = subprocess.Popen(cmd + [p], shell=True, stdout=subprocess.PIPE)
            out, err = child.communicate()
            if err:
                err = err.decode()
                print(err)