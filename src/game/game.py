# Libraries

import pygame
import time

from src.game.ui import *
from src.pygame_events import pygame_events
from src.game.fruits import *
from src.game.keyboard_input import keyboard_input
from src.popup import replay_menu_popup
from src.best_score import *

# Functions

def reset_values():

    fruits = {}
    counter = 0 #temporary just for now for me to test new fruits to not be popping all the time 
    fruit_rate = 90
    freeze = False
    freeze_time = 0
    score = 0
    strike = 0
    game_over = False

    return fruits, counter, fruit_rate, freeze, freeze_time, score, strike, game_over

def usr_slice(events, fruits, score, game_over, freeze, freeze_time):

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
                freeze = True
                freeze_time = time.monotonic()
                del fruits[key]

            else:
                del fruits[key]

        if not game_over:
            if len(to_delete) > 3:
                score += len(to_delete) + 1
            else:
                score += len(to_delete)

    return fruits, game_over, freeze, freeze_time, score

def game(screen, clock, my_fonts):

    running = True

    fruits, counter, fruit_rate, freeze, freeze_time, score, strike, game_over = reset_values()

    while running:

        dt = clock.tick(75) / 1000.0

        events, mouseclicked, escpressed = pygame_events()

        game_background_render(screen)

        if escpressed:
            running = False
        
        elif game_over:
            if score > read_best_score_file():
                write_best_score(score)
            game_over, usr_choice = replay_menu_popup(screen, my_fonts, mouseclicked, score)
            if usr_choice == 1:
                fruits, counter, fruit_rate, freeze, freeze_time, score, strike, game_over = reset_values()
                continue
            elif usr_choice == 2:
                running = False
        else:

            if not freeze:

                fruits = move_fruits(fruits, dt)

                out_fruits_id = fruits_out_id(screen, fruits)
                if out_fruits_id:
                    for id in out_fruits_id:
                        if fruits[id]["fruit_img"][0] != "bomb" and fruits[id]["fruit_img"][0] != "ice":
                            
                            strike += 1
                            if strike >= 3:
                                game_over = True
                        del fruits[id]

                if counter % fruit_rate == 0:
                    fruits = create_fruit(fruits)

                fruits_render(screen, fruits, my_fonts)

            else:
                fruits_render(screen, fruits, my_fonts)
                frozen_effect(screen)
                if time.monotonic() - freeze_time >= 3.0:
                    freeze = False
                    
            fruits, game_over, freeze, freeze_time, score = usr_slice(events, fruits, score, game_over, freeze, freeze_time)

            ui_render(screen, my_fonts, score, strike)

        counter += 1
        pygame.display.flip()
