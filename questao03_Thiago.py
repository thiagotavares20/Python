##### Pacotes utilizados #####
import numpy as np

##### Questão 3.a #####
def media (vetor_fun):                  # def é para criar um comando
    somador = 0
    contador = 0
    gi = 0
    for i in vetor_fun:
        somador = somador + i
        gi = gi + 1
        contador = contador + 1
        mean= somador/contador
    return mean

def variancia (vetor_fun):
    somador = 0
    gi = 0
    sdq = 0
    for i in vetor_fun:
        somador = somador + i
        gi = gi + 1
        sdq = sdq + i**2
    variancia = (sdq - ((somador**2/gi)))/(gi-1)
    return variancia

'''
print('-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=--=-=-=-=-=-=-=-=-=-=-==-=-=')
print('TESTE DA FUNÇÃO: ')
vetor = np.array ([10, 20, 30])
print('O vetor possui os seguintes elementos' + str(vetor) + ' a sua média é '
      + str(media(vetor)) + ' e a variância amostral é ' + str(variancia(vetor)))
print('-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=--=-=-=-=-=-=-=-=-=-=-==-=-=')
'''


