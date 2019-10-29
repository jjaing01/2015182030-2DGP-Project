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
m_BackObj=None
font = None
reCreateTime=0

pattern = 0

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
    global  m_map,m_ObjectMgr,m_BackObj

    m_ObjectMgr = ObjectMgr.CObjectMgr()
    m_ObjectMgr.Add_Object('PLAYER')
    m_ObjectMgr.Add_Object('MON_GREEN', None, 700.0, 100.0)
    m_ObjectMgr.Add_Object('MON_GREEN', None, 700.0, 300.0)
    m_ObjectMgr.Add_Object('MON_GREEN', None, 700.0, 500.0)

    m_BackObj=BackObject.CBack_Object()
    m_map = Map()

def exit():
    global m_map,m_ObjectMgr
    del(m_map)
    del(m_BackObj)
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
    global  reCreateTime,m_ObjectMgr,m_BackObj

    reCreateTime+=1
    if reCreateTime >= 300:
        reCreateTime=0

        for mon in range(3):
            m_ObjectMgr.Add_Object('MON_GREEN', None, 700, 100)
            m_ObjectMgr.Add_Object('MON_GREEN', None, 700, 300)
            m_ObjectMgr.Add_Object('MON_GREEN', None, 700, 500)

    m_BackObj.update()
    m_ObjectMgr.Update_Object()

    delay(0.015)

def draw():
    clear_canvas()
    m_map.draw()
    m_BackObj.draw()
    m_ObjectMgr.Render_Object()
    update_canvas()

