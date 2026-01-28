# Libraries

import pygame

from src.assets_loading import LOGO_TITLE, BACKGROUND_IMG, WOOD_BUTTON, WOOD_BUTTON_HOVER
from src.pygame_events import *
from src.game.game import game

# Functions

def menu_rendering(screen, my_fonts):

    background_rect = BACKGROUND_IMG.get_rect(topleft=(0, 0))
    background_scaled = pygame.transform.smoothscale(BACKGROUND_IMG, (BACKGROUND_IMG.get_size()[0]*0.84, BACKGROUND_IMG.get_size()[1]*0.84))
    screen.blit(background_scaled, background_rect)

    logo_title_rect = LOGO_TITLE.get_rect(center=(1130, 550))
    logo_title_scaled = pygame.transform.smoothscale(LOGO_TITLE, (LOGO_TITLE.get_size()[0]*0.4, LOGO_TITLE.get_size()[1]*0.4))
    screen.blit(logo_title_scaled, logo_title_rect) 

    wood_button_scaled = pygame.transform.smoothscale(WOOD_BUTTON, (WOOD_BUTTON.get_size()[0]*0.27, WOOD_BUTTON.get_size()[1]*0.27))
    wood_button_hover_scaled = pygame.transform.smoothscale(WOOD_BUTTON_HOVER, (WOOD_BUTTON_HOVER.get_size()[0]*0.27, WOOD_BUTTON_HOVER.get_size()[1]*0.27))
    wood_button_rect_play = wood_button_scaled.get_rect(center=(640, 440))
    wood_button_rect_option = wood_button_scaled.get_rect(center=(640, 590))

    play_button = pygame.Rect((464, 390, 356, 100))
    if play_button.collidepoint(pygame.mouse.get_pos()):
        screen.blit(wood_button_hover_scaled, wood_button_rect_play) 
    else:
        screen.blit(wood_button_scaled, wood_button_rect_play) 
    play_button_text = my_fonts[2].render("Play", True, (254, 250, 181))
    screen.blit(play_button_text, (597, 416))

    option_button = pygame.Rect((464, 540, 356, 100))
    if option_button.collidepoint(pygame.mouse.get_pos()):
        screen.blit(wood_button_hover_scaled, wood_button_rect_option) 
    else:
        screen.blit(wood_button_scaled, wood_button_rect_option) 
    option_button_text = my_fonts[2].render("Options", True, (254, 250, 181))
    screen.blit(option_button_text, (564, 567)) 

    return play_button, option_button 

def menu(screen, clock, my_fonts):

    screen_scale = 1

    while True:

        events, mouseclicked, escpressed = pygame_events()

        play_button, option_button = menu_rendering(screen, my_fonts)

        if escpressed:
            pygame.quit()
            raise SystemExit

        elif play_button.collidepoint(pygame.mouse.get_pos()) or option_button.collidepoint(pygame.mouse.get_pos()):
            if mouseclicked:
                pygame.mouse.set_cursor(pygame.SYSTEM_CURSOR_ARROW) 
                if play_button.collidepoint(pygame.mouse.get_pos()):
                    game(screen, clock, my_fonts)
                else:
                    #tbd option
                    pass
            else:
                pygame.mouse.set_cursor(pygame.SYSTEM_CURSOR_HAND)
        else:
            pygame.mouse.set_cursor(pygame.SYSTEM_CURSOR_ARROW)

        pygame.display.flip()  
        clock.tick(60)
