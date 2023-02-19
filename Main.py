from Estado import Estado
from Ponto import Ponto
from Gabarito import Gabarito
from labirinto import labirinto


matriz = labirinto(11,9)
inicio = matriz.ponto_Inicial
fim = matriz.ponto_Final
print("ini: {} fim: {}".format(inicio,fim))
matriz.imprime_Matriz()
caminho = []

estadoInicial = Estado(matriz.matriz,inicio,fim,0, caminho)
resposta = Gabarito.busca_Informada(estadoInicial) 
print("caminho: {}".format(estadoInicial.caminho))

if resposta == 0:
    print("Labirinto não tem solução")
else: 
    print(resposta)