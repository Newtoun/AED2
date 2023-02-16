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
        if ((x-1,y,x-2,y)) not in lista_proibida:
            lista.append((x-1,y,x-2,y))#esq
            lista_proibida.add((x-1,y,x-2,y))
        if ((x,y-1,x,y-2)) not in lista_proibida:    
            lista.append((x,y-1,x,y-2))#cima
            lista_proibida.add((x,y-1,x,y-2))
        if ((x,y-1,x,y-2)) not in lista_proibida:
            lista.append((x+1,y,x+2,y))#dir
            lista_proibida.add((x+1,y,x+2,y))
        if ((x,y+1,x,y+2)) not in lista_proibida:
            lista.append((x,y+1,x,y+2))#baixo
            lista_proibida.add((x,y+1,x,y+2))


        return lista
        

    def Gera_Labirinto(self):
        matriz = labirinto.inicializa_Matriz_Zero(self)
        lista_proibida = set()
        lista = []
        altura = self.altura-2
        largura = self.largura-2
        x=0
        y=0

        print("largura {} altura {}".format(largura,altura))
        while y%2==0 or x%2==0 and (y< altura and x< largura):
            x = randint(3,(largura-1))
            y = randint(3,(altura-1))
        print("Primeira escolha ({},{})".format(x, y))
        matriz[x][y]=1

        lista = labirinto.retorna_Corredores(lista_proibida,x,y)
        print("Lista: {}".format(lista))
        while len(lista) > 0:
            cont = 1
        #for i in range(5):
            print("##LOOP {} ##".format(cont))
            escolha = randint(0,len(lista)-1)
            print("Escolha: {}".format(escolha))
            Ponto = lista[escolha]
            print("Ponto: {}".format(Ponto))
            lista.pop(escolha)
            print("Lista Sem: {}".format(lista))
            
            if (Ponto[2] >= 0) and (Ponto[2] <= (self.largura)) and (Ponto[3] >= 0) and (Ponto[3] <= (self.altura)):
                print("passou no primeiro IF")
                print("({},{})".format(Ponto[2], Ponto[3]))
                if (matriz[Ponto[2]][Ponto[3]]==0):
                    print("Dentro Ponto = {}".format(matriz[Ponto[0]][Ponto[1]]))
                    matriz[Ponto[0]][Ponto[1]] = 1
                    matriz[Ponto[2]][Ponto[3]] =  1
                    
                    print()
                    print("######################################")
                    for i in range(self.altura):
                        for j in range(self.largura):
                            print(matriz[i][j],end=" ")
                        print()
                    print("######################################")
                    print()
                    lista += labirinto.retorna_Corredores(lista_proibida,Ponto[2],Ponto[3])
                    print("Lista ++: {}".format(lista))
                else:
                    print("valor matriz else {}".format(matriz[Ponto[2]][Ponto[3]]))
                    print("valor não entra")
            else:
                print("NÂO ENTRA POR CONTA DO INTERVALO")
            cont += 1
        for i in range(self.altura):
            for j in range(self.largura):
                print(matriz[i][j],end=" ")
            print()

        

#matriz = labirinto.inicializa_Matriz_Zero(9,11)
#labirinto.imprime_Matriz(matriz,9,11)

mat = labirinto(11,9)
mat.Gera_Labirinto()
#mat.imprime_Matriz()
 