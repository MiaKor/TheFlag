import pygame
import os

pygame.init()

SCREEN_GRID_START_ROWS = 25
SCREEN_GRID_COLS = 50
WINDOW_HEIGHT = 750
WINDOW_WIDTH=1500

SOLDIER = pygame.image.load(os.path.join('bin','soldier.png'))
SOLDIER_NIGHT = pygame.image.load(os.path.join('bin','soldier_nigth.png'))
FLAG = pygame.image.load(os.path.join('bin','flag.png'))
EXPLOSION = pygame.image.load(os.path.join('bin','explotion.png'))
MINE = pygame.image.load(os.path.join('bin','mine.png'))
INJURY = pygame.image.load(os.path.join('bin','injury.png'))
SNAKE = pygame.image.load(os.path.join('bin','snake.png'))
GRASS = pygame.image.load(os.path.join('bin','grass'))
SOLDIER_2 = pygame.image.load(os.path.join('bin','soldier (2).png'))

REGULAR_BACKGROUND = (138, 201, 38)
BACKGROUND_WHEN_ENTER = (0, 0, 0)
LIGHT_GREEN = (144, 238, 144)