class Ponto:
    def __init__(self,x,y):
        self.x = x
        self.y = y

    def __repr__(self):
        return "({},{})".format(self.x, self.y)
    
    def set_x(self,num):
        self.x+=num
    def set_y(self,num):
        self.y+=num

    def __eq__(self,other):
        return (self.x == other.x) and (self.y == other.y)
    
    def RetornaPonto(self, direcao):
        proxPonto = self
        #proxPonto = Ponto(self.x,self.y)
        if direcao == 1:
            #proxPonto.y -= 1
            proxPonto = Ponto(self.x,self.y)
            proxPonto.set_y(-1)
        if direcao == 2:
            #proxPonto.y += 1
            proxPonto = Ponto(self.x,self.y)
            proxPonto.set_y(+1)
        if direcao == 3:
            #proxPonto.x -= 1
            proxPonto = Ponto(self.x,self.y)
            proxPonto.set_x(-1)
        if direcao == 4:
            #proxPonto.x += 1
            proxPonto = Ponto(self.x,self.y)
            proxPonto.set_x(+1)
        return proxPonto
    
    def DistanciaEntreDoisPonto(self, other):
        return abs(self.x - other.x) + abs(self.y - other.y)

#for i in range(1,5):
#    print(i)
#    a = Ponto(1,1)
#    print(a.RetornaPonto(i))