import pygame
# --- Screen setup ---
SCREEN_X, SCREEN_Y = 1200, 800
SCREEN = pygame.display.set_mode((SCREEN_X, SCREEN_Y))
CLOCK = pygame.time.Clock()
TICK = 60

# --- Load assets ---
PLAYER_IMAGE_ORIG = pygame.image.load(
    "images/player_instance.png").convert_alpha()  # should point UP in image
MAP_IMAGE = pygame.image.load("images/map.png").convert()
UI = pygame.image.load("images/ui.png").convert()
CANNON = pygame.image.load("images/cannon.png").convert_alpha()


# assets data
MAP_WIDTH, MAP_HEIGHT = MAP_IMAGE.get_size()
UI_WIDTH, UI_HEIGHT = UI.get_size()
CANNON_WIDTH, CANNON_HEIGHT = CANNON.get_size()

# gameplay data
PLAYER_ROT_SPEED = 3         # degrees per frame
PLAYER_SPEED = 5             # pixels per frame
CANNON_ROT_SPEED = 1
