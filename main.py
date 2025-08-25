import pygame
import consts
import screen
import game_field
import soldier
import time

state = {"state": consts.RUNNING_STATE, "is_window_open": True, 'night': False}


def main():
    pygame.init()
    draw_board()
    # soldier.soldier()
    pygame.image.save(screen.screen,"image.png")
    background=pygame.image.load("image.png")
    screen.screen.blit(background,(0,0))
    while state["is_window_open"]:
        handle_user_events()
        screen.draw_solider()
        if state['night']:
            screen.draw_night_window()
            time.sleep(1)
            state['night'] =False
            screen.screen.blit(background, (0, 0))
            pygame.display.update()


        if is_lose():
            state["state"] = consts.LOSE_STATE
        elif is_win():
            state["state"] = consts.WIN_STATE
    pygame.display.update()


def draw_board():
    screen.draw_window()
    screen.draw_grass()
    screen.draw_flag()


def handle_user_events():
    for event in pygame.event.get():

        if event.type == pygame.QUIT:
            state["is_window_open"] = False
        elif state != consts.RUNNING_STATE:
            pass
        keys = pygame.key.get_pressed()
        if event.type == pygame.KEYDOWN:

            if event.key == pygame.K_RETURN:
                state['night'] = True
            else:
                state['night'] = False

            # if event.key == pygame.K_UP:
            #     soldier.soldier().y-=30
            # elif event.key == pygame.K_DOWN:
            #     soldier.soldier().y += 30
            # elif event.key == pygame.K_RIGHT:
            #     soldier.soldier().x -= 30
            # elif event.key == pygame.K_LEFT:
            #     soldier.soldier().x+=30



def is_lose():
    pass


def is_win():
    pass


if __name__ == '__main__':
    main()
