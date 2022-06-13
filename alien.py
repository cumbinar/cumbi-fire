import pygame
from pygame.sprite import Sprite


class alien(Sprite):
    def __init__(self, a_game):
        super().__init__()
        self.screen = a_game.screen
        