import random
import json
import os

from pico2d import *

import Player
import Player_Bullet
import Monster_Green
import Monster_Kar
import Monster_Pot
import Monster_Red
import Monster_Boss
import Monster_Bullet
import CollisionMgr
import Player_Shield
import Player_FireBall
import Boss_ThunderPointer
import Boss_Thunder
import Item

PLAYER, PLAYER_BULLET, MON_GREEN = range(3)

m_ObjectLst = []
m_PlayerLst = []
m_PBulletLst = []
m_ShieldLst = []
m_MBulletLst = []
m_MonsterLst = []
m_EffectLst = []
m_ItemLst = []
m_FireBallLst = []
m_ThunderPointLst = []
m_ThunderLst = []

Event = 0

m_ObjectLst.append(m_PBulletLst)
m_ObjectLst.append(m_PlayerLst)
m_ObjectLst.append(m_MonsterLst)
m_ObjectLst.append(m_EffectLst)
m_ObjectLst.append(m_MBulletLst)
m_ObjectLst.append(m_ItemLst)
m_ObjectLst.append(m_ShieldLst)
m_ObjectLst.append(m_FireBallLst)
m_ObjectLst.append(m_ThunderPointLst)
m_ObjectLst.append(m_ThunderLst)

class CObjectMgr:

    def __init__(self):
        self.m_IsDead = 0

    def Add_Object(self, name, _obj=None, x=0, y=0,idx=0):
        if name == 'PLAYER':
            obj = Player.CPlayer()
            m_PlayerLst.append(obj)

        elif name == 'PLAYER_BULLET':
            obj = Player_Bullet.CPlayer_Bullet(x, y)
            m_PBulletLst.append(obj)

        elif name == 'PLAYER_SHIELD':
            obj = Player_Shield.CPlayer_Shield(x, y)
            m_ShieldLst.append(obj)

        elif name == 'FIRE_BALL':
            obj = Player_FireBall.CPlayer_FireBall(x, y)
            m_FireBallLst.append(obj)

        elif name == 'THUNDER_POINTER':
            obj = Boss_ThunderPointer.CBoss_ThunderPointer(x, y,idx)
            m_ThunderPointLst.append(obj)

        elif name == 'THUNDER':
            obj = Boss_Thunder.CBoss_Thunder(x, y, idx)
            m_ThunderPointLst.append(obj)

        elif name == 'MON_GREEN':
            obj = Monster_Green.CMonGreen(x,y)
            m_MonsterLst.append(obj)
        elif name == 'MON_RED':
            obj = Monster_Red.CMonRed(x, y)
            m_MonsterLst.append(obj)
        elif name == 'MON_KAR':
            obj = Monster_Kar.CMonKar(x, y)
            m_MonsterLst.append(obj)
        elif name == 'MON_POT':
            obj = Monster_Pot.CMonPot(x, y)
            m_MonsterLst.append(obj)
        elif name == 'MON_BOSS':
            obj = Monster_Boss.CMonBoss(x, y)
            m_MonsterLst.append(obj)

        elif name == 'MONSTER_BULLET':
            obj = Monster_Bullet.CMonster_Bullet(x, y,False,0)
            m_MBulletLst.append(obj)

        elif name == 'MONSTER_BOSSBULLET':
            m_MBulletLst.append(_obj)

        elif name == 'ITEM':
            m_ItemLst.append(_obj)

        elif name == 'EFFECT':
            m_EffectLst.append(_obj)
            pass
        else:
            return 0
    def Dead_Object(self):
        for List in m_ObjectLst:
            for GameObj in List:
                GameObj.IsDead()

    def Get_MonsterList(self):
        return m_MonsterLst

    def Get_PlayerList(self):
        return m_PlayerLst

    def Update_Object(self):
        global Event
        global m_ObjectLst

        CollisionMgr.Collision_Monster_PLBullet(m_MonsterLst, m_PBulletLst)
        CollisionMgr.Collision_Monster_PLBullet(m_MonsterLst, m_FireBallLst)
        CollisionMgr.Collision_Player_Item(m_PlayerLst, m_ItemLst)
        CollisionMgr.Collision_Monster_Player(m_MonsterLst,m_PlayerLst)
        CollisionMgr.Collision_Shield_MBullet(m_ShieldLst,m_MBulletLst)

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
