import pyglet
from pyglet.window import key
import random
import copy

""" Ideas
Beep: print('\a')
PNGs: https://www.pngall.com/
"""

window = pyglet.window.Window()

global_score = 0
global_move_speed = 4.5
global_asteroid_speed = 3
global_shooting_speed = 0.3

# let's use set instead of list. set can have only one unique value in the same time.
list_of_keys = set()
list_of_bullets = []
last_fire = 10

def asteriod_doomed():
    global global_score
    global global_move_speed
    global global_asteroid_speed

    asteroid.y = window.height
    asteroid.x = random.randint(0, window.width)
    global_score += 1
    global_asteroid_speed += 1
    global_move_speed += 1
    label.text = f'Score: {global_score}'
    beep1.play()

def tick_bullet(t):
    global list_of_bullets
    global last_fire
    global global_shooting_speed

    if key.SPACE in list_of_keys and last_fire > global_shooting_speed:
        new_strela = pyglet.text.Label('l', font_size = 20)
        new_strela.x = ship.x + ship.width / 2 - 2
        new_strela.y = ship.y + ship.height - 10
        new_strela.visible = True
        list_of_bullets.append(new_strela)
        last_fire = 0
    else:
        last_fire += t

    for bullet in list_of_bullets:
        # Height of the bullet is not available thus using constant
        if  bullet.y + 20 >= asteroid.y and \
            bullet.x > asteroid.x and \
            bullet.x < asteroid.x + asteroid.width:
                asteriod_doomed()
                list_of_bullets.remove(bullet)

def tick(t):
    global global_score
    global global_move_speed
    global global_asteroid_speed

    asteroid.y -= global_asteroid_speed

    for bullet in list_of_bullets:
        bullet.y += 10
        if bullet.y > window.height:
            list_of_bullets.remove(bullet)

    if key.A in list_of_keys:
        ship.x -= global_move_speed
    if key.D in list_of_keys:
        ship.x += global_move_speed

    if ship.x < 0:
        ship.x = window.width - ship.width
    if ship.x + ship.width > window.width:
        ship.x = 1

    if detect_touching(ship, asteroid):
        asteriod_doomed()

    if asteroid.y <= 0:
        asteroid.y = window.height
        asteroid.x = random.randint(0, window.width)
        global_score = 0
        global_move_speed = 4.5
        global_asteroid_speed = 3
        label.text = f'Score: {global_score}'
        beep2.play()

def detect_touching(sprite1, sprite2):
    return sprite1.x + sprite1.width >= sprite2.x \
        and sprite1.x <= sprite2.x + sprite2.width \
        and sprite1.y + sprite1.height >= sprite2.y \
        and sprite1.y <= sprite2.y + sprite2.height

def zpracuj_stisk_klavesy(symbol, modifier):
    global list_of_keys
    list_of_keys.add(symbol)

def zpracuj_pusteni_klavesy(symbol, modifier):
    global list_of_keys
    list_of_keys.discard(symbol)

def klik(x, y, tlacitko, mod):
    pass

def vykresli():
    window.clear()
    background_img.blit(0, 0)
    label.draw()
    ship.draw()
    asteroid.draw()
    for bullet in list_of_bullets:
        bullet.draw()

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

beep1 = pyglet.resource.media('beep-07a.wav')
beep2 = pyglet.resource.media('beep-10.wav')

# Very start of the program, initialization
ship.x = window.width / 2
ship.scale = 0.2
asteroid.scale = 0.3

label = pyglet.text.Label(f'Score: {global_score}',
                          font_name='Times New Roman',
                          font_size=36,
                          x=0, y=window.height-36)

pyglet.clock.schedule_interval(tick, 1/30)
pyglet.clock.schedule_interval(tick_bullet, 1/30)

pyglet.app.run()
