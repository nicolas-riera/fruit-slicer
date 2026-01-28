# Libraries

import pygame
import random
import string
import itertools

from src.assets_loading import FRUITS_SRC

# Variables 

fruit_id_gen = itertools.count()

# Functions

def create_fruit(fruits):

    pos = pygame.Vector2(float(random.randint(0, 1280)), float(random.randint(720, 800)))

    if pos[0] < 300: # means fruit is at left so needs to go right
        velocity = pygame.Vector2(float(random.randint(20, 500)), float(random.randint(-1250, -1000)))
    else: # then its the opposite ;D
        velocity = pygame.Vector2(float(random.randint(-500, -20)), float(random.randint(-1250, -1000)))

    fruits[next(fruit_id_gen)] = {
        "fruit_img": random.choice(list(FRUITS_SRC.items())),
        "pos": pos,
        "rotation": 0,
        "velocity":velocity,
        "letters": random.choice([l for l in string.ascii_lowercase if l not in  {fruit["letters"] for fruit in fruits.values()}]).lower(),
    }

    return fruits

def fruits_render(screen, fruits, my_fonts):

    for fruit in fruits.values():

        rotated_fruit = pygame.transform.rotate(fruit["fruit_img"][1], fruit["rotation"])
        rotated_fruit_rect = rotated_fruit.get_rect(center=fruit["pos"])
        screen.blit(rotated_fruit, rotated_fruit_rect)

        fruit_letter = my_fonts[2].render(fruit["letters"], True, (254, 250, 181))
        screen.blit(fruit_letter, (fruit["pos"][0], fruit["pos"][1] - 60))

def move_fruits(screen, fruits, dt):
    
    for fruit in fruits.values():
        fruit["velocity"][1] += 1000 * dt #y velocity increasing
        fruit["velocity"][0] += 0 * dt #x velocity linear
        fruit["pos"][1] += fruit["velocity"][1] * dt #y pos changing from velocity
        fruit["pos"][0] += fruit["velocity"][0] * dt #x pos changing from velocity
        fruit["rotation"] += 5

    return fruits

def check_fruits_out():
    
    return None