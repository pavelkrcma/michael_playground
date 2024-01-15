import pyglet

window = pyglet.window.Window()

def tik(t):
    had.x = had.x + t * 20

def zpracuj_text(text):
    if text == 'd':
        had.x += 10
    if text == 'w':
        had.y += 10
    if text == 'e':
        had.rotation += 20
    if text == 'a':        
        had.x -= 10
    if text == 's':
        had.y -= 10
    if text == 'q':
        had.rotation -= 20

def vykresli():
    window.clear()
    had.draw()

window.push_handlers(
    on_text=zpracuj_text,
    on_draw=vykresli,
    )

obrazek = pyglet.image.load('had.png')
had = pyglet.sprite.Sprite(obrazek)

#pyglet.clock.schedule_interval(tik, 1/30)
pyglet.app.run()
