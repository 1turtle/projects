import pygame
import math



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
LEFT_BORDER = 0
RIGHT_BORDER = screen.get_width()
TOP_BORDER = 0
BOTTOM_BORDER = screen.get_height()
COLORS = ["red", "orange", "yellow", "green", "blue", "purple"]
COLOR_IDX = 0
POSITIONS = []
ELAPSED_TIME = 0
COLLIDE_X = -1
COLLIDE_Y = -1

class Ball:
    def __init__(self, color, x, y, radius, width=0, vel_x=50000, vel_y=50000, acc_x=0, acc_y=500):
        self.color = color
        self.x = x
        self.y = y
        self.radius = radius
        self.width = width
        self.vel_x = vel_x
        self.vel_y = vel_y
        self.acc_x = acc_x
        self.acc_y = acc_y

ball = Ball("white", MID_X, MID_Y, 20)

def switch_color():
    global COLOR_IDX, COLLIDE_X, COLLIDE_Y

    if COLLIDE_X != ball.x or COLLIDE_Y != ball.y:
        if COLOR_IDX >= len(COLORS):
            COLOR_IDX = 0

        ball.color = COLORS[COLOR_IDX]
        COLOR_IDX+=1

    COLLIDE_X = ball.x
    COLLIDE_Y = ball.y

def check_collision():
    if ball.x - ball.radius < LEFT_BORDER:
        ball.x = LEFT_BORDER + ball.radius
        ball.vel_x *= -0.8
        switch_color()
    elif ball.x + ball.radius > RIGHT_BORDER:
        ball.x = RIGHT_BORDER - ball.radius
        ball.vel_x *= -0.8
        switch_color()
    elif ball.y - ball.radius < TOP_BORDER:
        ball.y = TOP_BORDER + ball.radius
        ball.vel_y *= -0.8
        switch_color()
    elif ball.y + ball.radius > BOTTOM_BORDER:
        ball.y = BOTTOM_BORDER - ball.radius
        ball.vel_y *= -0.8
        ball.vel_x *= 0.8
        switch_color()
    else:
        ... # do nothing

def calculate_trajectory():
    """
    ball.vel_y += ball.acc_y * dt
    ball.vel_x += ball.acc_x * dt

    ball.y += ball.vel_y * dt
    ball.x += ball.vel_x * dt
    """

    ball.vel_y += ball.acc_y * dt
    ball.vel_x += ball.acc_x * dt

    ball.y += (ball.vel_y * dt) + (0.5 * ball.acc_y * math.pow(dt, 2))
    ball.x += (ball.vel_x * dt) + (0.5 * ball.acc_x * math.pow(dt, 2))


def draw_trajectory():
    if len(POSITIONS) > 20:
        POSITIONS.pop(0)

    for item in POSITIONS:
        pygame.draw.circle(screen, "white", (item[0], item[1]), 5)

while running:
    ELAPSED_TIME += dt
    #print("x: " + str(ball.x) + ", " + "y: " + str(ball.y))
    #print("cx: " + str(COLLIDE_X) + ", " + "cy: " + str(COLLIDE_Y))

    # poll for events
    # pygame.QUIT event means the user clicked X to close your window
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # fill the screen with a color to wipe away anything from last frame
    screen.fill(BACKGROUND_COLOR)

    #------------------------------------------------------------------------------------------------------------------#
    draw_trajectory()
    pygame.draw.circle(screen, ball.color, (ball.x, ball.y), ball.radius)
    calculate_trajectory()

    if ELAPSED_TIME >= 0.05:
        POSITIONS.append((ball.x, ball.y))
        ELAPSED_TIME = 0

    check_collision()
    #------------------------------------------------------------------------------------------------------------------#

    # flip() the display to put your work on screen
    pygame.display.flip()

    # limits FPS to 60
    # dt is delta time in seconds since last frame, used for framerate-
    # independent physics.
    dt = clock.tick(60) / 1000