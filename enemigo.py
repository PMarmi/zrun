import pygame

class Enemigo:
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.ancho = 65
        self.alto = 65
        self.velocidad = 5
        self.color = "purple"
        self.rect = pygame.Rect(self.x,self.y,self.ancho,self.alto)
        self.vida = 3
        self.imagen = pygame.image.load("1_game/img/enemigo.png")
        self.imagen = pygame.transform.scale(self.imagen, (65, 65))
    
    def dibujar(self, ventana):
        self.rect = pygame.Rect(self.x,self.y,self.ancho,self.alto)
        # pygame.draw.rect(ventana,self.color,self.rect)
        ventana.blit(self.imagen, (self.x, self.y))
    
    def movimiento(self):
        self.y += self.velocidad
    