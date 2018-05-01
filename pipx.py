# -*- coding: utf-8 -*-


import argparse

import subprocess

child = subprocess.Popen('pip3 list --format columns --outdate', shell=True, stdout=subprocess.PIPE)
out, err = child.communicate()
out = out.decode()

for package in out.split('\n')[2:-1]:
    if package:
        name, version, latest, type_ = package.split()
        print(name, latest)

