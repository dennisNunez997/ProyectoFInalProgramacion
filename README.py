# PygameProyectoJuego
# proyecto final de programacion

# importar librerias
import pygame, sys
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
# clase nave espacial



class NaveEspacial (pygame.sprite.Sprite):
    # funciones de la clase

    # *************funcion principal*******************
    def __init__(self):
        pygame.sprite.Sprite.__init__ (self)

        # implementacion de la imagen de la nave
        self.ImagenNave = pygame.image.load ('00001.png')
        self.rect = self.ImagenNave.get_rect ()

        # coordenadas de la nave
        self.rect.centerx = ancho - 800
        self.rect.centery = alto / 2
        # --------------------------

        # efecto de sonido de la nave
        self.sonidoDisparo = pygame.mixer.Sound ("disparo.ogg")

        # disparos de la nave almacenados en un arreglo
        self.listaDisparo = []

        # self.Vida = True

    # ********************disparar**********************

    def disparar(self, x, y):
        # variable para llamar a la funcion proyectil donde
        # x es la posicion en x de la posicion del enemigo, y es la posicion en y de la posicion del enemigo, "enemigo.png"
        # es la imagen a usar de la clase enemigo, True es la ruta para saber si el disparo es del enemigo o de la nave

        # nota: revisar en funcion proyectil
        miProyectil = Proyectil (x, y, "enemigo.png", True)

        # nueva variable para agregar la variable miProyectil
        self.listaDisparo.append (miProyectil)

        # sonido de disparo perteneciente a la clase nave
        self.sonidoDisparo.play ()  # pass

    # *******************dibujar nave espacial ****************
    def dibujar(self, superficie):
        # dibuja la imagen de nave
        superficie.blit (self.ImagenNave, self.rect)

    #------------Destruccion--------------


# -----------------------------Clase Proyectil-----------------------
class Proyectil (pygame.sprite.Sprite):
    # *********************creacion de funciones**********************

    # *******************funcion principal***************************

    def __init__(self, posx, posy, ruta, personaje):
        pygame.sprite.Sprite.__init__ (self)

        # crea imagen del disparo
        self.imageProyectil = pygame.image.load ('disparo.png')
        # obtiene la forma (rectangulo) de la variable proyectil
        self.rect = self.imageProyectil.get_rect ()
        # velocidad de disparo de la clase nave
        self.velocidadDisparo = 20
        # posicion del disparo en relacion a la nave
        self.rect.top = posy
        self.rect.left = posx
        # -----------------------------------------------------
        # se agrega la variable disparoPersonaje para identificar el disparo de la nave
        self.disparoPersonaje = personaje

    # *****************creacion de la funcion trayectoria********************

    def trayectoria(self):
        # identifica el disparo de la nave o del enemigo de acuerdo a la ruta usando TRUE
        # en este caso TRUE es para el disparo del personaje que ira hacia la derecha
        if self.disparoPersonaje == True:
            self.rect.left = self.rect.left + self.velocidadDisparo
        # ELSE indica que el disparo lo hizo la nave enemiga
        else:
            self.rect.left = self.rect.left - self.velocidadDisparo

    # ***********************funcion para dibujar el proyectil

    def dibujar(self, superficie):
        superficie.blit (self.imageProyectil, self.rect)


# creacion de la clase enemigo

class enemigo (pygame.sprite.Sprite):

    # *********************funcion principal de la clase*******************************+
    def __init__(self, posx, posy):

        pygame.sprite.Sprite.__init__ (self)
        # carga la imagen del enemigo
        self.imageProyectil = pygame.image.load ('enemigo.png')
        self.rect = self.imageProyectil.get_rect ()
        self.explotar = pygame.image.load ("fuego.png")
        self.conquista = False
        # almacena el disparo de la nave enemiga
        self.listaDisparo = []
        # variable para la velocidad del disparo
        self.velocidadDisparo = 15
        # obtiene la posicion de la nave enemiga
        self.rect.top = posy
        self.rect.left = posx
        # rango para visualizar el tiempo de disparo
        self.rangoDisparo = 5
        self.tiempoCambio =1

    # ******************************funcion para la trayectoria del disparo del enemigo***********
    def trayectoria(self):

        self.rect.left = self.rect.left + self.velocidadDisparo

    # ******************************funion para dibujar la nave**********************
    def dibujar(self, superficie):
        superficie.blit (self.imageProyectil, self.rect)
        self.derecha = True
        self.izq = False
        self.velocidad = 5
        if self.rect.left > -6000:
            self.rect.left -= self.velocidad
        else:
            self.derecha = True

    # *******************funcion de ataque de la nave enemiga**************
    def ataque(self):
        # dentro del rango o y 100 y dado que el rango sea mayor, la nave enemiga disparara
        if (randint (0, 400) < self.rangoDisparo):
            # llama a la funcion disparo
            self.__disparo ()

    # *******************funcion para disparar del enemigo**************
    def __disparo(self):
        # obtiene las coordenadas del enemigo para disparar los proyectiles de esa posicion
        x, y = self.rect.center
        # la funcion esta definida de la misma manera de la funcion disparo de la clase nave
        miProyectil = Proyectil (x, y, "ProyectilEnemigo.png", False)
        self.listaDisparo.append (miProyectil)




# creacion de la funcion principal

def cargarEnemigos():
    posX = 900
    enemy = enemigo (1000, 490)
    listaEnemigo.append (enemy)
    for x in range (1, 2):
        enemy = enemigo (posX, 300)
        listaEnemigo.append (enemy)
        posX = posX + 200
    enemy = enemigo (2000, 50)
    listaEnemigo.append (enemy)

    for x in range (1, 3):
        enemy = enemigo (posX, 200)
        listaEnemigo.append (enemy)
        posX = posX + 200

    enemy = enemigo (2000, 15000)
    listaEnemigo.append (enemy)
    for x in range (1, 4):
        enemy = enemigo (posX, 400)
        listaEnemigo.append (enemy)
        posX = posX + 500

    for x in range (1, 3):
        enemy = enemigo (posX, 150)
        listaEnemigo.append (enemy)
        posX = posX + 250

    for x in range (1, 4):
        enemy = enemigo (posX, 490)
        listaEnemigo.append (enemy)
        posX = posX + 300

    for x in range (1, 2):
        enemy = enemigo (posX, 300)
        listaEnemigo.append (enemy)
        posX = posX + 200

    enemy = enemigo (2000, 50)
    listaEnemigo.append (enemy)
    for x in range (1, 3):
        enemy = enemigo (posX, 200)
        listaEnemigo.append (enemy)
        posX = posX + 200

    for x in range (1, 2):
        enemy = enemigo (posX, 300)
        listaEnemigo.append (enemy)
        posX = posX + 200

    enemy = enemigo (1000, 490)
    listaEnemigo.append (enemy)
    for x in range (1, 2):
        enemy = enemigo (posX, 300)
        listaEnemigo.append (enemy)
        posX = posX + 200
    enemy = enemigo (2000, 50)
    listaEnemigo.append (enemy)

    for x in range (1, 3):
        enemy = enemigo (posX, 200)
        listaEnemigo.append (enemy)
        posX = posX + 200

    enemy = enemigo (2000, 15000)
    listaEnemigo.append (enemy)
    for x in range (1, 4):
        enemy = enemigo (posX, 400)
        listaEnemigo.append (enemy)
        posX = posX + 500

    for x in range (1, 3):
        enemy = enemigo (posX, 150)
        listaEnemigo.append (enemy)
        posX = posX + 250

    for x in range (1, 4):
        enemy = enemigo (posX, 490)
        listaEnemigo.append (enemy)
        posX = posX + 300

    for x in range (1, 2):
        enemy = enemigo (posX, 300)
        listaEnemigo.append (enemy)
        posX = posX + 200

    enemy = enemigo (2000, 50)
    listaEnemigo.append (enemy)
    for x in range (1, 3):
        enemy = enemigo (posX, 200)
        listaEnemigo.append (enemy)
        posX = posX + 200

    for x in range (1, 2):
        enemy = enemigo (posX, 300)
        listaEnemigo.append (enemy)
        posX = posX + 200

    enemy = enemigo (1000, 490)
    listaEnemigo.append (enemy)
    for x in range (1, 2):
        enemy = enemigo (posX, 300)
        listaEnemigo.append (enemy)
        posX = posX + 200
    enemy = enemigo (2000, 50)
    listaEnemigo.append (enemy)

    for x in range (1, 3):
        enemy = enemigo (posX, 200)
        listaEnemigo.append (enemy)
        posX = posX + 200

    enemy = enemigo (2000, 15000)
    listaEnemigo.append (enemy)
    for x in range (1, 4):
        enemy = enemigo (posX, 400)
        listaEnemigo.append (enemy)
        posX = posX + 500

    for x in range (1, 3):
        enemy = enemigo (posX, 150)
        listaEnemigo.append (enemy)
        posX = posX + 250

    for x in range (1, 4):
        enemy = enemigo (posX, 490)
        listaEnemigo.append (enemy)
        posX = posX + 300

    for x in range (1, 2):
        enemy = enemigo (posX, 300)
        listaEnemigo.append (enemy)
        posX = posX + 200

    enemy = enemigo (2000, 50)
    listaEnemigo.append (enemy)
    for x in range (1, 3):
        enemy = enemigo (posX, 200)
        listaEnemigo.append (enemy)
        posX = posX + 200

    for x in range (1, 2):
        enemy = enemigo (posX, 300)
        listaEnemigo.append (enemy)
        posX = posX + 200

    enemy = enemigo (1000, 490)
    listaEnemigo.append (enemy)
    for x in range (1, 2):
        enemy = enemigo (posX, 300)
        listaEnemigo.append (enemy)
        posX = posX + 200

    enemy = enemigo (2000, 50)
    listaEnemigo.append (enemy)
    for x in range (1, 3):
        enemy = enemigo (posX, 200)
        listaEnemigo.append (enemy)
        posX = posX + 200

    for x in range (1, 2):
        enemy = enemigo (posX, 300)
        listaEnemigo.append (enemy)
        posX = posX + 200




def SpaceAttack():
    # funcion cronometro
    aux = 1

    cargarEnemigos ()

    # inicializacion del juego
    pygame.init ()
    # creacion de la ventana del juego
    ventana = pygame.display.set_mode ((ancho, alto))
    # titulo del juego
    pygame.display.set_caption ("SpaceAttack")
    # musica de fondo del juego
    pygame.mixer.music.load ("TheFatRat mixing video game music with EDM.ogg")
    # numero de repeticiones de la musica
    pygame.mixer.music.play (2)

    # cronometro
    fuente1 = pygame.font.SysFont ("Arial", 34, True, False)

    # llamado de la clase nave espacial mediante la creacion de una variable
    jugador = NaveEspacial ()


    # creacion de una variable para llamar a la clase enemigo

    # imagen de fondo
    mi_imagen = pygame.image.load ("fondoPanoramica.png")
    explosion = pygame.image.load ("fuego.png")


    #Fuente de puntaje
    miFuente = pygame.font.SysFont ("Arial", 40)
    # coteo de puntaje
    cont = 0
    cont2 = 42

    #-----
    posX = 0
    posY = 0
    black = [0, 0, 0]
    velocidad = 1
    derecha = True
    izq = False
    # dibujado de la imagen de fondo
    ventana.blit (mi_imagen, (posX, posY))
    # actualizacion de la imagen de fondo para evitar que las imagenes de la nave se queden guardadeas en el fondo
    pygame.display.flip ()
    # DemoProyectil = Proyectil(ancho-800,alto/2)
    # condiciones para saber si el juego aun esta continuando
    enJuego = True
    handled = False

    # mientras la ventana este abierta
    while True:
        # cargar imagen de fondo
        ventana.fill (black)
        ventana.blit (mi_imagen, (posX, posY))
        Tiempo = pygame.time.get_ticks () / 1000
        if aux == Tiempo:
            aux += 1

        # condicion para cerrar el juego dependiendo del evento
        for event in pygame.event.get ():

            if event.type == QUIT:
                pygame.quit ()
                sys.exit ()
            # mientras el juego este en proceso
            if enJuego == True:
                # se asigna un evento de mouse para que el objeto(nave) acompane al mouse
                jugador.rect.centerx, jugador.rect.centery = pygame.mouse.get_pos ()
                # condicion de evento de teclado presionando la tecla S
                if event.type == pygame.KEYDOWN:
                    if event.key == K_s:
                        # EVENTOS DE LA FUNCION DISPARO DE LA NAVE
                        x, y = jugador.rect.center
                        jugador.disparar (x, y)
        if posX > -6000:
            posX -= velocidad
        else:
            derecha = True
        # dibujado de la nave enemiga

        contador = fuente1.render ("tiempo: " + str (Tiempo), 0, (255, 255, 255))
        ventana.blit (contador, (10, 10))

        # ----------no usar--------------------
        # posX,posY =pygame.mouse.get_pos()
        # DemoProyectil.dibujar(ventana)
        # ------------------------------------
        # en esta condicion se usara para que la nave dispare
        # se cololca a la nave dentro de la ventana
        jugador.dibujar (ventana)
        ##en esta condicion se dibuja los disparos de la nave
        if len (jugador.listaDisparo) > 0:
            for x in jugador.listaDisparo:
                x.dibujar (ventana)
                x.trayectoria ()
                if x.rect.left < 100:
                    jugador.listaDisparo.remove (x)
                else:
                    for enemy in listaEnemigo:
                        if x.rect.colliderect (enemy.rect):
                            listaEnemigo.remove (enemy)
                            ventana.blit (explosion, (enemy))
                            cont += 5

        if len (listaEnemigo)> 0:
            for enemy in listaEnemigo:
                enemy.ataque()
                enemy.dibujar(ventana)

                if len (enemy.listaDisparo) > 0:
                    for x in enemy.listaDisparo:
                        x.dibujar (ventana)
                        x.trayectoria ()
                        if x.rect.top > 900:
                            enemy.listaDisparo.remove (x)

                        else:
                            if x.rect.colliderect (jugador.rect):
                                enemy.listaDisparo.remove (x)
                                ventana.blit (explosion, (jugador))
                                cont2 -= 1




                            for disparo in jugador.listaDisparo:
                                if x.rect.colliderect (disparo.rect):
                                    jugador.listaDisparo.remove (disparo)
                                    enemy.listaDisparo.remove (x)


        mensaje = miFuente.render ("PUNTAJE: " + str (cont), 0, (0, 49, 83))
        ventana.blit (mensaje, (750, 30))

        mensaje1 = miFuente.render ("VIDA JUGADOR UNO: " + str (cont2), 0, (0, 0, 0))
        ventana.blit (mensaje1, (0, 80))


        if cont2 ==0:

            PERDIOJUGADOR = miFuente.render ("PERDIO JUGADOR UNO CON LA PUNTUACION DE:  "+ str(cont), 0, (0, 0, 0))
            ventana.blit (PERDIOJUGADOR, (250, 120))

            for disparo in enemy.listaDisparo:
                enemy.listaDisparo.remove(disparo)


            for disparo in jugador.listaDisparo:
                jugador.listaDisparo.remove (disparo)

            finjuego = miFuente.render ("FIN DE JUEGO:  ", 0, (0, 0, 0))
            pygame.mixer.music.fadeout (3000)
            ventana.blit (finjuego, (250, 130))


        pygame.display.update ()


#-----------------------
#--------------------------ñAVION EnemiMultijugador--------------------
class  NaveEspacialEnmi(pygame.sprite.Sprite):

    # funciones de la clase

    # *************funcion principal*******************
    def __init__(self):
        pygame.sprite.Sprite.__init__ (self)

        # implementacion de la imagen de la nave
        self.NaveEne = pygame.image.load('enemigo.png')
        self.rect = self.NaveEne.get_rect()
        self.explotar = pygame.image.load ("fuego.png")


        # coordenadas de la nave
        self.rect.centerx = ancho - 120
        self.rect.centery = alto / 2
        # --------------------------
        self.conquista = False
        # efecto de sonido de la nave
        self.sonidoDisparo = pygame.mixer.Sound ("disparo.ogg")

        # disparos de la nave almacenados en un arreglo
        self.listaDisparo2 = []

        self.velocidad2 =60

    def comportamiento(self):
        if self.conquista == False:
            self.movimiento()
            self.sonidoDisparo.stop()


    def movimiento(self):
        if self.rect.left <= -1000:
            self.rect.left = -880

        if self.rect.rigth> 1000:
           self.rect.rigth = 880

        if self.rect.top >= 600:
           self.rect.top = 480

        elif self.rect.bottom > -600:
             self.rect.bottom = -480

    def disparar2(self, x, y):
        # variable para llamar a la funcion proyectil donde
        # x es la posicion en x de la posicion del enemigo, y es la posicion en y de la posicion del enemigo, "enemigo.png"
        # es la imagen a usar de la clase enemigo, True es la ruta para saber si el disparo es del enemigo o de la nave

        # nota: revisar en funcion proyectil
        miProyectil2 = Proyectil(x, y, "00001.png", False)

        # nueva variable para agregar la variable miProyectil
        self.listaDisparo2.append(miProyectil2)

        # sonido de disparo perteneciente a la clase nave
        self.sonidoDisparo.play ()  # pass


        # ******************************funion para dibujar la nave**********************

    def destruccion(self):
        self.vida = False
        self.velocidad2=0
        self.imagenNave2 = self.ImagenExplo

    def dibujar(self, superficie2):
            # dibuja la imagen de nave
            superficie2.blit (self.NaveEne, self.rect)

    class Proyectil (pygame.sprite.Sprite):
        # *********************creacion de funciones**********************

        # *******************funcion principal***************************

        def __init__(self, posx, posy, ruta, personaje2):
            pygame.sprite.Sprite.__init__ (self)

            # crea imagen del disparo
            self.imageProyectil2 = pygame.image.load ('enemigoProyectil.png')
            # obtiene la forma (rectangulo) de la variable proyectil
            self.rect = self.imageProyectil2.get_rect ()
            # velocidad de disparo de la clase nave
            self.velocidadDisparo2 = 20
            # posicion del disparo en relacion a la nave
            self.rect.top = posy
            self.rect.left = posx
            # -----------------------------------------------------
            # se agrega la variable disparoPersonaje para identificar el disparo de la nave

# *****************creacion de la funcion trayectoria********************

        def trayectoria(self):
            self.rect.left = self.rect.left + self.velocidadDisparo2

            # ***********************funcion para dibujar el proyectil

        def dibujar(self, superficie2):
            superficie2.blit(self.imageProyectil2, self.rect)


#---------------------------Multijugador Zona Principal-----------------------

def Multijugador():
    # inicializacion del juego
    pygame.init()
    # creacion de la ventana del juego
    ventana = pygame.display.set_mode((ancho, alto))
    # titulo del juego
    pygame.display.set_caption("Multijugador")
    # musica de fondo del juego
    pygame.mixer.music.load("TheFatRat mixing video game music with EDM.ogg")
    # numero de repeticiones de la musica
    pygame.mixer.music.play(2)

    miFuente = pygame.font.SysFont("Arial",30)
    cont =0
    cont2 =10
    cont3 =0
    cont4 =10

    # llamado de la clase nave espacial mediante la creacion de una variable
    jugador = NaveEspacial()

    jugador2 = NaveEspacialEnmi()

    # imagen de fondo
    mi_imagen = pygame.image.load("fondoPanoramica.png")
    explosion = pygame.image.load ("fuego.png")
    posX = 0
    posY = 0
    black = [0, 0, 0]
    velocidad = 1
    derecha = True
    izq = False
    # dibujado de la imagen de fondo
    ventana.blit(mi_imagen, (posX, posY))
    # actualizacion de la imagen de fondo para evitar que las imagenes de la nave se queden guardadeas en el fondo
    pygame.display.flip()
    # DemoProyectil = Proyectil(ancho-800,alto/2)
    # condiciones para saber si el juego aun esta continuando
    enJuego = True
    handled = False
    # mientras la ventana este abierta
    while True:
        # cargar imagen de fondo
        ventana.fill (black)
        ventana.blit (mi_imagen, (posX, posY))

        pygame.display.flip()
        # ------no usar----------------
        # Mi_imagen = pygame.image.load("ciudad1.png")
        # ventana.blit(Mi_imagen,(ancho,alto))
        # DemoProyectil.trayectoria()
        # -----------------------------
        # condicion para cerrar el juego dependiendo del evento
        for event in pygame.event.get():

            if event.type == QUIT:
                pygame.quit()
                sys.exit()
            # mientras el juego este en proceso
            if enJuego == True:
                # se asigna un evento de mouse para que el objeto(nave) acompañe al mouse
                jugador.rect.centerx, jugador.rect.centery = pygame.mouse.get_pos()
                 #LLama constantemente  el evneto movimiento

                # condicion de evento de teclado presionando la tecla S
                if event.type == pygame.KEYDOWN:

                     if event.key == K_s:
                        # EVENTOS DE LA FUNCION DISPARO DE LA NAVE
                         x, y = jugador.rect.center
                         jugador.disparar(x, y)

                        # condicion de evento de teclado presionando la tecla S
            if enJuego == True:

                if event.type == pygame.KEYDOWN:

                         if event.key == K_LEFT:
                             jugador2.rect.left -= jugador2.velocidad2

                         if event.key == K_RIGHT:
                             jugador2.rect.right += jugador2.velocidad2

                         if event.key == K_UP:
                             jugador2.rect.top -= jugador2.velocidad2

                         if event.key == K_DOWN:
                             jugador2.rect.bottom += jugador2.velocidad2

                         elif event.key == K_i:
                            x, y = jugador2.rect.center
                            jugador2.disparar2(x,y)

        if posX > -6000:
            posX -= velocidad
        else:
            derecha = True

        # en esta condicion se usara para que la nave dispare
        # se cololca a la nave dentro de la ventana
        jugador.dibujar(ventana)
        ##en esta condicion se dibuja los disparos de la nave
        if len(jugador.listaDisparo) > 0:
            for x in jugador.listaDisparo:
                x.dibujar(ventana)
                x.trayectoria()
                if x.rect.left < 100:
                    jugador.listaDisparo.remove(x)
                else:
                    if x.rect.colliderect(jugador2.rect):
                        jugador.listaDisparo.remove(x)
                        ventana.blit (explosion, (jugador2))
                        cont += 5
                        cont2 -= 1




        # misma condicion para la clase enemiga
        jugador2.dibujar (ventana)
        ##en esta condicion se dibuja los disparos de la nave
        if len (jugador2.listaDisparo2)>0:
            for x in jugador2.listaDisparo2:
                x.dibujar(ventana)
                x.trayectoria()
                if x.rect.top > 800:
                    jugador2.listaDisparo2.remove(x)

                else:
                    if x.rect.colliderect (jugador.rect):
                        jugador2.listaDisparo2.remove (x)
                        ventana.blit (explosion, (jugador))
                        cont3 +=5
                        cont4 -=1

        mensaje = miFuente.render ("PUNTAJE JUGADOR UNO: "+str(cont),0, (176, 196, 222))
        ventana.blit (mensaje, (20, 15))

        mensaje1 = miFuente.render ("VIDA JUGADOR UNO: " + str (cont4), 0, (176, 196, 222))
        ventana.blit (mensaje1, (20, 50))



        #Puntaje y Vida Jugador2
        mensaje2 = miFuente.render ("PUNTAJE JUGADOR DOS: " + str (cont3), 0, (0, 49, 83))
        ventana.blit (mensaje2, (600, 15))
        mensaje3 = miFuente.render("VIDA JUGADOR DOS : "+str(cont2),0,(0,49,83))
        ventana.blit (mensaje3, (600,50))


        if cont2 ==0:
            PERDIOJUGADOR2 = miFuente.render ("PERDIO JUGADOR DOS CON LA PUNTUACION DE:  "+ str(cont3), 0, (0, 49, 83))
            ventana.blit (PERDIOJUGADOR2, (250, 140))

            GANOJUGADOR1 = miFuente.render ("GANO JUGADOR UNO CON LA PUNTUACION DE : "+str(cont), 0, (176, 196, 222))
            ventana.blit (GANOJUGADOR1, (250, 90))



            finjuego = miFuente.render ("!!....FIN DE JUEGO...!!  ", 0, (186, 196, 200))

            pygame.mixer.music.fadeout (3000)
            ventana.blit (finjuego, (425, 200))

            for disparo in jugador2.listaDisparo2:
                jugador2.listaDisparo2.remove(disparo)
                jugador2.conquista = True

            for disparo in jugador.listaDisparo:
                jugador.listaDisparo.remove (disparo)
                jugador.conquista = True









        if cont4 ==0:

            PERDIOJUGADOR1 = miFuente.render ("PERDIO JUGADOR UNO CON LA PUNTUACION DE:  " + str (cont), 0, (176, 196, 222))
            ventana.blit (PERDIOJUGADOR1, (250, 90))

            GANOJUGADOR2 = miFuente.render ("GANO JUGADOR DOS CON LA PUNTUACION DE : " + str (cont3), 0, (0, 49, 83))
            ventana.blit (GANOJUGADOR2, (250, 140))

            for disparo in jugador2.listaDisparo2:
                jugador2.listaDisparo2.remove (disparo)
                jugador2.conquista = True

            for disparo in jugador.listaDisparo:
                jugador.listaDisparo.remove (disparo)
                jugador.conquista = True


            finjuego = miFuente.render ("FIN DE JUEGO:  ", (186, 196, 200))
            pygame.mixer.music.fadeout (3000)
            ventana.blit (finjuego, (425, 200))





        pygame.display.update ()


#Menu Principal del juego

#Cursor
class Cursor(pygame.Rect):
    def __init__(self):
        pygame.Rect.__init__(self,0,0,1,1)
    def update(self):
        self.left,self.top=pygame.mouse.get_pos()

#Creacion de botones
class Boton(pygame.sprite.Sprite):
    def __init__(self,imagen1,imagen2,x=200,y=200):
        self.imagen_normal=imagen1
        self.imagen_seleccion=imagen2
        self.imagen_actual=self.imagen_normal
        self.rect=self.imagen_actual.get_rect()
        self.rect.left,self.rect.top=(x,y)

    def update(self,pantalla,cursor):
        if cursor.colliderect(self.rect):
            self.imagen_actual = self.imagen_seleccion
        else: self.imagen_actual = self.imagen_normal

        pantalla.blit(self.imagen_actual,self.rect)





#Menu del Juego
def main():
    pygame.init()  # inicializo el modulo

    # fijo las dimensiones de la pantalla a 300,300 y creo una superficie que va ser la principal
    pantalla = pygame.display.set_mode((700, 350))

    pygame.display.set_caption("Mi Ventana")  # Titulo de la Ventana
    # creo un reloj para controlar los fps
    reloj1 = pygame.time.Clock()

    inicio1=pygame.image.load("inicio1.png")
    inicio2 = pygame.image.load("inicio2.png")
    multijugador1 = pygame.image.load("multijugador1.png")
    multijugador2 = pygame.image.load("multijugador2.png")
    salir1 = pygame.image.load("salir1.png")
    salir2 = pygame.image.load("salir2.png")
    #DETENER SONIDO


    fondo = pygame.image.load("fondo1.png")
    #SONIDO

    pygame.mixer.music.load('fondoSonido.ogg')
    pygame.mixer.music.play(3)

    # Ubicacion del boton
    boton1 =  Boton(inicio1,inicio2,247,80)
    boton2 = Boton(multijugador1, multijugador2, 247, 150)
    boton3 = Boton(salir1,salir2,247, 220)


    cursor1=Cursor()



    salir = False
    # LOOP PRINCIPAL
    while salir != True:
        # recorro todos los eventos producidos
        # en realidad es una lista
        for event in pygame.event.get():
             if event.type==pygame.MOUSEBUTTONDOWN:

                if cursor1.colliderect(boton1.rect):

                    SpaceAttack()

                if cursor1.colliderect(boton2.rect):
                    Multijugador()

                if cursor1.colliderect(boton3.rect):
                    salir = True
            # pygame.QUIT( cruz de la ventana)
        if event.type == pygame.QUIT:
                salir = True

        reloj1.tick(20)  # operacion para que todo corra a 20fps
        pantalla.blit(fondo,(0,0))
        cursor1.update()
        boton1.update(pantalla,cursor1)
        boton2.update(pantalla, cursor1)
        boton3.update(pantalla, cursor1)


        pygame.display.update()  # actualizo el display

    pygame.quit()



main()
