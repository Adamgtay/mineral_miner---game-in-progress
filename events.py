import pygame
import math


def fire_projectile(cannon_angle, screen_width, screen_height):
    projectile_angle = cannon_angle

    # Spawn at tank center
    projectile_x = screen_width // 2
    projectile_y = screen_height // 2

    return projectile_angle, projectile_x, projectile_y


def travelling_projectile(projectile_angle, projectile_speed, projectile_x, projectile_y):
    rad = math.radians(projectile_angle)

    projectile_x -= math.sin(rad) * projectile_speed
    projectile_y -= math.cos(rad) * projectile_speed

    return projectile_x, projectile_y
