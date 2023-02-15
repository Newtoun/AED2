from Estado import Estado

from Heap import Heap
from Ponto import Ponto
from Matriz import Matriz

def busca_Informada(estado):
    filaDePrioridade = [] #heapMinima
    Estados_Passados = set()
    ProxEstado = estado
    filaDePrioridade.append(ProxEstado)
    vetor = []

    while len(filaDePrioridade) > 0 and (ProxEstado.PontoAtual.x != ProxEstado.PontoFinal.x) or  (ProxEstado.PontoAtual.y != ProxEstado.PontoFinal.y):
        print(ProxEstado.PontoAtual.x, ProxEstado.PontoAtual.y)
        Estados_Passados.add((ProxEstado.PontoAtual.x, ProxEstado.PontoAtual.y))
        #print(vetor)
        vetor = Estado.transicoes(ProxEstado, Estados_Passados)
        print(vetor)
        filaDePrioridade = Estado.montar_heap(vetor)
        print(filaDePrioridade)
        ProxEstado = filaDePrioridade[0]
    print(Estados_Passados)

def busca_Informada2(estado):
    if estado.PontoAtual == estado.PontoFinal:
        return estado.filaDePrioridade
    else:
        
        
    
inicio = Ponto(1, 1)
fim = Ponto(1, 9)
estadoInicial = Estado(inicio,fim,0)
busca_Informada(estadoInicial) 