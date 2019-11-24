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


class CPlayer_Shield:
    def __init__(self):
        pass

    def __init__(self, _x, _y):
        global image, image_num
        self.x, self.y = _x, _y

        address='Tengai/Resource/Shield/'
        extension ='.png'

        for n in range(0, 4):
            all_address = address + str(n) + extension
            image_num = load_image(all_address)
            image.append(image_num)

        self.m_bIsDead = False
        self.m_LifeTime = 100
        self.m_iAtk = 50
        self.m_Rad = 8
        self.m_fSpeed = 350
        self.iNumber = 0.0

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
        self.x += self.m_fSpeed * game_framework.frame_time

        # 애니메이션
        if self.iNumber > 4.0:
            self.iNumber = 3.0

        self.iNumber += 5 * game_framework.frame_time

    def draw(self):
        image[int(self.iNumber)].draw(self.x, self.y,100,100)
