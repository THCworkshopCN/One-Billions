# -*- coding:utf-8-*
# Copyright (C) 2021 THCWorkshopCN
from modules import classes, events
from modules import global_values as gv
import pygame
from pygame.locals import *
from modules import events
from modules import classes
from app import basic_display

def render_text(
    _text:str, size:int=50, location:tuple=(0,0), color=(255,255,255), location_type:str = "basic", sysfont:str = None, font:str=None, _antialias:bool=True
    ) -> classes.display.display_map:
    """渲染文字"""
    screen = gv.get("screen")
    background = gv.get("background")
    if sysfont is not None:
        text = pygame.font.SysFont(sysfont,size)
    else:
        if font is not None:
            text = pygame.font.Font(font,size)
        else:
            text = pygame.font.Font(".\\fonts\\SourceHanSans-Light.otf",size)
    text_fmt = text.render(_text,_antialias,color)
    textpos = text_fmt.get_rect()
    textpos.center = text_fmt.get_rect().center
    if location_type == "basic":
        pass
    elif location_type == "middle":
        textpos = text_fmt.get_rect()
    basic_display.renderer().addobject(text_fmt,location)