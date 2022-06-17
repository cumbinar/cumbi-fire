import pygame
from pygame.sprite import Sprite


class Alien(Sprite):
    def __init__(self, a_game):
        super().__init__()
        self.screen = a_game.screen

        self.image = pygame.image.load("imagenes/alien.png")
        self.rect = self.image.get_rect()

        self.rect.x = self.rect.width
        self.rect.y = self.rect.height

        self.x = float(self.rect.x)
        self.velocidad_Alien = a_game.velocidad_Alien
        