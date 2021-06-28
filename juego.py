import pygame
import random

AZUL_CLARO=[76,160,233]
VERDE_CLARO=[16, 183, 18]
NEGRO=[0,0,0]
BLANCO=[255,255,255]
AMARILLO=[237, 234, 29]
ROJO=[255, 0, 0]

ANCHO=1000
ALTO=600

class Jugador(pygame.sprite.Sprite):
    def __init__(self, cl=AZUL_CLARO):
        pygame.sprite.Sprite.__init__(self)
        self.image=pygame.Surface([40, 50])
        self.image.fill(cl)
        self.rect= self.image.get_rect()
        self.rect.x= 200
        self.rect.y= 200
        self.velx=0
        self.vely=0

    def update(self):
        self.rect.x += self.velx  







if __name__ == '__main__':
    pygame.init()
    pantalla = pygame.display.set_mode([ANCHO, ALTO])



    jugadores = pygame.sprite.Group()

    j=Jugador()
    jugadores.add(j)




    reloj=pygame.time.Clock()
    fin_juego=False
    fin=False

    while (not fin) and (not fin_juego):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                fin = True




        jugadores.update()
        

        # Refresco de pantalla
        pantalla.fill(NEGRO)

        # Dibujo de los elementos
        jugadores.draw(pantalla)
        
        
        
        pygame.display.flip()
        reloj.tick(40)