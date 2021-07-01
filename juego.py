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
    def __init__(self, imagen, cl=AZUL_CLARO):
        pygame.sprite.Sprite.__init__(self)
        self.imagen=imagen

        self.columna=0
        self.direccion=0

        self.image=self.imagen[self.direccion][self.columna]
        
        self.rect= self.image.get_rect()
        self.rect.x= 200
        self.rect.y= 200
        self.velx=0
        self.vely=0

        self.bloques=pygame.sprite.Group()
        

    def update(self):

        self.rect.x += self.velx        # Actualizacion de la velocidad en x
        

        
        colision=pygame.sprite.spritecollide(self, self.bloques, False)     # Control de posicion y colision con el bloque cuando el jugador se mueve en x
        for b in colision:
            if self.velx > 0:
                if self.rect.right >= b.rect.left:
                    self.rect.right = b.rect.left
            else:
                if self.rect.left <= b.rect.right:
                    self.rect.left = b.rect.right
            self.velx = 0
    

        

        if pygame.key.get_pressed()[pygame.K_RIGHT] or pygame.key.get_pressed()[pygame.K_LEFT] or pygame.key.get_pressed()[pygame.K_UP] or pygame.key.get_pressed()[pygame.K_DOWN]:
            if self.columna == 0:
                self.columna = 1
            else:
                self.columna = 0
            self.image=self.imagen[self.direccion][self.columna]
        else:
            self.columna = 0
        
        self.image=self.imagen[self.direccion][self.columna]

        
        

        if self.rect.left < 0:     # Limite en x (izquierda)
            self.rect.left = 0
        
        
        if self.rect.right > ANCHO: # Otra forma de definir los limites
            self.rect.right = ANCHO
        

        """ self.rect.x += self.velx
        # Control de posicion y colision con el bloque cuando el jugador se mueve en x
        colision=pygame.sprite.spritecollide(self, self.bloques, False)
        #print (colision)
        for b in colision:
            print (" For de la colision")
            if self.velx != 0:
                if self.rect.left < b.rect.right:
                        self.rect.left = b.rect.right
                        print ("< ------ ")
                
                if self.rect.right != b.rect.left:
                    self.rect.right = b.rect.left
                    print ("------ >")
                    
                self.velx = 0
        
        print ("Posicion en x: ", self.bloques) """
        



        # Actualizacion de la velocidad en y
        self.rect.y += self.vely



        # Control de posicion y colision con el bloque cuando el jugador se mueve en y
        colision=pygame.sprite.spritecollide(self, self.bloques, False)
        for b in colision:
            if self.vely > 0:
                if self.rect.bottom > b.rect.top:
                    self.rect.bottom = b.rect.top
            else:
                if self.rect.top < b.rect.bottom:
                    self.rect.top = b.rect.bottom
            self.vely = 0


        # Limites en Y
        if self.rect.y < 0:
                self.rect.y=0
        
        if self.rect.bottom > ALTO:
            self.rect.bottom = ALTO
        
        
        




class Bloque(pygame.sprite.Sprite):
    def __init__(self, pos, dim, cl=ROJO):
        pygame.sprite.Sprite.__init__(self)
        self.image=pygame.Surface(dim)
        self.colorb= self.image.set_alpha(50)
        self.image.fill(cl)
        self.rect= self.image.get_rect()
        self.rect.x= pos[0]
        self.rect.y= pos[1]
        self.velx= 0
        self.vely= 0
        self.jugadores=pygame.sprite.Group()
    
    def update(self):
        self.rect.x += self.velx

        # Control de posicion y colision con el jugador cuando el bloque se mueve en x
        colision_con_jugador=pygame.sprite.spritecollide(self, self.jugadores, False)
        for b in colision_con_jugador:
            if self.velx > 0:
                if self.rect.right > b.rect.left:
                    self.rect.right = b.rect.left
            else:
                if self.rect.left < b.rect.right:
                    self.rect.left = b.rect.right
            self.velx = 0 

        self.rect.y += self.vely

        # Control de posicion y colision con el jugador cuando el bloque se mueve en x
        colision_con_jugador=pygame.sprite.spritecollide(self, self.jugadores, False)
        for b in colision_con_jugador:
            if self.vely > 0:
                if self.rect.bottom > b.rect.top:
                    self.rect.bottom = b.rect.top
            else:
                if self.rect.top < b.rect.bottom:
                    self.rect.top = b.rect.bottom
            self.vely = 0 


# Funcion para recortar el sprite
def Matriz_imagen(imagenes, columnas, filas):
    info=imagenes.get_rect()
    corte_ancho=info[2]/columnas
    corte_alto=info[3]/filas
    lista=[]
    for i in range(filas):
        lista_aux=[]
        for j in range(columnas):
            cuadro = sprite_conejo.subsurface(corte_ancho * j, corte_alto * i, corte_ancho, corte_alto)
            lista_aux.append(cuadro)
        lista.append(lista_aux)
    return lista


if __name__ == '__main__':
    pygame.init()
    pantalla = pygame.display.set_mode([ANCHO, ALTO])       # Creacion de la ventana de juego


    #Cargando el fondo
    fondo=pygame.image.load("Fondo2.png")
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

    lim_derecho=ANCHO-100
    lim_izquierdo=100

    lim_superior=100
    lim_inferior=ALTO-100


    #Cargando sprites
    sprite_conejo = pygame.image.load('conejo.png')

    conejo = Matriz_imagen(sprite_conejo, 2, 6)
    

    #Grupos
    jugadores = pygame.sprite.Group()
    bloques = pygame.sprite.Group()

    # Instanciacion de elementos
    j=Jugador(conejo)
    j.bloques=bloques
    jugadores.add(j)

    
    b=Bloque([0, 0], [100, f_alto])    # limite izquierdo de la pantalla
    b.jugadores=jugadores
    bloques.add(b)

    
    b2=Bloque([f_ancho - 100, 0], [100, f_alto])  # limite Derecho de la pantalla
    b2.jugadores=jugadores
    bloques.add(b2)
    
    b3=Bloque([0, 0], [f_ancho, 100])    # Limite superior
    b3.jugadores=jugadores
    bloques.add(b3)


    b4=Bloque([0, f_alto - 130], [f_ancho, 130])     # limite inferior
    b4.jugadores=jugadores
    bloques.add(b4)
    

    # Bloques parte superior del tren
    b5=Bloque([280, 265], [40, 160]) # Sprite listo
    b5.jugadores=jugadores
    bloques.add(b5)

    b6=Bloque([975, 590], [170, 68]) # Sprite listo
    b6.jugadores=jugadores
    bloques.add(b6)

    b7=Bloque([1090, 990], [19, 62]) # Sprite listo
    b7.jugadores=jugadores
    bloques.add(b7)
    
    b8=Bloque([2050, 390], [19, 144]) # Sprite listo
    b8.jugadores=jugadores
    bloques.add(b8)

    b9=Bloque([2855, 470], [646, 135]) # Sprite listo
    b9.jugadores=jugadores
    bloques.add(b9)

    b10=Bloque([2970, 916], [22, 61]) # Sprite listo
    b10.jugadores=jugadores
    bloques.add(b10)

    b11=Bloque([4010, 195], [21, 62]) # Sprite listo
    b11.jugadores=jugadores
    bloques.add(b11)

    b12=Bloque([4170, 670], [21, 62]) # Sprite listo
    b12.jugadores=jugadores
    bloques.add(b12)

    # Bloques parte inferior del tren
    b13=Bloque([290, 1555], [20, 176]) # Sprite listo
    b13.jugadores=jugadores
    bloques.add(b13)

    b12=Bloque([220, 2230], [644, 140]) # Sprite listo
    b12.jugadores=jugadores
    bloques.add(b12)

    b13=Bloque([1010, 1710], [19, 65]) # Sprite listo
    b13.jugadores=jugadores
    bloques.add(b13)

    b14=Bloque([2050, 2070], [20, 60]) # Sprite listo
    b14.jugadores=jugadores
    bloques.add(b14)
    
    b15=Bloque([1810, 1395], [174, 62]) # Sprite listo
    b15.jugadores=jugadores
    bloques.add(b15)

    b16=Bloque([2610, 1475], [19, 66]) # Sprite listo
    b16.jugadores=jugadores
    bloques.add(b16)

    b17=Bloque([3170, 2230], [21, 142]) # Sprite listo
    b17.jugadores=jugadores
    bloques.add(b17)

    b18=Bloque([3690, 1910], [21, 144]) # Sprite listo
    b18.jugadores=jugadores
    bloques.add(b18)

    b19=Bloque([4090, 1630], [175, 67]) # Sprite listo
    b19.jugadores=jugadores
    bloques.add(b19)
    
    
    
    
    
    
    

    # Variable velocidad de jugador y fondo
    velocidad = 40

    reloj=pygame.time.Clock()
    fin_juego=False
    fin=False

    while (not fin) and (not fin_juego):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                fin = True
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_RIGHT:
                    j.velx=velocidad
                    j.vely=0
                    j.direccion=0
                    """ pantalla.blit(fondo, [f_x, f_y])
                    pantalla.blit(conejo[j.direccion][1], [j.rect.x + 8, j.rect.y])
                    pygame.display.flip()
                    reloj.tick(10) """
                if event.key == pygame.K_LEFT:
                    j.velx=-velocidad
                    j.vely=0
                    j.direccion=1
                    """ pantalla.blit(fondo, [f_x, f_y])
                    pantalla.blit(conejo[j.direccion][1], [j.rect.x - 8, j.rect.y])
                    pygame.display.flip()
                    reloj.tick(10) """
                if event.key == pygame.K_UP:
                    j.velx=0
                    j.vely=-velocidad
                    j.direccion=2
                    """ pantalla.blit(fondo, [f_x, f_y])
                    pantalla.blit(conejo[j.direccion][1], [j.rect.x, j.rect.y - 10])
                    pygame.display.flip()
                    reloj.tick(10) """
                if event.key == pygame.K_DOWN:
                    j.velx=0
                    j.vely=velocidad
                    j.direccion=3
                    """ pantalla.blit(fondo, [f_x, f_y])
                    pantalla.blit(conejo[j.direccion][1], [j.rect.x, j.rect.y + 10])
                    pygame.display.flip()
                    reloj.tick(10) """
            if event.type == pygame.KEYUP:
                j.vely=0
                j.velx=0
        

        # Control de fondo en x
        if j.rect.right > lim_derecho:
            j.rect.right = lim_derecho
            #j.velx=0
            f_vx=-velocidad
        elif j.rect.left < lim_izquierdo:
            j.rect.left = lim_izquierdo
            #j.velx=0
            f_vx=velocidad
        else:
            f_vx = 0
        

        #Control de fondo en y
        if j.rect.top < lim_superior:
            j.rect.top = lim_superior
            #j.velx=0
            f_vy=velocidad
        elif j.rect.bottom > lim_inferior:
            j.rect.bottom = lim_inferior
            #j.velx=0
            f_vy=-velocidad
        else:
            f_vy = 0


        ''' for b in bloques:
            if f_x > f_limite_x:
                b.velx=f_vx
            else:
                b.velx=0
            
            if f_y > f_limite_y:
                b.vely=f_vy
            else:
                b.vely=0 '''
        
        for b in bloques:
            b.velx=f_vx
            b.vely=f_vy
            

        
        
        

        # Refresco de pantalla
        
        #pantalla.fill(NEGRO)
        pantalla.blit(fondo, [f_x, f_y])

        #pantalla.blit(conejo[0][0], [100, 100])
        
        pygame.display.flip()
        

        # Dibujo de los elementos
        jugadores.draw(pantalla)
        bloques.draw(pantalla)

        bloques.update()
        jugadores.update()
        pygame.display.flip()
        reloj.tick(5)
        

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