import pygame

class Cubo:
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.ancho = 75
        self.alto = 75
        self.velocidad = 10
        self.color = "red"
        self.rect = pygame.Rect(self.x,self.y,self.ancho,self.alto)
        self.imagen = pygame.image.load("1_game/img/personaje.png")
        self.imagen = pygame.transform.scale(self.imagen, (75, 75))
    
    def dibujar(self, ventana):
        self.rect = pygame.Rect(self.x,self.y,self.ancho,self.alto)
        # pygame.draw.rect(ventana,self.color,self.rect)
        ventana.blit(self.imagen, (self.x, self.y))