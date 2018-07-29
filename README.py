# ProyectoFInalProgramacion
trabajo definitivo de programacion

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


def SpaceAttack():
    #funcion cronometro
    aux = 1
    rival1 = enemigo(1000,300)
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
    rival = enemigo(800,300)
    rival1 = enemigo(1000,400)
    rival2 = enemigo(1200,200)
    rival3 = enemigo(1300,500)
    rival4 = enemigo(1500,150)
    rival5 = enemigo(2000,350)
    rival6 = enemigo(2500,200)
    rival7 = enemigo(2300,460)
    rival8 = enemigo(2600,444)
    rival9 = enemigo(2900,222)
    rival10 = enemigo(3000,100)
    rival11 = enemigo(3500,290)
    rival12 = enemigo(3700,440)
    rival13 = enemigo(3800,330)
    rival14 = enemigo(4000,100)
    rival15 = enemigo(4500,220)
    rival16 = enemigo(4900,500)
    rival17 = enemigo(5500,243)
    rival18 = enemigo(5880, 431)
    rival19 = enemigo(6000,490)
    rival20 = enemigo(6300,142)

    
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
        rival.dibujar(ventana)
        rival1.dibujar(ventana)
        rival2.dibujar(ventana)
        rival3.dibujar(ventana)
        rival4.dibujar(ventana)
        rival5.dibujar(ventana)
        rival6.dibujar(ventana)
        rival7.dibujar(ventana)
        rival8.dibujar(ventana)
        rival9.dibujar(ventana)
        rival10.dibujar(ventana)
        rival11.dibujar(ventana)
        rival12.dibujar(ventana)
        rival13.dibujar(ventana)
        rival14.dibujar(ventana)
        rival15.dibujar(ventana)
        rival16.dibujar(ventana)
        rival17.dibujar(ventana)
        rival18.dibujar(ventana)
        rival19.dibujar(ventana)
        rival20.dibujar(ventana)
        
        
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
                    if x.rect.colliderect(rival):
                        ventana.blit(explosion,(rival))
                    if x.rect.colliderect(rival1):
                        ventana.blit(explosion,(rival1))
                    if x.rect.colliderect(rival2):
                        ventana.blit(explosion,(rival2))
                    if x.rect.colliderect(rival3):
                        ventana.blit(explosion,(rival3))
                    if x.rect.colliderect(rival4):
                        ventana.blit(explosion,(rival4))
                    if x.rect.colliderect(rival5):
                        ventana.blit(explosion,(rival5))
                    if x.rect.colliderect(rival6):
                        ventana.blit(explosion,(rival6))
                    if x.rect.colliderect(rival7):
                        ventana.blit(explosion,(rival7))
                    if x.rect.colliderect(rival8):
                        ventana.blit(explosion,(rival8))
                    if x.rect.colliderect(rival9):
                        ventana.blit(explosion,(rival9))
                    if x.rect.colliderect(rival10):
                        ventana.blit(explosion,(rival10))
                    if x.rect.colliderect(rival11):
                        ventana.blit(explosion,(rival11))
                    if x.rect.colliderect(rival12):
                        ventana.blit(explosion,(rival12))
                    if x.rect.colliderect(rival13):
                        ventana.blit(explosion,(rival13))
                    if x.rect.colliderect(rival14):
                        ventana.blit(explosion,(rival14))
                    if x.rect.colliderect(rival15):
                        ventana.blit(explosion,(rival15))
                    if x.rect.colliderect(rival16):
                        ventana.blit(explosion,(rival16))
                    if x.rect.colliderect(rival16):
                        ventana.blit(explosion,(rival17))
                    if x.rect.colliderect(rival7):
                        ventana.blit(explosion,(rival17))
                    if x.rect.colliderect(rival18):
                        ventana.blit(explosion,(rival18))
                    if x.rect.colliderect(rival19):
                        ventana.blit(explosion,(rival19))
                    if x.rect.colliderect(rival20):
                        ventana.blit(explosion,(rival20))
                    
        
        #misma condicion para la clase enemiga
        if len(rival.listaDisparo)>0:
            for x in rival.listaDisparo:
                x.dibujar(ventana)
                x.trayectoria()
                if x.rect.colliderect(jugador):
                    jugador.destruccion()
                    enJuego = False
                if x.rect.top > 900:
                    rival.listaDisparo.remove(x)
                else:
                    for disparo in jugador.listaDisparo:
                        if x.rect.colliderect(disparo.rect):
                            jugador.listaDisparo.remove(disparo)
                            rival.listaDisparo.remove(x)
                            rival.explotar
        pygame.display.update()


SpaceAttack()
