# Libraries

import pygame
import unicodedata

# Functions

def keyboard_input(events):

    '''
    Translate in a more friendly way keyboard inputs selected pygame events.
    All events other than letters are ignored.       
    ### PARAMETER
            events: pygame.Events
    ### RETURN
            str
    '''

    for event in events:
        if event.type == pygame.KEYDOWN:
            char = event.unicode
            if unicodedata.category(char).startswith("L"):  
                return char
    return ""