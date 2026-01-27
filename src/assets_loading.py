# Libraries

import pygame
import os

# Variables

BASE_DIR = os.path.dirname(os.path.abspath(__file__))

LOGO_TITLE = pygame.image.load(os.path.join(BASE_DIR, "..", "assets", "img", "logo_title.png"))
BACKGROUND_IMG = pygame.image.load(os.path.join(BASE_DIR, "..", "assets", "img", "background.png"))

WOOD_BUTTON = pygame.image.load(os.path.join(BASE_DIR, "..", "assets", "img", "wood_button.png"))
WOOD_BUTTON_HOVER = WOOD_BUTTON.copy()
filtre = pygame.Surface(WOOD_BUTTON.get_size(), pygame.SRCALPHA)
filtre.fill((25, 10, 0, 0))
WOOD_BUTTON_HOVER.blit(filtre, (0, 0), special_flags=pygame.BLEND_RGBA_ADD)