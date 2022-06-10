import pygame
import sys
from nave import Nave

class CumbiFire:
    def __init__(self):
        pygame.init()
        self.screen = pygame.display.set_mode((800, 500))
        pygame.display.set_caption("Cumbi Fire")
        self.color = (255,200,0)
        self.nave = Nave(self)

    def corre_juego(self):
        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    sys.exit()
                elif event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_RIGHT:
                        self.nave.mover_derecha = True
                    if event.key == pygame.K_LEFT: 
                        self.nave.mover_izquierda = True  
                elif event.type == pygame.KEYUP:
                    if event.key == pygame.K_RIGHT:
                        self.nave.mover_derecha = False
                    if event.key == pygame.K_LEFT:
                        self.nave.mover_izquierda = False

            self.nave.mover()            

            self.screen.fill(self.color)
            self.nave.corre()
            pygame.display.flip()  


if __name__ == "__main__":
    a = CumbiFire()
    a.corre_juego()            

