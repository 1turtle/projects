import pygame
import utility as util


# pygame setup
pygame.init()
screen = pygame.display.set_mode((1280, 720))
clock = pygame.time.Clock()
running = True
dt = 0

BACKGROUND_COLOR = "black"
WIDTH = screen.get_width()
HEIGHT = screen.get_height()
BOTTOM_BAR_X = 140
BOTTOM_BAR_Y = HEIGHT / 2
BOTTOM_BAR_WIDTH = 1000
BOTTOM_BAR_HEIGHT = 3
BOTTOM_BAR = pygame.Rect(BOTTOM_BAR_X, BOTTOM_BAR_Y, BOTTOM_BAR_WIDTH, BOTTOM_BAR_HEIGHT)
BOTTOM_BAR_COLOR = "white"
TEXT_COLOR = "white"
TEXT_POS_X = 140
TEXT_POS_Y = HEIGHT / 2 - 25
MAX_CHARACTERS = 80
TEXT_BAR = ""
text = ""
font = pygame.font.Font(None, 32)
match_font = pygame.font.Font(None, 64)
#word_list = ["do", "dad", "donut", "dinosaur", "dynamite", "doom"]
word_list = util.read_file()
match_list = []
MATCH_POSITION_X = 140
MATCH_POSITION_Y = HEIGHT / 2 + 25
MATCH_INCREMENT = 25
MATCH_COLOR = "white"
MATCH_SEL_COLOR = "red"
MATCH_BORDER_WIDTH = 1000
MATCH_BORDER_HEIGHT = 20
MATCH_BORDER = pygame.Rect(MATCH_POSITION_X, MATCH_POSITION_Y, MATCH_BORDER_WIDTH, MATCH_BORDER_HEIGHT)
DISPLAY_TEXT = ""
DISPLAY_TEXT_COLOR = "white"
DISPLAY_TEXT_X = 140
DISPLAY_TEXT_Y = HEIGHT / 3
TAB_IDX = -1
fps_text = ""
FPS_COLOR = "white"
FPS_POS_X = 1150
FPS_POS_Y = 50


while running:
    # fill the screen with a color to wipe away anything from last frame
    screen.fill(BACKGROUND_COLOR)
    pygame.draw.rect(screen, BOTTOM_BAR_COLOR, BOTTOM_BAR)

    # poll for events
    # pygame.QUIT event means the user clicked X to close your window
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_RETURN:
                if len(text) > 0:
                    DISPLAY_TEXT = text
                    text = ""
                    TAB_IDX = -1
                    match_list.clear()
                    TEXT_BAR = ""
            elif event.key == pygame.K_BACKSPACE:
                DISPLAY_TEXT = ""
                text = text[:-1]
                match_list = util.find_all(text, word_list)
                TAB_IDX = -1
            elif event.key == pygame.K_TAB or event.key == pygame.K_DOWN:
                if len(match_list) > 0 and TAB_IDX < len(match_list) - 1:
                    TAB_IDX+=1
                    text = match_list[TAB_IDX]
            elif event.key == pygame.K_LSHIFT or event.key == pygame.K_UP:
                if len(match_list) > 0 and 0 < TAB_IDX:
                    TAB_IDX-=1
                    text = match_list[TAB_IDX]
            else:
                if len(text) <= MAX_CHARACTERS:
                    DISPLAY_TEXT = ""
                    text += event.unicode
                    match_list = util.find_all(text.lower(), word_list)
                    TAB_IDX = -1
                    TEXT_BAR = "|"

    #print(TAB_IDX)

    """
    keys = pygame.key.get_pressed()
    if keys[pygame.K_BACKSPACE]:
        DISPLAY_TEXT = ""
        text = text[:-1]
        match_list = util.find_all(text, word_list)
        TAB_IDX = -1
    """

    txt_surface = font.render(text + TEXT_BAR, True, TEXT_COLOR)
    screen.blit(txt_surface, (TEXT_POS_X, TEXT_POS_Y))

    display_txt_surface = match_font.render(DISPLAY_TEXT, True, DISPLAY_TEXT_COLOR)
    screen.blit(display_txt_surface, (DISPLAY_TEXT_X, DISPLAY_TEXT_Y))

    MATCH_POSITION_Y = HEIGHT / 2 + 25
    for idx, match in enumerate(match_list):
        match_surface = font.render(match, True, MATCH_COLOR)
        screen.blit(match_surface, (MATCH_POSITION_X, MATCH_POSITION_Y))
        if idx == TAB_IDX:
            pygame.draw.rect(screen, MATCH_SEL_COLOR, (MATCH_POSITION_X, MATCH_POSITION_Y, MATCH_BORDER_WIDTH, MATCH_BORDER_HEIGHT), 1)

        MATCH_POSITION_Y+=MATCH_INCREMENT

    fps_text = "FPS: " + str(int(clock.get_fps()))
    fps_surface = font.render(fps_text, True, FPS_COLOR)
    screen.blit(fps_surface, (FPS_POS_X, FPS_POS_Y))

    # flip() the display to put your work on screen
    pygame.display.flip()

    # limits FPS to 60
    clock.tick(60)

pygame.quit()