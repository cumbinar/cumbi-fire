import pygame
import sys

class CumbiFire:
    def __init__(self):
        pygame.init()
        self.screen = pygame.display.set_mode((800, 500))
        pygame.display.set_caption("Cumbi Fire")
        self.color = (242,242,242)

    def corre_juego(self):
        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    sys.exit()
            self.screen.fill(self.color)
            pygame.display.flip()  


if __name__ == "__main__":
    a = CumbiFire()
    a.corre_juego()            

