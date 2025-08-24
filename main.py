import pygame
import consts
import screen
import game_field
import soldier


def handle_user_events():
    for event in pygame.event.get():

        if event.type == pygame.QUIT:
            run = False
        elif  != consts.RUNNING_STATE:
            continue
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
    state=consts.RUNNING_STATE
    run = True
    while run:
        handle_user_events()
        screen.draw_window()
    if is_lose():
        state= consts.LOSE_STATE
    elif is_win():
        state= consts.WIN_STATE


def is_lose():
    pass
def is_win():
    pass

if __name__ == '__main__':
    main()
