from Ponto import Ponto
from random import randint

class labirinto:

    def __init__(self,largura,altura):
        self.largura = largura # X
        self.altura = altura # Y
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
    
    def retorna_Corredores(lista_proibida,x,y):
        lista = []
        if (x-1,y,x-2,y) not in lista_proibida:
            lista.append((x-1,y,x-2,y))#esq
            lista_proibida.add((x-1,y,x-2,y))
        if (x,y-1,x,y-2) not in lista_proibida:    
            lista.append((x,y-1,x,y-2))#cima
            lista_proibida.add((x,y-1,x,y-2))
        if (x+1,y,x+2,y) not in lista_proibida:
            lista.append((x+1,y,x+2,y))#dir
            lista_proibida.add((x+1,y,x+2,y))
        if (x,y+1,x,y+2) not in lista_proibida:
            lista.append((x,y+1,x,y+2))#baixo
            lista_proibida.add((x,y+1,x,y+2))


        return lista
        

    def Gera_Labirinto(self):
        lista_proibida = set()
        lista = []

        altura = self.altura
        largura = self.largura

        x=y=0

        while y%2==0 or x%2==0 and(y<altura-2 and x< largura-2):
            y = randint(3,(altura-3))
            x = randint(3,(largura-3))
        
            
        self.matriz[y][x]=1

        lista = labirinto.retorna_Corredores(lista_proibida,x,y)

        while len(lista)> 0 :
            escolha = randint(0,len(lista)-1)
            ponto = lista[escolha]
            lista.pop(escolha)

            if (ponto[2] >= 0) and (ponto[3] >= 0) and (ponto[2]< largura -1) and (ponto[3]<altura-1):
                if (self.matriz[ponto[3]][ponto[2]]==0):
                    self.matriz[ponto[1]][ponto[0]] = 1
                    self.matriz[ponto[3]][ponto[2]] = 1
                    labirinto.imprime_Matriz(self)
                    lista += labirinto.retorna_Corredores(lista_proibida,ponto[2],ponto[3])



mat = labirinto(11,9)
mat.Gera_Labirinto()
mat.imprime_Matriz()
 