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
        self.m_LifeTime = 0.0
        self.m_iAtk = 50
        self.m_Rad = 10
        self.m_fSpeed = 350
        self.iNumber = 0.0
        self.m_fAngle = 0.0

    def Dead_Object(self):
        self.m_bIsDead = True

    def update(self):
        #죽음
        if self.m_bIsDead == True:
            return -1
        # 죽는 조건
        if self.m_LifeTime > 1000.0:
            self.m_bIsDead = True

        self.m_fAngle += 800.0 * game_framework.frame_time
        self.m_LifeTime += 70.0 * game_framework.frame_time

        #쉴드 방향
        tempList = main_state.m_ObjectMgr.Get_PlayerList()

        targetX,targetY = tempList[0].Get_Position()

        self.x = targetX + math.cos(self.m_fAngle * 3.141592 / 180.0) * 100.0
        self.y = targetY - math.sin(self.m_fAngle * 3.141592 / 180.0) * 100.0


        # 애니메이션
        if self.iNumber > 4.0:
            self.iNumber = 3.0

        self.iNumber += 5 * game_framework.frame_time

    def draw(self):
        image[int(self.iNumber)].draw(self.x, self.y,100,100)
