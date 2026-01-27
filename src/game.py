# Libraries

import pygame

from src.assets_loading import BACKGROUND_IMG

# Functions

def rendering(screen):

    background_rect = BACKGROUND_IMG.get_rect(topleft=(0, 0))
    background_scaled = pygame.transform.smoothscale(BACKGROUND_IMG, (BACKGROUND_IMG.get_size()[0]*0.84, BACKGROUND_IMG.get_size()[1]*0.84))
    screen.blit(background_scaled, background_rect)

def game(screen, clock, events, mouseclicked, escpressed:bool):

    running = True

    while running:
        
        rendering(screen)

        # Logic

        if escpressed:
            running = False
            continue

        pygame.display.flip()  
        clock.tick(60)

