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
    fruit_rate = 1
    freeze = False
    freeze_time = 0
    pause = False
    score = 0
    combo = 0
    combo_timer = 0
    combo_timeout = 1.2
    combo_multiplier = 1
    strike = 0
    game_over = False

    return fruits, fruit_rate, freeze, freeze_time, pause, score, combo, combo_timer, combo_timeout, combo_multiplier, strike, game_over

def usr_slice(
    events,
    fruits,
    score,
    game_over,
    freeze,
    freeze_time,
    combo,
    combo_timer,
    combo_multiplier,
    combo_timeout
):
    
    sliced_count = 0

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
                sliced_count += 1
                freeze_time = time.monotonic()
                del fruits[key]

            else:
                sliced_count += 1
                del fruits[key]

        if not game_over:
            score, combo, combo_timer, combo_multiplier = update_combo_score(
            score,
            sliced_count,
            combo,
            combo_timer,
            combo_multiplier,
            combo_timeout
        )
            
    return fruits, game_over, freeze, freeze_time, score, combo, combo_timer, combo_multiplier

def update_combo_score(
    score,
    sliced_count,
    combo,
    combo_timer,
    combo_multiplier,
    combo_timeout
):
    now = time.monotonic()

    if sliced_count > 0:
        if now - combo_timer <= combo_timeout:
            combo += sliced_count
        else:
            combo = sliced_count

        combo_timer = now
        combo_multiplier = 1 + combo // 3
        score += sliced_count * combo_multiplier

    else:
        if now - combo_timer > combo_timeout:
            combo = 0
            combo_multiplier = 1

    return score, combo, combo_timer, combo_multiplier


def game(screen, clock, my_fonts):

    running = True
    time_since_last_fruit = time.monotonic()
    time_since_last_fruit_rate_update = time.monotonic()
    time_since_last_spawn_rate_update = time.monotonic()
    time_to_spawn = 1

    fruits, fruit_rate, freeze, freeze_time, pause, score, combo, combo_timer, combo_timeout, combo_multiplier, strike, game_over = reset_values()

    while running:

        dt = clock.tick(75) / 1000.0

        events, mouseclicked, escpressed = pygame_events()

        game_background_render(screen)

        if escpressed and not pause:
            pause = True
            pause_start_time = time.monotonic()
        
        elif game_over:
            if score > read_best_score_file():
                write_best_score(score)
            game_over, usr_choice = replay_menu_popup(screen, my_fonts, mouseclicked, score)
            if usr_choice == 1:
                fruits, fruit_rate, freeze, freeze_time, pause, score, combo, combo_timer, combo_timeout, combo_multiplier, strike, game_over = reset_values()
                continue
            elif usr_choice == 2:
                running = False
        else:

            if not (freeze or pause):
                fruits = move_fruits(fruits, dt)
                out_fruits_id = fruits_out_id(screen, fruits)
                if out_fruits_id:
                    for id in out_fruits_id:
                        if fruits[id]["fruit_img"][0] != "bomb" and fruits[id]["fruit_img"][0] != "ice":
                            
                            strike += 1
                            if strike >= 3:
                                game_over = True
                        del fruits[id]

                if time.monotonic() - time_since_last_fruit >= time_to_spawn:
                    if time_to_spawn == 1 and fruit_rate == 1:
                        time_to_spawn = 4
                    fruit_count = random.randint(1, min(fruit_rate, 5))
                    for i in range(fruit_count):
                        fruits = create_fruit(fruits)
        
                    time_since_last_fruit = time.monotonic()


                if time.monotonic() - time_since_last_fruit_rate_update >= 15.0:
                    time_since_last_fruit_rate_update = time.monotonic()
                    fruit_rate += 1
                
                if time.monotonic() - time_since_last_spawn_rate_update >= 15.0:
                    time_since_last_spawn_rate_update = time.monotonic()
                    if time_to_spawn > 2.5:
                        time_to_spawn -= 1
    
                fruits_render(screen, fruits, my_fonts)

            elif freeze and not pause:
                fruits_render(screen, fruits, my_fonts)
                frozen_effect(screen)
                if time.monotonic() - freeze_time >= 3.0:
                    freeze = False

            elif pause:
                fruits_render(screen, fruits, my_fonts)
                if freeze:
                    frozen_effect(screen)

                pause_ui(screen, my_fonts)

                usr_unpause = keyboard_input(events)

                if escpressed:
                    running = False
                elif usr_unpause:
                    freeze_time += time.monotonic() - pause_start_time 
                    pause = False
                    continue

            fruits, game_over, freeze, freeze_time, score, combo, combo_timer, combo_multiplier = usr_slice(
            events,
            fruits,
            score,
            game_over,
            freeze,
            freeze_time,
            combo,
            combo_timer,
            combo_multiplier,
            combo_timeout
        )
            
            ui_render(screen, my_fonts, score, strike)

        pygame.display.flip()
