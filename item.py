from entidad import Entidad
import random

class Item(Entidad):
    def __init__(self, x, y):
        self.tipo = random.choice([1, 2, 3])
        if self.tipo == 1:
            imagen_path = "img/dmg.png"
        elif self.tipo == 2:
            imagen_path = "img/velo.png"
        else:
            imagen_path = "img/vida.png"
        super().__init__(x, y, 30, 30, 10, imagen_path)
    
    def movimiento(self):
        self.y += self.velocidad
        self.rect.topleft = (self.x, self.y)