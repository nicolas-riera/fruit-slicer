# Libraries

import pygame

from src.game.ui import ui_render
from src.pygame_events import pygame_events
from src.game.fruits import *

# Functions

def game(screen, clock):

    running = True

    fruits = {}
    counter = 0 #temporary just for now for me to test new fruits to not be popping all the time 
    while running:
        dt = clock.tick(60) / 1000.0

        events, mouseclicked, escpressed = pygame_events()

        if escpressed:
            running = False

        ui_render(screen)
        fruits_render(screen, fruits)
        fruits = move_fruits(screen, fruits, dt)

        fruit_id = check_fruits_out()
        if fruit_id:
            del fruits[fruit_id]

        if counter % 30 == 0 or counter == 0:
            fruits = create_fruit(fruits)
            print(fruits)

        # Logic

        counter += 1
        pygame.display.flip()
