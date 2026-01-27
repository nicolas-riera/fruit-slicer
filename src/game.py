# Libraries

import pygame
import random
import string

from src.ui import ui_render
from .pygame_events import pygame_events
from src.assets_loading import fruits_src

# Functions

def create_fruit(fruits):
    fruits[len(fruits)] = {
        "fruit": random.choice(list(fruits_src.items())),
        "pos": (random.randint(-400, 1500), random.randint(-100, -10)),
        "letters": random.choice(string.ascii_letters).lower()
    }

    return fruits


def game(screen, clock):

    running = True

    fruits = {}
    counter = 0 #temporary just for now for me to test new fruits to not be popping all the time 
    while running:
        events, mouseclicked, escpressed = pygame_events()

        if escpressed:
            running = False

        ui_render(screen)
        if counter % 240 == 0 or counter == 0:
            fruits = create_fruit(fruits)
            print(fruits)

        # Logic

        counter += 1
        pygame.display.flip()
        clock.tick(60)

