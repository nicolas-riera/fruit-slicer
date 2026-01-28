# Libraries

import pygame
import os

# Variables

BASE_DIR = os.path.dirname(os.path.abspath(__file__))

LOGO_TITLE = pygame.image.load(os.path.join(BASE_DIR, "..", "assets", "img", "logo_title.png"))
LOGO_TITLE_RECT = LOGO_TITLE.get_rect(center=(1130, 550))
LOGO_TITLE_SCALED = pygame.transform.smoothscale(LOGO_TITLE, (LOGO_TITLE.get_size()[0]*0.4, LOGO_TITLE.get_size()[1]*0.4))

BACKGROUND_IMG = pygame.image.load(os.path.join(BASE_DIR, "..", "assets", "img", "background.png"))
BACKGROUND_RECT = BACKGROUND_IMG.get_rect(topleft=(0, 0))
BACKGROUND_SCALED = pygame.transform.smoothscale(BACKGROUND_IMG, (BACKGROUND_IMG.get_size()[0]*0.84, BACKGROUND_IMG.get_size()[1]*0.84))

WOOD_BUTTON = pygame.image.load(os.path.join(BASE_DIR, "..", "assets", "img", "wood_button.png"))
WOOD_BUTTON_HOVER = WOOD_BUTTON.copy()
filter = pygame.Surface(WOOD_BUTTON.get_size(), pygame.SRCALPHA)
filter.fill((25, 10, 0, 0))
WOOD_BUTTON_HOVER.blit(filter, (0, 0), special_flags=pygame.BLEND_RGBA_ADD)

POPUP_FRAME = pygame.image.load(os.path.join(BASE_DIR, "..", "assets", "img", "popup_frame.png"))
POPUP_FRAME_RECT = POPUP_FRAME.get_rect(topleft=(260, 5))
POPUP_FRAME_SCALED = pygame.transform.smoothscale(POPUP_FRAME, (POPUP_FRAME.get_size()[0]*0.37, POPUP_FRAME.get_size()[1]*0.37))

GAME_OVER_IMG = pygame.image.load(os.path.join(BASE_DIR, "..", "assets", "img", "game_over.png"))
GAME_OVER_RECT = GAME_OVER_IMG.get_rect(topleft=(349, 160))
GAME_OVER_SCALED = pygame.transform.smoothscale(GAME_OVER_IMG, (GAME_OVER_IMG.get_size()[0]*0.3, GAME_OVER_IMG.get_size()[1]*0.3))

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

X_BLACK = pygame.image.load(os.path.join(BASE_DIR, "..", "assets", "img", "X_black.png"))
X_BLACK_SCALED = pygame.transform.smoothscale(X_BLACK, (X_BLACK.get_size()[0]*0.1, X_BLACK.get_size()[1]*0.1))

X_RED = pygame.image.load(os.path.join(BASE_DIR, "..", "assets", "img", "X_red.png"))
X_RED_SCALED = pygame.transform.smoothscale(X_RED, (X_RED.get_size()[0]*0.1, X_RED.get_size()[1]*0.1))

FROZEN_EFFECT = pygame.image.load(os.path.join(BASE_DIR, "..", "assets", "img", "frozen_effect.png"))
FROZEN_EFFECT_SCALED = pygame.transform.scale(FROZEN_EFFECT, (FROZEN_EFFECT.get_size()[0]*5, FROZEN_EFFECT.get_size()[1]*5))
FROZEN_EFFECT_RECT = FROZEN_EFFECT_SCALED.get_rect(center=(640, 360))

