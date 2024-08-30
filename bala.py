from entidad import Entidad
class Bala(Entidad):
    def __init__(self, x, y):
        super().__init__(x, y, 10, 20, 40, "img/bala.png")
    
    def movimiento(self):
        self.y -= self.velocidad
        self.rect.topleft = (self.x, self.y)