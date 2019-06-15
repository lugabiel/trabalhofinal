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
        temp = conjuntoUPAs()
        for bairro in self.bairros:
            temp.bairros.append(c.pos[rin(0,len(c.pos) - 1)])
        temp.fitness(c)
        return temp

    def fitness(self, c = cliente()):
        fit = 0
        bairro = 0
        for i in range(len(c.pos)):
            for k in self.bairros:
                min = 10000
                upaDist = pow(pow(k.x - c.pos[i].x, 2) + pow(k.y - c.pos[i].y, 2), 1/2)
                if min > upaDist:
                    min = upaDist
                    bairro = i
            fit += min
        self.fit = fit


class populacao(object):
    def __init__(self, c = cliente(), tam = 5):
        self.upas = [] #lista de ponteiros para objetos conjuntoUPAs
        self.selecao = [] #quais upas estao selecionadas para cada cliente
        solucao = []
        self.c = c
        for j in range(tam):
            for i in range(0,4):
                solucao.append(c.pos[rin(0,len(c.pos) - 1)])
            temp = conjuntoUPAs(solucao)
            temp.fitness(self.c)
            self.upas.append(temp)
            solucao = []
        self.upas = sorted(self.upas, key = lambda x: x.fit)

    def atualiza(self):
        upas = sorted(self.upas, key = lambda x: x.fit)
        temp = []
        temp2 = []
        mut = 0.75
        for cUPA1 in upas:
            for cUPA2 in upas:
                if uni(0,1) > 1:
                    temp.append(cUPA1.mutacao(self.c))

                temp.append(self.transa(cUPA1, cUPA2))
            temp.append(cUPA1)
        temp = sorted(temp, key = lambda y: y.fit)
        for i in range(len(upas) - 1):
            temp2.append(temp[i])
        self.upas = temp2

    def transa(self, c1 = conjuntoUPAs(), c2 = conjuntoUPAs()):
        filho = conjuntoUPAs()
        if len(c1.bairros) != len(c2.bairros):
            return filho
        for upa in range(0, len(c1.bairros) - 1): # cruzamento dos pais
            if rin(0,1) > 0.7:
                filho.bairros.append(c1.bairros[upa])
            else:
                filho.bairros.append(c2.bairros[upa])
        filho.fitness(self.c)
        return filho



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
plt.show()

pop = populacao(c, 5)
for i in range(10):
    upax = []
    upay = []
    for i in pop.upas[0].bairros:
        upax.append(i.x)
        upay.append(i.y)
    pop.atualiza()
    plt.scatter(upax, upay, label = 'UPAs',marker = 'o')
    plt.draw()
    plt.scatter(x, y, label = 'Bairros',marker = '*')
    plt.draw()
    plt.show()
