# Libraries

import pygame
import random
import string

from src.assets_loading import fruits_src

# Functions

def create_fruit(fruits):

    pos = pygame.Vector2(float(random.randint(0, 1280)), float(random.randint(720, 800)))

    if pos[0] < 300: # means fruit is at left so needs to go right
        velocity = pygame.Vector2(float(random.randint(20, 500)), float(random.randint(-1250, -1000)))
    else: # then its the opposite ;D
        velocity = pygame.Vector2(float(random.randint(-500, -20)), float(random.randint(-1250, -1000)))

    fruits[len(fruits)] = {
        "fruit_img": random.choice(list(fruits_src.items())),
        "pos": pos,
        "velocity":velocity,
        "letters": random.choice(string.ascii_letters).lower(),
    }

    return fruits

def fruits_render(screen, fruits):

    for fruit in fruits.values():
        screen.blit(fruit["fruit_img"][1], fruit["pos"])

def move_fruits(screen, fruits, dt):
    
    for fruit in fruits.values():
        fruit["velocity"][1] += 1000 * dt #y velocity increasing
        fruit["velocity"][0] += fruit["velocity"][0] * dt #x velocity linear
        fruit["pos"][1] += fruit["velocity"][1] * dt #y pos changing from velocity
        fruit["pos"][0] += fruit["velocity"][0] * dt #x pos changing from velocity

    return fruits

def check_fruits_out():
    
    return None