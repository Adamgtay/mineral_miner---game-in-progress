import pygame
import math


def key_inputs(player_rotation_speed, player_speed, player_angle, current_map_x, current_map_y):
    # --- Key input ---
    keys = pygame.key.get_pressed()

    # Rotate left/right
    if keys[pygame.K_LEFT]:
        player_angle += player_rotation_speed
    if keys[pygame.K_RIGHT]:
        player_angle -= player_rotation_speed

    # Movement along sprite's top (leading edge)
    rad = math.radians(player_angle)

    if keys[pygame.K_UP]:
        current_map_x -= math.sin(rad) * player_speed
        current_map_y -= math.cos(rad) * player_speed
    if keys[pygame.K_DOWN]:
        current_map_x += math.sin(rad) * player_speed
        current_map_y += math.cos(rad) * player_speed

    return player_angle, current_map_x, current_map_y
