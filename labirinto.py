from Ponto import Ponto
from random import randint

class labirinto:

    def __init__(self,altura,largura):
        self.altura = altura
        self.largura = largura
        self.matriz = self.inicializa_Matriz_Zero()
        self.ponto_Inicial = None
        self.ponto_Final = None

    def inicializa_Matriz_Zero(self):
        mat = []     
        for i in range(self.altura):
            lista = [0]*self.largura
            mat.append(lista)
        return mat
    
    def imprime_Matriz(self):
        for i in range(self.altura):
            for j in range(self.largura):
                print(self.matriz[i][j],end=" ")
            print()
    
    def retorna_Corredores(x,y):
        lista = []
        lista.append((x-1,y,x-2,y))
        lista.append((x,y-1,x,y-2))
        lista.append((x+1,y,x+2,y))
        lista.append((x,y+1,x,y+2))

        return lista
        
    def Gera_Labirinto(self):
        lista = []

        y = randint(3,self.altura-2)
        x = randint(3,self.largura-2)
        print("Primeira escolha ({},{})".format(x, y))
        self.matriz[x][y] = 1

        lista = labirinto.retorna_Corredores(x,y)
        print("Lista: {}".format(lista))
        #while len(lista) > 0:
        cont = 1
        for i in range(5):
            print("##LOOP {} ##".format(cont))
            escolha = randint(0,len(lista)-1)
            print("Escolha: {}".format(escolha))
            Ponto = lista[escolha]
            print("Ponto: {}".format(Ponto))
            lista.pop(escolha)
            print("Lista Sem: {}".format(lista))
            
            if (Ponto[2] >= 0) and (Ponto[2] < self.largura-2) and (Ponto[3] >= 0) and (Ponto[3] < self.altura-2):
                print("passou no primeiro IF")
                if (self.matriz[Ponto[2]][Ponto[3]]!=1):
                    self.matriz[Ponto[0]][Ponto[1]] = 1
                    self.matriz[Ponto[2]][Ponto[3]] =  1
                    lista += labirinto.retorna_Corredores(Ponto[2],Ponto[3])
                    print("Lista ++: {}".format(lista))
            cont += 1

        

#matriz = labirinto.inicializa_Matriz_Zero(9,11)
#labirinto.imprime_Matriz(matriz,9,11)

mat = labirinto(9,11)
mat.Gera_Labirinto()
mat.imprime_Matriz()
 