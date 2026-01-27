# Libraries

import pygame

from src.assets_loading import WOOD_BUTTON, WOOD_BUTTON_HOVER, POPUP_FRAME, GAME_OVER_IMG

# Functions

def popup_rendering(screen, my_fonts):

    screen_fade = pygame.Surface((screen.get_width(), screen.get_height()))
    screen_fade.fill((0, 0, 0))
    screen_fade.set_alpha(160)
    screen.blit(screen_fade, (0, 0))

    popup_frame_rect = POPUP_FRAME.get_rect(topleft=(260, 5))
    popup_frame_scaled = pygame.transform.smoothscale(POPUP_FRAME, (POPUP_FRAME.get_size()[0]*0.37, POPUP_FRAME.get_size()[1]*0.37))
    screen.blit(popup_frame_scaled, popup_frame_rect) 

    game_over_rect = GAME_OVER_IMG.get_rect(topleft=(349, 160))
    game_over_scaled = pygame.transform.smoothscale(GAME_OVER_IMG, (GAME_OVER_IMG.get_size()[0]*0.3, GAME_OVER_IMG.get_size()[1]*0.3))
    screen.blit(game_over_scaled, game_over_rect) 

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

def replay_menu_popup(screen, my_fonts, mouseclicked):

    usr_choice = 0
    loop_locker = True
        
    replay_button, gotomenu_button = popup_rendering(screen, my_fonts)

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