# -*- coding:utf-8-*
# Copyright (C) 2021 THCWorkshopCN
"""语言系统"""
import i18n
i18n.load_path.append("./translations/terminal_output")
i18n.load_path.append("./translations")

def trans(content:str):
    return i18n.t(content)