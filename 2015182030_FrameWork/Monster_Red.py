import random
import json
import os
import win32api

from pico2d import *

import game_framework
import Player_Bullet
import main_state

name = "Mon_Red"

m_MonRed = None

class CMonRed:
    def __init__(self):
        pass

    def __init__(self,x,y):
        self.x, self.y = x,y
        self.frame = 0
        self.image = None
        if self.image is None:
            self.image = load_image('Tengai/Resource/Monster/Red.png')
        self.dirX = 1.0
        self.dirY = 1.0
        self.iHp = 100
        self.m_bIsDead=False
        self.m_Rad=60
        self.m_AttackTime = random.randint(0,10)
        self.max_frame = 7
        self.Frame_speed = 0.3
        self.m_fSpeed = 60

    def Dead_Object(self):
        self.m_bIsDead=True

    def Change_Dir(self):
        if self.x <= 200 or self.x > 1080:
            self.dirX = self.dirX * -1.0
        if self.y >= 600 or self.y <= 0:
            self.dirY = self.dirY * -1.0

    def update(self):
        # 죽음
        if self.m_bIsDead == True:
            main_state.m_SoundMgr.Search_Sound('MONSTER_DEAD')
            return -1
        # 죽는 조건
        if self.iHp == 0:
            self.m_bIsDead = True

        # 공격 주기
        if self.m_AttackTime > 100:
            main_state.m_ObjectMgr.Add_Object('MONSTER_BULLET', None, self.x, self.y)
            main_state.m_ObjectMgr.Add_Object('MONSTER_BULLET', None, self.x, self.y + 30)
            main_state.m_ObjectMgr.Add_Object('MONSTER_BULLET', None, self.x, self.y - 30)
            self.m_AttackTime = 0

        self.m_AttackTime += 50 * game_framework.frame_time

        # 움직임
        self.Change_Dir()

        self.x += self.dirX * self.m_fSpeed * game_framework.frame_time
        self.y += self.dirY * self.m_fSpeed * game_framework.frame_time

        # Animation
        self.frame = (self.frame + self.Frame_speed)
        if self.frame >= self.max_frame:
            self.frame = 0

    def draw(self):
        self.image.clip_draw(int(self.frame) * 100, 0, 100, 80, self.x,self.y,50,50)

