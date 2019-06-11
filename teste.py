import matplotlib.pyplot as plt
import random
from random import randint as rin
import csv



class cliente(object):
    def __init__(self):
        self.x = []
        self.y = []
class populacao(object):
    def __init__(self, c = cliente(), tam = 5):
        self.upa = []
        solucao = []
        for j in range(tam):
            for i in range(5):
                solucao.append(rin(0,len(c.x)))
                self.upa.append(solucao)
            
            solucao = []

c = cliente()


with open('pmedian324.txt','r') as csvfile:
    plots = csv.reader(csvfile, delimiter = ' ')
    for linha in plots:
        c.x.append(int(linha[0]))
        c.y.append(int(linha[1]))




plt.scatter(c.x,c.y, label = 'Bairros',marker = '+')
plt.xlabel('x')
plt.ylabel('y')

#plt.xticks(x)
#plt.yticks(y)


plt.Artist()
plt.title('Distribuição de Bairros')
plt.legend()
plt.show()

