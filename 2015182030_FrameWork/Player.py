import random
import json
import os
import win32api

from pico2d import *

import game_framework
import Player_Bullet
import main_state
import Effect
import ObjectMgr
import CollisionMgr

name = "Player"

m_player = None

class CPlayer:
    def __init__(self):
        self.x, self.y = 0, 90
        self.frame = 0
        self.framenum = 1
        # Player
        self.image = load_image('Tengai/Resource/Player/Player.png')
        # Life UI
        self.hpUI = None
        if self.hpUI is None:
            self.hpUI = load_image('Tengai/Resource/UI/LIFE/LIFE.png')
        # Skill UI
        self.skillUI = None
        if self.skillUI is None:
            self.skillUI = load_image('Tengai/Resource/UI/Ultimate/Ultimate.png')

        self.dir = 1
        self.state = 'Right'
        self.m_bIsDead=False
        self.m_CreateBulletTime = 0
        self.m_CreateTigerSkillTime = 0
        self.m_bIsSkill_Tiger = False
        self.iHP = 3
        self.m_Rad = 60
        self.m_SkillCnt = 3
        self.m_fSpeed = 250

    def update(self):
        if self.m_bIsDead == True:
            pass

        self.frame = (self.frame + 1) % self.framenum
        if (win32api.GetAsyncKeyState(0x25) & 0x8000 or win32api.GetAsyncKeyState(0x26) & 0x8000
                or win32api.GetAsyncKeyState(0x27) & 0x8000 or win32api.GetAsyncKeyState(0x28) & 0x8000):
            if win32api.GetAsyncKeyState(0x25) & 0x8000:
                self.x -= self.m_fSpeed * game_framework.frame_time
                self.PlayerState = 'Left'
                self.dir = 2
                self.framenum = 3
            if win32api.GetAsyncKeyState(0x27) & 0x8000:
                self.x += self.m_fSpeed * game_framework.frame_time
                self.PlayerState = 'Right'
                self.dir = 1
                self.framenum = 3
            if win32api.GetAsyncKeyState(0x26) & 0x8000:  # UP
                self.y += self.m_fSpeed * game_framework.frame_time
                self.PlayerState = 'Up'
                self.framenum = 3
            if win32api.GetAsyncKeyState(0x28) & 0x8000:  # DOWN
                self.y -= self.m_fSpeed * game_framework.frame_time
                self.PlayerState = 'Down'
                self.framenum = 3
            else:
                self.PlayerState = 'Idle'
                self.framenum = 1

        if win32api.GetAsyncKeyState(0x20) & 0x8000:  # SPACE
            if self.m_CreateBulletTime > 4:
                main_state.m_ObjectMgr.Add_Object('PLAYER_BULLET',None,self.x,self.y)

        if win32api.GetAsyncKeyState(0x31) & 0x8000:  # 1
            if self.m_bIsSkill_Tiger == False:
                # PosX, PosY, CX, CY, Speed, IsSingleEffect, IsAnimationEndDead, MaxFrame, LifeTime, ScaleX, ScaleY, FileName
                GameObj = Effect.CEffect(self.x,60, 256, 256, 0.3, False, False, 64, 10, 800, 800, "PSkill.png")
                main_state.m_ObjectMgr.Add_Object("EFFECT", GameObj)
                CollisionMgr.Collision_Skill_1(ObjectMgr.m_MonsterLst)

            self.m_bIsSkill_Tiger = True

        if win32api.GetAsyncKeyState(0x32) & 0x8000:  # 2
            if self.m_CreateBulletTime > 4:
                main_state.m_ObjectMgr.Add_Object("PLAYER_SHIELD", None, self.x, self.y)

        if self.m_CreateBulletTime <= 5:
            self.m_CreateBulletTime += 50 * game_framework.frame_time
        else:
            self.m_CreateBulletTime = 0

        if self.m_bIsSkill_Tiger:
            if self.m_CreateTigerSkillTime <= 50:
                self.m_CreateTigerSkillTime += 10 * game_framework.frame_time
            else:
                self.m_CreateTigerSkillTime = 0
                if self.m_SkillCnt >= 1:
                    self.m_SkillCnt -= 1
                self.m_bIsSkill_Tiger = False

    def draw(self):
        self.image.clip_draw(self.frame * 32, 32 * self.dir, 32, 32, self.x, self.y, 70, 70)

        # Player HP
        if self.iHP >= 3:
            self.hpUI.draw(15,580)
            self.hpUI.draw(47,580)
            self.hpUI.draw(79,580)
        elif self.iHP == 2:
            self.hpUI.draw(15, 580)
            self.hpUI.draw(47, 580)
        elif self.iHP == 1:
            self.hpUI.draw(15, 580)
        elif self.iHP == 0:
            pass

        # Player Skill
        if self.m_SkillCnt >= 3:
            self.skillUI.draw(15, 530)
            self.skillUI.draw(47, 530)
            self.skillUI.draw(79, 530)
        elif self.m_SkillCnt == 2:
            self.skillUI.draw(15, 530)
            self.skillUI.draw(47, 530)
        elif self.m_SkillCnt == 1:
            self.skillUI.draw(15, 530)
        elif self.m_SkillCnt == 0:
            pass

    def Skill_plus(self):
        if self.m_SkillCnt < 4:
            self.m_SkillCnt += 1

    def Set_Life(self):
        self.iHP -= 1

    def HP_plus(self):
        if self.iHP < 4:
            self.iHP += 1

    def Get_Position(self):
        return self.x,self.y
