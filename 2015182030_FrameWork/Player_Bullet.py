import random
import json
import os
import win32api

from pico2d import *

import game_framework
import main_state

name = "PlayerBullet"

class CPlayer_Bullet:
    def __init__(self):
        pass

    def __init__(self, _x, _y):
        self.rand=random.randint(0,1)
        self.x, self.y = _x, _y
        self.m_image = None

        if  self.m_image is None:
            address='Tengai/Resource/Bullet/Player/Bullet_Player'
            extension ='.png'
            all_address = address+str(self.rand)+extension
            self.m_image = load_image(all_address)

        self.m_bIsDead = False
        self.m_LifeTime = 100
        self.m_iAtk=50
        self.m_Rad=8


    def Dead_Object(self):
        self.m_bIsDead = True

    def update(self):
        #죽음
        if self.m_bIsDead == True:
            return -1
        # 죽는 조건
        if 1080 <= self.x:
            self.m_bIsDead = True
        #총알 방향
        self.x += 5

    def draw(self):
        self.m_image.draw(self.x, self.y, 16, 8)
