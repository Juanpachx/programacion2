from multimethod import multimethod
import math

class AlgebraVectorial:

    def __init__(self, x=0, y=0):
        self.x = x
        self.y = y

    def producto_punto(self, otro):
        return self.x * otro.x + self.y * otro.y

    def modulo(self):
        return math.sqrt(self.x**2 + self.y**2)

    def producto_cruz(self, otro):
        return self.x * otro.y - self.y * otro.x

    @multimethod
    def perpendicular(self, otro: "AlgebraVectorial"):
        return self.producto_punto(otro) == 0

    @multimethod
    def perpendicular(self, otro: "AlgebraVectorial", metodo: int):
        if metodo == 1:
    
            suma = AlgebraVectorial(self.x + otro.x, self.y + otro.y)
            resta = AlgebraVectorial(self.x - otro.x, self.y - otro.y)
            return suma.modulo() == resta.modulo()

        elif metodo == 2:
    
            suma = AlgebraVectorial(self.x + otro.x, self.y + otro.y)
            return suma.modulo()**2 == self.modulo()**2 + otro.modulo()**2
        return False

    @multimethod
    def paralelo(self, otro: "AlgebraVectorial"):
        
        return self.producto_cruz(otro) == 0

    @multimethod
    def paralelo(self, otro: "AlgebraVectorial", metodo: int):
        
        if otro.x != 0:
            r = self.x / otro.x
            return self.y == r * otro.y
        elif otro.y != 0:
            r = self.y / otro.y
            return self.x == r * otro.x
        return False

    def proyeccion(self, otro):
        escalar = self.producto_punto(otro) / (otro.modulo()**2)
        return AlgebraVectorial(escalar * otro.x, escalar * otro.y)

    def componente(self, otro):
        return self.producto_punto(otro) / otro.modulo()

    def __str__(self):
        return f"({self.x}, {self.y})"

a = AlgebraVectorial(3, 4)
b = AlgebraVectorial(1, 2)


print("Perpendicular (producto punto):", a.perpendicular(b))
print("Perpendicular (metodo 1):", a.perpendicular(b, 1))
print("Perpendicular (metodo 2):", a.perpendicular(b, 2))
print("Paralelo (cruz):", a.paralelo(b))
print("Paralelo (proporcional):", a.paralelo(b, 1))
print("Proyección:", a.proyeccion(b))
print("Componente:", a.componente(b))