# -*- coding:utf-8-*
# Copyright (C) 2021 THCWorkshopCN
from modules import classes, events
from modules import global_values as gv
import pygame
from pygame.locals import *
from modules import events
from modules import classes
from app import basic_display

def render_text(_text:str,size:int=50,location:tuple=(0,0),color=(255,255,255),font:str="等线Light") -> classes.display.display_map:
    screen = gv.get("screen")
    text = pygame.font.SysFont(font,size)
    text_fmt = text.render(_text,True,color)
    screen.blit(text_fmt,location)