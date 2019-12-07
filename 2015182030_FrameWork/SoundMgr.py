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

m_SoundLst = []

Event = 0


class CSoundMgr:

    def __init__(self):
        self.m_IsDead = 0
        self.Monster_Bullet = load_wav('Tengai/Sound/Attack.wav')
        self.Monster_Bullet.set_volume(32)
        self.Monster_Bullet.play(1)
        m_SoundLst.append(self.Monster_Bullet)

        self.Player_Skill = load_wav('Tengai/Sound/AyinSpecialAttack.wav')
        self.Player_Skill.set_volume(32)
        self.Player_Skill.play(1)
        m_SoundLst.append(self.Player_Skill)

        self.Monster_Dead = load_wav('Tengai/Sound/Explode.wav')
        self.Monster_Dead.set_volume(32)
        self.Monster_Dead.play(1)
        m_SoundLst.append(self.Monster_Dead)

        self.Item = load_music('Tengai/Sound/Item.mp3')
        self.Item.set_volume(32)
        self.Item.play(1)
        m_SoundLst.append(self.Item)

    def Dead_Object(self):
        for List in m_SoundLst:
            for GameObj in List:
                GameObj.IsDead()

    def Update_Object(self):
        global Event
        global m_SoundLst

        for List in m_SoundLst:
            for GameObj in List:
                Event = GameObj.update()

                # 게임 오브젝트 사망시 제거.
                if Event == -1:
                    List.remove(GameObj)
                    del GameObj


    def Release_Object(self):
        for List in m_SoundLst:
            for obj in List:
                del (obj)