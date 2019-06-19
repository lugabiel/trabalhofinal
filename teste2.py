import matplotlib.pyplot as plt
import matplotlib.animation as animation
import random
import csv
import math
import time
from math import pow as pow
from random import uniform as uni
from random import randint as rin

class bairro(object):
    def __init__(self, x = 0,y = 0):
        self.x = x
        self.y = y
    '''metodo p/ calcular distancia entre Bairros'''
    def calculaDist(self, bairro): 
        dist = pow(pow(self.x - bairro.x,2) + pow(self.y - bairro.y,2),1/2)
        return dist

class UPA(bairro):
    def __init__(self, x, y, bAdjacentes = []):
        super().__init__(x, y)
        '''Conj dos bairros mais proximos a UPA'''
        self.bAdjacentes = bAdjacentes
        '''Metodo p/ calcular somatorio das distancias aos bAdjacentes'''
    def calcSomatorio():
        super().calculaDist()
        soma = 0
        for bairro in bAdjacentes:
            soma = self.calculaDist(bairro)
        self
    
class mapa(object):
    def __init__(self, bairros = []):
        self.bairros = bairros

class conjuntoUPAs(object):
    def __init__(self, bairros = [], fit = 10000):
        self.bairros = bairros
        self.fit = fit
    def calculaFit():
        a = 0
    
    def mutacao():
        b = 0

class populacao(object):
    def __init__(self, arranjoUPAs = [], mapa = [], tamanho = 5):
        self.pop = arranjoUPAs
        self.tam = tamanho
        self.mapa = mapa
        
    