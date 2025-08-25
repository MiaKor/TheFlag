import pygame
import consts
import screen
import game_field
import soldier
import time

state = {"state": consts.RUNNING_STATE, "is_window_open": True, 'night': False}


def main():
    pygame.init()
    clock = pygame.time.Clock()
    draw_board()
    pygame.image.save(screen.screen,"image.png")
    background=pygame.image.load("image.png")
    screen.screen.blit(background,(0,0))
    add = 0
    while state["is_window_open"]:
        handle_user_events()
        screen.screen.blit(background, (0, 0))
        screen.draw_solider()
        if state['night'] and add == 0:
            screen.draw_night_window()
            pygame.image.save(screen.screen, "image_night.png")
            time.sleep(1)
            screen.screen.blit(background, (0, 0))
            add += 1
            pygame.display.update()
            state['night'] = False
        elif state['night'] and add != 0:
            background_night = pygame.image.load("image_night.png")
            screen.screen.blit(background_night, (0, 0))
            screen.screen.blit(background_night, (0, 0))
            pygame.display.update()
            time.sleep(1)
            screen.screen.blit(background, (0, 0))
            pygame.display.update()
            state['night'] = False

        pygame.display.update()

        if is_lose():
            state["state"] = consts.LOSE_STATE
        elif is_win():
            state["state"] = consts.WIN_STATE
    clock.tick(60)


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
        if event.type == pygame.KEYDOWN:

            if event.key == pygame.K_RETURN:
                state['night'] = True
            else:
                state['night'] = False

        keys = pygame.key.get_pressed()
        if keys[pygame.K_UP]:
            consts.SOLDIER_Y -= 30
        if keys[pygame.K_DOWN]:
            consts.SOLDIER_Y += 30
        if keys[pygame.K_LEFT]:
            consts.SOLDIER_X -= 30
        if keys[pygame.K_RIGHT]:
            consts.SOLDIER_X += 30



def is_lose():
    pass


def is_win():
    pass


if __name__ == '__main__':
    main()
