# BROKEN FILE THIS DOES NOT WORK PROPERLY
import pygame
import math
#from copy import copy


# pygame setup
pygame.init()
screen = pygame.display.set_mode((1280, 720))
clock = pygame.time.Clock()
running = True
dt = 0
BACKGROUND_COLOR = "black"

WIDTH = screen.get_width()
HEIGHT = screen.get_height()
MID_X = WIDTH / 2
MID_Y = HEIGHT / 2
TIME = 0

class Ring:
    def __init__(self, color, x, y, radius, width=0):
        self.color = color
        self.x = x
        self.y = y
        self.radius = radius
        self.width = width

class Ball(Ring):
    def __init__(self, color, x, y, radius, width=0, vel_x=0, vel_y=0, acc_x=0, acc_y=9.8):
        super().__init__(color, x, y, radius, width)
        self.vel_x = vel_x
        self.vel_y = vel_y
        self.acc_x = acc_x
        self.acc_y = acc_y


ring = Ring("white", MID_X, MID_Y, 325, 1)
ball = Ball("white", MID_X, MID_Y, 20)

def inverse():
    #ball.vel_x += (ball.acc_x * TIME)
    #ball.vel_x *= -1

    ball.vel_y += (ball.acc_y * TIME)
    ball.vel_y *= -1

def normalize():
    # unit vector
    ...

def check_collision():
    difference_x = ball.x - ring.x
    difference_y = ball.y - ring.y
    sum_xy = math.pow(difference_x, 2) + math.pow(difference_y, 2)
    distance = math.sqrt(sum_xy)

    if distance + ball.radius >= ring.radius:
        ball.color = "green"
        inverse()

def calculate_trajectory():
    ball.y += (ball.vel_y * TIME) + (0.5 * ball.acc_y * math.pow(TIME, 2))
    ball.x += (ball.vel_x * TIME) + (0.5 * ball.acc_x * math.pow(TIME, 2))

while running:
    #TIME = pygame.time.get_ticks() / 1000
    TIME += dt
    #print(ball.vel_y)
    #print("x: " + str(ball.x) + "," + "y: " + str(ball.y))

    # poll for events
    # pygame.QUIT event means the user clicked X to close your window
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # fill the screen with a color to wipe away anything from last frame
    screen.fill(BACKGROUND_COLOR)

    #--------------------#
    pygame.draw.circle(screen, ball.color, (ball.x, ball.y), ball.radius)
    pygame.draw.circle(screen, ring.color, (ring.x, ring.y), ring.radius, ring.width)

    #ball.x = ball.x + 3
    calculate_trajectory()
    check_collision()



    #--------------------#

    # flip() the display to put your work on screen
    pygame.display.flip()

    # limits FPS to 60
    # dt is delta time in seconds since last frame, used for framerate-
    # independent physics.
    dt = clock.tick(60) / 1000