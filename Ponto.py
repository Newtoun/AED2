class Ponto:
    # É inserido o ponto x e y que representa o ponto
    def __init__(self,x,y):
        self.x = x
        self.y = y

    # Imprime o Ponto
    def __repr__(self):
        return "({},{})".format(self.x, self.y)
    
     # Modifica os valor de x
    def set_x(self,num):
        self.x+=num
        
    # Modifica o valor de y
    def set_y(self,num): 
        self.y+=num

    # Sobrecarrega a funcao que compara a igualdade
    def __eq__(self,other):
        return (self.x == other.x) and (self.y == other.y)
        
    # Retorna os pontos de possiveis movimentações a partir de um ponto
    def RetornaPonto(self, direcao):
        proxPonto = Ponto(self.x,self.y)
        if direcao == 1:
            proxPonto.set_y(-1) # Para cima
        elif direcao == 2:
            proxPonto.set_y(+1) # Para baixo
        elif direcao == 3:
            proxPonto.set_x(-1) # Para esquerda
        elif direcao == 4:
            proxPonto.set_x(+1) # para direita
        
        return proxPonto
    
    # Retorna a distancia entre dois pontos
    def DistanciaEntreDoisPonto(self, other): 
        return abs(self.x - other.x) + abs(self.y - other.y)
