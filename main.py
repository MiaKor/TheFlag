import pygame
import consts
import screen
import game_field
import soldier


def handle_user_events():
    for event in pygame.event.get():

        if event.type == pygame.QUIT:
           pass

        if event.type == pygame.MOUSEMOTION:
            pass

        elif event.type == pygame.MOUSEBUTTONDOWN:
            pass


def main():
    pygame.init()
    pass


if __name__ == '__main__':
    main()
