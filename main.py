# Libraries

import pygame
import os

from src.menu import *

# Variables

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
FONT_PATH = os.path.join(BASE_DIR, "assets", "font", "LiberationSans-Regular.ttf")

# Main program

if __name__ == "__main__":

    pygame.init()
    pygame.font.init()

    pygame.display.set_caption("Fruit Slicer")

    pygame.key.set_repeat(400, 50)

    screen = pygame.display.set_mode((1280, 720))
    my_fonts = pygame.font.Font(FONT_PATH, 30), pygame.font.Font(FONT_PATH, 50)
    clock = pygame.time.Clock()

    menu(screen, clock, my_fonts)
