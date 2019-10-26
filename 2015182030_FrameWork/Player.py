import random
import json
import os

from pico2d import *

import game_framework

name = "Player"

m_player = None

class CPlayer:
    def __init__(self):
        self.x, self.y = 0, 90
        self.frame = 0
        self.image = load_image('Tengai/Resource/Player/Player.png')
        self.dir = 1

    def update(self):
        self.frame = (self.frame + 1) % 2
        self.x += self.dir
        if self.x >= 800:
            self.dir = -1

        elif self.x <= 0:
            self.dir = 1

    def draw(self):
        self.image.clip_draw(self.frame * 32, 32, 32, 32, self.x,self.y,70,70)


def enter():
    global m_player
    m_player = CPlayer()


def exit():
    global m_player
    del(m_player)


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
    m_player.update()
    pass

def draw():
    clear_canvas()
    m_player.draw()
    update_canvas()
