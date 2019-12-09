import game_framework
from pico2d import *

name = "EndState"
image = None

def enter():
    global image
    image = load_image('Tengai/Resource/LoadGame.png')

def exit():
    global image
    del(image)

def handle_events():
    # global iNumber
    # events = get_events()
    # for event in events:
    #     if event.type == SDL_QUIT:
    #         game_framework.quit()
    #     else:
    #         if (event.type, event.key) == (SDL_KEYDOWN, SDLK_ESCAPE):
    #             game_framework.quit()
    pass

def draw():
    global image
    clear_canvas()
    image.draw(540, 300,1080,600)
    update_canvas()


def update():
    pass


def pause():
    pass


def resume():
    pass





