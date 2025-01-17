import random
import json
import os

from pico2d import *

import game_framework
import title_state
import Player
import Monster_Green
import Monster_Kar
import Monster_Pot
import Monster_Red
import Monster_Boss
import ObjectMgr
import BackObject
import SoundMgr

name = "MainState"

m_ObjectMgr = None
m_map = None
m_BackObj1=None
m_BackObj2=None
m_SoundMgr = None
font = None
reCreateTime = 0

m_pattern = 0
m_bIsCreate=True

class Font:
    def __init__(self):
        self.image = load_image('pause.png')

    def draw(self):
        self.image.draw(400, 300)

class Map:
    def __init__(self):
        self.image = load_image('Tengai/Resource/Map/forest.png')
        self.image2 = load_image('Tengai/Resource/Map/forest.png')
        self.m_ScrollX = 5.0
        self.m_Map1_ScrollX = 540.0
        self.m_Map2_ScrollX = 1620.0
        self.bgm = load_music('Tengai/Sound/tengai.ogg')
        self.bgm.set_volume(64)
        self.bgm.repeat_play()

    def draw(self):
        #self.image.draw(400, 300)
        self.image.clip_draw(0,0,3520,720,self.m_Map1_ScrollX,300,1080,600)
        self.image2.clip_draw(0,0,3520,720,self.m_Map2_ScrollX,300,1080,600)

    def update(self):
        self.m_Map1_ScrollX -= self.m_ScrollX
        self.m_Map2_ScrollX -= self.m_ScrollX

        if self.m_Map1_ScrollX < -540.0:
            self.m_Map1_ScrollX = 1610.0

        if self.m_Map2_ScrollX < -540.0:
            self.m_Map2_ScrollX = 1610.0

def enter():
    global m_map, m_ObjectMgr, m_BackObj1, m_BackObj2, m_SoundMgr

    m_ObjectMgr = ObjectMgr.CObjectMgr()
    m_ObjectMgr.Add_Object('PLAYER')
    m_ObjectMgr.Add_Object('MON_GREEN', None, 700.0, 100.0)
    m_ObjectMgr.Add_Object('MON_GREEN', None, 700.0, 300.0)
    m_ObjectMgr.Add_Object('MON_GREEN', None, 700.0, 500.0)

    m_SoundMgr = SoundMgr.CSoundMgr()

    m_BackObj1 = BackObject.CBack_Object(240,500)
    m_BackObj2 = BackObject.CBack_Object(1300,500)
    m_map = Map()

def exit():
    global m_map,m_ObjectMgr,m_BackObj1,m_BackObj2
    del(m_map)
    del(m_BackObj1)
    del(m_BackObj2)
    m_ObjectMgr.Release_Object()

def pause():
    pass

def resume():
    pass

def handle_events():
   events = get_events()
   for event in events:
       if event.type == SDL_QUIT:
           game_framework.quit()
       elif event.type == SDL_KEYDOWN and event.key == SDLK_ESCAPE:
           game_framework.change_state(title_state)
       elif event.type == SDL_KEYDOWN and event.key == SDLK_p:
           pass


def update():
    global  reCreateTime,m_ObjectMgr,m_BackObj,m_pattern,m_bIsCreate

    tempMonList = m_ObjectMgr.Get_MonsterList()

    # 패턴마다 나오는 몬스터를 다 죽이면 다음 패턴으로 이동
    if len(tempMonList) <= 0:
        m_pattern += 1
        m_bIsCreate = True

    # 패턴 1
    if m_pattern == 0 and m_bIsCreate == True:
        m_ObjectMgr.Add_Object('MON_KAR', None, 1080, 300)
        m_ObjectMgr.Add_Object('MON_KAR', None, 1080, 500)
        m_ObjectMgr.Add_Object('MON_POT', None, 1080, 300)
        m_ObjectMgr.Add_Object('MON_RED', None, 1080, 500)
        m_ObjectMgr.Add_Object('MON_GREEN', None, 900, 400)
        m_ObjectMgr.Add_Object('MON_GREEN', None, 900, 200)
        m_bIsCreate = False

    # 패턴 2
    elif m_pattern == 1 and m_bIsCreate == True:
        m_ObjectMgr.Add_Object('MON_RED', None, 1080, 100)
        m_ObjectMgr.Add_Object('MON_RED', None, 1080, 300)
        m_ObjectMgr.Add_Object('MON_GREEN', None, 1080, 500)
        m_ObjectMgr.Add_Object('MON_POT', None, 900, 400)
        m_ObjectMgr.Add_Object('MON_POT', None, 900, 200)
        m_ObjectMgr.Add_Object('MON_KAR', None, 900, 300)
        m_bIsCreate = False

    # 패턴 3
    elif m_pattern == 2 and m_bIsCreate == True:
        m_ObjectMgr.Add_Object('MON_GREEN', None, 1080, 100)
        m_ObjectMgr.Add_Object('MON_RED', None, 1080, 300)
        m_ObjectMgr.Add_Object('MON_RED', None, 1080, 500)
        m_ObjectMgr.Add_Object('MON_RED', None, 900, 400)
        m_ObjectMgr.Add_Object('MON_GREEN', None, 900, 200)
        m_bIsCreate = False

        # 패턴 3
    elif m_pattern == 3 and m_bIsCreate == True:
        m_ObjectMgr.Add_Object('MON_KAR', None, 1080, 100)
        m_ObjectMgr.Add_Object('MON_KAR', None, 1080, 300)
        m_ObjectMgr.Add_Object('MON_KAR', None, 1080, 500)
        m_ObjectMgr.Add_Object('MON_KAR', None, 900, 400)
        m_ObjectMgr.Add_Object('MON_KAR', None, 900, 200)
        m_bIsCreate = False

    # 패턴 4 - 보스
    elif m_pattern == 4 and m_bIsCreate == True:
        m_ObjectMgr.Add_Object('MON_BOSS', None, 800, 400)
        m_ObjectMgr.Add_Object('MON_KAR', None, 1080, 300)
        m_ObjectMgr.Add_Object('MON_KAR', None, 1080, 500)
        m_ObjectMgr.Add_Object('MON_KAR', None, 900, 400)
        m_ObjectMgr.Add_Object('MON_KAR', None, 900, 200)
        m_bIsCreate = False

    m_BackObj1.update()
    m_BackObj2.update()
    m_map.update()
    m_ObjectMgr.Update_Object()

    #delay(0.015)

def draw():
    clear_canvas()
    m_map.draw()
    m_BackObj1.draw()
    m_BackObj2.draw()
    m_ObjectMgr.Render_Object()
    update_canvas()

