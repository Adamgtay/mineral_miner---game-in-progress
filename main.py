import pygame
import math
import constants
import draw_player
import keys
import events

# --- Pygame init ---
pygame.init()


# --- Player & map state ---
player_angle = 180             # degrees
cannon_angle = 0
projectile_speed = 30
is_projectile = False
current_map_x, current_map_y = 0-(constants.MAP_WIDTH/2), 0 - \
    (constants.MAP_HEIGHT/2)    # map offset

# --- Game loop ---
running = True
while running:

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                projectile_angle, projectile_x, projectile_y = events.fire_projectile(
                    cannon_angle, constants.SCREEN_X, constants.SCREEN_Y)
                is_projectile = True

    # key input handling
    cannon_angle, player_angle, current_map_x, current_map_y = keys.key_inputs_movement(constants.PLAYER_ROT_SPEED,
                                                                                        constants.PLAYER_SPEED, player_angle, cannon_angle, constants.CANNON_ROT_SPEED, current_map_x, current_map_y)

    # Draw map at current state
    constants.SCREEN.blit(constants.MAP_IMAGE, (current_map_x, current_map_y))

    # ui display
    constants.SCREEN.blit(
        constants.UI, (0, constants.SCREEN_Y-constants.UI_HEIGHT))

    # draw player at current state
    draw_player.draw_player(constants.PLAYER_IMAGE_ORIG, player_angle,
                            constants.SCREEN_X, constants.SCREEN_Y, constants.SCREEN)
    # draw cannon at current state
    draw_player.draw_cannon(constants.CANNON, cannon_angle,
                            constants.SCREEN_X, constants.SCREEN_Y, constants.SCREEN)
    print(is_projectile)

    # draw projecile if true
    if is_projectile:
        projectile_x, projectile_y = events.travelling_projectile(
            projectile_angle, projectile_speed, projectile_x, projectile_y)
        pygame.draw.circle(constants.SCREEN, (255, 0, 0),
                           (int(projectile_x), int(projectile_y)), 5)

    # --- Update display ---
    pygame.display.flip()
    constants.CLOCK.tick(constants.TICK)

pygame.quit()
