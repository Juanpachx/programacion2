import random
class Juego:
    def __init__(self, numeroDeVidas, record):
        self.numeroDeVidas=numeroDeVidas
        self.record=0
        self.vidasIniciales=self.numeroDeVidas

    def reiniaPartida(self):
        self.numeroDeVidas=self.vidasIniciales
    
    def actualizarRecord(self):
        if self.intentos>self.record:
            self.record=self.intentos
    
    def quitaVida(self):
        if self.numeroDeVidas>0:
            self.numeroDeVidas-=1
    
class JuegoAdivinaNumero(Juego):
    def __init__(self, numeroAAdivinar):
        super().__init__(self.numeroDeVidas)
        self.numeroAAdivinar=0

    def juega(self):
        self.reiniaPartida()
        self.numeroAAdivinar=random.randint(0,10)
        intentos=0
        print("Adivina un numero entre 0 y 10: ")

        while True:
            numero=int(input("Ingrese tu numero: "))
            intentos+=1

            if numero==self.numeroAAdivinar:
                print("Acertaste!")
                self.actualizarRecord(intentos)
                print("Record actual: ",self.record)
                break
            else:
                quedan=self.quitaVida()
                if quedan:
                    if numero<self.numeroAAdivinar:
                        print("El numero es mayor")
                    else:
                        print("El numero es menor")
                    print("Te quedan ",self.numeroDeVidas," vidas")
                else:
                    print("Te quedaste sin vidas")
                    print("El numero era: ", self.numeroAAdivinar)
                    break

juego = JuegoAdivinaNumero(3)
juego.juega()