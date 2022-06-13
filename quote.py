#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import pybrainyquote
import fire


def get_quote(*args, **kwargs):
    quote = pybrainyquote.Quote.random(*args, **kwargs)
    print(quote.pretty())

fire.Fire(get_quote)
