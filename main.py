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
current_map_x, current_map_y = 0-(constants.MAP_WIDTH/2), 0 - \
    (constants.MAP_HEIGHT/2)    # map offset

# --- Game loop ---
running = True
while running:

    running = events.events(running)

    # key input handling
    cannon_angle, player_angle, current_map_x, current_map_y = keys.key_inputs(constants.PLAYER_ROT_SPEED,
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

    # --- Update display ---
    pygame.display.flip()
    constants.CLOCK.tick(constants.TICK)

pygame.quit()
