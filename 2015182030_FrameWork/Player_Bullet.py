import random
import json
import os
import win32api

from pico2d import *

import game_framework

name = "PlayerBullet"

m_playerBullet = None

class CPlayer_Bullet:
    def __init__(self):
        pass

    def __init__(self,x,y):
        self.x, self.y = x,y
        self.image = load_image('Tengai/Resource/Bullet/Player/Bullet_Player.png')

    def update(self):
        self.x+=1

    def draw(self):
        self.image.draw(self.x,self.y,14,8)

def enter():
    global m_playerBullet
    m_playerBullet = CPlayer_Bullet()

def exit():
    global m_playerBullet
    del(m_playerBullet)


def pause():
    pass


def resume():
    pass


def handle_events():
   events = get_events()
   for event in events:
       if event.type == SDL_KEYDOWN and event.key == SDLK_p:
           pass

def update():
    m_playerBullet.update()

def draw():
    clear_canvas()
    m_playerBullet.draw()
    update_canvas()
