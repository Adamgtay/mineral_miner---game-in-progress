import pygame


def draw_player(player_image_original, player_angle, screen_width, screen_height, screen):
    # Rotate player sprite
    player_image = pygame.transform.rotate(
        player_image_original, player_angle)
    player_rect = player_image.get_rect(
        center=(screen_width // 2, screen_height // 2))
    screen.blit(player_image, player_rect)
