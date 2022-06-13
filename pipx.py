#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""Upgrade packages

just run `pipx.py` in clt

Menu:
    q: quit
    s: sudo mode
    u: usual mode
    l: list the packages not upgraded
    m: install the previous packages again
"""


import sh
import collections

Package = collections.namedtuple('package', ['name', 'version', 'latest', 'type_'])

MIRRORS = {'tsinghua': 'https://pypi.tuna.tsinghua.edu.cn/simple'}

parallel = False
from threading import Semaphore
pool = Semaphore(10)


def done(cmd, success, exit_code):
    pool.release()

def _install(current, packages):
    global PARAMS

    cmd = sh.pip3.install
    if sudo:
        if 'password' not in globals():
            globals()['password'] = input('Your password:')
        cmd = sh.sudo.bake("-S", _in=password).pip3.install
        # cmd = sh.contrib.sudo(password="********", _with=True).pip3.install

    successful = []

    if parallel:
        def do(p):
            pool.acquire()
            try:
                cmd(*PARAMS, p, _bg=True, _done=done)
                successful.append(p)
                print(f'{p} has been installed.')
            except Exception as e:
                print(e)
        for p in current:
            do(p).wait()
    else:
        for p in current:
            try:
                outdate = cmd(*PARAMS, p)
                successful.append(p)
                print(f'{p} has been installed.')
            except Exception as e:
                print(e)

    return [package for package in packages if package.name not in successful]


def get_outdate(source=None):
    # get outdate packages
    if source:
        outdate = sh.pip3.list('--format', 'columns', '--outdate', '-i', MIRRORS[source])
    else:
        outdate = sh.pip3.list('--format', 'columns', '--outdate')
    return [Package._make(package.split()) for package in outdate.split('\n')[2:-1] if package]

def display(packages):
    print('''
        Name  Version  Latest
        ----------------------
        ''')
    for package in packages:
        print('    ', package.name, package.version, package.latest)

sudo = False
current = []
PARAMS = ('--upgrade',)

def install(source=None):
    global sudo, current, PARAMS

    packages = get_outdate(source=source)

    display(packages)

    if source:
        PARAMS = (*PARAMS, '-i', MIRRORS[source])

    print('''====Type one or some names of packages wantted.====
        q: quit
        s: sudo mode
        u: usual mode
        l: list the packages
        m: install the previous packages again
        -----------------------
        ''')
    while True:
        ps = input('>=> ')
        # if ps.startswith('%'):
        #     a, _, b = ps.lstrip('%').partition('=')
        #     a = a.strip()
        #     b = b.strip()
        #     if b.isdigit():
        #         b = int(b)
        #     globals()[a] = b

        if ps == 'q':
            print('Bye.')
            break
        elif ps == 's':
            sudo = True
            print('in sudo mode')
        elif ps == 'u':
            sudo = False
            print('not in sudo mode')
        elif ps == 'l':
            display(packages)
        elif ps == 'm':
            if not current:
                print('m could not be used now!')
                continue

            packages = _install(current, packages)

        else:
            current = ps.split()
            for c in current.copy():
                if not any(c == package.name for package in packages):
                    print(f'{c} is not in the list of packages!')
                    current.remove(c)
                else:
                    print(f'{c} will be installed.')

            packages = _install(current, packages)

import fire
fire.Fire(install)

