from Ponto import Ponto
from Heap import Heap
from Matriz import Matriz

class Estado:
    def __init__(self,PontoAtual,PontoFinal, passos):
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
            if (Matriz.acessaPonto(proxEstado.x, proxEstado.y) != 0) and ((proxEstado.x, proxEstado.y) not in estados_Passados):
                saida.append(Estado(proxEstado, self.PontoFinal, self.g + 1))
        return saida
    def montar_heap(vetor):
        heap = []
        for i in vetor:
            tam = len(heap)
            heap = Estado.aumentar_chave(heap, tam , i)
        return heap


    
    def aumentar_chave(heap, pos, novo):
        tam = len(heap)
        if pos == tam:
            heap.append(novo)
        else:
            heap[pos] = novo
        pai = (pos-1)//2
        while (pos > 0 ) and (heap[pos]<heap[pai]):
            heap[pai],heap[pos] = heap[pos],heap[pai]
            pos = pai
            pai = (pos-1)//2
        return heap
    
    def __repr__(self):
        return "({})".format(self.PontoAtual)



