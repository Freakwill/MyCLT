#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import pathlib
import matplotlib.pyplot as plt

import pandas as pd

# mark styles for classes
styles = ['ro', 'b+', 'g*', 'yd', 'kV']

def classify2d(path, key1, key2, *args, **kwargs):
    """Draw 2dim-data classification
    
    Arguments:
        path {str} -- the path of .csv or .xls
        key1, key2 {st} -- 2 keys of DataFrame
    """
    if isinstance(path, str):
        path = pathlib.Path(path)
    if path.suffix == '.csv':
        df = pd.read_csv(path, *args, **kwargs)
    else:
        df = pd.read_excel(path, *args, **kwargs)
    cs = set(df.iloc[:,0])
    fig = plt.figure()
    ax = fig.add_subplot(111)
    names = []
    for c, style in zip(cs, styles):
        dfc=(df.loc[df.iloc[:, 0]==c])[[key1, key2]]
        ax.plot(dfc[key1], dfc[key2], style)
        names.append(f'class {c}')
    ax.set_xlabel(key1)
    ax.set_ylabel(key2)
    plt.legend(names)
    plt.show()

import fire
fire.Fire(classify2d)