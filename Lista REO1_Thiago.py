'''
########################################################################################################################
print('-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=--=-=-=-=-=-=-=-=-=-=-==-=-=')
print('DISCIPLINA: VISÃO COMPUTACIONAL NO MELHORAMENTO DE PLANTAS')
print('ALUNO: THIAGO TAVARES BOTELHO')
print('MATRÍCULA: 2019260138')
print('PROFESSOR: VINÍCIUS QUINTÃO CARNEIRO')
print('-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=--=-=-=-=-=-=-=-=-=-=-==-=-=')
'''

#PACOTE UTILIZADO

import numpy as np
import matplotlib.pyplot as plt

#################################################################################################################
######################################## EXERCÍCIO 01 ###########################################################
#################################################################################################################
'''
################################    Questão 01.A   ##############################################################
print('EXERCÍCIO 01:')
print('1.a)   Declare os valores 43.5,150.30,17,28,35,79,20,99.07,15 como um array numpy.')
print('Resposta:')
exe01 = (43.5,150.30,17,28,35,79,20,99.07,15)               # criei uma lista
vetor01 = np.array(exe01)                                   # declarei como vetor array
print('Vetor formado: ' + str(vetor01))
print('O vetor é do tipo:' + str(type(vetor01)))

################################    Questão 01.B    ##############################################################
print('-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=--=-=-=-=-=-=-=-=-=-=-==-=-=')
print('1.b)   Obtenha as informações de dimensão, média, máximo, mínimo e variância deste vetor.')
print('Resposta:')
dim01 = len(vetor01)                                        # comando "len" para obter a dimensão
media01 = np.mean(vetor01)                                  # comando "np.mean" para obter a média
max01 = max(vetor01)                                        # comando "max" para obter o valor máximo
min01 = min(vetor01)                                        # comando "min" para obter o valor mínimo
var01 = np.var(vetor01)                                     # comando "np.var" para obter a variância
print('Dimensão do vetor: ' + str(dim01))
print('Média do vetor: ' + str(media01))
print('Máximo do vetor: ' + str(max01))
print('Mínimo do vetor: ' + str(min01))
print('Variância do vetor: ' + str(var01))

################################    Questão 01.C    ##############################################################
print('-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=--=-=-=-=-=-=-=-=-=-=-==-=-=')
print('1.c)   Obtenha um novo vetor em que cada elemento é dado pelo quadrado da diferença entre cada elemento do '
      'vetor declarado na letra a e o valor da média deste.')
print('Resposta:')
media01 = np.mean(vetor01)
vetor02 = np.array((vetor01-media01)**2)
print('O novo vetor: ' + str(vetor02))
print('Tipo: ' + str(type(vetor02)))

################################    Questão 01.D    ##############################################################
print('-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=--=-=-=-=-=-=-=-=-=-=-==-=-=')
print('1.d)   Obtenha um novo vetor que contenha todos os valores superiores a 30.')
print('Resposta:')
bool_maior_30 = vetor01>30                                  # cria uma variável booleana
print('Vetor original: ' + str(vetor01))
print('Vetor booleanos com os valores maiores que 30: ' + str(bool_maior_30))
vetor03 = vetor01[bool_maior_30]                            # cria um novo vetor, com os valores maiores que 30
print('Novo vetor com os valores maiores que 30:' + str(vetor03))
print('Tipo: ' + str(type(vetor03)))

################################    Questão 01.E    ##############################################################
print('-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=--=-=-=-=-=-=-=-=-=-=-==-=-=')
print('1.e)   Identifique quais as posições do vetor original possuem valores superiores a 30')
print('Resposta:')
pos = np.where(vetor01>30)                                  # comando "np.where" indica a localização
print('Vetor original: ' + str(vetor01))
print('As posições dos valores >30 são: ' + str(pos))

################################    Questão 01.F    ##############################################################
print('-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=--=-=-=-=-=-=-=-=-=-=-==-=-=')
print('1.f)   Apresente um vetor que contenha os valores da primeira, quinta e última posição.')
print('Resposta:')
prim = vetor01[0]
quin = vetor01[4]
ult = vetor01[-1]
vetor04 = [prim, quin, ult]
vetor04 = np.array(vetor04)
print('Vetor original: ' + str(vetor01))
print('O vetor contendo os valores da primeira, quinta e última posição:', vetor04)
print('Tipo: ' + str(type(vetor04)))

################################    Questão 01.G    ##############################################################
print('-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=--=-=-=-=-=-=-=-=-=-=-==-=-=')
print('1.g)   Crie uma estrutura de repetição usando o for para apresentar cada valor e a sua respectiva posição durante as '
      'iterações')
print('Resposta:')
contador = 0
print('Considerando que o Python pondera a primeira posição sendo 0:')
for position,valor in enumerate(vetor01):
    contador = contador + 1
    print('Iteração ' + str(contador) + ': Na posição ' + str(position) + ', ocorre o valor ' + str(valor))

################################    Questão 01.H    ##############################################################
print('-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=--=-=-=-=-=-=-=-=-=-=-==-=-=')
print('1.h)   Crie uma estrutura de repetição usando o for para fazer a soma dos quadrados de cada valor do vetor.')
print('Resposta:')
def somatorio (vetor01):
    somador = 0
    it = 1
    for el in vetor01:
        print('Elemento: ' + str(el))
        print('Somador: ' + str(somador))
        somador = somador + (el)**2
        it = it + 1
        print('Iteração ' + str(it) + ': Somatorio é ' + str(somador))
    return somador
print(vetor01)
somatorio(vetor01)

################################    Questão 01.I    ##############################################################
print('-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=--=-=-=-=-=-=-=-=-=-=-==-=-=')
print('1.i)   Crie uma estrutura de repetição usando o while para apresentar todos os valores do vetor')
print('Resposta:')

pos = 0
while vetor01[pos] !=8:
    print(vetor01[pos])
    pos = pos + 1
    if pos ==(len(vetor01)):
        print('Posição igual a: ' + str(pos) + ' - A condição estabelecida retornou true, a ação é interrompida')
        break


################################    Questão 01.J    ##############################################################
print('-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=--=-=-=-=-=-=-=-=-=-=-==-=-=')
print('1.j)   Crie um sequência de valores com mesmo tamanho do vetor original e que inicie em 1 e o passo seja também 1.')
print('Resposta:')
vetor05 = list(range(1, len(vetor01)+1, 1))               # range retorna uma série numérica        # inicia em um, tem o mesmo tamanho do vetor01 e vai de 1 em 1
print('Sequência de valores: ' + str(vetor05))

################################    Questão 01.K    ##############################################################
print('-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=--=-=-=-=-=-=-=-=-=-=-==-=-=')
print('k)   Concatene o vetor da letra a com o vetor da letra j.')
print('Resposta:')
vetor06 = np.concatenate((vetor01, vetor05), axis=0)              # axis indica o número de eixos
print('O novo vetor formado pela junção do vetor da letra "a" e "j": ' + str(vetor06))

'''

#################################################################################################################
######################################## EXERCÍCIO 02 ###########################################################
#################################################################################################################
'''
################################    Questão 02.A    ##############################################################
print('-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=--=-=-=-=-=-=-=-=-=-=-==-=-=')
print('EXERCÍCIO 02:')
print('2.a)   Declare a matriz abaixo com a biblioteca numpy.')
print('1 3 22')
print('2 8 18')
print('3 4 22')
print('4 1 23')
print('5 2 52')
print('6 2 18')
print('7 2 25')
print('Resposta:')
matriz01 = np.array([[1, 3, 22], [2, 8, 18], [3, 4, 22], [4, 1, 23],[5, 2, 52], [6, 2, 18], [7, 2, 25]])
print('Matriz: ')
print(matriz01)
print(type(matriz01))

################################    Questão 02.B    ##############################################################
print('-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=--=-=-=-=-=-=-=-=-=-=-==-=-=')
print('2.b)   Obtenha o número de linhas e de colunas desta matriz')
print('Resposta:')
dim02 = np.shape(matriz01)
nl,nc = np.shape(matriz01)
print('A dimensão da matriz: ' + str(dim02))
print('O número de linhas: ' + str(nl))
print('O número de colunas: ' + str(nc))

################################    Questão 02.C    ##############################################################
print('-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=--=-=-=-=-=-=-=-=-=-=-==-=-=')
print('2.c)   Obtenha as médias das colunas 2 e 3.')
print('Resposta:')
submatriz_coluna2 = matriz01[:,1]
media_coluna2 = np.average(submatriz_coluna2)                       # np.average calcula a média
print('A média da coluna 2: ' + str(media_coluna2))
submatriz_coluna3 = matriz01[:,-1]
media_coluna3 = np.average(submatriz_coluna3)
print('A média da coluna 3: ' + str(media_coluna3))

################################    Questão 02.D    ##############################################################
print('-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=--=-=-=-=-=-=-=-=-=-=-==-=-=')
print('2.d)   Obtenha as médias das linhas considerando somente as colunas 2 e 3')
print('Resposta:')
matriz02 = matriz01[0:,1:]
print('A nova matriz com as colunas 2 e 3:')
print(matriz02)
submatriz_linha1= matriz02[0,:]
media_linha1 = np.average(submatriz_linha1)
print('A média da linha 1, considerando as colunas 2 e 3: ' + str(media_linha1))
submatriz_linha2= matriz02[1,:]
media_linha2 = np.average(submatriz_linha2)
print('A média da linha 2, considerando as colunas 2 e 3: ' + str(media_linha2))
submatriz_linha3= matriz02[2,:]
media_linha3 = np.average(submatriz_linha3)
print('A média da linha 3, considerando as colunas 2 e 3: ' + str(media_linha3))
submatriz_linha4= matriz02[3,:]
media_linha4 = np.average(submatriz_linha4)
print('A média da linha 4, considerando as colunas 2 e 3: ' + str(media_linha4))
submatriz_linha5= matriz02[4,:]
media_linha5 = np.average(submatriz_linha5)
print('A média da linha 5, considerando as colunas 2 e 3: ' + str(media_linha5))
submatriz_linha6= matriz02[5,:]
media_linha6 = np.average(submatriz_linha6)
print('A média da linha 6, considerando as colunas 2 e 3: ' + str(media_linha6))
submatriz_linha7= matriz02[6,:]
media_linha7 = np.average(submatriz_linha7)
print('A média da linha 7, considerando as colunas 2 e 3: ' + str(media_linha7))


################################    Questão 02.E    ##############################################################
print('-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=--=-=-=-=-=-=-=-=-=-=-==-=-=')
print('2.e) Considerando que a primeira coluna seja a identificação de genótipos, a segunda nota de severidade de uma doença '
      'e a terceira peso de 100 grãos. Obtenha os genótipos que possuem nota de severidade inferior a 5.')
print('Resposta:')
coluna_2 = (matriz01[:, 1])
print('Notas de severidade dos genótipos: ' + str(coluna_2))
notas_menor5 = np.where(coluna_2<5)
print('As posições na matriz dos genótipos que possuem notas inferiores a 5 são:' + str(notas_menor5))
bol_menor5 = coluna_2<5
coluna_1 = (matriz01[:,0])
genotipos_notas_menor5 = coluna_1[bol_menor5]
print('Os genótipos com notas inferiores a 5 são: ' + str(genotipos_notas_menor5))

################################    Questão 02.F    ##############################################################
print('-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=--=-=-=-=-=-=-=-=-=-=-==-=-=')
print('2.f)   Considerando que a primeira coluna seja a identificação de genótipos, a segunda nota de severidade de uma '
      'doença e a terceira peso de 100 grãos. Obtenha os genótipos que possuem nota de peso de 100 grãos superior ou '
      'igual a 22.')
print('Resposta:')
coluna_3 = (matriz01[:, -1])
print('Notas de peso de 100 grãos dos genótipos: ' + str(coluna_3))
notas_maior_igual22 = np.where(coluna_3>=22)
print('As posições na matriz dos genótipos que possuem notas superior ou igual a 22 são:' + str(notas_maior_igual22))
bol_maior_igual22 = coluna_3>=22
coluna_1 = (matriz01[:,0])
genotipos_notas_maior_igual22 = coluna_1[bol_maior_igual22]
print('Os genótipos com nota superior ou igual a 22 são: ' + str(genotipos_notas_maior_igual22))

################################    Questão 02.G    ##############################################################
print('-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=--=-=-=-=-=-=-=-=-=-=-==-=-=')
print('2.g) Considerando que a primeira coluna seja a identificação de genótipos, a segunda nota de severidade de uma doença '
      'e a terceira peso de 100 grãos. Obtenha os genótipos que possuem nota de severidade igual ou inferior a 3 e peso de 100'
      'grãos igual ou superior a 22.')
print('Resposta:')
notas_menor3 = np.where(coluna_2<=3)
bol_menor3 = coluna_2<=3
print('As posições  dos genótipos que possuem nota inferior ou igual a 3 são ' + str(notas_menor3) + 'e as posições dos '
      'genótipos com peso de 100 grãos superior ou igual a 22: ' + str(notas_maior_igual22))
genot_3e22 = coluna_1[bol_maior_igual22 & bol_menor3]
print('Os genótipos com peso de 100 grãos superior ou igual a 22 e nota de severidade de doença inferior ou '
      'igual a 3: ' + str(genot_3e22))

################################    Questão 02.H    ##############################################################
print('-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=--=-=-=-=-=-=-=-=-=-=-==-=-=')
print('2.h) Crie uma estrutura de repetição com uso do for (loop) para apresentar na tela cada uma das posições da matriz '
      'e o seu respectivo valor. Utilize um iterador para mostrar ao usuário quantas vezes está sendo repetido.'
      'Apresente a seguinte mensagem a cada iteração "Na linha X e na coluna Y ocorre o valor: Z".'
      'Nesta estrutura crie uma lista que armazene os genótipos com peso de 100 grãos igual ou superior a 25')
print('Resposta:')
print('Matriz de dados: ' + str(matriz01))
contador = 0
genot = []
for i in np.arange(0,nl,1):
      if matriz01[i, 2] >=25:
            genot.append(matriz01[i,0])
      for j in np.arange(0,nc,1):
            contador += 1
            print('Iteração '+ str(contador) + ': Na linha ' + str(i) + ' e na coluna ' + str(j) + ' ocorre o '
             'valor: ' + str(matriz01[int(i),int(j)]))

print('Os genótipos com peso de 100 grãos iguais ou superiores a 25 foram: ' + str(genot))

'''

#################################################################################################################
######################################## EXERCÍCIO 03 ###########################################################
#################################################################################################################
'''
print('-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=--=-=-=-=-=-=-=-=-=-=-==-=-=')
print('Exercício 03')
print('3.a) Crie uma função em um arquivo externo (outro arquivo .py) para calcular a média e a variância amostral um '
      'vetor qualquer, baseada em um loop (for).')
print('Resposta:')
print('Um arquivo externo (.py) com a função foi criado, sendo ele função.questão03_Thiago.py')
from questao03_Thiago import media,variancia

################################    Questão 03.B    ##############################################################
print('-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=--=-=-=-=-=-=-=-=-=-=-==-=-=')
print('3.b) Simule três arrays com a biblioteca numpy de 10, 100, e 1000 valores e com distribuição normal com média 100 '
      'e variância 2500. Pesquise na documentação do numpy por funções de simulação.')
print('Resposta:')
vetor_10 = np.random.normal(100,50,10)                # media de 100, desvio padrão de 50 e numero de valores igual a 10
vetor_100 = np.random.normal(100,50,100)
vetor_1000 = np.random.normal(100,50,1000)
print('O vetor com 10 valores: ' + str(vetor_10))
print('Tipo: ' + str(type(vetor_10)))
print('----------------------------------------')
print('O vetor com 100 valores: ' + str(vetor_100))
print('Tipo: ' + str(type(vetor_100)))
print('----------------------------------------')
print('Devido a dimensão, o vetor com 1000 valores não será lido')
#print('O vetor com 1000 valores: ' + str(vetor_1000))
#print('Tipo: ' + str(type(vetor_1000)))

################################    Questão 03.C    ##############################################################
print('-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=--=-=-=-=-=-=-=-=-=-=-==-=-=')
print('3.c) Utilize a função criada na letra a para obter as médias e variâncias dos vetores simulados na letra b.')
print('Resposta:')
print('O vetor de tamanho 10, apresenta média igual a ' + str(media(vetor_10)) + ' e variância igual '
        'a ' + str(variancia(vetor_10)))
print('O vetor de tamanho 100,apresenta média igual a ' + str(media(vetor_100)) + ' e variância igual '
        'a ' + str(variancia(vetor_100)))
print('O vetor de tamanho 1000,apresenta média igual a ' + str(media(vetor_1000)) + ' e variância igual '
        'a ' + str(variancia(vetor_1000)))

################################    Questão 03.D    ##############################################################
print('-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=--=-=-=-=-=-=-=-=-=-=-==-=-=')
print('3.d) Crie histogramas com a biblioteca matplotlib dos vetores simulados com valores de 10, 100, 1000 e 100000.')
print('Resposta:')
plt.style.use('dark_background')
histogram_10 = plt.hist(vetor_10, bins=10, color='b')
plt.title('Vetor 1 - 10 dados')
plt.xlim(0, 200)                                 # tamanho do eixo x
plt.ylim(0, 5)                                    # tamanho do eixo y
plt.grid(True)                                     # grafico quadriculado
plt.show()
histogram_100 = plt.hist(vetor_100, bins=10, color='b')
plt.title('Vetor 2 - 100 dados')
plt.xlim(-50, 300)                                 # tamanho do eixo x
plt.ylim(0, 30)                                    # tamanho do eixo y
plt.grid(True)                                     # grafico quadriculado
plt.show()
histogram_1000 = plt.hist(vetor_1000, bins=20, color='b')
plt.title('Vetor 3 - 1000 dados')
plt.xlim(-100, 300)                                 # tamanho do eixo x
plt.ylim(0, 150)                                    # tamanho do eixo y
plt.grid(True)                                     # grafico quadriculado
plt.show()
vetor_100000 = np.random.normal(100,50,100000)
histogram_100000 = plt.hist(vetor_100000, bins=300, color='b')
plt.title('Vetor 3 - 100000 dados')
plt.xlim(-150, 350)                                 # tamanho do eixo x
plt.ylim(0, 1500)                                    # tamanho do eixo y
plt.grid(True)                                     # grafico quadriculado
plt.show()
'''

#################################################################################################################
######################################## EXERCÍCIO 04 ###########################################################
#################################################################################################################
'''
print('-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=--=-=-=-=-=-=-=-=-=-=-==-=-=')
print('Exercício 04')
print('4.a) O arquivo dados.txt contem a avaliação de genótipos (primeira coluna) em repetições (segunda coluna) quanto a '
      'quatro variáveis (terceira coluna em diante). Portanto, carregue o arquivo dados.txt com a biblioteca numpy, '
      'apresente os dados e obtenha as informações de dimensão desta matriz.')
print('Resposta:')
dados = np.loadtxt('dados.txt')
print('Dados:')
print('    Gen    Rep    V1     V2     V3     V4     V5')
print(dados)
nl,nc = np.shape(dados)
print('Número de linhas: ' + str(nl))
print('Número de colunas: ' + str(nc))

################################    Questão 04.B    ##############################################################
print('-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=--=-=-=-=-=-=-=-=-=-=-==-=-=')
print('4.b) Pesquise sobre as funções np.unique e np.where da biblioteca numpy')
print('Resposta:')
print(' Foi realizada a pesquisa das duas funcões com o auxílio do comando help')
#help(np.unique)
#help(np.where)

################################    Questão 04.C    ##############################################################
print('-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=--=-=-=-=-=-=-=-=-=-=-==-=-=')
print('c) Obtenha de forma automática os genótipos e quantas repetições foram avaliadas')
print('Resposta:')
print('Os genótipos avaliados foram: ' + str(np.unique(dados[:,0])))            # retirar os valores duplicados
print('As repetições são: ' + str(np.unique(dados[:,1])))

################################    Questão 04.D    ##############################################################
print('-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=--=-=-=-=-=-=-=-=-=-=-==-=-=')
print('4.d) Apresente uma matriz contendo somente as colunas 1, 2 e 4')
print('Resposta:')
dados02 = dados[:,[0,1,3]]              #dados[:,[0,1,3]] ->Todas as linhas, das colunas 0, 1 e 3
print('Dados Selecionados: ')
print('   Gen    Rep    V2')
print(dados02)
print(type(dados02))

################################    Questão 04.E    ##############################################################
print('-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=--=-=-=-=-=-=-=-=-=-=-==-=-=')
print('4.e)   Obtenha uma matriz que contenha o máximo, o mínimo, a média e a variância de cada genótipo para a variavel da'
      ' coluna 4. Salve esta matriz em bloco de notas.')
print('Resposta:')
matriz_final = np.zeros((len(np.unique(dados02[:, 0])), 5))
contador = 0
for i in range(0, len(np.unique(dados02[:, 0])), 1):                                   #
    contador = contador + 1
    print('------------------------------------------------------------------')
    print('Genótipos: ' + str(contador))
    print("Máximo: " + str(np.max((dados02[dados02[:, 0] == i + 1])[:, 2])))
    print("Mínimo: " + str(np.min((dados02[dados02[:, 0] == i + 1])[:, 2])))
    print("Média: " + str(np.around(np.mean((dados02[dados02[:, 0] == i + 1])[:, 2]), 2)))          #np.around é para arredondar o valor final
    print("Variância: " + str(np.around(np.var((dados02[dados02[:, 0] == i + 1])[:, 2]), 2)))
    matriz_final[i, 0] = i + 1
    matriz_final[i, 1] = np.max((dados02[dados02[:, 0] == i + 1])[:, 2])
    matriz_final[i, 2] = np.min((dados02[dados02[:, 0] == i + 1])[:, 2])
    matriz_final[i, 3] = np.around(np.mean((dados02[dados02[:, 0] == i + 1])[:, 2]), 2)
    matriz_final[i, 4] = np.around(np.var((dados02[dados02[:, 0] == i + 1])[:, 2]), 2)
np.savetxt('Matriz Final.txt', matriz_final, fmt='%2.2f', delimiter='\t')

################################    Questão 04.F    ##############################################################
print('-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=--=-=-=-=-=-=-=-=-=-=-==-=-=')
print('4.f)   Obtenha os genótipos que possuem média (médias das repetições) igual ou superior a 500 da matriz gerada na '
      'letra anterior.')
print('Resposta:')
superior500 = np.loadtxt('Matriz Final.txt')
vetor_genotipo = (superior500[:, 0])
vetor_media = (superior500[:, 3])
vetor_500 = np.where(vetor_media>=5)
bol_maior500 = vetor_media>=500
print('As posições na matriz dos genótipos que possuem notas superior ou igual 500 são:' + str(bol_maior500))
final = vetor_genotipo[bol_maior500]
print('Os genótipos com média superior ou igual a 500 são: ' + str(final))

################################    Questão 04.G    ##############################################################
print('-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=--=-=-=-=-=-=-=-=-=-=-==-=-=')
print('4.g) Apresente os seguintes graficos: 1) Médias dos genótipos para cada variável. Utilizar o comando plt.subplot '
      'para mostrar mais de um grafico por figura. 2)Disperão 2D da médias dos genótipos (Utilizar as três primeiras '
      'variáveis). No eixo X uma variável e no eixo Y outra.')
print('Resposta:')
media1 = np.zeros((10,1))               # criei um vetor de zeros com 10 linhas e 1 coluna
media2 = np.zeros((10,1))
media3 = np.zeros((10,1))
media4 = np.zeros((10,1))
media5 = np.zeros((10,1))
contador = 0
for i in np.arange(0,30,3):             #percorre as 30 linhas do vetor original de acordo com o numero de repetições
    media1[contador,0] = np.mean(dados[i:i + 3, 2], axis=0)
    media2[contador,0] = np.mean(dados[i:i + 3, 3], axis=0)
    media3[contador,0] = np.mean(dados[i:i + 3, 4], axis=0)
    media4[contador,0] = np.mean(dados[i:i + 3, 5], axis=0)
    media5[contador,0] = np.mean(dados[i:i + 3, 6], axis=0)
    contador = contador + 1
genotipos = np.unique(dados[0:30,0:1], axis=0)
tabel_medias = np.concatenate((genotipos, media1, media2, media3, media4, media5), axis=1)

print('Gráficos - Médias dos genótipos para cada variável')
plt.style.use('ggplot')
fig = plt.figure('Gráfico de Médias')
plt.subplot(2,3,1)
plt.bar(tabel_medias[:,0], tabel_medias[:,1])
plt.title('Variável 1')
plt.xticks(tabel_medias[:,0])           #indicar o nome dos genótipos
plt.subplot(2,3,2)
plt.bar(tabel_medias[:,0], tabel_medias[:,2])
plt.title('Variável 2')
plt.xticks(tabel_medias[:,0])
plt.subplot(2,3,3)
plt.bar(tabel_medias[:,0], tabel_medias[:,3])
plt.title('Variável 3')
plt.xticks(tabel_medias[:,0])
plt.subplot(2,3,4)
plt.bar(tabel_medias[:,0], tabel_medias[:,4])
plt.title('Variável 4')
plt.xticks(tabel_medias[:,0])
plt.subplot(2,3,5)
plt.bar(tabel_medias[:,0], tabel_medias[:,5])
plt.title('Variável 5')
plt.xticks(tabel_medias[:,0])
fig.tight_layout()              # ajustar os gráficos
plt.show()
nome = 'medias_barras'
fig.savefig((nome+'.png'),bbox_inches='tight')           #Adequar tamanho imagem - bbox_inches='tight'

print('Gráficos - Dispersão')
plt.style.use('ggplot')
fig = plt.figure('Dispersão')
plt.subplot(2,2,1)                      # 1, 2 - delimitam como seria a figura    1 - posição do gráfico
plt.scatter(tabel_medias[:,1], tabel_medias[:,2], s=50, alpha=1, c='blue')    #coordenada x- [:,1] coordenada y- [:,2] tamanho- s=50 transparencia- alpha=1
plt.title('Dispersão')
plt.xlabel('Var 1')
plt.xlabel('Var 2')
plt.subplot(2,2,2)
plt.scatter(tabel_medias[:,1], tabel_medias[:,3], s=50, alpha=1, c='blue')
plt.title('Dispersão')
plt.xlabel('Var 1')
plt.xlabel('Var 3')
plt.subplot(2,2,3)
plt.scatter(tabel_medias[:,2], tabel_medias[:,3], s=50, alpha=1, c='blue')
plt.title('Dispersão')
plt.xlabel('Var 2')
plt.xlabel('Var 3')
fig.tight_layout()   
plt.show()
nome = 'medias_dispersao'
fig.savefig((nome+'.png'),bbox_inches='tight')

'''