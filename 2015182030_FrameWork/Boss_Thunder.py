import random
import json
import os
import win32api

from pico2d import *

import game_framework
import main_state

name = "PlayerBullet"

image = []
image_num=None


class CBoss_Thunder:
    def __init__(self):
        pass

    def __init__(self, _x, _y, idx):
        global image, image_num
        self.x, self.y = _x, _y

        address = 'Tengai/Resource/Bullet/Thunder/Thunder'
        extension ='.png'

        for n in range(0, 10):
            all_address = address + str(n) + extension
            image_num = load_image(all_address)
            image.append(image_num)

        self.m_bIsDead = False
        self.m_LifeTime = 0.0
        self.m_iAtk = 200
        self.m_Rad = 15
        self.m_fSpeed = random.randint(100,450)
        self.iNumber = 0.0
        self.m_fAngle = 0.0

        if idx == 1:
            main_state.m_SoundMgr.Search_Sound("BOSS_THUNDER")

    def Dead_Object(self):
        self.m_bIsDead = True

    def update(self):
        #죽음
        if self.m_bIsDead == True:
            return -1
        # 죽는 조건
        if self.m_LifeTime > 800.0:
            self.m_bIsDead = True

        self.m_LifeTime += 70.0 * game_framework.frame_time

        # 애니메이션
        if self.iNumber > 9.0:
            self.m_bIsDead = True

        self.iNumber += 15.0 * game_framework.frame_time

    def draw(self):
        #image[int(self.iNumber)].draw(self.x, self.y,50, 50)
        image[int(self.iNumber)].clip_composite_draw(int(self.iNumber), 0, 140, 650, self.m_fAngle, '', self.x, self.y)
