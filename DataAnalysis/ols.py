#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import pandas as pd
import statsmodels.api as sm

def stat(path, xkeys, ykeys, *args, **kwargs):
    data = pd.read_excel(path, *args, **kwargs)
    Xtrain, Ytrain = data[xkeys].values, data[ykeys].values
    ols = sm.OLS(y, X)
    results = ols.fit()
    print(results.summary())

import fire
fire.Fire(stat)
