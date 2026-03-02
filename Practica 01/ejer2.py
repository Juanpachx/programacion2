class EcuacionLineal:
    def __init__(self,a,b,c,d,f):
        self.__a=a
        self.__b=b
        self.__c=c
        self.__d=d
        self.__f=f
        
    def tieneSolucion(self):
        if self.__a*self.__d-self.__b*self.__c !=0:
            return True
    def getX(self,e):
         return (e*self.__d-self.__b*self.__f)/(self.__a*self.__d-self.__b*self.__c)
    def getY(self,e):
         return (self.__a*self.__f-e*self.__c)/(self.__a*self.__d-self.__b*self.__c)
a=float(input("Ingrese a: "))
b=float(input("Ingrese b: "))
c=float(input("Ingrese c: "))
d=float(input("Ingrese d: "))
e=float(input("Ingrese e: "))
f=float(input("Ingrese f: "))

ec=EcuacionLineal(a,b,c,d,f)

if ec.tieneSolucion():
    print("La solucion de x es: ",ec.getX(e))
    print("La solucion de y es: ", ec.getY(e))
else:
    print("La ecuación no tiene solución")
                        