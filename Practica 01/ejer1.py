import time

class Cronometro:
    def __init__(self):
        
        self.__inicia = time.time() * 1000
        self.__finaliza = self.__inicia

    def iniciar(self):
        return self.__inicia

    def finalizar(self):
        return self.__finaliza

    def inicia(self):
        self.__inicia = time.time() * 1000

    def detener(self):
        self.__finaliza = time.time() * 1000

    def lapsoDeTiempo(self):
        return self.__finaliza - self.__inicia
import random

def ordenacion_por_seleccion(lista):
    n = len(lista)
    for i in range(n):
        min = i
        for j in range(i + 1, n):
            if lista[j] < lista[min]:
                min = j
        
        lista[i], lista[min] = lista[min], lista[i]


if __name__ == "__main__":
   
    print("Generando 100,000 números...")
    numeros = [random.randint(1, 5000) for _ in range(5000)]
    
    reloj = Cronometro()
    
    print("Iniciando ordenación por selección (esto puede tardar)...")
    reloj.inicia() 
    
    ordenacion_por_seleccion(numeros)
  
    reloj.detener()
    
    tiempo_total = reloj.lapsoDeTiempo()
    print(f"¡Completado!")
    print(f"Tiempo total de ejecución: {tiempo_total:.2f} milisegundos")
    print(f"En segundos: {tiempo_total / 1000:.2f} s")