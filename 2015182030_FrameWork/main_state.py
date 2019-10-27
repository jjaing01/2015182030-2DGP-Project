import random
import json
import os

from pico2d import *

import game_framework
import title_state
import Player

name = "MainState"

m_PBulletLst=[]
m_player = None
m_map = None
font = None

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
    global m_player, m_map,m_PBulletLst
    m_player=Player.CPlayer()
    m_map = Map()
    for n in m_PBulletLst:
        n.enter()

def exit():
    global m_player, m_map,m_PBulletLst
    del(m_player)
    del(m_map)
    for n in m_PBulletLst:
        del(n)


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
    m_player.update()
    for n in m_PBulletLst:
        n.update()

    delay(0.001)

def draw():
    clear_canvas()
    m_map.draw()
    m_player.draw()
    for n in m_PBulletLst:
        n.draw()

    update_canvas()
