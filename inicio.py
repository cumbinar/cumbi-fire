import pygame
import sys
from nave import Nave
from bala import Bullet

class CumbiFire:
    def __init__(self):
        pygame.init()
        self.screen = pygame.display.set_mode((800, 500))
        self.screen_width = self.screen.get_rect().width
        self.screen_height = self.screen.get_rect().height
        pygame.display.set_caption("Cumbi Fire")
        self.color = (255,200,0)
        self.velocidad = 0.5
        self.anchobala = 6
        self.altobala = 16
        self.colorbala =(225,0,0)
        self.nave = Nave(self)
        self.bullets = pygame.sprite.Group()
        self.balas_totales = 3

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
                    if event.key == pygame.K_SPACE:   
                        self._fire_bullet() 
                elif event.type == pygame.KEYUP:
                    if event.key == pygame.K_RIGHT:
                        self.nave.mover_derecha = False
                    if event.key == pygame.K_LEFT:
                        self.nave.mover_izquierda = False

            self.nave.mover()            

            self.screen.fill(self.color)
            self.nave.corre()
            self.bullets.update()
            for bullet in self.bullets.copy():
                if bullet.rect.bottom <= 0:
                    self.bullets.remove(bullet) 
                    #print(len(self.bullets))

            for bullet in self.bullets.sprites():
                bullet.draw_bullet()
                

            pygame.display.flip() 

    def _fire_bullet(self):
        if self.balas_totales != 0:
            new_bullet = Bullet(self)
            self.bullets.add(new_bullet)     
            self.balas_totales = self.balas_totales - 1   


if __name__ == "__main__":
    a = CumbiFire()
    a.corre_juego()            

