import pygame, pgzrun, math, random
WIDTH = 993
HEIGHT = 477

time_left = 10
score = 0
start = False
over = False

pos_possible = [
    (162,373),
    (460,215),
    (624,83),
    (810,202),
    (923,346),
    (102,100)
]

background = Actor("background")
enemy = Actor("zombie1")
enemy.pos = (102,100)
player = Actor("target1")
background_begin = Actor("begin")
play_box = Rect(0, 0, 305, 45)
play_box.move_ip(355, 365)
background_over = Actor("over")
play_again = Actor("again")
play_again.pos = (513, 390)

def enemy_reset():
    global enemy
    enemy = Actor("zombie1")
    enemy.pos = pos_possible[random.randint(0,5)]
clock.schedule_interval(enemy_reset, 1.5)

def hang_up():
    player.image = "target1"

def on_mouse_move(pos):
    player.pos = (pos[0], pos[1])
    if play_box.collidepoint(pos):
        background_begin.image = "begin1"
    else:
        background_begin.image = "begin" 

    if play_again.collidepoint(pos):
        play_again.image = "again1"
    else:
        play_again.image = "again" 

def on_mouse_down(pos):
    global score, start, over, time_left
    player.image = "target2"
    clock.schedule_unique(hang_up, 0.1)
    if enemy.collidepoint(pos):
        enemy.image = "zombie2"
        score += 1
        clock.schedule(enemy_reset, 0.3)
    if play_box.collidepoint(pos):
        start = True
        over = False
        play_box.move_ip(1000, 1000)
        time_left = 10

    if play_again.collidepoint(pos):
        start = True
        over = False
        score = 0
        time_left = 10

def time_up():
    global time_left, start, over
    if time_left:
        time_left -= 1
    else:
        over = True
        start = False
clock.schedule_interval(time_up, 1.0)

def update():
    global select_x, select_y
    mouse_x, mouse_y = pygame.mouse.get_pos()
    select_x = math.floor(mouse_x)
    select_y = math.floor(mouse_y)

def draw():
    if not start and not over:
        background_begin.draw()
    elif not over:
        background.draw()
        enemy.draw()
        player.draw()
        screen.draw.text("Time: "+str(time_left), (850, 30), fontsize=30)
        screen.draw.text("Score: "+str(score), (850, 400), fontsize=30, color="red")
    else:
        background_over.draw()
        screen.draw.text("Score: "+str(score), (440, 309), fontsize=50, color="red")
        play_again.draw()
    screen.draw.text("X coor:"+str(select_x)+"Y coor:"+str(select_y),(0,0))
pgzrun.go()