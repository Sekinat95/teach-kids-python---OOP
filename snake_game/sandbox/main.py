# create your python environment
# WINDOWs => python -m virtualenv damienv
# nameenv\Scripts\activate.bat


# MAC python -m virtualenv damienv
# ./nameofenv/bin/activate
import pygame
# pip install pygame
from pygame.locals import *
import os


def draw_block():
    surface.fill((50, 168, 62))
    surface.blit(block, (block_x, block_y))
    pygame.display.flip()


if __name__ == "__main__":
    pygame.init()

    surface = pygame.display.set_mode((500, 500))
    surface.fill((50, 168, 62))

    block = pygame.image.load('./resources/block.jpg').convert()
    block_x = 100
    block_y = 100
    surface.blit(block, (block_x, block_y))

    pygame.display.flip()

    running = True

    while running:
        for event in pygame.event.get():
            if event.type == KEYDOWN:
                if event.key == K_ESCAPE:  # esc
                    running = False
                if event.key == K_UP:
                    # vertical movement so only block_y chnages
                    block_y -= 10
                    draw_block()
                if event.key == K_DOWN:
                    block_y += 10
                    draw_block()
                if event.key == K_LEFT:
                    block_x -= 10
                    draw_block()
                if event.key == K_RIGHT:
                    block_x += 10
                    draw_block()
            elif event.type == QUIT:
                running = False
