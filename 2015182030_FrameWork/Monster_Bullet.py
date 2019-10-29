import random
import json
import os
import win32api

from pico2d import *

import game_framework

import main_state

name = "MonsterBullet"

class CMonster_Bullet:
    image = None

    def __init__(self):
        pass

    def __init__(self, _x, _y):
        self.x, self.y = _x, _y
        if CMonster_Bullet.image is None:
            CMonster_Bullet.image = load_image('Tengai/Resource/Bullet/Monster/enemyMissile.png')
        self.m_bIsDead = False
        self.m_LifeTime = 100
        self.m_iAtk=10
        self.m_Rad=10

    def Dead_Object(self):
        self.m_bIsDead = True

    def update(self):
        if self.m_bIsDead == True:
            return -1

        if 800 < self.x:
            self.m_bIsDead = True

        self.x -= 5

    def draw(self):
        CMonster_Bullet.image.draw(self.x, self.y, 27, 29)
