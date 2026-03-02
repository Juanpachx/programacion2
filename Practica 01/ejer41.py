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
        