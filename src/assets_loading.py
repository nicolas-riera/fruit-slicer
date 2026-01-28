# Libraries

import pygame
import os

# Variables

BASE_DIR = os.path.dirname(os.path.abspath(__file__))

LOGO_TITLE = pygame.image.load(os.path.join(BASE_DIR, "..", "assets", "img", "logo_title.png"))
BACKGROUND_IMG = pygame.image.load(os.path.join(BASE_DIR, "..", "assets", "img", "background.png"))

WOOD_BUTTON = pygame.image.load(os.path.join(BASE_DIR, "..", "assets", "img", "wood_button.png"))
WOOD_BUTTON_HOVER = WOOD_BUTTON.copy()
filtre = pygame.Surface(WOOD_BUTTON.get_size(), pygame.SRCALPHA)
filtre.fill((25, 10, 0, 0))
WOOD_BUTTON_HOVER.blit(filtre, (0, 0), special_flags=pygame.BLEND_RGBA_ADD)

POPUP_FRAME = pygame.image.load(os.path.join(BASE_DIR, "..", "assets", "img", "popup_frame.png"))
GAME_OVER_IMG = pygame.image.load(os.path.join(BASE_DIR, "..", "assets", "img", "game_over.png"))

FRUIT_SIZE = (70, 70)
FRUITS_SRC = {
    "apple": pygame.transform.scale(
            pygame.image.load(os.path.join(
            BASE_DIR, "..", "assets", "img", "fruits", "apple.png")
        ),
        FRUIT_SIZE
    ),
    "banana": pygame.transform.scale(
        pygame.image.load(os.path.join(
        BASE_DIR, "..", "assets", "img", "fruits", "banana.png")
        ),
        FRUIT_SIZE
    ),
    "bomb": pygame.transform.scale(
        pygame.image.load(os.path.join(
        BASE_DIR, "..", "assets", "img", "fruits", "bomb.png")
        ),
        FRUIT_SIZE
    ),
    "cherry": pygame.transform.scale(
        pygame.image.load(os.path.join(
        BASE_DIR, "..", "assets", "img", "fruits", "cherry.png")
        ),
        FRUIT_SIZE
    ),
    "ice": pygame.transform.scale(
        pygame.image.load(os.path.join(
        BASE_DIR, "..", "assets", "img", "fruits", "ice.png")
        ),
        FRUIT_SIZE
    ),
    "lemon": pygame.transform.scale(
        pygame.image.load(os.path.join(
        BASE_DIR, "..", "assets", "img", "fruits", "lemon.png")
        ),
        FRUIT_SIZE
    ),
    "mango": pygame.transform.scale(
        pygame.image.load(os.path.join(
        BASE_DIR, "..", "assets", "img", "fruits", "mango.png")
        ),
        FRUIT_SIZE
    ),
    "orange": pygame.transform.scale(
        pygame.image.load(os.path.join(
        BASE_DIR, "..", "assets", "img", "fruits", "orange.png")
        ),
        FRUIT_SIZE
    ),
    "pear": pygame.transform.scale(
        pygame.image.load(os.path.join(
        BASE_DIR, "..", "assets", "img", "fruits", "pear.png")
        ),
        FRUIT_SIZE
    ),
    "pumpkin": pygame.transform.scale(
        pygame.image.load(os.path.join(
        BASE_DIR, "..", "assets", "img", "fruits", "pumpkin.png")
        ),
        FRUIT_SIZE
    ),
    "strawberry": pygame.transform.scale(
        pygame.image.load(os.path.join(
        BASE_DIR, "..", "assets", "img", "fruits", "strawberry.png")
        ),
        FRUIT_SIZE
    ),
    "watermelon": pygame.transform.scale(
        pygame.image.load(os.path.join(
        BASE_DIR, "..", "assets", "img", "fruits", "watermelon.png")
        ),
        FRUIT_SIZE
    )
}
