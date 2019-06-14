import matplotlib.pyplot as plt
import random
from random import randint as rin
import math
from math import pow as pow
import csv

class bairro(object):
    def __init__(self, x = 0, y = 0):
        self.x = x
        self.y = y

class cliente(object):
    def __init__(self):
        self.pos = []

class conjuntoUPAs(object):
    def __init__(self, v = []):
        self.bairro = v
        self.fit = 10000
    pass

class populacao(object):
    def __init__(self, c = cliente(), tam = 5):
        self.upas = [] #lista de ponteiros para objetos conjuntoUPAs
        self.selecao = [] #quais upas estao selecionadas para cada cliente
        solucao = []
        for j in range(tam):
            for i in range(5):
                solucao.append(c.pos[rin(0,len(c.pos))])
            self.upas.append(UPAs(solucao))
            solucao = []

    def fit(self, c = cliente()):
        pass

    def minUPA(self, c = cliente()):
        pos = c.pos
        for j in self.upas:
            fit = 0
            bairro = 0
            for i in len(pos):
                for k in j.bairro:
                    min = 10000
                    upaDist = pow(pow(k.x - pos[i].x, 2) + pow(k.y - pos[y].y, 2), 1/2)
                    if min > upaDist:
                        min = upaDist
                        bairro = i
                fit += min
            j.fit = fit
c = cliente()
x = []
y = []



with open('pmedian324.txt','r') as csvfile:
    plots = csv.reader(csvfile, delimiter = ' ')
    for linha in plots:
        c.pos.append(bairro(int(linha[0]), int(linha[1])))
        x.append(int(linha[0]))
        y.append(int(linha[1]))

plt.scatter(x, y, label = 'Bairros',marker = '+')
plt.xlabel('x')
plt.ylabel('y')

plt.title('Distribuição de Bairros')
plt.legend()
plt.show()

pop = populacao(c)

while 