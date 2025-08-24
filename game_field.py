import pygame
import consts
import random
import screen

def create_field():
    game_field = []
    for i in range (consts.SCREEN_GRID_START_ROWS):
        for j in range (consts.SCREEN_GRID_COLS):
            game_field.append([])

# mines_positions = []
# def random_positions():
#     g = create_field()
#     for i in len()

    # random.choices()

def randon_mines():
    for i in range(consts.BUSHES_AMOUNT):
        x = random.randint(0,consts.WINDOW_WIDTH)
        y = random.randint(0,consts.WINDOW_HEIGHT)
        screen.blit(consts.MINE, (x,y))



