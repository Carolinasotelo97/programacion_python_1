# En el archivo "fondo.py"
import pygame

class Fondo:
    def __init__(self, pantalla, ancho, alto, ruta_imagen):
        self.imagen = pygame.image.load(ruta_imagen)
        self.imagen = pygame.transform.scale(self.imagen, (ancho, alto))
        self.rect = self.imagen.get_rect()
        self.pantalla = pantalla

    def dibujar(self):
        self.pantalla.blit(self.imagen, self.rect)
