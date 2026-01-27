# Libraries

import pygame
import random
import string

from src.ui import ui_render
from .pygame_events import pygame_events
from src.assets_loading import fruits_src

# Functions

def create_fruit(fruits):
    fruit_name = random.choice(list(fruits_src.items()))
    fruits[fruit_name] = [
        (random.randint(-400, 1500), random.randint(-100, -10)), random.choice(string.ascii_letters)
    ]

    return fruits


def game(screen, clock):

    running = True
    # fruits_pos = {
    #     "apple0": [(300, 200), "k"]
    # }

    fruits = {}

    while running:
        events, mouseclicked, escpressed = pygame_events()

        if escpressed:
            running = False

        ui_render(screen)
        fruits = create_fruit(fruits)

        # Logic


        pygame.display.flip()
        clock.tick(60)

