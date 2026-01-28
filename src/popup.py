# Libraries

import pygame

from src.assets_loading import WOOD_BUTTON, WOOD_BUTTON_HOVER, POPUP_FRAME_RECT, POPUP_FRAME_SCALED, GAME_OVER_RECT, GAME_OVER_SCALED
from src.best_score import read_best_score_file

# Functions

def popup_rendering(screen, my_fonts, score):

    screen_fade = pygame.Surface((screen.get_width(), screen.get_height()))
    screen_fade.fill((0, 0, 0))
    screen_fade.set_alpha(160)
    screen.blit(screen_fade, (0, 0))

    screen.blit(POPUP_FRAME_SCALED, POPUP_FRAME_RECT) 

    screen.blit(GAME_OVER_SCALED, GAME_OVER_RECT) 

    score_text = my_fonts[2].render(f"Score : {score}", True, (254, 250, 181))
    screen.blit(score_text, (560, 310))
    best_score_text = my_fonts[2].render(f"Best Score : {read_best_score_file()}", True, (254, 250, 181))
    screen.blit(best_score_text, (510, 360))

    wood_button_scaled = pygame.transform.smoothscale(WOOD_BUTTON, (WOOD_BUTTON.get_size()[0]*0.19, WOOD_BUTTON.get_size()[1]*0.19))
    wood_button_hover_scaled = pygame.transform.smoothscale(WOOD_BUTTON_HOVER, (WOOD_BUTTON_HOVER.get_size()[0]*0.19, WOOD_BUTTON_HOVER.get_size()[1]*0.19))
    wood_button_rect_replay = wood_button_scaled.get_rect(center=(492, 510))
    wood_button_rect_gotomenu = wood_button_scaled.get_rect(center=(778, 510))
    
    replay_button = pygame.Rect((366, 474, 250, 70))
    if replay_button.collidepoint(pygame.mouse.get_pos()):
        screen.blit(wood_button_hover_scaled, wood_button_rect_replay)
    else:
        screen.blit(wood_button_scaled, wood_button_rect_replay) 
    replay_button_text = my_fonts[3].render("Replay", True, (254, 250, 181))
    screen.blit(replay_button_text, (448, 495))

    gotomenu_button = pygame.Rect((655, 474, 250, 70))
    if gotomenu_button.collidepoint(pygame.mouse.get_pos()):
         screen.blit(wood_button_hover_scaled, wood_button_rect_gotomenu)
    else:
        screen.blit(wood_button_scaled, wood_button_rect_gotomenu) 
    gotomenu_button_text = my_fonts[3].render("Menu", True, (254, 250, 181))
    screen.blit(gotomenu_button_text, (742, 495))

    return replay_button, gotomenu_button

def replay_menu_popup(screen, my_fonts, mouseclicked, score):

    usr_choice = 0
    loop_locker = True
        
    replay_button, gotomenu_button = popup_rendering(screen, my_fonts, score)

    if replay_button.collidepoint(pygame.mouse.get_pos()):
        if mouseclicked:
            pygame.mouse.set_cursor(pygame.SYSTEM_CURSOR_ARROW)
            usr_choice = 1
            loop_locker = False

        else:
            pygame.mouse.set_cursor(pygame.SYSTEM_CURSOR_HAND)

    elif gotomenu_button.collidepoint(pygame.mouse.get_pos()):
        if mouseclicked:
            pygame.mouse.set_cursor(pygame.SYSTEM_CURSOR_ARROW)
            usr_choice = 2
            loop_locker = False

        else:
            pygame.mouse.set_cursor(pygame.SYSTEM_CURSOR_HAND)

    else:
        pygame.mouse.set_cursor(pygame.SYSTEM_CURSOR_ARROW) 

    return loop_locker, usr_choice