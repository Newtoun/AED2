from Estado import Estado
from Ponto import Ponto
from Gabarito import Gabarito

inicio = Ponto(1, 1)
fim = Ponto(1, 9)
estadoInicial = Estado(inicio,fim,0)
resposta = Gabarito.busca_Informada(estadoInicial) 

if resposta == 0:
    print("Labirinto não tem solução")
else: 
    print(resposta)