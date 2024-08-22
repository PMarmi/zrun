import pygame
import time
class Bala:
    def __init__(self, x, y, tiempo_vida=2):
        self.x = x
        self.y = y
        self.ancho = 20
        self.alto = 20
        self.velocidad = 10
        self.color = "white"
        self.rect = pygame.Rect(self.x,self.y,self.ancho,self.alto)
        self.tiempo_vida = tiempo_vida * 1000
        self.creacion = pygame.time.get_ticks()

    def actualizar(self):
        if pygame.time.get_ticks() - self.creacion >= self.tiempo_vida:
            return True
        return False
    
    def dibujar(self, ventana):
        self.rect = pygame.Rect(self.x,self.y,self.ancho,self.alto)
        pygame.draw.rect(ventana,self.color,self.rect)
    
    def movimiento(self):
        self.y -= self.velocidad