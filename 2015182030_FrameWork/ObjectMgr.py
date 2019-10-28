import random
import json
import os

from pico2d import *

import Player
import Player_Bullet
import Monster_Green

PLAYER, PLAYER_BULLET, MON_GREEN = range(3)

m_ObjectLst = []
m_PlayerLst = []
m_PBulletLst = []
m_MonsterLst = []

Event = 0

m_ObjectLst.append(m_PBulletLst)
m_ObjectLst.append(m_PlayerLst)
m_ObjectLst.append(m_MonsterLst)

class CObjectMgr:

    def __init__(self):
        self.m_IsDead = 0

    def Add_Object(self, name, x=0, y=0):
        if name == 'PLAYER':
            obj = Player.CPlayer()
            m_PlayerLst.append(obj)
        elif name == 'PLAYER_BULLET':
            obj = Player_Bullet.CPlayer_Bullet(x, y)
            m_PBulletLst.append(obj)

        elif name == 'MON_GREEN':
            obj = Monster_Green.CMonGreen()
            m_MonsterLst.append(obj)
        else:
            return 0

    def Update_Object(self):

        global Event
        global m_ObjectLst

        for List in m_ObjectLst:
            for GameObj in List:
                Event = GameObj.update()

                # 게임 오브젝트 사망시 제거.
                if Event == -1:
                    List.remove(GameObj)
                    del GameObj

    def Render_Object(self):
        for List in m_ObjectLst:
            for obj in List:
                obj.draw()

    def Release_Object(self):
        for List in m_ObjectLst:
            for obj in List:
                del (obj)
