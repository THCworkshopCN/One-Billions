# -*- coding:utf-8-*
# Copyright (C) 2021 THCWorkshopCN
"""基础的显示模块"""

from modules import classes
from modules import global_values as gv
import pygame
from pygame.locals import *
def _init():
    """初始化display模块"""
    global screen,screen_size,screen_width,screen_height
    screen_size = screen_width, screen_height = 800, 600
    global fps
    fps = pygame.time.Clock()
    screen = pygame.display.set_mode(screen_size,RESIZABLE)
    gv.set("screen",screen)
    gv.set("screen_size",screen_size)
    gv.set("screen_width",screen_width)
    gv.set("screen_height",screen_height)

def render_text(_text:str,size:int=50,location:tuple=(0,0),color=(255,255,255),font:str="等线Light") -> classes.display.display_map:
    text = pygame.font.SysFont(font,size)
    text_fmt = text.render(_text,True,color)
    screen.blit(text_fmt,location)

class renderer(object):
    def __init__(self) -> None:
        pass
    def addobject(self,_source) -> classes.display.display_map:
        """往下一次渲染计划中添加object"""
        pass
    def render(self) -> classes.display:
        """渲染画面"""
        pass

def resize(isfullscreen) -> classes.display:
    # 这个函数中必须先判断窗口大小是否变化，在判断是否全屏
    # 否则，在全屏之后，pygame会判定为全屏操作也是改变窗体大小的一个操作，所以会显示一个比较大的窗口但不是全屏模式
    for event in pygame.event.get(VIDEORESIZE):
        screen_size = screen_width, screen_height = event.size[0], event.size[1]
        screen = pygame.display.set_mode((screen_width, screen_height), RESIZABLE)
    for event in pygame.event.get(KEYDOWN):
        if event.key == K_F11:
            if not isfullscreen:
                isfullscreen = True
                screen_size = screen_width, screen_height =  pygame.display.list_modes()[0]
                screen = pygame.display.set_mode(screen_size, FULLSCREEN)
            else:
                isfullscreen = False 
                screen_size = screen_width, screen_height = 1000, 800
                screen = pygame.display.set_mode((screen_width, screen_height), RESIZABLE)
        pygame.event.post(event)
    return isfullscreen