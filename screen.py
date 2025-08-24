import consts
import pygame

pygame.init()
screen = pygame.display.set_mode((consts.WINDOW_WIDTH, consts.WINDOW_HEIGHT))
run= True
while run:
    for event in pygame.event.get():
        if event.type==pygame.QUIT:
            run= False
pygame.quit()
