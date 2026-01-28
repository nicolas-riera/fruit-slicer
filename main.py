# Libraries

import pygame
import os

from src.menu import *

# Variables

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
LIBREATIONSANS_FONT_PATH = os.path.join(BASE_DIR, "assets", "font", "LiberationSans-Regular.ttf")
MANGAT_FONT_PATH = os.path.join(BASE_DIR, "assets", "font", "mangat.ttf")

# Main program

if __name__ == "__main__":

    pygame.init()
    pygame.font.init()

    pygame.display.set_caption("Fruit Slicer")

    screen = pygame.display.set_mode((1280, 720))
    my_fonts = pygame.font.Font(LIBREATIONSANS_FONT_PATH, 30), pygame.font.Font(LIBREATIONSANS_FONT_PATH, 50), pygame.font.Font(MANGAT_FONT_PATH, 30), pygame.font.Font(MANGAT_FONT_PATH, 20), pygame.font.Font(MANGAT_FONT_PATH, 50)
    clock = pygame.time.Clock()

    menu(screen, clock, my_fonts)
