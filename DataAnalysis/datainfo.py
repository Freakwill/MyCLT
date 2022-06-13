#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import pathlib
import matplotlib.pyplot as plt

import pandas as pd

def hist(path, key=0, *args, **kwargs):
    """Draw a histogram for data

    dataframe is read from <path>
    
    Arguments:
        path {str} -- the path of data with suffix .csv or .xls(x)
        *args, **kwargs -- same with read_csv or read_excel
    
    Keyword Arguments:
        key {number|str} -- the key of dataFrame (default: {0})
    """
    if isinstance(path, str):
        path = pathlib.Path(path)
    if path.suffix == '.csv':
        df = pd.read_csv(path, *args, **kwargs)
    else:
        df = pd.read_excel(path, *args, **kwargs)
    if isinstance(key, int):
        x = df.iloc[:,key]
    else:
        x = df[key]
    ax=x.plot.hist(bins=12, density=1)
    x.plot.density(style='g--',ax=ax)  
    plt.show()

def show(path, keys=None, method='describe', *args, **kwargs):
    """show information of dataframe

    dataframe is read from <path>
    
    Arguments:
        path {str} -- the path of data with suffix .csv or .xls(x)
        *args, **kwargs -- same with read_csv or read_excel
    
    Keyword Arguments:
        keys {[str]} -- some keys of dataFrame
    """
    if isinstance(path, str):
        path = pathlib.Path(path)
    if path.suffix == '.csv':
        df = pd.read_csv(path, *args, **kwargs)
    else:
        df = pd.read_excel(path, *args, **kwargs)
    if keys:
        df = df[keys]
    print(getattr(df, method)())

import fire
fire.Fire()
