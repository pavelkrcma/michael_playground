import pyglet
import random

window = pyglet.window.Window()

had_direction_step = 1

def tik(t):
    global had_direction_step
    screen_x, screen_y = window.get_size()
    had.x += had_direction_step
    if had.x >= screen_x - had.width:
        had_direction_step = -1
    elif had.x == 0:
        had_direction_step = 1

    had2.x = random.randint(0, screen_x)
    had2.y = random.randint(0, screen_y)

def zpracuj_text(text):
    if text == 'd':
        had.x += 40
    if text == 'w':
        had.y += 40
    if text == 'e':
        had.rotation += 20
    if text == 'a':        
        had.x -= 40
    if text == 's':
        had.y -= 40
    if text == 'q':
        had.rotation -= 20

def klik(x, y, tlacitko, mod):
    if mod == 0:
        had2.x = x
        had2.y = y
    else:
        had2.rotation -= 25

def vykresli():
    window.clear()
    had.draw()
    had2.draw()

window.push_handlers(
    on_text=zpracuj_text,
    on_draw=vykresli,
    on_mouse_press=klik,
    )

obrazek = pyglet.image.load('had.png')
obrazek2 = pyglet.image.load('had2.png')
had = pyglet.sprite.Sprite(obrazek)
had2 = pyglet.sprite.Sprite(obrazek2)

pyglet.clock.schedule_interval(tik, 1/30)
pyglet.app.run()
