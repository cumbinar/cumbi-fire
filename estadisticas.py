import pygame

class Estadisticas:

    def __init__(self, a_game):
        #self.reinicia()
        self.juego = a_game
        self.reinicia()
        
    def reinicia(self):
        self.naves_restantes = self.juego.naves_restantes
