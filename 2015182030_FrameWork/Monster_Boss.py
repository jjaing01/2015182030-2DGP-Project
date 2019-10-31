import random
import json
import os
import win32api

from pico2d import *

import game_framework
import Player_Bullet
import Monster_Bullet
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
        self.dirX = 1.0
        self.dirY = 1.0
        self.iHp = 5000
        self.m_bIsDead=False
        self.m_Rad=100
        self.m_AttackTime = random.randint(0,10)
        self.max_frame = 3
        self.Frame_speed = 0.3
        self.AtkPattern = 0
        self.bIsAtkPattern = True

    def Dead_Object(self):
        self.m_bIsDead = True

    def Change_Dir(self):
        if self.x <= 600 or self.x > 1080:
            self.dirX = self.dirX * -1.0
        if self.y >= 600 or self.y <= 200:
            self.dirY = self.dirY * -1.0

    def update(self):
        # 죽음
        if self.m_bIsDead == True:
            return -1
        # 죽는 조건
        if self.iHp == 0:
            self.m_bIsDead = True

        # 공격 주기
        if self.m_AttackTime > 80:
            main_state.m_ObjectMgr.Add_Object('MONSTER_BULLET', None, self.x, self.y)
            self.m_AttackTime = 0
            self.bIsAtkPattern = True

        self.m_AttackTime += 1

        # 공격 패턴
        # 1. 난사 1회
        if self.AtkPattern == 0 and self.bIsAtkPattern == True:
            main_state.m_ObjectMgr.Add_Object('MONSTER_BOSSBULLET',Monster_Bullet.CMonster_Bullet(self.x, self.y, True, 235))
            main_state.m_ObjectMgr.Add_Object('MONSTER_BOSSBULLET',Monster_Bullet.CMonster_Bullet(self.x, self.y, True, 275))
            main_state.m_ObjectMgr.Add_Object('MONSTER_BOSSBULLET',Monster_Bullet.CMonster_Bullet(self.x, self.y, True, 305))
            main_state.m_ObjectMgr.Add_Object('MONSTER_BOSSBULLET',Monster_Bullet.CMonster_Bullet(self.x, self.y, True, 335))
            main_state.m_ObjectMgr.Add_Object('MONSTER_BOSSBULLET',Monster_Bullet.CMonster_Bullet(self.x, self.y, True, 365))
            main_state.m_ObjectMgr.Add_Object('MONSTER_BOSSBULLET',Monster_Bullet.CMonster_Bullet(self.x, self.y, True, 175))
            main_state.m_ObjectMgr.Add_Object('MONSTER_BOSSBULLET',Monster_Bullet.CMonster_Bullet(self.x, self.y, True, 205))
            main_state.m_ObjectMgr.Add_Object('MONSTER_BOSSBULLET',Monster_Bullet.CMonster_Bullet(self.x, self.y, True, 145))
            main_state.m_ObjectMgr.Add_Object('MONSTER_BOSSBULLET',Monster_Bullet.CMonster_Bullet(self.x, self.y, True, 105))
            main_state.m_ObjectMgr.Add_Object('MONSTER_BOSSBULLET',Monster_Bullet.CMonster_Bullet(self.x, self.y, True, 75))
            main_state.m_ObjectMgr.Add_Object('MONSTER_BOSSBULLET',Monster_Bullet.CMonster_Bullet(self.x, self.y, True, 45))
            main_state.m_ObjectMgr.Add_Object('MONSTER_BOSSBULLET',Monster_Bullet.CMonster_Bullet(self.x, self.y, True, 15))
            self.bIsAtkPattern=False
            self.AtkPattern=0

        # 2.유도탄 3발
        # 3.레이저
        # 4.투명

        #움직임
        self.Change_Dir()

        self.y += self.dirY
        self.x += self.dirX

        # Animation
        self.frame = (self.frame + self.Frame_speed)
        if self.frame >= self.max_frame:
            self.frame = 0

    def draw(self):
        self.image.clip_draw(int(self.frame) * 450, 0, 450, 500, self.x,self.y,300,300)

