import pygame
import consts
import screen
import game_field
import soldier


def handle_user_events(run):
    while run:
        for event in pygame.event.get():

            if event.type == pygame.QUIT:
                run = False

            if event.type == pygame.MOUSEMOTION:
                pass

            elif event.type == pygame.MOUSEBUTTONDOWN:
                pass


def main():
    pygame.init()
    run = True
    handle_user_events(run)


if __name__ == '__main__':
    main()
