# Libraries

import pygame

from src.assets_loading import BACKGROUND_RECT, BACKGROUND_SCALED, WOOD_BUTTON, WOOD_BUTTON_HOVER
from src.pygame_events import pygame_events

# Functions

def option_rendering(screen, my_fonts):
    
    screen.blit(BACKGROUND_SCALED, BACKGROUND_RECT)

    screen_fade = pygame.Surface((screen.get_width(), screen.get_height()))
    screen_fade.fill((0, 0, 0))
    screen_fade.set_alpha(80)
    screen.blit(screen_fade, (0, 0))

    wood_button_scaled = pygame.transform.smoothscale(WOOD_BUTTON, (WOOD_BUTTON.get_size()[0]*0.27, WOOD_BUTTON.get_size()[1]*0.27))
    wood_button_hover_scaled = pygame.transform.smoothscale(WOOD_BUTTON_HOVER, (WOOD_BUTTON_HOVER.get_size()[0]*0.27, WOOD_BUTTON_HOVER.get_size()[1]*0.27))
    wood_button_rect_clear_best_score = wood_button_scaled.get_rect(center=(640, 440))
    wood_button_rect_change_scale = wood_button_scaled.get_rect(center=(640, 510))
    wood_button_rect_back = wood_button_scaled.get_rect(center=(640, 590))

    change_scale_button = pygame.Rect((464, 390, 356, 100))
    if change_scale_button.collidepoint(pygame.mouse.get_pos()):
        screen.blit(wood_button_hover_scaled, wood_button_rect_change_scale) 
    else:
        screen.blit(wood_button_scaled, wood_button_rect_change_scale) 
    change_scale_button_text = my_fonts[2].render("Change Window Size", True, (254, 250, 181))
    screen.blit(change_scale_button_text, (597, 416))

    clear_best_score_button = pygame.Rect((464, 460, 356, 100))
    if clear_best_score_button.collidepoint(pygame.mouse.get_pos()):
        screen.blit(wood_button_hover_scaled, wood_button_rect_clear_best_score) 
    else:
        screen.blit(wood_button_scaled, wood_button_rect_clear_best_score) 
    clear_best_score_button_text = my_fonts[2].render("Clear Best Score", True, (254, 250, 181))
    screen.blit(clear_best_score_button_text, (597, 416))

    back_button = pygame.Rect((464, 540, 356, 100))
    if back_button.collidepoint(pygame.mouse.get_pos()):
        screen.blit(wood_button_hover_scaled, wood_button_rect_back) 
    else:
        screen.blit(wood_button_scaled, wood_button_rect_back) 
    back_button_text = my_fonts[2].render("Back", True, (254, 250, 181))
    screen.blit(back_button_text, (564, 567)) 

    return change_scale_button, clear_best_score_button, back_button

def options(screen, clock, my_fonts, screen_scale):

    while True:

        events, mouseclicked, escpressed = pygame_events()

        change_scale_button, clear_best_score_button, back_button = option_rendering(screen, my_fonts)

        if escpressed:
            break

        elif change_scale_button.collidepoint(pygame.mouse.get_pos()) or clear_best_score_button.collidepoint(pygame.mouse.get_pos()) or back_button.collidepoint(pygame.mouse.get_pos()):
            if mouseclicked:
                pygame.mouse.set_cursor(pygame.SYSTEM_CURSOR_ARROW) 
                if change_scale_button.collidepoint(pygame.mouse.get_pos()):
                    # tbd scale
                    pass
                elif clear_best_score_button.collidepoint(pygame.mouse.get_pos()):
                    #tbd clear best score
                    pass
                else:
                    break
            else:
                pygame.mouse.set_cursor(pygame.SYSTEM_CURSOR_HAND)
        else:
            pygame.mouse.set_cursor(pygame.SYSTEM_CURSOR_ARROW)

        pygame.display.flip()  
        clock.tick(60)
