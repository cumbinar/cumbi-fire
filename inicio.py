import pygame
import sys
from nave import Nave
from bala import Bullet
from alien import Alien
from estadisticas import Estadisticas
from time import sleep
from Boton import Boton

class CumbiFire:
    def __init__(self):
        pygame.init()
        self.ancho = 800
        self.alto = 500
        self.screen = pygame.display.set_mode((self.ancho, self.alto))
        self.screen_width = self.screen.get_rect().width
        self.screen_height = self.screen.get_rect().height
        pygame.display.set_caption("Cumbi Fire")
        self.color = (220,220,220)
        self.velocidad = 2
        self.anchobala = 7
        self.altobala = 16
        self.colorbala =(225,0,0)
        self.naves_restantes = 3  # tres vidas
        self.estadisticas = Estadisticas(self)
        self.nave = Nave(self)
        self.bullets = pygame.sprite.Group()
        self.balas_totales = 500
        self.aliens = pygame.sprite.Group()
        self.velocidad_Alien = 0.8
        self.flota_velocidad = 20
        self.flota_direccion = 1
        self.juego_activado = False
        self.play_boton = Boton(self, "Play")

        pygame.mixer.music.load("imagenes/guaguanco.wav")
        pygame.mixer.music.play(-1)
        pygame.mixer.music.set_volume(0.5)
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
                elif event.type == pygame.MOUSEBUTTONDOWN:
                    mousePos = pygame.mouse.get_pos()
                    self.checaBoton(mousePos)     

            if self.juego_activado:
                self.nave.mover()            
                self.screen.fill(self.color)
                self.nave.corre()
                self.bullets.update()
                self.update_alien()

                for bullet in self.bullets.copy():
                    if bullet.rect.bottom <= 0:
                        self.bullets.remove(bullet) 
                        #print(len(self.bullets))

                for bullet in self.bullets.sprites():
                    bullet.draw_bullet()
                self.aliens.draw(self.screen)   
                
            if not self.juego_activado:
                self.play_boton.dibujaBoton()

            pygame.display.flip() 

    
    def _fire_bullet(self):
        
        new_bullet = Bullet(self)
        self.bullets.add(new_bullet) 
       

    def  _create_fleet(self): 
        alien = Alien(self)  
        alien_width, alien_height =  alien.rect.size
        availableSpace = self.ancho - (2*alien_width)
        numerodeAliens = availableSpace // (2*alien_width)
        nave_height = self.nave.rect.height
        availableSpacey = self.alto- (3 * alien_height)- nave_height
        numeroFilas = availableSpacey // (2 * alien_height)

        for fila in range(numeroFilas):
            for numeroAlien in range(numerodeAliens):
               self._create_alien(numeroAlien, fila)

    def _create_alien(self, numeroAlien, fila): 
        alien = Alien(self)
        alien_width, alien_height = alien.rect.size
        alien.x = alien_width + 2 * alien_width * numeroAlien
        alien.rect.x = alien.x
        alien.rect.y = alien.rect.height + 2 * alien.rect.height * fila
        self.aliens.add(alien)

    def checa_bordesFlota(self):
        for alien in self.aliens.sprites():
            if alien.checa_bordes():
                self.cambia_direccion()
                break
    def cambia_direccion(self):
        for alien in self.aliens.sprites():
            alien.rect.y += self.flota_velocidad
        self.flota_direccion *= - 1    

    def update_alien(self):
        self.checa_bordesFlota()
        self.aliens.update()
        if not self.aliens:
            self.bullets.empty()
            self._create_fleet()
        if pygame.sprite.spritecollideany(self.nave, self.aliens):
           #print("fin")
           self.nave_colisionada()

    def nave_colisionada(self):
        if self.naves_restantes > 0:

            self.naves_restantes -= 1   
            
            self.aliens.empty()  
            self.bullets.empty()  

            self._create_fleet()
            self.nave.centrar_nave()

            sleep(1) #pausa 1 segundo para reiniciar

        else:
            self.juego_activado = False 

    def checaBoton(self, mousePos):
        #if self.play_boton.rect.collindepoint(mousePos):
        self.estadisticas.reinicia()
        self.juego_activado = True
        
        self.aliens.empty()
        self.bullets.empty()
        
        self._create_fleet()
        self.nave.centrar_nave()
        self.naves_restantes = 3
        




            
    
    '''def _fire_bullet(self): # se limita el numero de balas
        if self.balas_totales != 0:
            new_bullet = Bullet(self)
            self.bullets.add(new_bullet)     
            self.balas_totales = self.balas_totales - 1'''   




if __name__ == "__main__":
    a = CumbiFire()
    a.corre_juego()            

