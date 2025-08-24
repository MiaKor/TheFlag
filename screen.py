from symtable import Class

import consts
import pygame
import random

pygame.init()
screen = pygame.display.set_mode((consts.WINDOW_WIDTH, consts.WINDOW_HEIGHT))

def draw_window():
    screen.fill(consts.REGULAR_BACKGROUND)
    pygame.display.update()

def draw_grass():
    for i in range(consts.BUSHES_AMOUNT):
        x = random.randint(0,consts.WINDOW_WIDTH)
        y = random.randint(0,consts.WINDOW_HEIGHT)
        screen.blit(consts.GRASS, (x,y))
        pygame.display.update()

