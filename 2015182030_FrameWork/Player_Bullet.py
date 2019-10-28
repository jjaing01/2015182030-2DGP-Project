import random
import json
import os
import win32api

from pico2d import *

import game_framework

import main_state

name = "PlayerBullet"

class CPlayer_Bullet:
    image = None

    def __init__(self):
        pass

    def __init__(self, _x, _y):
        self.x, self.y = _x, _y
        if CPlayer_Bullet.image is None:
            CPlayer_Bullet.image = load_image('Tengai/Resource/Bullet/Player/Bullet_Player.png')
        self.m_bIsDead = False
        self.m_LifeTime = 100

    def update(self):
        if self.m_bIsDead == True:
            return -1

        if 500 < self.x:
            self.m_bIsDead = True

        self.x += 1


    def draw(self):
        print('render')
        CPlayer_Bullet.image.draw(self.x, self.y, 14, 8)
