from entidad import Entidad
class Enemigo(Entidad):
    def __init__(self, x, y):
        super().__init__(x, y, 65, 65, 3, "img/enemigo.png")
        self.vida = 3
    
    def movimiento(self):
        self.y += self.velocidad
        self.rect.topleft = (self.x, self.y)
        
    def actualizar_velocidad(self, puntos, w_presionada):
        if puntos >= 700:
            self.velocidad = 43
        elif puntos >= 600:
            self.velocidad = 37
        elif puntos >= 400:
            self.velocidad = 35
        elif puntos >= 300:
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
            self.velocidad = 12
        else:
            self.velocidad = 9
        if w_presionada:
            self.velocidad *= 2