from Ponto import Ponto
from random import randint
x = y = 0

while y%2==0 or x%2==0 and (y<9 and x<11):
    x = randint(3,(11-2))
    y = randint(3,(9-2))

print("x {} Y{}".format(x,y))