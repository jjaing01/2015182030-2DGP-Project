import game_framework
from pico2d import *
import main_state


name = "TitleState"
image = []
image_num=None
iNumber=0


def enter():
    global image
    global image_num
    address = 'Tengai/Resource/Menu/Select_Character'
    extension = '.png'
    for n in range(0,5):
        all_address=address+str(n)+extension
        image_num = load_image(all_address)
        image.append(image_num)


def exit():
    global image
    #del(image)
    image.clear()


def handle_events():
    global iNumber
    events = get_events()
    for event in events:
        if event.type == SDL_QUIT:
            game_framework.quit()
        else:
            if (event.type, event.key) == (SDL_KEYDOWN, SDLK_ESCAPE):
                game_framework.quit()
            elif (event.type, event.key) == (SDL_KEYDOWN, SDLK_SPACE):
                game_framework.change_state(main_state)
            elif(event.type, event.key) == (SDL_KEYDOWN, SDLK_RIGHT):
                if iNumber > 3:
                    iNumber = 0
                else:
                    iNumber += 1
            elif (event.type, event.key) == (SDL_KEYDOWN, SDLK_LEFT):
                if iNumber < 1:
                    iNumber = 4
                else:
                    iNumber -= 1

def draw():
    global iNumber
    clear_canvas()
    image[iNumber].draw(400, 300)
    update_canvas()


def update():
    pass


def pause():
    pass


def resume():
    pass





