class LinearCon:
    def __init__(self, seed = 453):
        self.m = 14343
        self.a = 345
        self.c = 230
        self.x = seed
        
    def next(self):
        self.x = (self.a*self.x + self.c) % self.m
        return self.x/ self.m
    
gen = LinearCon(3490)
for i in range(11):
    print(gen.next())