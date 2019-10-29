import random
import json
import os
import win32api

from pico2d import *

import game_framework
import Player_Bullet
import main_state

name = "Mon_Boss"

m_MonBoss = None

class CMonBoss:
    def __init__(self):
       pass

    def __init__(self,x,y):
        self.x, self.y = x,y
        self.frame = 0
        self.image = load_image('Tengai/Resource/Monster/Boss.png')
        self.dir = 0.5
        self.iHp = 1000
        self.m_bIsDead=False
        self.m_Rad=100
        self.m_AttackTime = random.randint(0,10)
        self.max_frame = 3
        self.Frame_speed = 0.3

    def Dead_Object(self):
        self.m_bIsDead = True

    def update(self):
        if self.m_bIsDead == True:
            return -1

        if self.iHp == 0:
            self.m_bIsDead = True

        if self.m_AttackTime>80:
            main_state.m_ObjectMgr.Add_Object('MONSTER_BULLET', None, self.x, self.y)
            self.m_AttackTime=0

        self.m_AttackTime+=1

        if self.y>=500 or self.y<=50:
            self.dir = dir*-1.0

        self.y += self.dir

        # Animation
        self.frame = (self.frame + self.Frame_speed)
        if self.frame >= self.max_frame:
            self.frame = 0

    def draw(self):
        self.image.clip_draw(int(self.frame) * 450, 0, 450, 500, self.x,self.y,300,300)

