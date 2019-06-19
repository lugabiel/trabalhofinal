from time import sleep
import string

bairros = ['409442 435913',
    '409408 436075',
    '409344 436201',
    '409398 436213',
    '409638 435143']
conjBairro = [
'410888 435542',
'410885 435668',
'410895 435848',
'410901 435964',
'410946 435666']

def atualizaGrafico(arquivo, conjBairros = []):
    with open(arquivo,'r+') as arquivo:
        for bairro in conjBairros:
            aux = '\n' + bairro
            arquivo.write(aux)
            print('adiciona bairro')
