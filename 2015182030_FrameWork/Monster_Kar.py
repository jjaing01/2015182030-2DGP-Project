import random
import json
import os
import win32api
import math

from pico2d import *

import game_framework
import Player_Bullet
import main_state

name = "Mon_Kar"

m_MonKar = None

class CMonKar:
    def __init__(self):
        pass

    def __init__(self,x,y):
        self.x, self.y = x,y
        self.frame = 0
        self.image = None
        if self.image is None:
            self.image = load_image('Tengai/Resource/Monster/Kamikaze.png')
        self.dirX = 1.7
        self.dirY = 1.5
        self.iHp = 300
        self.m_bIsDead=False
        self.m_Rad=60
        self.m_AttackTime = random.randint(0,10)
        self.myAngle = 0.0 #플레이어를 향하는 각도
        self.max_frame = 6
        self.Frame_speed = 0.3

    def Dead_Object(self):
        self.m_bIsDead=True

    def Cal_Degree(self,ax, bx, ay, by):
        w = ax - bx
        h = ay - by
        d = math.sqrt(pow(w, 2) + pow(h, 2))

        angle = math.acos(w / d)

        if (by > ay):
            angle = angle * -1

        return angle * 180.0 / math.pi

    def Change_Dir(self):
        if self.x<=200 or self.x>1080:
            self.dirX = self.dirX * -1.0
        if self.y>=600 or self.y<=0:
            self.dirY = self.dirY * -1.0

    def update(self):
        # 죽음
        if self.m_bIsDead == True:
            return -1
        # 죽는 조건
        if self.iHp == 0:
            self.m_bIsDead=True
        # 공격 주기
        if self.m_AttackTime>80:
            main_state.m_ObjectMgr.Add_Object('MONSTER_BULLET', None, self.x, self.y)
            self.m_AttackTime=0

        self.m_AttackTime += 1

        # 움직임
        tempMonList = main_state.m_ObjectMgr.Get_PlayerList()
        self.myAngle = self.Cal_Degree(self.x, tempMonList[0].x, self.y,  tempMonList[0].y)

        self.Change_Dir()

        self.x -= math.cos(self.myAngle * math.pi / 180.0) * self.dirX
        self.y -= math.sin(self.myAngle * math.pi / 180.0) * self.dirY

        # Animation
        self.frame = (self.frame + self.Frame_speed)
        if self.frame >= self.max_frame:
            self.frame = 0

    def draw(self):
        self.image.clip_draw(int(self.frame) * 100, 0, 100, 80, self.x,self.y,50,50)

