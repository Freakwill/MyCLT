#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import argparse

import itchat

parser = argparse.ArgumentParser(description='WeChat')
parser.add_argument('-a', dest='auto_reply', action='store', default=';)', metavar='AUTO_REPLAY')

args = parser.parse_args()

@itchat.msg_register(itchat.content.TEXT)
def text_reply(msg):
    return args.auto_reply

itchat.auto_login()
itchat.run()