from Estado import Estado
from Gabarito import Gabarito
from labirinto import labirinto
import teste

def retorna_Movimento(index1, index2):
   #print("{}".format(type(lista[0])))
   string = []
   print("{} == {} - {} < {}".format(index1[0],index2[0],index1[1],index2[1]))
   if int(index1[0])==int(index2[0]) and int(index1[1])<int(index2[1]):
      string.append("down")
   elif int(index1[0])==int(index2[0]) and int(index1[1])>int(index2[1]):
      string.append("up")
   elif int(index1[1])==int(index2[1]) and int(index1[0])<int(index2[0]):
      string.append("right")
   else:
         string.append("left")
   return string

matriz = labirinto(33,27)
inicio = matriz.ponto_Inicial
fim = matriz.ponto_Final
print("ini: {} fim: {}".format(inicio,fim))
matriz.imprime_Matriz() 



estadoInicial = Estado(matriz.matriz, inicio, fim, 0, [])
resposta = Gabarito.busca_Informada(estadoInicial)
print(retorna_Movimento(resposta[0], resposta[1]))


print(resposta[0][0])



if resposta == 0:
    print("Labirinto não tem solução")
else: 
    print(resposta)