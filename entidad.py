import pygame

class Entidad:
    def __init__(self, x, y, ancho, alto, velocidad, imagen_path):
        self.x = x
        self.y = y
        self.ancho = ancho
        self.alto = alto
        self.velocidad = velocidad
        self.rect = pygame.Rect(self.x, self.y, self.ancho, self.alto)
        self.imagen = pygame.image.load(imagen_path)
        self.imagen = pygame.transform.scale(self.imagen, (self.ancho, self.alto))

    def dibujar(self, ventana):
        self.rect.topleft = (self.x, self.y)
        ventana.blit(self.imagen, (self.x, self.y))

    def movimiento(self):
        pass  # Este método será implementado por las subclases