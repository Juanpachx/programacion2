import random
class Juego:
    def __init__(self, numeroDeVidas):
        self.numeroDeVidas = numeroDeVidas
        self.vidasIniciales = numeroDeVidas
        self.record = 0

    def reiniciaPartida(self):
        self.numeroDeVidas = self.vidasIniciales

    def actualizaRecord(self, intentos):
        if intentos > self.record:
            self.record = intentos

    def quitaVida(self):
        self.numeroDeVidas -= 1
        return self.numeroDeVidas > 0

class JuegoAdivinaNumero(Juego):
    def __init__(self, numeroDeVidas):
        super().__init__(numeroDeVidas)
        self.numeroAAdivinar = 0

    def validaNumero(self, numero):
        return 0 <= numero <= 1
    
    def generarNumero(self):
        return random.randint(0, 10)

    def juega(self):
        self.reiniciaPartida()
        self.numeroAAdivinar = self.generarNumero()

        intentos = 0
        print("Adivina un número entre 0 y 10")

        while True:
            numero = int(input("Ingresa tu número: "))

            if not self.validaNumero(numero):
                print("Número inválido")
                continue

            intentos += 1

            if numero == self.numeroAAdivinar:
                print("¡Acertaste!")
                self.actualizaRecord(intentos)
                print("Record:", self.record)
                break
            else:
                if self.quitaVida():
                    print("Fallaste te quedan ",self.numeroDeVidas, "intentos")

                    if numero < self.numeroAAdivinar:
                        print("El número es mayor")
                    else:
                        print("El número es menor")
                else:
                    print("Te quedaste sin vidas")
                    print("El número era:", self.numeroAAdivinar)
                    break

class JuegoAdivinaPar(JuegoAdivinaNumero):
    def validaNumero(self, numero):
        if numero % 2 != 0:
            print("Error: debes ingresar un número PAR")
            return False
        return 0 <= numero <= 10

    def generarNumero(self):
        return random.choice([0, 2, 4, 6, 8, 10])

class JuegoAdivinaImpar(JuegoAdivinaNumero):
    def validaNumero(self, numero):
        if numero % 2 == 0:
            print("Error: debes ingresar un número IMPAR")
            return False
        return 0 <= numero <= 10

    def generarNumero(self):
        return random.choice([1, 3, 5, 7, 9])

juego1 = JuegoAdivinaNumero(3)
juego2 = JuegoAdivinaPar(3)
juego3 = JuegoAdivinaImpar(3)

print("JUEGO PAR")
juego2.juega()

print("JUEGO IMPAR")
juego3.juega()