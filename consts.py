import pygame
import os

pygame.init()

SCREEN_GRID_START_ROWS = 25
SCREEN_GRID_COLS = 50
WINDOW_HEIGHT = 750
WINDOW_WIDTH=1500

BUSHES_AMOUNT= 20
BUSH_HEIGHT=50
BUSH_WIDTH=50

MINE_AMOUNT = 20
MINE_HEIGHT = 30
MINE_WIDTH = 90

SOLDIER = pygame.image.load(os.path.join('bin','soldier.png'))
SOLDIER_NIGHT = pygame.image.load(os.path.join('bin','soldier_nigth.png'))
FLAG = pygame.image.load(os.path.join('bin','flag.png'))
EXPLOSION = pygame.image.load(os.path.join('bin','explotion.png'))
MINE = pygame.image.load(os.path.join('bin','mine.png'))
INJURY = pygame.image.load(os.path.join('bin','injury.png'))
SNAKE = pygame.image.load(os.path.join('bin','snake.png'))
GRASS = pygame.image.load(os.path.join('bin','grass.png'))
SOLDIER_2 = pygame.image.load(os.path.join('bin','soldier (2).png'))

GRASS=pygame.transform.scale(GRASS,(BUSH_WIDTH,BUSH_HEIGHT))

REGULAR_BACKGROUND = (0, 77, 0)
# REGULAR_BACKGROUND = (255, 255, 255)

BACKGROUND_WHEN_ENTER = (0, 0, 0)
LIGHT_GREEN = (144, 238, 144)
RUNNING_STATE = 1
LOSE_STATE = 2
WIN_STATE = 3