# Libraries

import pygame

from src.assets_loading import BACKGROUND_IMG
from src.game.ui import ui_render
from src.pygame_events import pygame_events
from src.game.fruits import *
from src.game.keyboard_input import keyboard_input
from src.popup import replay_menu_popup

# Functions

def reset_values():

    fruits = {}
    counter = 0 #temporary just for now for me to test new fruits to not be popping all the time 
    fruit_rate = 100
    score = 0
    strike = 0
    game_over = False

    return fruits, counter, fruit_rate, score, strike, game_over

def game(screen, clock, my_fonts):

    running = True
    
    background_rect = BACKGROUND_IMG.get_rect(topleft=(0, 0))
    background_scaled = pygame.transform.smoothscale(BACKGROUND_IMG, (BACKGROUND_IMG.get_size()[0]*0.84, BACKGROUND_IMG.get_size()[1]*0.84))

    fruits, counter, fruit_rate, score, strike, game_over = reset_values()

    while running:

        dt = clock.tick(60) / 1000.0

        events, mouseclicked, escpressed = pygame_events()

        ui_render(screen, background_scaled, background_rect)

        if escpressed:
            running = False
        
        elif game_over:
            game_over, usr_choice = replay_menu_popup(screen, my_fonts, mouseclicked)
            if usr_choice == 1:
                fruits, counter, fruit_rate, score, strike, game_over = reset_values()
                continue
            elif usr_choice == 2:
                running = False
        else:

            fruits_render(screen, fruits, my_fonts)
            fruits = move_fruits(screen, fruits, dt)

            fruit_id = check_fruits_out()
            if fruit_id:
                del fruits[fruit_id]

            if counter % fruit_rate == 0:
                fruits = create_fruit(fruits)

            usr_input = keyboard_input(events)

        if usr_input != "":
            to_delete = []

            for key, fruit in fruits.items():
                if usr_input == fruit["letters"]:
                    to_delete.append(key)

            for key in to_delete:
                
                if fruits[key]["fruit_img"][0] == "bomb":
                    game_over = True

                elif fruits[key]["fruit_img"][0] == "ice":
                    pass
                    # tbd freeze

                else:
                    del fruits[key]

            if len(to_delete) > 3:
                score += len(to_delete) + 1
            else:
                score += len(to_delete)

        counter += 1
        pygame.display.flip()
