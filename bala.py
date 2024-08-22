import pygame

class Bala:
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.ancho = 20
        self.alto = 20
        self.velocidad = 10
        self.color = "white"
        self.rect = pygame.Rect(self.x,self.y,self.ancho,self.alto)
    
    def dibujar(self, ventana):
        self.rect = pygame.Rect(self.x,self.y,self.ancho,self.alto)
        pygame.draw.rect(ventana,self.color,self.rect)
    
    def movimiento(self):
        self.y -= self.velocidad