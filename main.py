import pygame
import consts
import screen
import game_field
import soldier

state = {"state": consts.RUNNING_STATE, "is_window_open": True, 'night': False}


def main():
    pygame.init()

    screen.draw_window()
    screen.draw_grass()
    screen.draw_solider()
    screen.draw_flag()
    while state["is_window_open"]:
        handle_user_events()
        if state['night']:
            screen.draw_night_window()
            continue

        if is_lose():
            state["state"] = consts.LOSE_STATE
        elif is_win():
            state["state"] = consts.WIN_STATE


def handle_user_events():
    for event in pygame.event.get():

        if event.type == pygame.QUIT:
            state["is_window_open"] = False
        elif state != consts.RUNNING_STATE:
            pass
        if event.type == pygame.KEYDOWN:

            if event.key == pygame.K_RETURN:
                state['night'] = True

            if event.key == pygame.K_UP:
                pass
            elif event.key == pygame.K_DOWN:
                pass
            elif event.key == pygame.K_RIGHT:
                pass
            elif event.key == pygame.K_LEFT:
                pass


def is_lose():
    pass


def is_win():
    pass


if __name__ == '__main__':
    main()
