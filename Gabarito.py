from Estado import Estado
from Heap import Heap
from Ponto import Ponto

class Gabarito:

    def busca_Informada(estado):
        fila_De_Prioridade = [] # heapMinima
        estados_Passados = set()
        estado_Atual = estado
        fila_De_Prioridade.append(estado_Atual)
        vetor = []
        while len(fila_De_Prioridade) > 0:
            if (estado_Atual.PontoAtual.x == estado_Atual.PontoFinal.x) and  (estado_Atual.PontoAtual.y == estado_Atual.PontoFinal.y):
                estados_Passados.add((estado_Atual.PontoAtual.x, estado_Atual.PontoAtual.y))
                return estados_Passados
            
            estados_Passados.add((estado_Atual.PontoAtual.x, estado_Atual.PontoAtual.y))

            vetor = Estado.transicoes(estado_Atual, estados_Passados)

            fila_De_Prioridade = Heap.atualizar_Heap(fila_De_Prioridade, vetor)
            
            fila_De_Prioridade = Heap.remover_Primeiro_Elemento(fila_De_Prioridade)

            if len(fila_De_Prioridade)!=0:# tratar o caso que nao tem solucao
                estado_Atual = fila_De_Prioridade[0]
        
        return 0
