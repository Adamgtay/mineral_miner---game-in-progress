import pygame
import math
import constants

# --- Pygame init ---
pygame.init()


# --- Player & map state ---
player_angle = 180             # degrees


map_x, map_y = 0-(constants.MAP_WIDTH/2), 0 - \
    (constants.MAP_HEIGHT/2)    # map offset

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
        player_angle += constants.PLAYER_ROT_SPEED
    if keys[pygame.K_RIGHT]:
        player_angle -= constants.PLAYER_ROT_SPEED

    # Movement along sprite's top (leading edge)
    rad = math.radians(player_angle)

    if keys[pygame.K_UP]:
        map_x -= math.sin(rad) * constants.PLAYER_SPEED
        map_y -= math.cos(rad) * constants.PLAYER_SPEED
    if keys[pygame.K_DOWN]:
        map_x += math.sin(rad) * constants.PLAYER_SPEED
        map_y += math.cos(rad) * constants.PLAYER_SPEED

    # --- Draw ---
    constants.SCREEN.fill((0, 0, 0))  # clear screen

    # Draw map at current offset
    constants.SCREEN.blit(constants.MAP_IMAGE, (map_x, map_y))

    # Rotate player sprite
    player_image = pygame.transform.rotate(
        constants.PLAYER_IMAGE_ORIG, player_angle)
    player_rect = player_image.get_rect(
        center=(constants.SCREEN_X // 2, constants.SCREEN_Y // 2))
    constants.SCREEN.blit(player_image, player_rect)

    # --- Update display ---
    pygame.display.flip()
    constants.CLOCK.tick(constants.TICK)

pygame.quit()
