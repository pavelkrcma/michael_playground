import pyglet

window = pyglet.window.Window()

def tik(t):
    had.x = had.x + t * 20

def zpracuj_text(text):
    if text == 'a':
        had.x += 10
    if text == 'b':
        had.y += 10
    if text == 'c':
        had.rotation += 20

def vykresli():
    window.clear()
    had.draw()

window.push_handlers(
    on_text=zpracuj_text,
    on_draw=vykresli,
    )

obrazek = pyglet.image.load('had.png')
had = pyglet.sprite.Sprite(obrazek)

pyglet.clock.schedule_interval(tik, 1/30)
pyglet.app.run()
