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
    def __init__(self):
        self.x, self.y = 0, 90

        global image
        global image_num
        address = 'Tengai/Resource/Bullet/Ultimate/Screen/screen_'
        extension = '.png'
        for n in range(0, 32):
            all_address = address + str(n) + extension
            image_num = load_image(all_address)
            image.append(image_num)

        self.frame=0

    def update(self):
        global iNumber
        if iNumber > 30:
            iNumber=0

        iNumber+=0.1

    def draw(self):
        image[int(iNumber)].draw(540, 500)
