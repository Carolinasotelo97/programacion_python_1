import pygame, sys
import random #para el posicionamiento aleatorio de algo
from pygame.locals import * 
from personaje import Personaje
from fondo import Fondo

#inicializo todos los modulos
pygame.init()

FPS = 80
RELOJ = pygame.time.Clock()
ANCHO = 1800
ALTO = 800
x = 0
y= 0

direccion = "derecha"

#creo la pantalla
pantalla = pygame.display.set_mode((ANCHO,ALTO)) #seteo el tamaño de la ventana
pygame.display.set_caption("Juego de Plataformas") #titulo del videojuego

#creo el fondo
ruta_imagen_fondo = 'Videojuego\\imagenes\\espacio4.jpg'
fondo = Fondo(pantalla, ANCHO, ALTO, ruta_imagen_fondo)


#fondo = pygame.transform.scale(fondo, (ANCHO,ALTO))

#creo el personaje
#personaje_der = pygame.image.load('Videojuego\\imagenes\\personaje-arma.png')
#personaje_izq = pygame.image.load('Videojuego\\imagenes\\personaje-arma_izq.png')
#alien = pygame.image.load('Videojuego\\imagenes\\alien.png')


# Crear un sprite para el personaje
jugador = Personaje(ALTO)

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    # Dibuja el fondo en su posición actual
    fondo.dibujar()
    
    # Calcula el desplazamiento relativo y ajusta si es necesario
    x_relativa = x % fondo.rect.width

    # Dibuja el fondo en su posición actual
    pantalla.blit(fondo.imagen, (x_relativa, 0))

    # Comprueba si se debe repetir el fondo
    if x_relativa < ANCHO:
        # Dibuja una segunda copia del fondo que se superpone al final
        pantalla.blit(fondo.imagen, (x_relativa - fondo.rect.width, 0))

    x -= 4  # Controla la velocidad del desplazamiento del fondo

    # Actualiza el sprite del personaje
    jugador.update(ALTO, ANCHO)

    # Dibuja el personaje
    pantalla.blit(jugador.image, jugador.rect)

    pygame.display.update()
    RELOJ.tick(FPS)

'''while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    #dibujo el fondo
    fondo.dibujar()

    x_relativa = x % fondo.rect.width
    pantalla.blit(fondo.imagen, (x_relativa, 0))


    if(x_relativa < ANCHO):
        pantalla.blit(fondo.imagen,(x_relativa,0))
    x -= 4
    # Actualizar el sprite del personaje
    jugador.update(ALTO)

    # Dibujar el personaje
    pantalla.blit(jugador.image, jugador.rect)

    pygame.display.update()
    RELOJ.tick(FPS)'''

'''
clock = pygame.time.Clock()
juego_terminado = False
while not juego_terminado:
    clock.tick(100)
    for evento in pygame.event.get():
       if evento.type == pygame.QUIT:
            juego_terminado = True
      
    pantalla.blit(fondo, (0,0)) #Le inidico 0,0 para que tome toda la pantalla de fondo
    #hago los movimientos
    #pressed = pygame.key.get_pressed()

    #if pressed[pygame.K_UP]:
     #   y -= 3
        
    #if pressed[pygame.K_DOWN]:
     #   y +=3
    pressed = pygame.key.get_pressed()
    if pressed[pygame.K_LEFT]:
        x -= 3
        direccion = "izquierda"
    if pressed[pygame.K_RIGHT]:
        x += 3
        direccion = "derecha"
       

    # Voltear la imagen según la dirección
    if direccion == "izquierda":
        personaje = pygame.transform.flip(personaje_izq, True, False)
    else:
        personaje = personaje_der

    #muevo al personaje +1
   
    pantalla.blit(personaje, (x,y))
    #pantalla.blit(alien,(x,y))
    pygame.display.update()
    clock.tick(60)

pygame.quit()'''