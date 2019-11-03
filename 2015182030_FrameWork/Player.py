import random
import json
import os
import win32api

from pico2d import *

import game_framework
import Player_Bullet
import main_state

name = "Player"

m_player = None

class CPlayer:
    def __init__(self):
        self.x, self.y = 0, 90
        self.frame = 0
        self.framenum = 1
        self.image = load_image('Tengai/Resource/Player/Player.png')
        self.hpUI=None
        if self.hpUI is None:
            self.hpUI=load_image('Tengai/Resource/UI/LIFE/LIFE.png')
        self.dir = 1
        self.state='Right'
        self.m_bIsDead=False
        self.m_CreateBulletTime=0
        self.iHP = 3
        self.m_Rad = 60

    def update(self):
        if self.m_bIsDead == True:
            pass

        self.frame = (self.frame + 1) % self.framenum
        if (win32api.GetAsyncKeyState(0x25) & 0x8000 or win32api.GetAsyncKeyState(0x26) & 0x8000
                or win32api.GetAsyncKeyState(0x27) & 0x8000 or win32api.GetAsyncKeyState(0x28) & 0x8000):
            if win32api.GetAsyncKeyState(0x25) & 0x8000:
                self.x -= 5
                self.PlayerState = 'Left'
                self.dir=2
                self.framenum = 3
            if win32api.GetAsyncKeyState(0x27) & 0x8000:
                self.x += 5
                self.PlayerState = 'Right'
                self.dir=1
                self.framenum = 3
            if win32api.GetAsyncKeyState(0x26) & 0x8000:  # UP
                self.y += 5
                self.PlayerState = 'Up'
                self.framenum = 3
            if win32api.GetAsyncKeyState(0x28) & 0x8000:  # DOWN
                self.y -= 5
                self.PlayerState = 'Down'
                self.framenum = 3
            else:
                self.PlayerState = 'Idle'
                self.framenum = 1

        if win32api.GetAsyncKeyState(0x20) & 0x8000:  # SPACE
            if self.m_CreateBulletTime > 4:
                main_state.m_ObjectMgr.Add_Object('PLAYER_BULLET',None,self.x,self.y)

        if self.m_CreateBulletTime <= 5:
            self.m_CreateBulletTime += 1
        else:
            self.m_CreateBulletTime = 0

    def draw(self):
        self.image.clip_draw(self.frame * 32, 32*self.dir, 32, 32, self.x,self.y,70,70)
        self.hpUI.draw(15,580)
        self.hpUI.draw(47,580)
        self.hpUI.draw(79,580)
