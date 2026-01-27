# Libraries

import pygame
import os

# Variables

BASE_DIR = os.path.dirname(os.path.abspath(__file__))

LOGO_TITLE = pygame.image.load(os.path.join(BASE_DIR, "..", "assets", "img", "logo_title.png"))
BACKGROUND_IMG = pygame.image.load(os.path.join(BASE_DIR, "..", "assets", "img", "background.png"))
WOOD_BUTTON = pygame.image.load(os.path.join(BASE_DIR, "..", "assets", "img", "wood_button.png"))