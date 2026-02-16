import pygame


def events(running):
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    return running
