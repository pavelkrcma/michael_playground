import pyglet
from pyglet.window import key
import random

""" Ideas
Beep: print('\a')
PNGs: https://www.pngall.com/
"""

window = pyglet.window.Window()

global_score = 0

def detect_touching(sprite1, sprite2):
    return sprite1.x + sprite1.width >= sprite2.x \
        and sprite1.x <= sprite2.x + sprite2.width \
        and sprite1.y + sprite1.height >= sprite2.y \
        and sprite1.y <= sprite2.y + sprite2.height

def detect_touching_from_scheduler(t):
    global global_score
#    if detect_touching(had, had2):
#        global_score+=1
#        label.text = f'Score: {global_score}'

def zpracuj_stisk_klavesy(symbol, modifier):
    if symbol == key.A:
        pass

def zpracuj_pusteni_klavesy(symbol, modifier):
    pass

def klik(x, y, tlacitko, mod):
    pass

def vykresli():
    window.clear()
    background_img.blit(0, 0)
    label.draw()
    ship.draw()
    asteroid.draw()

window.push_handlers(
    on_key_press=zpracuj_stisk_klavesy,
    on_key_release=zpracuj_pusteni_klavesy,
    on_draw=vykresli,
    on_mouse_press=klik,
    )

spaceship_img = pyglet.image.load('spaceship.png')
asteroind_img = pyglet.image.load('asteroid.png')
background_img = pyglet.image.load('background.png')
ship = pyglet.sprite.Sprite(spaceship_img)
asteroid = pyglet.sprite.Sprite(asteroind_img)

label = pyglet.text.Label(f'Score: {global_score}',
                          font_name='Times New Roman',
                          font_size=36,
                          x=0, y=window.height-36)

pyglet.clock.schedule_interval(detect_touching_from_scheduler, 1/30)
pyglet.app.run()
