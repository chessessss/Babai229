from pygame import *
window = display.set_mode((1400, 800))
display.set_caption('Доганялки')
background = transform.scale(image.load('background.png'), (1400, 800))

x1 = 150
y1 = 500
x2 = 800
y2 = 450

sprite1=transform.scale(image.load('sprite1.png'), (100, 100))
sprite2=transform.scale(image.load('sprite2.png'), (125, 125))
speed1 = 15
speed2 = 20


game = True
clock = time.Clock()
FPS = 75


while game:
    window.blit(background,(0,0))
    window.blit(sprite1, (x1, y1))
    window.blit(sprite2, (x2, y2))


    for e in event.get():
        if e.type == QUIT:
            game = False
    keys_pressed = key.get_pressed()
    if keys_pressed[K_LEFT] and x1 > 5:
        x1 -= speed1
    if keys_pressed[K_RIGHT] and x1 < 1295:
        x1 += speed1
    if keys_pressed[K_UP] and y1 > 5:
        y1 -= speed1
    if keys_pressed[K_DOWN] and y1 < 695:
        y1 += speed1



    if keys_pressed[K_a] and x2 > 5:
        x2 -= speed2
    if keys_pressed[K_d] and x2 < 1280:
        x2 += speed2
    if keys_pressed[K_w] and y2 > 10:
        y2 -= speed2
    if keys_pressed[K_s] and y2 < 670:
        y2+= speed2
    display.update()
    clock.tick(FPS)