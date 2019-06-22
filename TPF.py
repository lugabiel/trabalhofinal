import matplotlib.pyplot as plt
import random
from random import randint as rin
from random import uniform as uni
import math
from math import pow as pow
import csv
import time
import tqdm

class bairro(object):
    def __init__(self, x = 0, y = 0):
        self.x = x
        self.y = y
    def distancia(self, b):
        dist = pow(self.x - b.x, 2)
        dist += pow(self.y - b.y, 2)
        return pow(dist, 1/2)

class mapa(object):
    def __init__(self):
        self.bairros = []
    def add(self, b = bairro()):
        self.bairros.append(b)

class conjuntoUPAs(object):
    def __init__(self, m = mapa()):
        self.bairrosUPAs = m
        self.fit = 10000

    def mutacao(self, m = mapa()):
        temp = conjuntoUPAs()
        for bairro in self.bairrosUPAs.bairros:
            temp.bairrosUPAs.add(m.bairros[rin(0,len(m.bairros) - 1)])
        temp.fitness(m)
        return temp

    def fitness(self, m = mapa()):
        fit = 0
        dist = 10000
        if len(self.bairrosUPAs.bairros) > 5:
            self.fit = dist
            return
        for i in m.bairros:
            dist = 10000
            for k in self.bairrosUPAs.bairros:
                if k.distancia(i) < dist:
                    dist = k.distancia(i)
            fit += dist
        self.fit = fit



class populacao(object):
    def __init__(self, m = mapa(), tamUPAs = 5, tamPop = 5):
        self.upas = [] #lista de ponteiros para objetos conjuntoUPAs
        solucao = mapa()
        self.m = m
        self.tamUPAs = tamUPAs
        self.tamPop = tamPop
        for j in range(self.tamPop):
            for i in range(self.tamUPAs):
                solucao.add(self.m.bairros[rin(0,len(self.m.bairros) - 1)])
            temp = conjuntoUPAs(solucao)
            solucao = mapa()
            temp.fitness(self.m)
            self.upas.append(temp)
        self.upas = sorted(self.upas, key = lambda x: x.fit)

    def atualiza(self):
        upas = []
        upas = sorted(self.upas, key = lambda x: x.fit)
        upasFilho = []
        for i in upas:
            for k in self.upas:
                upasFilho.append(self.transa(i, k))
            upasFilho.append(i)
        upasFilho = sorted(upasFilho, key = lambda y: y.fit)
        self.upas = []
        for i in range(self.tamPop):
            self.upas.append(upasFilho[i])
            print(upasFilho[i].fit)
        print("--------")

    def transa(self, c1 = conjuntoUPAs(), c2 = conjuntoUPAs()):
        map = mapa()
        tam1 = len(c1.bairrosUPAs.bairros)
        tam2 = len(c2.bairrosUPAs.bairros)
        if tam1 != tam2 or tam1 == 0:
            for i in range(self.tamUPAs):
                map.add(self.m.bairros[rin(0,len(self.m.bairros) - 1)])
            filho = conjuntoUPAs(map)
            filho.fitness(self.m)
            return filho
        else:
            for i in range(self.tamUPAs):
                if rin(0,1) > 0.85:
                    map.add(self.m.bairros[rin(0,len(self.m.bairros) - 1)])
                elif rin(0,1) > 0.5:
                    map.add(c1.bairrosUPAs.bairros[i])
                else:
                    map.add(c2.bairrosUPAs.bairros[i])
        filho = conjuntoUPAs(map)
        filho.fitness(self.m)
        return filho

m = mapa()
x = []
y = []



with open('pmedian324.txt','r') as csvfile:
    plots = csv.reader(csvfile, delimiter = ' ')
    for linha in plots:
        m.bairros.append(bairro(int(linha[0]), int(linha[1])))
        x.append(int(linha[0]))
        y.append(int(linha[1]))

plt.scatter(x, y, label = 'Bairros',marker = '*')
plt.xlabel('x')
plt.ylabel('y')

plt.title('Distribuição de Bairros')
plt.legend()
plt.draw()
plt.show()

pop = populacao(m, 5, 50) #(mapa de bairros, número de UPAs por solução, número de soluções)
for k in range(10):
    upax = []
    upay = []
    for i in pop.upas[0].bairrosUPAs.bairros:
        upax.append(i.x)
        upay.append(i.y)
    pop.atualiza()
    plt.scatter(upax, upay, label = 'UPAs',marker = 'o')
    plt.draw()
    plt.scatter(x, y, label = 'Bairros',marker = '*')
    plt.draw()
    plt.show()
    time.sleep(1)
