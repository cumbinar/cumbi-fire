import pygame
import sys
from nave import Nave
from bala import Bullet
from alien import Alien

class CumbiFire:
    def __init__(self):
        pygame.init()
        self.ancho = 800
        self.screen = pygame.display.set_mode((self.ancho, 500))
        self.screen_width = self.screen.get_rect().width
        self.screen_height = self.screen.get_rect().height
        pygame.display.set_caption("Cumbi Fire")
        self.color = (220,220,220)
        self.velocidad = 0.5
        self.anchobala = 6
        self.altobala = 16
        self.colorbala =(225,0,0)
        self.nave = Nave(self)
        self.bullets = pygame.sprite.Group()
        #self.balas_totales = 3
        self.aliens = pygame.sprite.Group()
        self._create_fleet()

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

            self.aliens.draw(self.screen)   
                

            pygame.display.flip() 

    
    def _fire_bullet(self):
        
        new_bullet = Bullet(self)
        self.bullets.add(new_bullet) 

    def  _create_fleet(self): 
        alien = Alien(self)  
        alien_width = alien.rect.width
        availableSpace = self.ancho - (2*alien_width)
        numerodeAliens = availableSpace // (2*alien_width)

        for numeroAlien in range(numerodeAliens):
            alien = Alien(self)
            alien.x = alien_width + 2 * alien_width * numerodeAlien
            alien.rect.x = alien.x
            self.aliens.add(alien)

            
    
    '''def _fire_bullet(self): # se limita el numero de balas
        if self.balas_totales != 0:
            new_bullet = Bullet(self)
            self.bullets.add(new_bullet)     
            self.balas_totales = self.balas_totales - 1'''   




if __name__ == "__main__":
    a = CumbiFire()
    a.corre_juego()            

