import pygame
import math

# --- Pygame init ---
pygame.init()

# --- Screen setup ---
SCREEN_X, SCREEN_Y = 800, 600
SCREEN = pygame.display.set_mode((SCREEN_X, SCREEN_Y))
CLOCK = pygame.time.Clock()
TICK = 60

# --- Load assets ---
PLAYER_IMAGE_ORIG = pygame.image.load(
    "images/player_instance.png").convert_alpha()  # should point UP in image
MAP_IMAGE = pygame.image.load("images/map.png").convert()
map_width, map_height = MAP_IMAGE.get_size()

# --- Player & map state ---
player_angle = 180             # degrees
PLAYER_ROT_SPEED = 3         # degrees per frame
PLAYER_SPEED = 5             # pixels per frame

map_x, map_y = 0-(map_width/2), 0-(map_height/2)    # map offset

# --- Game loop ---
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # --- Key input ---
    keys = pygame.key.get_pressed()

    # Rotate left/right
    if keys[pygame.K_LEFT]:
        player_angle += PLAYER_ROT_SPEED
    if keys[pygame.K_RIGHT]:
        player_angle -= PLAYER_ROT_SPEED

    # Movement along sprite's top (leading edge)
    rad = math.radians(player_angle)

    if keys[pygame.K_UP]:
        map_x -= math.sin(rad) * PLAYER_SPEED
        map_y -= math.cos(rad) * PLAYER_SPEED
    if keys[pygame.K_DOWN]:
        map_x += math.sin(rad) * PLAYER_SPEED
        map_y += math.cos(rad) * PLAYER_SPEED

    # --- Draw ---
    SCREEN.fill((0, 0, 0))  # clear screen

    # Draw map at current offset
    SCREEN.blit(MAP_IMAGE, (map_x, map_y))

    # Rotate player sprite
    player_image = pygame.transform.rotate(PLAYER_IMAGE_ORIG, player_angle)
    player_rect = player_image.get_rect(center=(SCREEN_X // 2, SCREEN_Y // 2))
    SCREEN.blit(player_image, player_rect)

    # --- Update display ---
    pygame.display.flip()
    CLOCK.tick(TICK)

pygame.quit()
