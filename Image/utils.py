#! python3
# encoding: utf-8
"""
@author:    Yize Wang
@contact:    wangyize@hust.edu.cn
@file:    public_utils.py
@time:   2022/9/2 11:23
@description:    一些和图像处理有关的函数
"""

import numpy as np

from PIL import Image


def is_colored(image: Image.Image):
    """
    :param image: 读取到的图像
    :return: 是否是彩色图像，彩色图像的通道数至少大于1
    """

    data = np.array(image)

    if len(data.shape) == 2:
        # 只有一个通道，不是彩色图像
        return False
    elif len(data.shape) > 2 and data.shape[2] == 1:
        # 只有一个通道，不是彩色图像
        return False
    elif len(data.shape) > 2 and data.shape[2] > 1:
        # 有多个通道，是彩色图像
        return True
    else:
        # 为避免调用该函数的函数出错，将此范围之外的图像均视为非彩色图像
        return False
