#! python3
# encoding: utf-8
"""
@author:    Yize Wang
@contact:    wangyize@hust.edu.cn
@file:    pickRGB.py
@time:   2022/9/2 10:37
@description:    从图像中提取RGB三色通道的数据，并分别保存至文件中
"""

import os
import numpy as np

from PIL import Image

from public_utils import get_root, get_filename_without_postfix, get_postfix
from Image.utils import is_colored
from decorators import read_filename


@read_filename
def pick_channels(filename: str = None, save_flag: bool = False):
    """
    :param filename: 图像文件名
    :param save_flag: 是否直接保存到文件
    :return: 返回图像RGB三个通道的数值或直接保存在文件中
    """

    image = Image.open(filename)

    if not is_colored(image):
        print("错误：所输入的图像不是彩色图像，无法提取RBG通道的数据")
        return None

    if save_flag:
        # 需要保存时，解析如下数据
        root = get_root(filename)  # 文件夹
        postfix = get_postfix(filename)  # 后缀
        filename_without_postfix = get_filename_without_postfix(filename)  # 无后缀文件名

    image = np.array(image)

    red, green, blue = image[:, :, 0], image[:, :, 1], image[:, :, 2]
    red, green, blue = Image.fromarray(red), Image.fromarray(green), Image.fromarray(blue)

    if save_flag:
        red.save(os.path.join(root, "{}_r{}".format(filename_without_postfix, postfix)))
        green.save(os.path.join(root, "{}_g{}".format(filename_without_postfix, postfix)))
        blue.save(os.path.join(root, "{}_b{}".format(filename_without_postfix, postfix)))
        return None
    else:
        return red, green, blue


if __name__ == "__main__":
    pick_channels(save_flag=True)
