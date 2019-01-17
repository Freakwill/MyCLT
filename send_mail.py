#!/usr/bin/env python3
# -*- coding: utf-8 -*-

''' send mails to some email
grammar:
send_mail.py -p pathname -f from -t to -s subject
pathname: a file or folder
'''

import os
import pathlib
import subprocess

import argparse

from envelopes import Envelope


# dictionary for passwords of emails
neteasy = {'addr':'songcwzjut@163.com', 'password':'mail2017', 'server':'smtp.163.com'}
sina = {'addr':'songcongwei54@sina.com', 'password':'time2017', 'server':'smtp.sina.com'}

parser = argparse.ArgumentParser(description='send mail with envelopes')
parser.add_argument('-p', dest='pathname', action='store', metavar='PATH', type=pathlib.Path)
parser.add_argument('-f', dest='from_addr', action='store', default=neteasy['addr'], metavar='FROM_ADDRESS', help='from which email')
parser.add_argument('-t', dest='to_addr', action='store', default=sina['addr'], metavar='TO_ADDRESS', help='to which email')
parser.add_argument('-s', dest='subject', action='store', default='hello', metavar='SUBJECT')
parser.add_argument('-b', dest='body', action='store', default='Best Wishes!', metavar='BODY')
parser.add_argument('-l', dest='longbody', action='store', default='body.txt', metavar='LONGBODY', type=pathlib.Path)

args = parser.parse_args()

if args.longbody.is_file():
    body = args.body + '/n/n' + args.longbody.read_text()
else:
    body = args.body

envelope = Envelope(
    from_addr=(args.from_addr, 'From William Song'),
    to_addr=(args.to_addr, 'To you'),
    subject=args.subject,
    text_body=body)

path = args.pathname
if path:
    if path.is_dir():
        # compress the folder before submitting
        # compressed file is named by subject
        compath = path.parent / (args.subject+".7z")
        subprocess.run(["7z", "a", "-t7z", compath, path])
        envelope.add_attachment(str(compath))
    elif path.is_file():
        envelope.add_attachment(str(path))

    envelope.send(neteasy['server'], login=args.from_addr, password=neteasy['password'], tls=True)
    print('The email is sent to %s.'%args.to_addr)

    if path.is_dir():
        # delete the compressed file finally
        os.remove(compath)
        print('compressed file is removed.')
