import pygame
import random
import math
import time
import threading

from pygame.draw import circle
from pygame.sprite import collide_circle, collide_circle_ratio, spritecollide

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
        self.rect.x= 500
        self.rect.y= 200
        self.velx=0
        self.vely=0

        self.vidas = 3
        self.win = 0

        self.bloques=pygame.sprite.Group()
        self.zanahorias=pygame.sprite.Group()
        

    def update(self):
        self.rect.x += self.velx        # Actualizacion de la velocidad en x
        
        colision_con_bloque=pygame.sprite.spritecollide(self, self.bloques, False)     # Control de posicion y colision con el bloque cuando el jugador se mueve en x
        for b in colision_con_bloque:
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
        
        # Actualizacion de la velocidad en y
        self.rect.y += self.vely

        # Control de posicion y colision con el bloque cuando el jugador se mueve en y
        colision_con_bloque=pygame.sprite.spritecollide(self, self.bloques, False)
        for b in colision_con_bloque:
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
        self.colorb= self.image.set_alpha(0)
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

class Zanahoria(pygame.sprite.Sprite):
    def __init__(self, imagen, pos, cl=BLANCO):
        pygame.sprite.Sprite.__init__(self)
        self.imagen=imagen

        self.columna=0
        self.direccion=0

        self.image = self.imagen[self.direccion][self.columna]
        #self.image.fill(cl)
        self.rect= self.image.get_rect()
        self.rect.x= pos[0]
        self.rect.y= pos[1]
        self.velx= 0
        self.vely= 0
        self.jugadores=pygame.sprite.Group()
        self.bloques=pygame.sprite.Group()

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


class Zanahoria_win(pygame.sprite.Sprite):
    def __init__(self, imagen, pos):
        pygame.sprite.Sprite.__init__(self)
        self.imagen=imagen

        self.columna=0
        self.direccion=2

        self.image = self.imagen[self.direccion][self.columna]
        #self.image.fill(cl)
        self.rect= self.image.get_rect()
        self.rect.x= pos[0]
        self.rect.y= pos[1]
        self.velx= 0
        self.vely= 0

        self.aux = False
        self.posicion_auxiliar = 400

        self.jugadores=pygame.sprite.Group()
        self.bloques=pygame.sprite.Group()


    def update(self):
        colision_conejo_win = pygame.sprite.spritecollide(self, self.jugadores, False)
        if colision_conejo_win:
            self.posicion_auxiliar+=30


        if self.columna < 5:
            self.columna+=1
        else:
            self.columna = 0

        self.image = self.imagen[self.direccion][self.columna]
        
        self.rect.x += self.velx 


        self.rect.y += self.vely
        
        


class Digito(pygame.sprite.Sprite):
    def __init__(self, imagen):
        pygame.sprite.Sprite.__init__(self)
        self.imagen=imagen

        self.temp = 100
        self.aux = None
        self.d = None

        self.columna=9
        self.direccion=0

        self.image=self.imagen[self.direccion][self.columna]
        
        self.rect= self.image.get_rect()
        self.rect.x= 850
        self.rect.y= 32

        self.jugador=pygame.sprite.Group()
        self.zanahoria= pygame.sprite.Group()

    def update(self):

        self.temp -= 2
        self.d= math.modf(self.temp/10)
        self.aux=int(self.d[1])

        self.image=self.imagen[self.direccion][self.aux]

class Lobo(pygame.sprite.Sprite):
    def __init__(self, imagen, pos):
        pygame.sprite.Sprite.__init__(self)
        self.imagen=imagen

        self.columna=random.randrange(0, 5)
        self.direccion=0

        self.image = self.imagen[self.direccion][self.columna]

        self.rect= self.image.get_rect()
        self.rect.x= pos[0]
        self.rect.y= pos[1]
        self.velx=30
        self.vely=0
        self.salir=False
        
        self.temp=random.randrange(500, 700)
    

    def update(self):
        self.temp-=1
        if self.temp <= 0:
            self.salir = True
        

        self.image=self.imagen[self.direccion][self.columna]
        if self.columna < 5:
            self.columna+=1
        else:
            self.columna = 0

        self.rect.x += self.velx + f_vx

        for l in lobos:
            if l.rect.left > f_ancho:
                lobos.remove(l)
        
        self.rect.y += self.vely + f_vy

class Perro(pygame.sprite.Sprite):
    def __init__(self, imagen, pos, cl=BLANCO):
        pygame.sprite.Sprite.__init__(self)
        self.imagen=imagen

        self.columna=0
        self.direccion=2

        self.image = self.imagen[self.direccion][self.columna]

        self.rect= self.image.get_rect()
        self.rect.x= pos[0]
        self.rect.y= pos[1]
        self.velx=0
        self.vely=0
        
        self.bloques=pygame.sprite.Group()

        self.orientacion = 0
        self.radius = 500
    

    def update(self):
        self.rect.x += self.velx + f_vx

        colision_perro_bloques=pygame.sprite.spritecollide(self, self.bloques, False)
        for b in colision_perro_bloques:
            if self.velx > 0:
                if self.rect.right > b.rect.left:
                    self.rect.right = b.rect.left
                    self.direccion = random.randrange(0, 3)
            else:
                if self.rect.left < b.rect.right:
                    self.rect.left = b.rect.right
                    self.direccion = random.randrange(0, 3)
            #self.velx = 0
        
        
        if self.direccion == 0:
            self.velx = -random.randrange(5, 30) 
            self.vely = f_vy
        elif self.direccion == 1:
            self.velx = random.randrange(5, 30) 
            self.vely = f_vy
        elif self.direccion == 2:
            self.velx = f_vx
            self.vely = random.randrange(5, 30) 
        elif self.direccion == 3:
            self.velx = f_vx
            self.vely = -(random.randrange(5, 30)) 

        
        if self.direccion == 4 or self.direccion == 5 or self.direccion == 6 or self.direccion == 7:
            self.velx = f_vx
            

        if self.columna < 4:
            self.columna+=1
        else:
            self.columna = 0

        if self.direccion == 2 or self.direccion == 3 or self.direccion == 6 or self.direccion == 7:
            self.image=pygame.transform.rotate(self.imagen[self.direccion][self.columna], 90)
        else:
            self.image=self.imagen[self.direccion][self.columna]


        self.rect.y += self.vely + f_vy

        colision_perro_bloque=pygame.sprite.spritecollide(self, self.bloques, False)
        for b in colision_perro_bloque:
            if self.vely > 0:
                if self.rect.bottom > b.rect.top:
                    self.rect.bottom = b.rect.top
                    self.direccion = random.randrange(0, 3)
            else:
                if self.rect.top < b.rect.bottom:
                    self.rect.top = b.rect.bottom
                    self.direccion = random.randrange(0, 3)
            #self.vely = 0
        
        if self.direccion == 0:
            self.velx = -random.randrange(5, 30)
            self.vely = f_vy
        elif self.direccion == 1:
            self.velx = random.randrange(5, 30)
            self.vely = f_vy
        elif self.direccion == 2:
            self.velx = f_vx
            self.vely = random.randrange(5, 30)
        elif self.direccion == 3:
            self.velx = f_vx
            self.vely = -(random.randrange(5, 30))

        if self.direccion == 4 or self.direccion == 5 or self.direccion == 6 or self.direccion == 7:
            self.vely = f_vy


class Vida(pygame.sprite.Sprite):
    def __init__(self, imagen, pos):
        pygame.sprite.Sprite.__init__(self)
        self.imagen=imagen

        self.columna=0
        self.direccion=0

        self.image = self.imagen[self.direccion][self.columna]
        #self.image.fill(cl)
        self.rect= self.image.get_rect()
        self.rect.x= pos[0]
        self.rect.y= pos[1]

        self.aux= 200

    def update(self):
        self.image = self.imagen[self.direccion][self.columna]


class Tren(pygame.sprite.Sprite):
    def __init__(self, imagen, pos):
        pygame.sprite.Sprite.__init__(self)
        self.imagen=imagen

        self.columna=0
        self.direccion=1

        self.image=self.imagen[self.direccion][self.columna]
        
        self.rect= self.image.get_rect()
        self.rect.x= pos[0]
        self.rect.y= pos[1]

        self.velx = 0
        self.vely = 0


    def update(self):
        self.rect.x += self.velx + f_vx

        self.rect.y += self.vely + f_vy
        
        if self.rect.right < 0:
            self.direccion = 1
            self.velx = 30
        self.image=self.imagen[self.direccion][self.columna]
        
        if self.rect.left > 4500:
            self.direccion = 0
            self.velx = -30

        self.image=self.imagen[self.direccion][self.columna]



# Funcion para recortar el sprite
def Matriz_imagen(imagenes, columnas, filas):
    info=imagenes.get_rect()
    corte_ancho=info[2]/columnas
    corte_alto=info[3]/filas
    lista=[]
    for i in range(filas):
        lista_aux=[]
        for j in range(columnas):
            cuadro = imagenes.subsurface(corte_ancho * j, corte_alto * i, corte_ancho, corte_alto)
            lista_aux.append(cuadro)
        lista.append(lista_aux)
    return lista

    



if __name__ == '__main__':
    pygame.init()
    pantalla = pygame.display.set_mode([ANCHO, ALTO])       # Creacion de la ventana de juego


    #Cargando el fondo
    fondo=pygame.image.load("fondo3.png")
    gameover = pygame.image.load("gameover2.png")
    ganar = pygame.image.load("ganar.png")
    tiempo = pygame.image.load("tiempo.png")
    opciones = pygame.image.load("opciones.png")
    instrucciones = pygame.image.load('instrucciones.png')

    info=fondo.get_rect()
    f_ancho=info[2]
    f_alto=info[3]
    f_x=0
    f_vx=0
    f_limite_x= ANCHO - f_ancho
    
    f_y=0
    f_vy=0
    f_limite_y= ALTO - f_alto

    lim_derecho=ANCHO-100
    lim_izquierdo=100

    lim_superior=160
    lim_inferior=ALTO-100


    #Cargando sprites
    sprite_conejo = pygame.image.load('conejo.png')
    sprite_zanahoria = pygame.image.load('z2.png')
    sprite_digito= pygame.image.load('digito.png')
    sprite_lobo = pygame.image.load('wolf.png')
    sprite_perro = pygame.image.load('perro.png')
    sprite_vidas_conejo = pygame.image.load("conejo-header2.png")
    sprite_zanahoria_win = pygame.image.load('win.png')
    sprite_piedra = pygame.image.load('madriguera.png')
    sprite_tren = pygame.image.load('tren.png')


    conejo = Matriz_imagen(sprite_conejo, 2, 6)
    zanahoria = Matriz_imagen(sprite_zanahoria, 1, 1)
    digito = Matriz_imagen(sprite_digito, 10, 1)
    lobo = Matriz_imagen(sprite_lobo, 6, 4)
    perro = Matriz_imagen(sprite_perro, 5, 8)
    vidas_conejo = Matriz_imagen(sprite_vidas_conejo, 1, 1)
    zanahoria_win = Matriz_imagen(sprite_zanahoria_win, 6, 3)
    piedra = Matriz_imagen(sprite_piedra, 1, 1)
    tren = Matriz_imagen(sprite_tren, 1, 2)

    
    #Grupos
    jugadores = pygame.sprite.Group()
    bloques = pygame.sprite.Group()
    zanahorias = pygame.sprite.Group()
    digitos = pygame.sprite.Group()
    lobos = pygame.sprite.Group()
    perros = pygame.sprite.Group()
    vidas = pygame.sprite.Group()
    zanahorias_win = pygame.sprite.Group()
    zanahorias2_win = pygame.sprite.Group()
    piedras = pygame.sprite.Group()
    trenes = pygame.sprite.Group()



    # Instanciacion de elementos
    j=Jugador(conejo)
    j.bloques=bloques
    j.zanahorias=zanahorias
    jugadores.add(j)


    d=Digito(digito)
    d.jugador = jugadores
    d.zanahoria = zanahorias
    digitos.add(d)


    limite_vidas = 0
    posicion_vidas = 100
    while limite_vidas < j.vidas:
        v = Vida(vidas_conejo, [posicion_vidas, 13])
        vidas.add(v)
        limite_vidas+=1
        posicion_vidas+=50

    
    b=Bloque([0, 0], [100, f_alto])    # limite izquierdo de la pantalla
    b.jugadores=jugadores
    bloques.add(b)

    
    b2=Bloque([f_ancho - 100, 0], [100, f_alto])  # limite Derecho de la pantalla
    b2.jugadores=jugadores
    bloques.add(b2)
    
    b3=Bloque([0, 0], [f_ancho, 170])    # Limite superior
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


    b12=Bloque([4170, 670], [21, 62], AMARILLO) # Sprite listo
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
    
    b20=Bloque([1600, 1135], [1050, 90]) # Sprite tren listo
    b20.jugadores=jugadores
    bloques.add(b20)

    
    limite_zanahorias =  0
    while limite_zanahorias <= 300:
        b=Zanahoria(zanahoria, [random.randrange(lim_izquierdo, f_ancho - 100), random.randrange(lim_superior, f_alto - 100)])
        zanahorias.add(b)
        limite_zanahorias+=1
    
    for w in zanahorias:    # Elimina las zanaorias en las vias del tren
        if w.rect.bottom >= 1160 and w.rect.top <= 1280:
            zanahorias.remove(w)
    
    colision_zanahoria_con_bloque=pygame.sprite.groupcollide(zanahorias, bloques, True, False, collided = None)     # Elimina las zanahrias de los arbustos
    
    
    limite_perros = 0
    while limite_perros <= 100:
        p= Perro(perro, [random.randrange(lim_izquierdo, f_ancho - 100), random.randrange(lim_superior, f_alto - 100)], [random.randrange(255), random.randrange(255), random.randrange(255)])
        perros.add(p)
        p.bloques = bloques
        p.direccion = random.randrange(4, 8)
        limite_perros+=1
    
    
    posicion_auxiliar= 400
    # Variable velocidad de jugador y fondo
    velocidad = 35
    menu = 0
    menu2 = 0
    reloj=pygame.time.Clock()
    fin_juego=False
    fin=False
    
    while menu == 0 and menu2 == 0:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                fin = True
            if event.type == pygame.MOUSEBUTTONDOWN:
                event.pos
                pantalla.blit(opciones, [0, 0])
                pygame.display.flip()
                if (event.pos[0] >= 305 and event.pos[0] <= 685) and (event.pos[1] >= 220 and event.pos[1] <= 270):
                    menu = 1
                elif (event.pos[0] >= 305 and event.pos[0] <= 685) and (event.pos[1] >= 305 and event.pos[1] <= 350):
                    pantalla.blit(instrucciones, [0, 0])
                    pygame.display.flip()
                    menu2 == 1
                elif (event.pos[0] >= 305 and event.pos[0] <= 685) and (event.pos[1] >= 395 and event.pos[1] <= 425):
                    menu = 1
                    fin = True
    
    pygame.display.flip()


    while (not fin) and (not fin_juego):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                fin = True
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_RIGHT:
                    j.velx=velocidad
                    j.vely=0
                    j.direccion=0
                    
                if event.key == pygame.K_LEFT:
                    j.velx=-velocidad
                    j.vely=0
                    j.direccion=1
                
                if event.key == pygame.K_UP:
                    j.velx=0
                    j.vely=-velocidad
                    j.direccion=2
                
                if event.key == pygame.K_DOWN:
                    j.velx=0
                    j.vely=velocidad
                    j.direccion=3
                    
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


        
        for b in bloques:
            b.velx=f_vx
            b.vely=f_vy
        
        for z in zanahorias:
            z.velx=f_vx
            z.vely=f_vy
        
        for t in trenes:
            t.velx=f_vx
            t.vely=f_vy
        
        
        
        for j in jugadores:
            colision_conejo_zanahoria=pygame.sprite.spritecollide(j, zanahorias, True)
            for z in colision_conejo_zanahoria:
                d.temp = 100
                n=random.randrange(100)
                if n < 60:
                    w=Zanahoria_win(zanahoria_win, [random.randrange(lim_izquierdo, f_ancho - 200), random.randrange(lim_superior, f_alto - 200)])
                    #w=Zanahoria_win(zanahoria_win, [random.randrange(lim_izquierdo, ANCHO), random.randrange(lim_superior, ALTO)])
                    zanahorias_win.add(w)
                if n < 20:
                    limite_lobos =  0
                    while limite_lobos <= 15:
                        l=Lobo(lobo, [random.randrange(-1000, -50), (random.randrange(lim_superior, f_alto - 100))])
                        lobos.add(l)
                        limite_lobos+=1
        
        
        
        
        for zw in zanahorias_win:
            if zw.aux == False:
                zw.velx=f_vx
                zw.vely=f_vy
            else:
                zw.velx=0
                zw.vely=0

        
        for w in zanahorias_win:    # Elimina las zanaorias en las vias del tren
            if w.rect.bottom >= 1160 and w.rect.top <= 1280:
                zanahorias_win.remove(w)
        
        colision_zanahoria_win_con_bloque=pygame.sprite.groupcollide(zanahorias, bloques, True, False, collided = None)


        
        for j in jugadores:
            colision_conejo_zanahoria_win=pygame.sprite.spritecollide(j, zanahorias_win, True)
            if colision_conejo_zanahoria_win:
                j.win+=1
                s=Zanahoria_win(zanahoria_win, [posicion_auxiliar, 30])
                zanahorias2_win.add(s)
                w.aux = True
                posicion_auxiliar+=30

        
        
        for h in lobos:
            colision_lobo = pygame.sprite.spritecollide(h, jugadores, False)
            for f in colision_lobo:
                h.velx = 0
                if h.direccion == 0:
                    h.direccion = 2
                else:
                    h.direccion = 3
                if j.direccion == 0 or j.direccion == 1:
                    j.direccion = 5
                elif j.direccion == 2 or j.direccion == 3 :
                    j.direccion = 4
                j.vidas -= 3
        
        
        


        # Deteccion del conejo por parte del perro
        for p in perros:
            deteccion = pygame.sprite.collide_circle(p, j)
            if deteccion:
                #p.Deteccion(j.rect)
                if p.direccion == 4:
                    p.direccion = 0
                    p.velx = -random.randrange(15, 30) 
                    p.vely = 0
                elif p.direccion == 5:
                    p.direccion = 1
                    p.velx = random.randrange(15, 30)
                    p.vely = 0
                elif p.direccion == 6:
                    p.direccion = 2
                    p.velx = 0
                    p.vely = random.randrange(15, 30)
                elif p.direccion == 7:
                    p.direccion = 3
                    p.velx = 0
                    p.vely = -(random.randrange(15, 30))
        

        for t in trenes:
            deteccion_trenes = pygame.sprite.collide_circle(t, j)
            if deteccion_trenes:
                t.velx = 30
    
        
        for p in perros:
            colision_conejo_perro = pygame.sprite.spritecollide(p, jugadores, False)
            if colision_conejo_perro:
                v.aux -=15
                
                
        for v in vidas:
            if v.rect.x > v.aux:
                vidas.remove(v)
                j.vidas-=1
                if j.direccion == 0 or j.direccion == 1:
                    j.direccion = 5
                elif j.direccion == 2 or j.direccion == 3 :
                    j.direccion = 4
                
        
        if j.vidas <= 0:
            fin_juego= True
        

        if j.win == 3:
            fin_juego= True
        

        if d.temp <= 0:
            fin_juego=True
        


        bloques.update()
        jugadores.update()
        zanahorias.update()
        digitos.update()
        lobos.update()
        perros.update()
        vidas.update()
        zanahorias_win.update()
        zanahorias2_win.update()
        piedras.update()
        trenes.update()
        

        # Refresco de pantalla
        
        #pantalla.fill(NEGRO)
        pantalla.blit(fondo, [f_x, f_y])
        

        #pantalla.blit(conejo[0][0], [100, 100])
        
        pygame.display.flip()
        

        # Dibujo de los elementos 
        zanahorias.draw(pantalla)
        
        jugadores.draw(pantalla)
        
        bloques.draw(pantalla)
        perros.draw(pantalla)
        lobos.draw(pantalla)
        zanahorias_win.draw(pantalla)
        pygame.draw.rect(pantalla, [87, 111, 86], [0, 0, ANCHO, 100], 0)
        pygame.draw.rect(pantalla, [43, 54, 42], [0, 0, ANCHO, 100], 7)
        digitos.draw(pantalla)
        trenes.draw(pantalla)
        pantalla.blit(tiempo, [660, 26])

        vidas.draw(pantalla)
        
        zanahorias2_win.draw(pantalla)
        
        
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

    
    if j.vidas <= 0 or d.temp <= 0:
        pantalla.blit(gameover, [0, 0])
        pygame.display.flip()
    elif j.win >= 3:
        pantalla.blit(ganar, [0, 0])
        pygame.display.flip()
    
    
    
    while not fin:      #Ciclo de finalizacion
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                fin = True