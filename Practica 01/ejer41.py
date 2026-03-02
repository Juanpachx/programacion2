import math
class Estadistica:
    def __init__(self,x):
        self.x=x
        self.n=len(x)
    def promedio(self):
        return sum(self.x)/self.n
    def desviacion(self):
        media=self.promedio()
        cuadrado=sum((i-media)**2 for i in self.x)
        return math.sqrt(cuadrado/(self.n-1))
entrada=input("ingrese 10 numeros: ")
numeros=[float(i) for i in entrada.split()]
calc=Estadistica(numeros)
print("el promedio es: ",calc.promedio())
print("la desviacion estandar es: ",calc.desviacion())

#VENTAJAS DE UTILIZAR PROGRAMACION ORIENTADA A OBJETOS(P.O.O)

# Reutilización: Puedes usar el mismo código en diferentes partes sin copiar y pegar (usando la Herencia).

# Orden: El código se divide en "objetos" independientes, lo que hace que sea más fácil de leer y entender.

# Fácil mantenimiento: Si algo falla, solo arreglas el objeto dañado sin romper todo el programa.

# Seguridad: Proteges los datos importantes para que no cualquiera pueda modificarlos (usando el Encapsulamiento).

# Flexibilidad: Un mismo comando puede hacer cosas distintas según el objeto que lo reciba.