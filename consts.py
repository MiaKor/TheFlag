import pygame

pygame.init()

SCREEN_GRID_START_ROWS = 25
SCREEN_GRID_COLS = 50
WINDOW_HEIGHT = 750
WINDOW_WIDTH=1000

SOLDIER = pygame.image.load('bin','soldier.png')
SOLDIER_NIGHT = pygame.image.load('bin','soldier_night.png')
FLAG = pygame.image.load('bin','flag.png')
EXPLOSION = pygame.image.load('bin','explotion.png')
MINE = pygame.image.load('bin','mine.png')
INJURY = pygame.image.load('bin','injury.png')
SNAKE = pygame.image.load('bin','snake.png')
GRASS = pygame.image.load('bin','grass')
SOLDIER_2 = pygame.image.load('bin','soldier (2).png')

REGULAR_BACKGROUND = (138, 201, 38)
BACKGROUND_WHEN_ENTER = (0, 0, 0)
LIGHT_GREEN = (144, 238, 144)