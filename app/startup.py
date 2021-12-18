# -*- coding:utf-8-*
# Copyright (C) 2021 THCWorkshopCN
"""程序启动模块"""

from modules import classes, events
from modules import global_values as gv
import pygame
from pygame.locals import *
from modules import events
from modules import classes
from app import basic_display


def startup() -> None:
    """启动程序"""
    global screen_size, screen, screen_width, screen_height, isfullscreen
    screen = gv.get("screen")
    screen_size = gv.get("screen_size")
    screen_width = gv.get("screen_width")
    screen_height = gv.get("screen_height")
    
    events.program_start().announce()
    isfullscreen = False
    gv.set("isfullscreen",isfullscreen)
    screen = pygame.display.set_mode(screen_size,RESIZABLE)
    gv.set("screen",screen)
    pygame.display.set_caption("One Billions")
    screen.fill((104,204,255))
    basic_display.render_text("One Billions")