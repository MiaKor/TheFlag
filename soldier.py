import pygame
import consts
import screen
import game_field
import math

pygame.init()

def collision():
    bombs=game_field.randon_mines()
    pos=(consts.SOLDIER_X,consts.SOLDIER_Y)
    for i in bombs:
        if i==pos:
            return True

    return False
