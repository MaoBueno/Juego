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

        if self.rect.left < 0:     # Limite en x (izquierda)
            self.rect.left = 0
        
        
        if self.rect.right > ANCHO: # Otra forma de definir los limites
            self.rect.right = ANCHO





        self.rect.y += self.vely

        # Limites en Y
        if self.rect.y < 0:
                self.rect.y=0
        
        if self.rect.bottom > ALTO:
            self.rect.bottom = ALTO






if __name__ == '__main__':
    pygame.init()
    pantalla = pygame.display.set_mode([ANCHO, ALTO])
    fondo=pygame.image.load("Fondo.png")
    info=fondo.get_rect()
    f_ancho=info[2]
    f_alto=info[3]
    print("Propiedades del fondo: ", f_ancho, f_alto)
    f_x=0
    f_vx=0
    f_limite_x= ANCHO - f_ancho
    
    f_y=0
    f_vy=0
    f_limite_y= ALTO - f_alto

    lim_derecho=ANCHO-40
    lim_izquierdo=40

    lim_superior=40
    lim_inferior=ALTO-60



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
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_RIGHT:
                    j.velx=5
                    j.vely=0
                if event.key == pygame.K_LEFT:
                    j.velx=-5
                    j.vely=0
                if event.key == pygame.K_UP:
                    j.velx=0
                    j.vely=-5
                if event.key == pygame.K_DOWN:
                    j.velx=0
                    j.vely=5
            if event.type == pygame.KEYUP:
                j.vely=0
                j.velx=0
        
        # Control de fondo en x
        if j.rect.right > lim_derecho:
            j.rect.right = lim_derecho
            #j.velx=0
            f_vx=-5
        elif j.rect.left < lim_izquierdo:
            j.rect.left = lim_izquierdo
            #j.velx=0
            f_vx=5
        else:
            f_vx = 0
        

        #Control de fondo en y
        if j.rect.top < lim_superior:
            j.rect.top = lim_superior
            #j.velx=0
            f_vy=5
        elif j.rect.bottom > lim_inferior:
            j.rect.bottom = lim_inferior
            #j.velx=0
            f_vy=-5
        else:
            f_vy = 0




        jugadores.update()
        

        # Refresco de pantalla
        #pantalla.fill(NEGRO)
        pantalla.blit(fondo, [f_x, f_y])

        # Dibujo de los elementos
        jugadores.draw(pantalla)
        
        
        
        pygame.display.flip()
        reloj.tick(40)

        #Control del limite en x del fondo
        if f_x >= f_limite_x:
            f_x+=f_vx
        else:
            f_x = f_limite_x
        
        if f_x >= 0:
            f_x = 0
        

        #Control del limite en y del fondo
        if f_y >= f_limite_y:
            f_y+=f_vy
        else:
            f_y = f_limite_y
        
        if f_y >= 0:
            f_y = 0