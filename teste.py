import matplotlib.pyplot as plt
import random
from random import randint as rin
from random import uniform as uni
import math
from math import pow as pow
import csv
import time

class bairro(object):
    def __init__(self, x = 0, y = 0):
        self.x = x
        self.y = y

class cliente(object):
    def __init__(self):
        self.pos = []

class conjuntoUPAs(object):
    def __init__(self, v = []):
        self.bairros = v
        self.fit = 10000
    def mutacao(self, c = cliente()):
        temp = []
        for bairro in self.bairros:
            temp.append(c.pos[rin(0,len(c.pos) - 1)])
        return temp


class populacao(object):
    def __init__(self, c = cliente(), tam = 5):
        self.upas = [] #lista de ponteiros para objetos conjuntoUPAs
        self.selecao = [] #quais upas estao selecionadas para cada cliente
        solucao = []
        self.c = c
        for j in range(tam):
            for i in range(5):
                solucao.append(c.pos[rin(0,len(c.pos) - 1)])
            temp = conjuntoUPAs(solucao)
            temp.fit = self.fit(temp)
            self.upas.append(temp)
            solucao = []

    def fit(self, cUPA = conjuntoUPAs()):
            fit = 0
            bairro = 0
            for i in range(len(self.c.pos)):
                for k in cUPA.bairros:
                    min = 10000
                    upaDist = pow(pow(k.x - self.c.pos[i].x, 2) + pow(k.y - self.c.pos[i].y, 2), 1/2)
                    if min > upaDist:
                        min = upaDist
                        bairro = i
                fit += min
            return fit



    def atualiza(self):
        upas = sorted(self.upas, key = lambda x: x.fit)
        temp = []
        mut = 0.75
        for cUPA1 in upas:
            for cUPA2 in upas:
                if uni(0,1) > 0.9:
                    temp.append(cUPA1.mutacao)

                temp.append(self.transa(cUPA1, cUPA2))

    def transa(self, c1 = conjuntoUPAs(), c2 = conjuntoUPAs()):
        filho = []
        for upa in range(len(c1) - 1): # cruzanmento dos pais
            if rin(0,1) > 0.7 :
                filho.append(c1.bairro[upa])
            else:
                filho.append(c2.bairro[upa])

        return conjuntoUPAs(filho)



c = cliente()
x = []
y = []



with open('pmedian324.txt','r') as csvfile:
    plots = csv.reader(csvfile, delimiter = ' ')
    for linha in plots:
        c.pos.append(bairro(int(linha[0]), int(linha[1])))
        x.append(int(linha[0]))
        y.append(int(linha[1]))

plt.scatter(x, y, label = 'Bairros',marker = '*')
plt.xlabel('x')
plt.ylabel('y')

plt.title('Distribuição de Bairros')
plt.legend()
plt.draw()

pop = populacao(c)

upax = []
upay = []
for i in pop.upas[0].bairros:
    upax.append(i.x)
    upay.append(i.y)
plt.scatter(upax, upay, label = 'UPAs',marker = 'o')
plt.show()
