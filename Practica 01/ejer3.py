class EcuacionLineal:
    def __init__(self,a,b,c):
        self._a=a
        self._b=b
        self._c=c
    def getDiscriminante(self):
        return (self._b**2)-(4*self._a*self._c)
    def getRaiz1(self):
        dis=self.getDiscriminante()
        return (-self._b+(dis**0.5))/2*self._a
    def getRaiz2(self):
        dis=self.getDiscriminante()
        return (-self._b-(dis**0.5))/2*self._a
        
a=float(input("ingrese a: "))
b=float(input("ingrese b: "))
c=float(input("ingrese c: "))

sol=EcuacionLineal(a,b,c)
if sol.getDiscriminante() >0:
     print("La ecuacion tiene dos raices: ","r1",sol.getRaiz1(),"r2",sol.getRaiz2())
elif sol.getDiscriminante()==0:
        print("la ecuacion tiene una raiz: ",sol.getRaiz1())
else: print("la ecuacion no tiene raices reales")
        
    
        