# -*- coding: utf-8 -*-

''' send mails to some email
grammar:
send_mail.py -p pathname -f from -t to -s subject
pathname: a file or folder
'''

import os
import os.path
import subprocess

import argparse

from envelopes import Envelope, GMailSMTP


password_dict = {'songcwzjut@163.com':'mail2017'}  # dictionary for passwords of emails

parser = argparse.ArgumentParser(description='send mail with envelopes')
parser.add_argument('-p', dest='pathname', action='store', metavar='PATH')
parser.add_argument('-f', dest='from_addr', action='store', default='songcwzjut@163.com', metavar='FROM_ADDRESS')
parser.add_argument('-t', dest='to_addr', action='store', default='songcongwei54@sina.com', metavar='TO_ADDRESS')
parser.add_argument('-s', dest='subject', action='store', default='hello', metavar='SUBJECT')
parser.add_argument('-b', dest='body', action='store', default='Best Wishes!', metavar='BODY')
parser.add_argument('-l', dest='longbody', action='store', default='body.txt', metavar='LONGBODY')

args = parser.parse_args()

if os.path.isfile(args.longbody):
    with open(args.longbody) as fo:
        longbody = fo.read()
    body = args.body + '/n' + longbody
else:
    body = args.body

envelope = Envelope(
    from_addr=(args.from_addr, 'From William Song'),
    to_addr=(args.to_addr, 'To you'),
    subject=args.subject,
    text_body=body)

path = args.pathname
if path:
    if os.path.isdir(path):
        # compress the folder before submitting
        # compressed file is named by subject
        compath = os.path.join(os.path.dirname(path), args.subject+".7z")
        subprocess.run(["7z", "a", "-t7z", compath, path])
        envelope.add_attachment(compath)
    elif os.path.isfile(path):
        envelope.add_attachment(path)

    envelope.send('smtp.163.com', login=args.from_addr, password=password_dict[args.from_addr], tls=True)
    print('The email is sent to %s.'%args.to_addr)

    if os.path.isdir(path):
        # delete the compressed file finally
        os.remove(compath)