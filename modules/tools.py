# -*- coding:utf-8-*-
# Copyright (C) 2021 THCWorkshopCN
"""
工具箱
"""
from modules import global_values as gv

def get_type(variate:any) -> str:
    """判断值的类型"""
    type=None
    if isinstance(variate,int): type = "int"
    elif isinstance(variate,str): type = "str"
    elif isinstance(variate,float): type = "float"
    elif isinstance(variate,list): type = "list"
    elif isinstance(variate,tuple): type = "tuple"
    elif isinstance(variate,dict): type = "dict"
    elif isinstance(variate,set): type = "set"
    return type

def CENTER():
    screen_width, screen_height = gv.get("screen_size")
    CENTER = (screen_width/2, screen_height/2)
    return CENTER