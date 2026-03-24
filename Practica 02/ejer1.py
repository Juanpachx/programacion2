from multimethod import multimethod
import math
class MiPunto:
    def __init__(self,x=0,y=0):
        self.x=x
        self.y=y

    def getX(self):
        return self.x
    def getY(self):
        return self.y
    
    @multimethod
    def distancia(self,otro:MiPunto):
        return math.sqrt((otro.getX()-self.x)**2+(otro.getY()-self.y)**2)
    
    @multimethod
    def distancia(self,x:float,y:float):
        return math.sqrt((x-self.x)**2+(y-self.y)**2)
    
p1=MiPunto()
p2=MiPunto(10,30.5)
print(p1.distancia(p2))

