#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from snownlp import SnowNLP
import fire
import toolz

def summary(file='test.txt', *args, **kwargs):
    """Summarize Chinese text in a file
    """

    with open(file) as fo:
        text = fo.read()
    _summary(text, *args, **kwargs)

def _summary(text='', ns:int=7, nk:int=4, outfile:str=None):
    """Summarize Chinese text
    
    Keyword Arguments:
        text {str} -- text will be summarized (default: {''})
        ns {int} -- number of sentences (default: {7})
        nk {int} -- number of keywords (default: {4})
        outfile {str} -- where the summary is written (default: {None})
    """
    s = SnowNLP(text)
    output = '*摘要*\n'
    for k, sen in enumerate(toolz.unique(s.summary(ns)), 1):
        output += '%d. %s\n' % (k, sen)
    output += '\n*关键词*:' + ', '.join(s.keywords(nk))
    if outfile:
        with open(outfile, 'w') as fo:
            fo.write(output)
    else:
        print(output)

fire.Fire(summary)