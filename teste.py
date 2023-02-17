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


#mat = inicializa_Matriz_Zero()
#mat[4][3] = 1
#imprime_Matriz(mat)
#print()
#mat[1][2] = 2
#imprime_Matriz(mat)

lis= set()

lis.add((4,3,4,2))
lista = retorna_Corredores(lis,4,4)
print(lista)
print(lis)

