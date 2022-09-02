#! python3
# encoding: utf-8
"""
@author:    Yize Wang
@contact:    wangyize@hust.edu.cn
@file:    public_utils.py
@time:   2022/9/2 11:38
@description:    一些公用的功能函数
"""

import os


def get_root(filename: str = None):
    return os.path.dirname(filename)


def get_filename_without_postfix(filename: str = None):
    return os.path.splitext(os.path.basename(filename))[0]


def get_postfix(filename: str = None):
    return os.path.splitext(filename)[1]
