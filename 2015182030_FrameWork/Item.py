import random
import json
import os
import win32api

from pico2d import *

import game_framework
import Player_Bullet
import main_state


class CItem:
    def __init__(self):
       pass

    def __init__(self,x,y):
        self.x, self.y = x,y
        self.frame = 0
        self.rand = random.randint(0,1)
        self.image=None
        print(self.rand)
        if self.image is None:
            if self.rand == 0:
                self.image = load_image('Tengai/Resource/Item0.png')
            elif self.rand == 1:
                self.image = load_image('Tengai/Resource/Item1.png')

        self.dirX = 0.5
        self.dirY = 0.5
        self.m_bIsDead=False
        self.m_Rad=60

    def Dead_Object(self):
        self.m_bIsDead = True

    def Get_ItemOption(self):
        return self.rand

    def Change_Dir(self):
        if self.x<=200 or self.x > 1080:
            self.dirX = self.dirX * -1.0
        if self.y>=600 or self.y <= 0:
            self.dirY = self.dirY * -1.0

    def update(self):
        # 죽음
        if self.m_bIsDead == True:
            main_state.m_SoundMgr.Search_Sound('ITEM')
            return -1

        # 움직임
        self.Change_Dir()

        self.x += self.dirX
        self.y += self.dirY

        self.frame = (self.frame + 1) % 1



    def draw(self):
        if self.rand == 0:
            self.image.clip_draw(self.frame * 192, 0, 192, 98, self.x,self.y,50,50)
        elif self.rand == 1:
            self.image.clip_draw(self.frame * 190, 0, 190, 105, self.x, self.y, 50, 50)

