import pygame
from pygame.locals import *


def draw_block():
    surface.fill((222, 230, 64))
    surface.blit(block, (block_x, block_y))
    pygame.display.flip()


if __name__ == "__main__":
    pygame.init()

    # initialising game window
    surface = pygame.display.set_mode((500, 500))
    surface.fill((222, 230, 64))

    block = pygame.image.load('resources/block.jpg').convert()
    block_x = 100
    block_y = 100
    # put the block image over the surface at this coordinate
    surface.blit(block, (block_x, block_y))
    pygame.display.flip()

    # using eventloop-->UI progeamming
    running = True

    while running:
        for event in pygame.event.get():
            if event.type == KEYDOWN:
                if event.key == K_ESCAPE:
                    running = False
                if event.key == K_UP:
                    # moving verically. chamging the y position while x stays the same
                    block_y -= 10
                    draw_block()
                if event.key == K_DOWN:
                    block_y += 10
                    draw_block()
                if event.key == K_LEFT:
                    # moving horizontally. chamging the x position while y stays the same
                    block_x -= 10
                    draw_block()
                if event.key == K_RIGHT:
                    block_x += 10
                    draw_block()
            elif event.type == QUIT:
                running = False
