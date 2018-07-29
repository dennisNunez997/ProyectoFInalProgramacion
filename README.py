# PygameProyectoJuego
#proyecto final de programacion

#importar librerias
import pygame,sys
from pygame.locals import * 
from random import randint
import time
import threading

# variables globales
global segundos
segundos = 0
ancho = 1000
alto = 600

listaEnemigo = []

# creacion de clases
#clase nave espacial

class NaveEspacial(pygame.sprite.Sprite):
    #funciones de la clase

    #*************funcion principal*******************
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)

        #implementacion de la imagen de la nave
        self.ImagenNave = pygame.image.load('00001.jpg')
        self.rect = self.ImagenNave.get_rect()

        #coordenadas de la nave
        self.rect.centerx = ancho-800
        self.rect.centery = alto/2
        #--------------------------

        #efecto de sonido de la nave
        self.sonidoDisparo = pygame.mixer.Sound("disparo.ogg")

        #disparos de la nave almacenados en un arreglo
        self.listaDisparo=[]

        #self.Vida = True
        
    
    #********************disparar**********************

    def disparar(self,x,y):
        
        #variable para llamar a la funcion proyectil donde
        #x es la posicion en x de la posicion del enemigo, y es la posicion en y de la posicion del enemigo, "enemigo.png" 
        #es la imagen a usar de la clase enemigo, True es la ruta para saber si el disparo es del enemigo o de la nave

        #nota: revisar en funcion proyectil
        miProyectil = Proyectil(x,y,"enemigo.png",True)

        #nueva variable para agregar la variable miProyectil
        self.listaDisparo.append(miProyectil)

        #sonido de disparo perteneciente a la clase nave
        self.sonidoDisparo.play()
        #pass
    
    
    
    #*******************dibujar nave espacial ****************
    def dibujar(self,superficie):
        #dibuja la imagen de nave
        superficie.blit(self.ImagenNave,self.rect)

#-----------------------------Clase Proyectil-----------------------
class Proyectil(pygame.sprite.Sprite):
    #*********************creacion de funciones**********************

    #*******************funcion principal***************************

    def __init__(self, posx,posy, ruta, personaje):
        pygame.sprite.Sprite.__init__(self)

        #crea imagen del disparo
        self.imageProyectil = pygame.image.load('disparo.png')
        #obtiene la forma (rectangulo) de la variable proyectil
        self.rect = self.imageProyectil.get_rect()
        #velocidad de disparo de la clase nave
        self.velocidadDisparo = 20
        #posicion del disparo en relacion a la nave
        self.rect.top = posy
        self.rect.left = posx
        #-----------------------------------------------------
        #se agrega la variable disparoPersonaje para identificar el disparo de la nave
        self.disparoPersonaje = personaje

    #*****************creacion de la funcion trayectoria********************

    def trayectoria(self):
        #identifica el disparo de la nave o del enemigo de acuerdo a la ruta usando TRUE
        #en este caso TRUE es para el disparo del personaje que ira hacia la derecha
        if self.disparoPersonaje == True:
            self.rect.left = self.rect.left + self.velocidadDisparo
        #ELSE indica que el disparo lo hizo la nave enemiga
        else:
            self.rect.left = self.rect.left - self.velocidadDisparo
    
    #***********************funcion para dibujar el proyectil

    def dibujar(self,superficie):
        superficie.blit(self.imageProyectil,self.rect)


#creacion de la clase enemigo

class enemigo(pygame.sprite.Sprite):
    
    #*********************funcion principal de la clase*******************************+
    def __init__(self, posx,posy):
        
        pygame.sprite.Sprite.__init__(self)
        #carga la imagen del enemigo
        self.imageProyectil = pygame.image.load('enemigo.png')
        self.rect = self.imageProyectil.get_rect()
        self.explotar = pygame.image.load("fuego.png")
        #almacena el disparo de la nave enemiga
        self.listaDisparo = []
        #variable para la velocidad del disparo
        self.velocidadDisparo = 15
        #obtiene la posicion de la nave enemiga
        self.rect.top = posy
        self.rect.left = posx
        #rango para visualizar el tiempo de disparo 
        self.rangoDisparo = 5

       

    #******************************funcion para la trayectoria del disparo del enemigo***********  
    def trayectoria(self):

        self.rect.left = self.rect.left + self.velocidadDisparo
    #******************************funion para dibujar la nave**********************
    def dibujar(self,superficie):
        superficie.blit(self.imageProyectil,self.rect)
        self.derecha = True
        self.izq=False
        self.velocidad = 5
        if self.rect.left >-6000:
            self.rect.left -= self.velocidad
        else:
            self.derecha = True
        

 
    #*******************funcion de ataque de la nave enemiga**************
    def ataque(self):
        #dentro del rango o y 100 y dado que el rango sea mayor, la nave enemiga disparara
        if(randint(0,100)<self.rangoDisparo):
            #llama a la funcion disparo
            self.__disparo()
    #*******************funcion para disparar del enemigo**************
    def __disparo(self):
        #obtiene las coordenadas del enemigo para disparar los proyectiles de esa posicion
        x,y = self.rect.center
        #la funcion esta definida de la misma manera de la funcion disparo de la clase nave
        miProyectil = Proyectil(x,y, "ProyectilEnemigo.png",False)
        self.listaDisparo.append(miProyectil)
    

#creacion de la funcion principal

def cargarEnemigos():
    posX = 900
    enemy = enemigo(1000,490)
    listaEnemigo.append(enemy)
    for x in range(1,2): 
        enemy = enemigo(posX,300)
        listaEnemigo.append(enemy)
        posX = posX + 200
    enemy = enemigo(2000,50)
    listaEnemigo.append(enemy)
    for x in range(1,3):
        enemy = enemigo(posX,200)
        listaEnemigo.append(enemy)
        posX = posX + 200
    enemy = enemigo(2000,15000)
    listaEnemigo.append(enemy)
    for x in range(1,4):
        enemy = enemigo(posX,400)
        listaEnemigo.append(enemy)
        posX = posX + 500
    for x in range(1,3):
        enemy = enemigo(posX,150)
        listaEnemigo.append(enemy)
        posX = posX + 250
    for x in range (1,4):
        enemy = enemigo(posX,490)
        listaEnemigo.append(enemy)
        posX = posX + 300
        
    

def SpaceAttack():
    #funcion cronometro
    aux = 1
    
    cargarEnemigos()
    #inicializacion del juego
    pygame.init()
    #creacion de la ventana del juego
    ventana = pygame.display.set_mode((ancho,alto))
    #titulo del juego
    pygame.display.set_caption("SpaceAttack")
    #musica de fondo del juego
    pygame.mixer.music.load("TheFatRat mixing video game music with EDM.ogg")
    #numero de repeticiones de la musica
    pygame.mixer.music.play(2)
    
    #cronometro
    fuente1 = pygame.font.SysFont("Arial",34,True,False)
        
    #llamado de la clase nave espacial mediante la creacion de una variable
    jugador = NaveEspacial()
    #creacion de una variable para llamar a la clase enemigo
    
    #imagen de fondo
    mi_imagen = pygame.image.load("fondoPanoramica.png")
    explosion = pygame.image.load("fuego.png")
    posX = 0
    posY = 0
    black=[0,0,0]
    velocidad = 1
    derecha = True
    izq=False
    #dibujado de la imagen de fondo
    ventana.blit(mi_imagen,(posX,posY))
    #actualizacion de la imagen de fondo para evitar que las imagenes de la nave se queden guardadeas en el fondo
    pygame.display.flip()
    #DemoProyectil = Proyectil(ancho-800,alto/2)
    #condiciones para saber si el juego aun esta continuando
    enJuego = True
    handled = False
    
    #mientras la ventana este abierta
    while True:
        #cargar imagen de fondo
        ventana.fill(black)
        ventana.blit(mi_imagen,(posX,posY))
        Tiempo = pygame.time.get_ticks()/1000
        if aux == Tiempo:
            aux += 1
        
        #condicion para cerrar el juego dependiendo del evento
        for event in pygame.event.get():
            
            if event.type == QUIT:
                pygame.quit()
                sys.exit()
            #mientras el juego este en proceso
            if enJuego == True:
                #se asigna un evento de mouse para que el objeto(nave) acompane al mouse
                jugador.rect.centerx,jugador.rect.centery = pygame.mouse.get_pos()      
                #condicion de evento de teclado presionando la tecla S  
                if event.type == pygame.KEYDOWN:
                    if event.key == K_s:
                        #EVENTOS DE LA FUNCION DISPARO DE LA NAVE
                        x,y = jugador.rect.center
                        jugador.disparar(x,y)
        if posX>-6000:
            posX -= velocidad
        else:
            derecha = True
        #dibujado de la nave enemiga
        
        
        contador = fuente1.render("tiempo: "+str(Tiempo),0,(255,255,255))
        ventana.blit(contador,(10,10))
        

        #----------no usar--------------------
        #posX,posY =pygame.mouse.get_pos()
        #DemoProyectil.dibujar(ventana)
        #------------------------------------
        #en esta condicion se usara para que la nave dispare
        #se cololca a la nave dentro de la ventana
        jugador.dibujar(ventana)
        ##en esta condicion se dibuja los disparos de la nave
        if len(jugador.listaDisparo)>0:
            for x in jugador.listaDisparo:
                x.dibujar(ventana)
                x.trayectoria()
                if x.rect.left<100:
                    jugador.listaDisparo.remove(x)
                else: 
                    for enemy in listaEnemigo:
                        if x.rect.colliderect(enemy.rect):
                            listaEnemigo.remove(enemy)
                            jugador.listaDisparo.remove(x)
                            ventana.blit(explosion,(enemy))                    

             
        #misma condicion para la clase enemiga
        if len(listaEnemigo) > 0:
            for enemy in listaEnemigo:
                enemy.dibujar(ventana)
                

        if len(enemy.listaDisparo)>0:
            for x in enemy.listaDisparo:
                x.dibujar(ventana)
                x.trayectoria()
                if x.rect.colliderect(jugador):
                    jugador.destruccion()
                    enJuego = False
                if x.rect.top > 900:
                    enemy.listaDisparo.remove(x)
                else:
                    for disparo in jugador.listaDisparo:
                        if x.rect.colliderect(disparo.rect):
                            jugador.listaDisparo.remove(disparo)
                            enemy.listaDisparo.remove(x)
                            
                            
        pygame.display.update()


SpaceAttack()







