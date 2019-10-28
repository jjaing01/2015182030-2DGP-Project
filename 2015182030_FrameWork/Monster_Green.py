import random
import json
import os
import win32api

from pico2d import *

import game_framework
import Player_Bullet
import main_state

name = "Mon_Green"

m_MonGreen = None

class CMonGreen:
    def __init__(self):
        self.x, self.y = 500,400
        self.frame = 0
        self.image = load_image('Tengai/Resource/Monster/Green.png')
        self.dir = 1

    def update(self):
        self.frame = (self.frame + 1) % 4

    def draw(self):
        self.image.clip_draw(self.frame * 100, 0, 100, 80, self.x,self.y,70,70)

