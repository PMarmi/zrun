import pygame
class Enemigo:
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.ancho = 65
        self.alto = 65
        self.velocidad = 3
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
        
    def actualizar_velocidad(self, puntos, w_presionada):
        
        if puntos >= 300:
            self.velocidad = 32
        elif puntos >= 200:
            self.velocidad = 27
        elif puntos >= 130:
            self.velocidad = 22
        elif puntos >= 110:
            self.velocidad = 20
        elif puntos >= 100:
            self.velocidad = 17
        elif puntos >= 50:
            self.velocidad = 15
        elif puntos >= 30:
            self.velocidad = 10
        else:
            self.velocidad = 5  # Velocidad base o inicial
        if w_presionada:
            self.velocidad *= 2