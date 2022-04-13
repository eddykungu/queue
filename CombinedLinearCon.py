from dataclasses import dataclass

@dataclass
class Generator:
    a: int
    x: int
    m: int
    
class CLCM:
    
    def __init__(self):
        self.g1 = Generator(a=40014, x=1355643, m=21474835634)
        self.g2 = Generator(a=40692,x=325254,m=2147493399)
            
    def next(self):
        self.g1.x = (self.g1.a*self.g1.x)%self.g1.m
        self.g2.x = (self.g2.a*self.g2.x)%self.g2.m
        
        xi = (self.g1.x - self.g2.x)%(self.g1.m-1)
        if xi == 0:
            xi = self.g1.m-1
        return xi/self.g1.m
    
gen = CLCM()
for i in range(0,10):
    print(gen.next())