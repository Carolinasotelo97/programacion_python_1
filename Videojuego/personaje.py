import re
import pygame


# En el archivo "personaje.py"


class Personaje(pygame.sprite.Sprite):
    def __init__(self, base_y):
        super().__init__()
        self.image_derecha = pygame.image.load('Videojuego\\imagenes\\personaje-arma.png')
        self.image_izquierda = pygame.image.load('Videojuego\\imagenes\\personaje-arma_izq.png')
        self.image_derecha = pygame.transform.scale(self.image_derecha, (self.image_derecha.get_width() // 2, self.image_derecha.get_height() // 2))
        self.image_izquierda = pygame.transform.scale(self.image_izquierda, (self.image_izquierda.get_width() // 2, self.image_izquierda.get_height() // 2))
        self.image = self.image_derecha
        self.rect = self.image.get_rect()
        self.rect.center = (100, base_y)


    def update(self, ancho_ventana, alto_ventana):
        pressed = pygame.key.get_pressed()
        
        if pressed[pygame.K_UP] and self.rect.top > 0:
            self.rect.y -= 3
        if pressed[pygame.K_DOWN] and self.rect.bottom < alto_ventana:
            self.rect.y += 3

        if pressed[pygame.K_LEFT] and self.rect.left > 0:
            self.image = self.image_izquierda
            self.rect.x -= 3
        if pressed[pygame.K_RIGHT] and self.rect.right < ancho_ventana:
            self.image = self.image_derecha
            self.rect.x += 3

    '''def update(self, base_y):
        pressed = pygame.key.get_pressed()
        if pressed[pygame.K_UP] and self.rect.top > 0:
            self.rect.y -= 3
        if pressed[pygame.K_DOWN] and self.rect.bottom < base_y:
            self.rect.y += 3

        if pressed[pygame.K_LEFT]:
            self.image = self.image_izquierda
            self.rect.x -= 3
        if pressed[pygame.K_RIGHT]:
            self.image = self.image_derecha
            self.rect.x += 3'''

    ''' if pressed[pygame.K_UP]:
            self.rect.y -= 3    
        if pressed[pygame.K_DOWN]:
           self.rect.y +=3
        if pressed[pygame.K_LEFT]:
            self.image = self.image_izquierda
            self.rect.x -= 3
        if pressed[pygame.K_RIGHT]:
            self.image = self.image_derecha
            self.rect.x += 3'''
