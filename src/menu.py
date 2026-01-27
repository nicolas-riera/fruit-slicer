# Libraries

import os
import pygame

from src.assets_loading import LOGO_TITLE, BACKGROUND_IMG
from src.pygame_events import *
from src.game import game

# Functions

def menu(screen, clock, my_fonts):

    screen_scale = 1

    while True:
        
        # pygame events

        events, mouseclicked, escpressed = pygame_events()

        # Rendering 

        background_rect = BACKGROUND_IMG.get_rect(topleft=(0, 0))
        background_scaled = pygame.transform.smoothscale(BACKGROUND_IMG, (BACKGROUND_IMG.get_size()[0]*0.84, BACKGROUND_IMG.get_size()[1]*0.84))
        screen.blit(background_scaled, background_rect)

        logo_title_rect = LOGO_TITLE.get_rect(center=(1100, 550))
        logo_title_scaled = pygame.transform.smoothscale(LOGO_TITLE, (LOGO_TITLE.get_size()[0]*0.4, LOGO_TITLE.get_size()[1]*0.4))
        screen.blit(logo_title_scaled, logo_title_rect) 

        play_button = pygame.Rect((295, 400, 203, 80))
        play_button_text = my_fonts[0].render("Play", True, (0, 0, 0))
        screen.blit(play_button_text, (360, 420))

        option_button = pygame.Rect((295, 600, 203, 80))
        option_button_text = my_fonts[0].render("Options", True, (0, 0, 0))
        screen.blit(option_button_text, (346, 620))  

        # Logic

        if escpressed:
            pygame.quit()
            raise SystemExit

        elif play_button.collidepoint(pygame.mouse.get_pos()) or option_button.collidepoint(pygame.mouse.get_pos()):
            if mouseclicked:
                pygame.mouse.set_cursor(pygame.SYSTEM_CURSOR_ARROW)
                if play_button.collidepoint(pygame.mouse.get_pos()):
                    game(events, mouseclicked, escpressed)

                else:
                    # tbd options
                    pass
            else:
                pygame.mouse.set_cursor(pygame.SYSTEM_CURSOR_HAND)

        else:
            pygame.mouse.set_cursor(pygame.SYSTEM_CURSOR_ARROW)

        pygame.display.flip()  
        clock.tick(60)
