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
        self.image = load_image('Tengai/Resource/Player/Player.png')
        self.dir = 1
        self.state='Right'

    def update(self):
        self.frame = (self.frame + 1) % 2
        if (win32api.GetAsyncKeyState(0x25) & 0x8000 or win32api.GetAsyncKeyState(0x26) & 0x8000
                or win32api.GetAsyncKeyState(0x27) & 0x8000 or win32api.GetAsyncKeyState(0x28) & 0x8000):
            if win32api.GetAsyncKeyState(0x25) & 0x8000:
                self.x -= 1
                self.PlayerState = 'Left'
            if win32api.GetAsyncKeyState(0x27) & 0x8000:
                self.x += 1
                self.PlayerState = 'Right'
            if win32api.GetAsyncKeyState(0x26) & 0x8000:  # UP
                self.y += 1
                self.PlayerState = 'Up'
            if win32api.GetAsyncKeyState(0x28) & 0x8000:  # DOWN
                self.y -= 1
                self.PlayerState = 'Down'
            else:
                self.PlayerState = 'Idle'

        if win32api.GetAsyncKeyState(0x20) & 0x8000:  # SPACE
            main_state.m_PBulletLst.append(Player_Bullet.CPlayer_Bullet(self.x, self.y))

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

def draw():
    clear_canvas()
    m_player.draw()
    update_canvas()
