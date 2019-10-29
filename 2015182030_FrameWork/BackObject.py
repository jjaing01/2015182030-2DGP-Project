import random
import json
import os
import win32api

from pico2d import *

import game_framework
import main_state

name = "Back_Object"

image = []
image_num=None
iNumber=0

class CBack_Object:
    def __init__(self,x,y):
        self.x, self.y = x, y

        global image
        global image_num
        address = 'Tengai/Resource/Bullet/Ultimate/Screen/screen_'
        extension = '.png'
        for n in range(0, 32):
            all_address = address + str(n) + extension
            image_num = load_image(all_address)
            image.append(image_num)

        self.frame=0
        self.iNumber=random.randint(0,15)

    def update(self):
        global iNumber

        # 애니메이션
        if self.iNumber > 30:
            self.iNumber=0

        self.iNumber+=0.1

        # 움직임
        if self.x <= -600:
            self.x = 1600

        self.x -= 3

    def draw(self):
        image[int(self.iNumber)].draw(self.x, 500)
