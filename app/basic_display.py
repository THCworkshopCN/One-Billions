# -*- coding:utf-8-*
# Copyright (C) 2021 THCWorkshopCN
"""基础的显示模块"""

from modules import classes
from modules import global_values as gv
import pygame
from pygame.locals import *
def _init():
    """初始化display模块"""
    global screen,screen_size,screen_width,screen_height,background
    screen_size = screen_width, screen_height = 800, 600
    global fps
    fps = pygame.time.Clock()
    screen = pygame.display.set_mode(screen_size,RESIZABLE)
    background = pygame.Surface(screen.get_size())
    gv.set("screen",screen)
    gv.set("screen_size",screen_size)
    gv.set("screen_width",screen_width)
    gv.set("screen_height",screen_height)
    gv.set("background",background)
    global object_list
    object_list = []

class renderer(object):
    def __init__(self) -> None:
        global _fill
        global object_list
    def addobject(self,_source,location,name = None) -> classes.display.display_map:
        """往下一次渲染计划中添加object"""
        if not name is None:
            args = {"_source":_source,"location":location,"name":name}
        else:
            args = {"_source":_source,"location":location}
        object_list.append(args)
    def fill(self,color:tuple):
        global _fill_R, _fill_G, _fill_B
        _fill_R, _fill_G, _fill_B = color
    def render(self) -> classes.display:
        """渲染画面"""
        screen.fill((_fill_R,_fill_G,_fill_B))
        for i in range(len(object_list)):
            screen.blit(object_list[i]["_source"],object_list[i]["location"])

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