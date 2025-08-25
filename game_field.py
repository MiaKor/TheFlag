import pygame
import consts
import random
import screen


def create_field():
    field = []

    for i in range(consts.SCREEN_GRID_START_ROWS):
        row = []
        field.append(row)
        for j in range(consts.SCREEN_GRID_COLS):
            row.append(' ')
    return field


def randon_mines():
    tuple_list = []
    for i in range(consts.MINE_AMOUNT):
        x = random.randint(0, consts.SCREEN_GRID_COLS - 1)
        y = random.randint(0, consts.SCREEN_GRID_START_ROWS - 1)
        tuple_list.append((x*consts.SQUARED_PIXEL, y*consts.SQUARED_PIXEL))
    return tuple_list

    #    g = create_field()
# x = random.randint(0,consts.WINDOW_WIDTH)
#      while (x%50)!=0:
#          x = random.randint(0, consts.WINDOW_WIDTH)
#      y = random.randint(0,consts.WINDOW_HEIGHT)
#      while (y%25)!=0:
#          y = random.randint(0, consts.WINDOW_HEIGHT)
#
#      for j in range (3):
#          g.insert([x+j*50][y], consts.MINE)
#  return g
