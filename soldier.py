import pygame
import consts
import screen
screen=screen.screen
def soldier():
    pygame.init()
    player=pygame.Rect(150,150,consts.SOLDIER_WIDTH,consts.SOLDIER_HEIGHT)
    pygame.draw.rect(screen,(0,0,0),player)