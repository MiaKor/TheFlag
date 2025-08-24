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
        x = random.randint(0,consts.WINDOW_WIDTH-50)
        y = random.randint(0,consts.WINDOW_HEIGHT-50)
        screen.blit(consts.GRASS, (x,y))
        pygame.display.update()

def draw_night_window():
    screen.fill(consts.BACKGROUND_WHEN_ENTER)
    for i in range(0,consts.WINDOW_WIDTH,(consts.WINDOW_WIDTH//consts.SCREEN_GRID_COLS)):
        pygame.draw.line(screen, consts.LIGHT_GREEN,(i,0) ,(i,consts.WINDOW_HEIGHT) )
    for j in range(0,consts.WINDOW_HEIGHT,(consts.WINDOW_HEIGHT//consts.SCREEN_GRID_START_ROWS)):
        pygame.draw.line(screen, consts.LIGHT_GREEN, (0, j),(consts.WINDOW_WIDTH,j ),)
    pygame.display.update()