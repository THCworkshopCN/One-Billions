# -*- coding:utf-8-*-
"""
工具箱
"""

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

def screen_center():
    from pygame import display