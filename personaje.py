from entidad import Entidad
class Cubo(Entidad):
    def __init__(self, x, y):
        super().__init__(x, y, 60, 60, 10, "img/personaje.png")