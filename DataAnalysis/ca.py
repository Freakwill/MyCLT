#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import pathlib

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from sklearn.decomposition import PCA, FastICA, NMF


def get_data(path):
    path = pathlib.Path(path)
    if path.suffix in {'.xls', '.xlsx'}:
        data = pd.read_excel(path, index_col=0)
    elif path.suffix == '.csv':
        data = pd.read_csv(path, index_col=0)
    elif path.suffix in {'.jpg', '.jpeg', '.png'}:
        from PIL import Image, ImageMath
        data = np.asarray(Image.open(path).convert('L'))
        data = pd.DataFrame(data)
    elif path.suffix == '.txt':
        text=path.read_text()
        text = [a.strip() for a in text.split('\n\n')]
        from sklearn.feature_extraction.text import TfidfVectorizer
        vector = TfidfVectorizer(stop_words='english')
        vector.fit(text)
        vocabulary = list(vector.vocabulary_.keys())
        vocabulary.sort(key=lambda x:vector.vocabulary_[x])
        m = vector.transform(text).todense()
        data = pd.DataFrame(m.T, index=list(vector.vocabulary_.keys()))
    return data

def pca(path, output=None, n_components=2, *args, **kwargs):
    """pca for data in path
    
    Arguments:
        path {str} -- a xls or csv file
    
    Keyword Arguments:
        output {None|str} -- path the data are saved (default: {None})

    Example:
    Scripts/DataAnalysis/ca.py pca --path Folders/临时文件夹/光谱值数据.xlsx --n_components 2
    """

    data = get_data(path)
    pca = PCA(n_components=n_components, *args, **kwargs)
    pca.fit(data)
    r0, r1 = pca.explained_variance_ratio_
    Y = pca.transform(data)
    fig = plt.figure()
    ax1 = fig.add_subplot(121)
    ax1.plot(Y[:,0], Y[:,1], '.')
    ax1.set_title('Principal Components')
    ax1.set_xlabel('comp_0 (%.4f)' % r0)
    ax1.set_ylabel('comp_1 (%.4f)' % r1)
    ax2 = fig.add_subplot(122)
    ax2.plot(pca.components_[0,:], pca.components_[1,:], '.')
    ax2.set_title('Coordinates on Principal Components')
    ax2.set_xlabel('comp_0 (%.4f)' % r0)
    ax2.set_ylabel('comp_1 (%.4f)' % r1)
    if output:
        plt.save(output)
    else:
        plt.show()


def ica(path, output=None, n_components=2, *args, **kwargs):
    """ica for data in path
    
    Arguments:
        path {str} -- a xls or csv file
    
    Keyword Arguments:
        output {None|str} -- path the data are saved (default: {None})

    Example:
    Scripts/DataAnalysis/ca.py ica --path Folders/临时文件夹/光谱值数据.xlsx --n_components 2
    """
    data = get_data(path)
    pca = FastICA(n_components=n_components, *args, **kwargs)
    pca.fit(data)
    Y = pca.transform(data)
    fig = plt.figure()
    ax = fig.add_subplot(111)
    ax.plot(Y[:,0], Y[:,1], '.')
    ax.set_xlabel('comp_0')
    ax.set_ylabel('comp_1')
    if output:
        ax.save(output)
    else:
        plt.show()

def nmf(path, output=None, n_components=2, *args, **kwargs):
    """nmf for data in path
    
    Arguments:
        path {str} -- a xls or csv file
    
    Keyword Arguments:
        output {None|str} -- path the data are saved (default: {None})

    Example:
    Scripts/DataAnalysis/ca.py nmf --path Folders/临时文件夹/光谱值数据.xlsx --n_components 2
    """
    data = get_data(path)
    pca = NMF(n_components=n_components, *args, **kwargs)
    pca.fit(data)
    Y = pca.transform(data)
    fig = plt.figure()
    ax = fig.add_subplot(111)
    ax.plot(Y[:,0], Y[:,1], '.')
    ax.set_xlabel('comp_0')
    ax.set_ylabel('comp_1')
    if output:
        ax.save(output)
    else:
        plt.show()

import fire
fire.Fire()
