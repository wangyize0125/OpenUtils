#! python3
# encoding: utf-8
"""
@author:    Yize Wang
@contact:    wangyize@hust.edu.cn
@file:    decorators.py
@time:   2022/9/2 10:40
@description:    程序中需要用到的一些装饰器
"""

from functools import wraps

var_filename = "filename"


def read_filename(func):
    """
    :param func: 需要装饰器的函数
    :return: 返回添加了装饰器之后的函数
    """

    @wraps(func)    # 保留原有函数的属性，包括函数名、描述文档等
    def decorated(*args, **kwargs):
        need_read_filename = False
        if var_filename not in kwargs.keys():
            # 输入参数中不包含文件名
            need_read_filename = True
        elif var_filename in kwargs.keys():
            if not kwargs[var_filename]:
                # 输入参数中包含文件名但文件名为空
                need_read_filename = True
        else:
            pass

        if need_read_filename:
            filename = input("输入文件路径（绝对路径或相对路径）：")
            kwargs["filename"] = filename

        print("调用函数：{}，文件名：{}".format(func.__name__, kwargs["filename"]))

        return func(*args, **kwargs)
    return decorated
