import pygame
import time
class Bala:
    def __init__(self, x, y, tiempo_vida=2):
        self.x = x
        self.y = y
        self.ancho = 10
        self.alto = 20
        self.velocidad = 10
        self.color = "white"
        self.rect = pygame.Rect(self.x,self.y,self.ancho,self.alto)
        self.imagen = pygame.image.load("1_game/img/bala.png")
        self.imagen = pygame.transform.scale(self.imagen, (10, 10))

    
    def dibujar(self, ventana):
        self.rect = pygame.Rect(self.x,self.y,self.ancho,self.alto)
        # pygame.draw.rect(ventana,self.color,self.rect)
        ventana.blit(self.imagen, (self.x, self.y))

    
    def movimiento(self):
        self.y -= self.velocidad