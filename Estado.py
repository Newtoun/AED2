from Ponto import Ponto
from Heap import Heap
from labirinto import labirinto

class Estado:
    def __init__(self,matriz,PontoAtual,PontoFinal, passos):
        self.matriz = matriz
        self.PontoAtual = PontoAtual
        self.PontoFinal = PontoFinal

        #calcula f, g, h
        self.g = passos
        self.h = self.calcula_Heurística()
        self.f = self.g + self.h
    
    def __lt__(self, other):
        return self.f < other.f

    def calcula_Heurística(self):
        return int(Ponto.DistanciaEntreDoisPonto(self.PontoAtual, self.PontoFinal))
    
    def transicoes(self, estados_Passados):# 2, 2 
        saida = []
        #print("X={}  Y={}".format(self.PontoAtual.x, self.PontoAtual.y))
        print("elementos passados: {}".format(estados_Passados))
        for i in range(1,5):
            proxEstado = Ponto.RetornaPonto(self.PontoAtual, i)
            print(" x:{} - y:{}".format( proxEstado.x, proxEstado.y))
            if (self.matriz[proxEstado.y][proxEstado.x] != 0) and ((proxEstado.x, proxEstado.y) not in estados_Passados):
                saida.append(Estado(self.matriz,proxEstado, self.PontoFinal, self.g + 1))
        return saida
    
    
    def __repr__(self):
        return "({})".format(self.PontoAtual)



