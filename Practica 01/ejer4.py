import math
def promedio(datos):
    return sum(datos)/len(datos)
def desviacion(datos):
    n=len(datos)
    if n<=1:
        return 0
    media=promedio(datos)
    cuadrado=sum((i-media)**2 for i in datos) 
    return math.sqrt(cuadrado/(n-1))

entrada = input("ingrese 10 numeros: ")
numeros=[float(i) for i in entrada.split()]
print("el promedio es: ",promedio(numeros))
print("la desviacion estandar es: ",desviacion(numeros))
