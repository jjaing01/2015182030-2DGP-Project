import random
import json
import os
import win32api

from pico2d import *

import game_framework
import Player_Bullet
import main_state

name = "Mon_Green"

m_MonGreen = None

class CMonGreen:
    def __init__(self):
        self.x, self.y = 500,400
        self.frame = 0
        self.image = load_image('Tengai/Resource/Monster/Green.png')
        self.dir = 1
        self.iHp = 100
        self.m_bIsDead=False
        self.m_Rad=60

    def __init__(self,x,y):
        self.x, self.y = x,y
        self.frame = 0
        self.image = load_image('Tengai/Resource/Monster/Green.png')
        self.dir = 1
        self.iHp = 100
        self.m_bIsDead=False
        self.m_Rad=60

    def Dead_Object(self):
        self.m_bIsDead=True

    def update(self):
        if self.m_bIsDead == True:
            return -1

        if self.iHp == 0:
            self.m_bIsDead=True

        self.frame = (self.frame + 1) % 4
        self.x -= 1

    def draw(self):
        self.image.clip_draw(self.frame * 100, 0, 100, 80, self.x,self.y,70,70)

