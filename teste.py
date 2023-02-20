from random import randint
from labirinto import labirinto

def inicializa_Matriz_Zero():
        mat = []     
        for i in range(9):
            lista = [0]*11
            mat.append(lista)
        return mat
def imprime_Matriz(matriz):
        for i in range(9):
            for j in range(11):
                print(matriz[i][j],end=" ")
            print()

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
        matriz[y][x]=1
        
        print()
        print("######################################")
        for i in range(self.altura):
            for j in range(self.largura):
                print(matriz[i][j],end=" ")
            print()
        print("######################################")
        print()

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
            
            if (Ponto[2] >= 0) and (Ponto[2] < (self.largura-1)) and (Ponto[3] >= 0) and (Ponto[3] < (self.altura-1)):
                print("passou no primeiro IF")
                print("({},{})".format(Ponto[2], Ponto[3]))
                if (matriz[Ponto[3]][Ponto[2]]==0):
                    print("Dentro Ponto = {}".format(matriz[Ponto[0]][Ponto[1]]))
                    matriz[Ponto[1]][Ponto[0]] = 1
                    matriz[Ponto[3]][Ponto[2]] = 1
                    
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
                    #print("valor matriz else {}".format(matriz[Ponto[3]][Ponto[2]]))
                    print("valor não entra")
            else:
                print("NÂO ENTRA POR CONTA DO INTERVALO")
            cont += 1
        for i in range(self.altura):
            for j in range(self.largura):
                print(matriz[i][j],end=" ")
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

def retorna_Movimento(lista):
     string = []
     for i in range(len(lista)-1):
          if lista[i][0]==lista[i+1][0] and lista[i][1]<lista[i+1][1]:
               string.append("down")
          elif lista[i][0]==lista[i+1][0] and lista[i][1]>lista[i+1][1]:
               string.append("up")
          elif lista[i][1]==lista[i+1][1] and lista[i][0]<lista[i+1][0]:
               string.append("right")
          else:
               string.append("left")
     return string

#vet = [(0, 25), (1,25), (1,24), (1,23), (1,22), (1,21), (2,21), (3,21), (3,20), (3,19), (3,18), (3,17), (3,16), (3,15), (4,15), (5,15), (6,15), (7,15), (8,15), (9,15), (10,15), (11,15), (12,15), (13,15), (13,14), (13,13), (14,13), (15,13), (16,13), (17,13), (17,12), (17,11), (18,11), (19,11), (20,11), (21,11), (22,11), (23,11), (24,11), (25,11), (26,11), (27,11), (27,10), (27,9), (27,8), (27,7), (27,6), (27,5), (27,4), (27,3), (28,3), (29,3), (30,3), (31,3), (31,2), (31,1), (32,1)]
#resul = retorna_Movimento(vet)





