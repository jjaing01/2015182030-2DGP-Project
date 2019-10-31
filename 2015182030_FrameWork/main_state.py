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

name = "MainState"

m_ObjectMgr = None
m_map = None
m_BackObj1=None
m_BackObj2=None
font = None
reCreateTime=0

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

    def draw(self):
        self.image.draw(400, 300)


def enter():
    global  m_map,m_ObjectMgr,m_BackObj1,m_BackObj2

    m_ObjectMgr = ObjectMgr.CObjectMgr()
    m_ObjectMgr.Add_Object('PLAYER')
    m_ObjectMgr.Add_Object('MON_GREEN', None, 700.0, 100.0)
    m_ObjectMgr.Add_Object('MON_GREEN', None, 700.0, 300.0)
    m_ObjectMgr.Add_Object('MON_GREEN', None, 700.0, 500.0)

    m_BackObj1=BackObject.CBack_Object(240,500)
    m_BackObj2=BackObject.CBack_Object(1300,500)
    m_map = Map()

def exit():
    global m_map,m_ObjectMgr
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
        m_ObjectMgr.Add_Object('MON_GREEN', None, 1080, 300)
        m_ObjectMgr.Add_Object('MON_GREEN', None, 1080, 500)
        m_ObjectMgr.Add_Object('MON_GREEN', None, 900, 400)
        m_ObjectMgr.Add_Object('MON_GREEN', None, 900, 200)
        m_bIsCreate = False

    # 패턴 4 - 보스
    elif m_pattern == 3 and m_bIsCreate == True:
        m_ObjectMgr.Add_Object('MON_BOSS', None, 800, 400)
        m_ObjectMgr.Add_Object('MON_KAR', None, 1080, 300)
        m_ObjectMgr.Add_Object('MON_KAR', None, 1080, 500)
        m_ObjectMgr.Add_Object('MON_KAR', None, 900, 400)
        m_ObjectMgr.Add_Object('MON_KAR', None, 900, 200)
        m_bIsCreate = False

    # 보스 죽을 시 다음 스테이지 전환

    m_BackObj1.update()
    m_BackObj2.update()
    m_ObjectMgr.Update_Object()

    delay(0.015)

def draw():
    clear_canvas()
    m_map.draw()
    m_BackObj1.draw()
    m_BackObj2.draw()
    m_ObjectMgr.Render_Object()
    update_canvas()

