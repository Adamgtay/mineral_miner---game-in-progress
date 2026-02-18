import pygame


def draw_player(player_image_original, player_angle, screen_width, screen_height, screen):
    # Rotate player sprite
    player_image = pygame.transform.rotate(
        player_image_original, player_angle)
    player_rect = player_image.get_rect(
        center=(screen_width // 2, screen_height // 2))
    screen.blit(player_image, player_rect)


def draw_cannon(cannon_image_original, total_angle, screen_width, screen_height, screen):

    # Screen center (tank position)
    tank_center = pygame.math.Vector2(screen_width // 2, screen_height // 2)

    # Pivot point inside the cannon image (adjust these!)
    pivot = pygame.math.Vector2(
        cannon_image_original.get_width() // 10,
        cannon_image_original.get_height() - 30
    )

    # Offset from pivot to center
    offset = pygame.math.Vector2(0, 0) - pivot

    # Rotate offset
    rotated_offset = offset.rotate(-total_angle)

    # Final draw position
    rotated_image = pygame.transform.rotate(cannon_image_original, total_angle)
    rect = rotated_image.get_rect(center=tank_center + rotated_offset)

    screen.blit(rotated_image, rect)
