from typing import Any
import sys
import time
import pygame

#esquina superior derecha
ancho= 640
alto=480
#la esquina superior izquierda es (0,0)
color_azul = (0,0,64) #color azul para el fondo
color_blanco = (255,255,255)

pygame.init() #para inicializar el uso de fuentes

class Escena:
    def __init__(self):
        "inicializacion"
        self.proximaEscena = False
        self.jugando = True

    def leer_eventos(self, eventos):
        "lee la lista de todos los eventos"
        pass

    def actualizar(self):
        "calculos y logica"
        pass

    def dibujar(self, pantalla):
        "Dibujar los objetos en pantalla"
        pass

    def cambiar_escena(self, escena):
        "selecciona la nueva escena a ser desplegada"
        self.proximaEscena = escena
    
class Director:
    def __init__(self, titulo ="", res = (ancho, alto)):
        pygame.init()
        self.pantalla = pygame.display.set_mode(res) #inicializo la pantalla
        pygame.display.set_caption(titulo) #configuro el titulo de la pantalla
        self.reloj = pygame.time.Clock() #creo que el reloj
        self.escena= None
        self.escenas = {}

    def ejecutar(self, escena_inicial, fps=60):
        self.escena = self.escenas[escena_inicial]
        jugando = True
        while jugando:
            self.reloj.tick(fps)
            eventos = pygame.event.get()
                #revisamos los eventos
            for evento in eventos:
                if evento.type == pygame.QUIT:
                    jugando= False

            self.escena.leer_eventos(eventos)
            self.escena.actualizar()
            self.escena.dibujar(self.pantalla)

            self.elegirEscena(self.escena.proximaEscena)

            if jugando:
                jugando = self.escena.jugando

            pygame.display.flip()

        time.sleep(3)

    def elegirEscena(self, proximaEscena):
        if proximaEscena:
            if proximaEscena not in self.escenas:
                self.agregarEscena(proximaEscena)
            self.escena = self.escenas[proximaEscena]

    def agregarEscena(self, escena):
        escenaClase = 'Escena'+escena
        escenaObj = globals()[escenaClase]
        self.escenas[escena] = escenaObj()

class EscenaNivel1(Escena):
    def __init__(self):
        Escena.__init__(self)
        
        self.bolita = Bolita()
        self.jugador = Barra()
        self.muro = Muro(50)

        self.puntuacion = 0
        self.vidas = 3
        self.esperando_saque = True

        pygame.key.set_repeat(30)#ajustar repeticion de evento de tecla presionada


    def leer_eventos(self, eventos):
        for evento in eventos:
            if evento.type == pygame.KEYDOWN:
                self.jugador.update(evento)
                if self.esperando_saque ==  True and evento.key == pygame.K_SPACE:
                    self.esperando_saque = False
                    if self.bolita.rect.centerx < ancho //2:
                        self.bolita.speed = [3, -3]
                    else:
                        self.bolita.speed = [-3,-3]
    
    def actualizar(self):
        #actualizar posicion de la bolita
        if self.esperando_saque == False:
            self.bolita.update() #actualizo la posicion de la bolita
        else: 
            self.bolita.rect.midbottom = self.jugador.rect.midtop

        if pygame.sprite.collide_rect(self.bolita, self.jugador): #esto hace que la bolta pueda tocar la barra sin pasarse
            self.bolita.speed[1] = -self.bolita.speed[1]

        #colision de la self.bolita con el muro
        lista = pygame.sprite.spritecollide(self.bolita, self.muro, False)

        if lista:
            ladrillo = lista[0]
            cx = self.bolita.rect.centerx
            if cx < ladrillo.rect.left or cx > ladrillo.rect.right:
                self.bolita.speed[0] = -self.bolita.speed[0]
            else:
                self.bolita.speed[1] = -self.bolita.speed[1]
            self.muro.remove(ladrillo)
            self.puntuacion += 10

        #revisar si la self.bolita sale de la pantalla
        if self.bolita.rect.top > alto:
            self.vidas -= 1
            self.esperando_saque = True

        if self.vidas <= 0:
            self.cambiar_escena('JuegoTerminado')

    def dibujar(self, pantalla):
        pantalla.fill(color_azul) #relleno la pantalla
        self.mostrar_puntuacion(pantalla) #muestro la puntuacion
        self.mostrar_vidas(pantalla) #muestro las vidas
        pantalla.blit(self.bolita.image, self.bolita.rect) #dibujo la bolita en pantalla blit es para dibujar en una superficie sobre otra
        pantalla.blit(self.jugador.image, self.jugador.rect) #dibujo la barra en pantalla blit es para dibujar en una superficie sobre otra
        self.muro.draw(pantalla)

    def mostrar_puntuacion(self, pantalla):
        fuente = pygame.font.SysFont('Consolas', 20)
        texto = fuente.render(str(self.puntuacion).zfill(5), True, (color_blanco))
        texto_rect = texto.get_rect()
        texto_rect.topleft = [0,0]
        pantalla.blit(texto, texto_rect)

    def mostrar_vidas(self, pantalla):
        fuente = pygame.font.SysFont('Consolas', 20)
        cadena = "Vidas: "+ str(self.vidas).zfill(2)
        texto = fuente.render(cadena, True, (color_blanco))
        texto_rect = texto.get_rect()
        texto_rect.topright = [ancho,0]
        pantalla.blit(texto, texto_rect)

class EscenaJuegoTerminado(Escena):
    def actualizar(self):
        self.jugando = False

    def dibujar(self, pantalla):
        fuente = pygame.font.SysFont('Arial', 72)
        texto = fuente.render('Juego terminado :( ', True, (color_blanco))
        texto_rect = texto.get_rect()
        texto_rect.center = [ancho // 2, alto // 2]
        pantalla.blit(texto, texto_rect)

            
class Bolita(pygame.sprite.Sprite): #sprite es un objeto visible en pantalla
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load("C:\\Users\\caroo\\OneDrive\\Escritorio\\Proyectos\\videojuegos\\ladrillos\\imagenes\\bolita.png")
        self.rect = self.image.get_rect()
        #posicion inicial centrada
        self.rect.centerx = ancho /2
        self.rect.centery = alto / 2 
        #establezco velocidad inicial de la bolita
        self.speed = [3,3]

    def update(self):
        
        if self.rect.top <= 0:#evito que se salga del cuadro hacia abajo o arriba
            self.speed[1] = -self.speed[1]
        elif self.rect.right >= ancho or self.rect.left <= 0: #evita que salga por la derecha
            self.speed[0] = -self.speed[0] 

        self.rect.move_ip(self.speed) #mover en base a posicion actual y velocidad 

class Barra(pygame.sprite.Sprite): #sprite es un objeto visible en pantalla
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load("C:\\Users\\caroo\\OneDrive\\Escritorio\\Proyectos\\videojuegos\\ladrillos\\imagenes\\paleta.png")
        self.rect = self.image.get_rect()
        #posicion inicial centrada
        self.rect.midbottom=(ancho//2, alto - 20)
        #establezco velocidad inicial de la barra
        self.speed = [0,0]
    
    def update(self, evento) :
        if evento.key == pygame.K_LEFT and self.rect.left > 0:  #buscar si se presiono flecha izquierda
            self.speed = [-5,0]
        elif evento.key == pygame.K_RIGHT and self.rect.right < ancho:
            self.speed = [5,0]
        else:
            self.speed = [0,0]
        self.rect.move_ip(self.speed) #mover en base a posicion actual y velocidad
         
class Ladrillo(pygame.sprite.Sprite): #sprite es un objeto visible en pantalla
    def __init__(self, posicion):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load("C:\\Users\\caroo\\OneDrive\\Escritorio\\Proyectos\\videojuegos\\ladrillos\\imagenes\\ladrillo.png")
        self.rect = self.image.get_rect()
        self.rect.topleft = posicion #posicion inicial, provista externamente

class Muro(pygame.sprite.Group):
    def __init__(self, cantidadLadrillos):
        pygame.sprite.Group.__init__(self)

        pos_x =0 
        pos_y= 20
        for i in range(cantidadLadrillos):
            ladrillo = Ladrillo((pos_x,pos_y))
            self.add(ladrillo)

            pos_x += ladrillo.rect.width
            if pos_x >= ancho:
                pos_x = 0
                pos_y += ladrillo.rect.height

        '''
        hago la prueba con dos ladrillos random
        ladrillo1 = Ladrillo((0,0))
        ladrillo2 = Ladrillo((100,100))

        self.add(ladrillo1)
        self.add(ladrillo2)'''

director = Director('Juego de Ladrillos', (ancho, alto))
director.agregarEscena('Nivel1')
director.ejecutar('Nivel1')