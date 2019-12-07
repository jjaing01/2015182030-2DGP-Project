import random
import json
import os
import win32api
import math

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
        self.m_iAtk = 10
        self.m_Rad = 10
        self.m_fSpeed = 250

    def __init__(self, _x, _y, randDir,_angle):
        self.x, self.y = _x, _y
        if CMonster_Bullet.image is None:
            CMonster_Bullet.image = load_image('Tengai/Resource/Bullet/Monster/enemyMissile.png')
        self.m_bIsDead = False
        self.m_LifeTime = 100
        self.m_iAtk = 10
        self.m_Rad = 13
        self.m_bIsRandomShoot = randDir
        self.m_Angle = _angle
        self.m_fSpeed = 250
        main_state.m_SoundMgr.Search_Sound('MONSTER_BULLET')

    def Dead_Object(self):
        self.m_bIsDead = True

    def update(self):
        if self.m_bIsDead == True:
            return -1

        if 0 >= self.x:
            self.m_bIsDead = True

        if self.m_bIsRandomShoot == True:
            self.x -= math.cos(self.m_Angle * math.pi / 180.0) * self.m_fSpeed * game_framework.frame_time
            self.y -= math.sin(self.m_Angle * math.pi / 180.0) * self.m_fSpeed * game_framework.frame_time
        else:
            self.x -= self.m_fSpeed * game_framework.frame_time

    def draw(self):
        CMonster_Bullet.image.draw(self.x, self.y, 27, 29)
