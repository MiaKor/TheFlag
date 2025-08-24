import pygame
import consts
import screen
import game_field
import soldier


def handle_user_events():
    for event in pygame.event.get():

        if event.type == pygame.QUIT:
            run = False
        if event.type == pygame.K_UP:
            pass
        elif event.type == pygame.K_DOWN:
            pass
        elif event.type == pygame.K_RIGHT:
            pass
        elif event.type == pygame.K_LEFT:
            pass
        elif event.type == pygame.MOUSEBUTTONDOWN:
            pass


def main():
    pygame.init()
    run = True
    while run:
        handle_user_events()
        screen.draw_window()


if __name__ == '__main__':
    main()
