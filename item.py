
import pygame
import random

class Item:
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.ancho = 30
        self.alto = 30
        self.velocidad = 10
        self.tipo = random.choice([1, 2, 3])
        if self.tipo == 1:
            self.imagen = pygame.image.load("1_game/img/dmg.png").convert_alpha()
        elif self.tipo == 2:
            self.imagen = pygame.image.load("1_game/img/velo.png").convert_alpha()
        else:
            self.imagen = pygame.image.load("1_game/img/vida.png").convert_alpha()
        
        self.imagen = pygame.transform.scale(self.imagen, (self.ancho, self.alto))
        self.rect = pygame.Rect(self.x,self.y,self.ancho,self.alto)

    def dibujar(self, ventana):
        # self.rect = pygame.Rect(self.x,self.y,self.ancho,self.alto)
        # pygame.draw.rect(ventana,self.color, self.rect)
        ventana.blit(self.imagen, (self.x, self.y))
    def movimiento(self):
        self.y += self.velocidad
        self.rect.topleft = (self.x, self.y)
