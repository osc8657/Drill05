from pico2d import *
import random

TUK_WIDTH, TUK_HEIGHT = 1280, 1024
open_canvas(TUK_WIDTH, TUK_HEIGHT)

TUK_ground = load_image('TUK_GROUND.png')
character = load_image('animation_sheet.png')
hand_arrow = load_image('hand_arrow.png')

def move_events(p1, p2, i):
    global running
    global x, y

    x1, y1 = p1[0], p1[1]
    x2, y2 = p2[0], p2[1]

    t = i / 100
    x = (1 - t) * x1 + t * x2
    y = (1 - t) * y1 + t * y2

    pass


running = True
x, y = TUK_WIDTH // 2, TUK_HEIGHT // 2
frame = 0

points = [(random.randint(0, TUK_WIDTH),random.randint(0,TUK_HEIGHT)) for i in range(10)]
points[9] = points[0]
while running:
    for i in range (9):
        clear_canvas()

        for ii in range(0, 100+1, 1):

            TUK_ground.draw(TUK_WIDTH // 2, TUK_HEIGHT // 2)
            hand_arrow.draw(points[i + 1][0], points[i + 1][1])
            if(points[i][0] <= points[i+1][0]):
                character.clip_draw(frame*100, 100*1, 100, 100, x, y)
            else:
                character.clip_draw(frame*100, 0, 100, 100, x, y)

            update_canvas()
            move_events(points[i], points[i+1], ii)

            frame = (frame + 1) % 8
            delay(0.01)


