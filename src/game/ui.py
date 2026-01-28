# Libraries

import pygame

from src.assets_loading import BACKGROUND_SCALED, BACKGROUND_RECT, X_BLACK_SCALED, X_RED_SCALED, FROZEN_EFFECT_RECT, FROZEN_EFFECT_SCALED

# Functions

def frozen_effect(screen):

    filter = pygame.Surface(screen.get_size(), pygame.SRCALPHA)
    filter.fill((0, 85, 105, 0))
    screen.blit(filter, (0, 0), special_flags=pygame.BLEND_RGBA_ADD)

    screen.blit(FROZEN_EFFECT_SCALED, FROZEN_EFFECT_RECT)

def display_strikes(screen, strike):    
    for i in range(3):
        if i < strike:
            x_red_rect = X_RED_SCALED.get_rect(center=(1150 + i *50, 28))
            screen.blit(X_RED_SCALED, x_red_rect)
        else:
            x_black_rect = X_BLACK_SCALED.get_rect(center=(1150 + i *50, 28))
            screen.blit(X_BLACK_SCALED, x_black_rect)

def display_scores(screen, my_fonts, score):
    score_text = my_fonts[2].render(f"Score : {score}", True, (254, 250, 181))
    screen.blit(score_text, (10, 10))

def ui_render(screen, my_fonts, score, strike):
    
    screen.blit(BACKGROUND_SCALED, BACKGROUND_RECT)

    display_strikes(screen, strike)

    display_scores(screen, my_fonts, score)