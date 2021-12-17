# -*- coding:utf-8-*-
# Copyright (C) 2021 THCWorkshopCN

import sys

sys.dont_write_bytecode = True

import threading

import pygame
from pygame.constants import *
from pygame.locals import *
pygame.init()

from modules import events, global_values as gv
gv._init()
from modules import tools
from modules import events
events._init()

class app(object):
    def __init__(self) -> None:
        pass
    class display(object):
        """有关于显示的部分"""
        def __init__(self) -> None:
            super().__init__()
        def render_text(self,_text:str,size:int=50,location:tuple=(0,0),color=(255,255,255),font:str="等线Light") -> None:
            text = pygame.font.SysFont(font,size)
            text_fmt = text.render(_text,True,color)
            screen.blit(text_fmt,location)
        def resize(isfullscreen):
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
    def startup(self) -> None:
        global screen_size, screen, screen_width, screen_height, isfullscreen
        events.program_start().announce()
        screen_size = screen_width, screen_height = 800, 600
        fps = pygame.time.Clock()
        isfullscreen = False
        screen = pygame.display.set_mode(screen_size,RESIZABLE)
        pygame.display.set_caption("One Billions")
        screen.fill((104,204,255))
        self.display().render_text("One Billions")
        

if __name__ == "__main__": #主程序过程
    app = app()
    app.startup()
    while True:  #主循环
        isfullscreen = app.display.resize(isfullscreen)
        for event in pygame.event.get(): #循环开始
            if event.type == QUIT: #退出事件
                pygame.quit()
                sys.exit()
        #循环末尾
        pygame.display.update() #更新画面