######  APRESENTAÇÃO REO2   #####
########################################################################################################################
# DATA: 27/07/2020
# DISCIPLINA: VISÃO COMPUTACIONAL NO MELHORAMENTO DE PLANTAS
# PROFESSOR: VINÍCIUS QUINTÃO CARNEIRO
# ALUNOS:
# CAROLINE MARCELA DA SILVA
# EWERTON LÉLYS RESENDE
# MARIANA ANDRADE DIAS
# THIAGO TAVARES BOTELHO

########################################################################################################################

# Pacotes utilizados- Importar

import cv2 # Importa o pacote opencv
import numpy as np # Importa o pacote numpy
from matplotlib import pyplot as plt # Importa o pacote matplotlib

########################################################################################################################

print('-='*50)
print('Exercício 01: Selecione uma imagem a ser utilizada no trabalho prático e realize os seguintes processos '
      'utilizando o pacote OPENCV do Python')
print('-='*50)
print('01.a) Apresente a imagem e as informações de número de linhas e colunas; número de canais e número total de pixels')
print('')

arquivo = ("trabalho.jpeg")                                 #criei uma variável para receber meu arquivo;
imagem = cv2.imread(arquivo,1)                              #função de leitura do opencv, como argumento, usa a variável e 1 para carregar a imagens coloridas;
print(imagem)                                               #vai imprimir a imagem na forma de matriz.

plt.figure('Imagem original')                               #cria uma figura com a imagem original, e posteriormante vamos usar para delimitar a área do recorte.
plt.imshow(imagem)                                          #função própria para apresentar a imagem a partir do arquivo matricial.
plt.title("Imagem original")
plt.show()

nl,nc,canais = np.shape(imagem)                             #informações sobre a dimensão da matriz,a partir da função shape do numpy;
print('Número de linhas: ' + str(nl))                       #altura da imagem;
print('Número de colunas: ' + str(nc))                      #largura da imagem;
print('Número de canais: ' + str(canais))                   #diferentes intensidades contidas em cada pixel.
numero_pixels=nl*nc
print('O número de pixels é:'+ str(numero_pixels))          #cada posição da matriz, corresponde a um pixel.
print('-='*50)
print('')

print('01.b) Faça um recorte da imagem para obter somente a área de interesse. Utilize esta imagem para a solução das '
      'próximas alternativas')
print('')

img_recorte = imagem[250:810,395:860]                       #variável que vai receber a imagem cortada e as dimensões de linha e coluna do corte;

plt.figure('Imagem recortada')                              #nova figura, agora com a imagem cortada.
plt.imshow(img_recorte)
plt.title("Imagem recortada")
plt.show()
print('-='*50)
print('')

print('01.c) Converta a imagem colorida para uma de escala de cinza (intensidade) e a apresente utilizando os mapas de'
      ' cores “Escala de Cinza” e “JET”')

# Todas em uma única figura
img_rgb = cv2.cvtColor(img_recorte, cv2.COLOR_BGR2RGB)      #converter a nossa imagem BGR para RBG, criando uma nova variável

plt.figure('Imagens')
plt.subplot(221)                                            #plotar diferentes figuras em uma imagem
plt.imshow(imagem)
plt.title("BGR")                                            #primeiro, imagem original
plt.xticks([]) # Eliminar o eixo X                          #eliminar a marcação dos eixos
plt.yticks([])  # #liminar o eixo y
plt.colorbar(orientation='horizontal')                      #colocar a barra de cor na horizontal

plt.subplot(222)
plt.imshow(img_rgb)
plt.title("RGB")                                            #no segundo quadrante, imagem rgb, cortada
plt.xticks([]) # Eliminar o eixo X
plt.yticks([])  # #liminar o eixo y
plt.colorbar(orientation='horizontal')

img_cinza = cv2.cvtColor(img_recorte,cv2.COLOR_BGR2GRAY)    #imagem em escala de cinza. Criamos uma variável e realizamos a conversão do RGB para o green
plt.subplot(223)
plt.imshow(img_cinza, cmap = 'gray')
plt.title("Escala de Cinza")
plt.xticks([]) # Eliminar o eixo X
plt.yticks([])  # #liminar o eixo y
plt.colorbar(orientation='horizontal')

plt.subplot(224)
plt.imshow(img_cinza, cmap = 'jet')
plt.title("JET")                                            #imagem na escala jet
plt.xticks([]) # Eliminar o eixo X
plt.yticks([])  # #liminar o eixo y
plt.colorbar(orientation='horizontal')
plt.show()                                                  #apresenta o resultado na tela
print('-='*50)
print('')

print('01.D) Apresente a imagem em escala de cinza e o seu respectivo histograma; Relacione o histograma e a imagem.')
print('')

histograma = cv2.calcHist([img_cinza],[0],None,[256],[0,256]) #construir histograma, parâmetros: imagem, número de canais, presença de mascaras, numero e intervalo de pontos.
print(histograma)

plt.subplot(1,2,1)                                            #construir a figura com a imagem e o histograma juntos
plt.imshow(img_cinza, cmap="gray")                            #mapa de cor "gray" delimita entre o preto e o branco, da imagem
plt.title("Imagem")

plt.subplot(1,2,2)
plt.plot(histograma, color='black')
plt.title("Histograma")
plt.xlabel("Valores de Pixels")
plt.ylabel("Número de Pixels")

plt.show()
print('-='*50)
print('')

print('01.E) Utilizando a imagem em escala de cinza (intensidade) realize a segmentação da imagem de modo a remover o '
      'fundo da imagem utilizando um limiar manual e o limiar obtido pela técnica de Otsu. Nesta questão apresente o '
      'histograma com marcação dos limiares utilizados, a imagem limiarizada (binarizada) e a imagem colorida final '
      'obtida da segmentação. Explique resultados.')
print('')

######Limiarização Manual#######

limiar_cinza = 155

(L, img_limiar) = cv2.threshold(img_cinza,limiar_cinza,255,cv2.THRESH_BINARY)  #função para fazer a limiarização manual, escolhendo um limiar;

(L, img_limiar_inv) = cv2.threshold(img_cinza,limiar_cinza,255,cv2.THRESH_BINARY_INV)  #vai inverter, abaixo do limiar recebe 255 e acima do limiar recebe 0, vai inverter a imagem

img_segmentada = cv2.bitwise_and(img_rgb,img_rgb,mask=img_limiar_inv)

print('Limiar: ' + str(L))

# Apresentar figuras

plt.figure('Thresholding')
plt.subplot(2,2,1)
plt.imshow(img_segmentada)                                                    #imagem rgb segmentada
plt.title('Segmentada RGB')

plt.subplot(2,2,2)
plt.plot(histograma,color = 'black')                                         #histograma
plt.axvline(x=limiar_cinza,color = 'r')                                      #linha na vertical que indica posição do limiar, limiar-cinza=155 e cor da linha, vermelho;
plt.title("Histograma - Cinza")
plt.xlim([0,256])                                                            #variação do eixo x
plt.xlabel("Valores Pixels")
plt.ylabel("Número de Pixels")

plt.subplot(2,2,3)
plt.imshow(img_limiar,cmap='gray')                                          #imagem limiarizada
plt.title('Binário - L: ' + str(limiar_cinza))

plt.subplot(2,2,4)
plt.imshow(img_limiar_inv,cmap='gray')                                      #imagem limiarizada
plt.title('Binário Invertido: L: ' + str(limiar_cinza))

plt.show()

#####Limiarização OTSU#####

(L1, img_otsu) = cv2.threshold(img_cinza,0,255,cv2.THRESH_BINARY+cv2.THRESH_OTSU)
(Linv, img_otsu_inv) = cv2.threshold(img_cinza,0,255,cv2.THRESH_BINARY_INV+cv2.THRESH_OTSU)

img_segmentada_otsu = cv2.bitwise_and(img_rgb,img_rgb,mask=img_otsu_inv)
print(L1)

# Apresentar figuras

plt.figure('Thresholding')
plt.subplot(2,2,1)
plt.imshow(img_segmentada_otsu)
plt.xticks([])
plt.yticks([])
plt.title('Segmentada RGB')

plt.subplot(2,2,2)
plt.plot(histograma,color = 'black')
plt.axvline(x=L,color = 'r')
plt.title("Histograma - Cinza")
plt.xlim([0,256])
plt.xlabel("Valores Pixels")
plt.ylabel("Número de Pixels")

plt.subplot(2,2,3)
plt.imshow(img_otsu,cmap='gray')
plt.title('OTSU - L: ' + str(L))
plt.xticks([])
plt.yticks([])

plt.subplot(2,2,4)
plt.imshow(img_otsu_inv,cmap='gray')
plt.title('OTSU - L inv: ' + str(L))
plt.xticks([])
plt.yticks([])

plt.show()
print('-='*50)
print('')

print('01.F) Apresente uma figura contento a imagem selecionada nos sistemas RGB, Lab, HSV e YCrCb.')
print('')

img_rgb = cv2.cvtColor(img_recorte,cv2.COLOR_BGR2RGB)
img_Lab = cv2.cvtColor(img_recorte,cv2.COLOR_BGR2Lab)
img_HSV = cv2.cvtColor(img_recorte,cv2.COLOR_BGR2HSV)
img_YCrCb = cv2.cvtColor(img_recorte,cv2.COLOR_BGR2YCR_CB)

plt.figure('Sistemas de cores')
plt.subplot(2,2,1)
plt.imshow(img_rgb)
plt.title('RGB')

plt.subplot(2,2,2)
plt.imshow(img_Lab)
plt.title('Lab')

plt.subplot(2,2,3)
plt.imshow(img_HSV)
plt.title('HSV')

plt.subplot(2,2,4)
plt.imshow(img_YCrCb)
plt.title("YCrCb")

plt.show()
print('-='*50)
print('')

print('01.G) Apresente uma figura para cada um dos sistemas de cores (RGB, HSV, Lab e YCrCb) contendo a imagem de cada '
      'um dos canais e seus respectivos histogramas.')
print('')

##### RGB #####

# Histograma de imagem em escala de cinza
hist_r = cv2.calcHist([img_rgb],[0],None,[256],[0,256])
hist_g = cv2.calcHist([img_rgb],[1],None,[256],[0,256])
hist_b = cv2.calcHist([img_rgb],[2],None,[256],[0,256])

# Apresentar imagens

plt.figure('IMAGEM')
plt.subplot(3,3,2)                                  #na posição 2, apresentar a imagem RGB;
plt.imshow(img_rgb,cmap="gray")
plt.title("RGB")

plt.subplot(3,3,4)
plt.imshow(img_rgb[:,:,0],cmap='gray')              #na posição 4, apresentar todas as linhas e colunas da matriz 0, que é do canal vermelho;
plt.title("R")

plt.subplot(3,3,7)
plt.plot(hist_r,color = 'r')                        #na posição 7, abaixo da figura do canal c, apresentar o histograma do canal vermelho;
plt.title("Histograma - R")
plt.xlim([0,256])
plt.xlabel("Valores Pixels")
plt.ylabel("Número de Pixels")

plt.subplot(3,3,5)
plt.imshow(img_rgb[:,:,1],cmap='gray')              #na posição 5, apresentar o canal verde da figura rgb;
plt.title("G")

plt.subplot(3,3,8)
plt.plot(hist_g,color = 'g')                        #histograma do canal verde;
plt.title("Histograma - G")
plt.xlim([0,256])
plt.xlabel("Valores Pixels")
plt.ylabel("Número de Pixels")

plt.subplot(3,3,6)
plt.imshow(img_rgb[:,:,2],cmap='gray')              #canal azul;
plt.title("B")

plt.subplot(3,3,9)
plt.plot(hist_b,color = 'blue')
plt.title("Histograma - B")                         #histograma canal azul.
plt.xlim([0,256])
plt.xlabel("Valores Pixels")
plt.ylabel("Número de Pixels")

plt.show()

##### HSV #####

# Histograma de imagem em escala de cinza
hist_H = cv2.calcHist([img_HSV],[0],None,[256],[0,256])
hist_S = cv2.calcHist([img_HSV],[1],None,[256],[0,256])
hist_V = cv2.calcHist([img_HSV],[2],None,[256],[0,256])

# Apresentar imagens

plt.figure('IMAGEM')
plt.subplot(3,3,1)                                  #imagem RGB;
plt.imshow(img_rgb,cmap="gray")
plt.title("RGB")

plt.subplot(3,3,2)
plt.imshow(img_HSV,cmap="gray")                     #imagem HSV;
plt.title("HSV")

plt.subplot(3,3,4)
plt.imshow(img_HSV[:,:,0],cmap='gray')              #imagem canal H;
plt.title("H")

plt.subplot(3,3,7)
plt.plot(hist_H,color = 'black')                    #histograma canal H;
plt.title("Histograma - H")
plt.xlim([0,256])
plt.xlabel("Valores Pixels")
plt.ylabel("Número de Pixels")

plt.subplot(3,3,5)
plt.imshow(img_HSV[:,:,1],cmap='gray')              #imagem canal S;
plt.title("S")

plt.subplot(3,3,8)
plt.plot(hist_S,color = 'black')                    #histograma canal S;
plt.title("Histograma - S")
plt.xlim([0,256])
plt.xlabel("Valores Pixels")
plt.ylabel("Número de Pixels")

plt.subplot(3,3,6)
plt.imshow(img_HSV[:,:,2],cmap='gray')              #imagem canal V;
plt.title("V")

plt.subplot(3,3,9)
plt.plot(hist_V,color = 'black')                    #histograma canal V.
plt.title("Histograma - V")
plt.xlim([0,256])
plt.xlabel("Valores Pixels")
plt.ylabel("Número de Pixels")

plt.show()

##### Lab #####

# Histograma de imagem em escala de cinza
hist_L = cv2.calcHist([img_Lab],[0],None,[256],[0,256])
hist_a = cv2.calcHist([img_Lab],[1],None,[256],[0,256])
hist_b = cv2.calcHist([img_Lab],[2],None,[256],[0,256])

# Apresentar imagens

plt.figure('IMAGEM')
plt.subplot(3,3,1)
plt.imshow(img_rgb,cmap="gray")                 #imagem RGB;
plt.title("RGB")

plt.subplot(3,3,2)
plt.imshow(img_Lab,cmap="gray")                 #imagem Lab;
plt.title("Lab")

plt.subplot(3,3,4)
plt.imshow(img_Lab[:,:,0],cmap='gray')          #imagem canal L do sistema Lab;
plt.title("L")

plt.subplot(3,3,7)
plt.plot(hist_L,color = 'black')                #histograma canal L- lab;
plt.title("Histograma - L")
plt.xlim([0,256])
plt.xlabel("Valores Pixels")
plt.ylabel("Número de Pixels")

plt.subplot(3,3,5)
plt.imshow(img_Lab[:,:,1],cmap='gray')           #imagem canal a do sistema Lab;
plt.title("a")

plt.subplot(3,3,8)
plt.plot(hist_a,color = 'black')                #histograma canal a- lab;
plt.title("Histograma - a")
plt.xlim([0,256])
plt.xlabel("Valores Pixels")
plt.ylabel("Número de Pixels")

plt.subplot(3,3,6)
plt.imshow(img_Lab[:,:,2],cmap='gray')           #imagem canal b do sistema Lab;
plt.title("b")

plt.subplot(3,3,9)
plt.plot(hist_b,color = 'black')                #histograma canal b- lab;
plt.title("Histograma - b")
plt.xlim([0,256])
plt.xlabel("Valores Pixels")
plt.ylabel("Número de Pixels")

plt.show()

##### YCRCB #####

# Histograma de imagem em escala de cinza
hist_Y = cv2.calcHist([img_YCrCb],[0],None,[256],[0,256])
hist_CR = cv2.calcHist([img_YCrCb],[1],None,[256],[0,256])
hist_CB = cv2.calcHist([img_YCrCb],[2],None,[256],[0,256])

# Apresentar imagens

plt.figure('IMAGEM')
plt.subplot(3,3,1)
plt.imshow(img_rgb,cmap="gray")                     #imagem RGB
plt.title("RGB")

plt.subplot(3,3,2)
plt.imshow(img_YCrCb,cmap="gray")                   #imagem YCrCo
plt.title("YCRCB")

plt.subplot(3,3,4)
plt.imshow(img_YCrCb[:,:,0],cmap='gray')            #imagem canal Y
plt.title("Y")

plt.subplot(3,3,7)
plt.plot(hist_Y,color = 'black')                    #histograma canal Y
plt.title("Histograma - Y")
plt.xlim([0,256])
plt.xlabel("Valores Pixels")
plt.ylabel("Número de Pixels")

plt.subplot(3,3,5)
plt.imshow(img_YCrCb[:,:,1],cmap='gray')             #imagem canal Cr
plt.title("CR")

plt.subplot(3,3,8)
plt.plot(hist_CR,color = 'black')                    #histograma canal Cr
plt.title("Histograma - CR")
plt.xlim([0,256])
plt.xlabel("Valores Pixels")
plt.ylabel("Número de Pixels")

plt.subplot(3,3,6)
plt.imshow(img_YCrCb[:,:,2],cmap='gray')            #imagem canal Co
plt.title("CB")

plt.subplot(3,3,9)
plt.plot(hist_CB,color = 'black')                    #histograma canal Co
plt.title("Histograma - CB")
plt.xlim([0,256])
plt.xlabel("Valores Pixels")
plt.ylabel("Número de Pixels")

plt.show()
print('-='*50)
print('')

print('01.H) h) Encontre o sistema de cor e o respectivo canal que propicie melhor segmentação da imagem de modo a '
      'remover o fundo da imagem utilizando limiar manual e limiar obtido pela técnica de Otsu. Nesta questão apresente'
      ' o histograma com marcação dos limiares utilizados, a imagem limiarizada (binarizada) e a imagem colorida final '
      'obtida da segmentação. Explique resultados e sua escolha pelo sistema de cor e canal utilizado na segmentação. '
      'Nesta questão apresente a imagem limiarizada (binarizada) e a imagem colorida final obtida da segmentação.')
print('')

#Para essa questão, notamos que a segmentação separa o fundo da folha, e não faz a distinção da lesão. Para isso, precisariamos fazer uma análise multisegmentar.
#Para segmentar o fundo, utilizamos o sistema HSV. E futuramente, quando formos tentar fazer tal segmentação composta, iremos utilizar o canal A do Lab, que permitiu boa diferenciação das lesões.

#Sistema de cores HSV

# Segmentação -Técnica Otsu

hist_H = cv2.calcHist([img_HSV],[0],None,[256],[0,256])           #histograma em escala de cinza
hist_S = cv2.calcHist([img_HSV],[1],None,[256],[0,256])
hist_V = cv2.calcHist([img_HSV],[2],None,[256],[0,256])

H,S,V = cv2.split(img_HSV)                                        # Partição dos canais

hist_S = cv2.calcHist([S],[0], None, [256],[0,256])               # Histograma escala de cinza do canal S

##### Limiarização - Thresholding- OTSU #####
(L2, img_limiar) = cv2.threshold(S,0,255,cv2.THRESH_BINARY+cv2.THRESH_OTSU)
img_segmentada1 = cv2.bitwise_and(img_rgb,img_rgb,mask=img_limiar)            # Obtendo imagem segmentada

# Apresentar figuras
plt.figure('OTSU')
plt.subplot(1,3,2)
plt.plot(hist_S,color = 'black')
plt.axvline(x=L2,color = 'r')
plt.title("Histograma - S")
plt.xlim([0,256])
plt.xlabel("Valores Pixels")
plt.ylabel("Número de Pixels")

plt.subplot(1,3,3)
plt.imshow(img_segmentada1)
plt.title('Segmentada - RGB')
plt.xticks([])
plt.yticks([])

plt.subplot(1,3,1)
plt.imshow(img_limiar,cmap = 'gray')
plt.title('Binarizada')
plt.xticks([])
plt.yticks([])

plt.show()
print('-='*50)
print('')

##### Segmentação Manual #####

img_HSV = cv2.cvtColor(img_recorte,cv2.COLOR_BGR2HSV)             # Conversão imagem

hist_H = cv2.calcHist([img_HSV],[0],None,[256],[0,256])           # Histograma de imagem em escala de cinza
hist_S = cv2.calcHist([img_HSV],[1],None,[256],[0,256])
hist_V = cv2.calcHist([img_HSV],[2],None,[256],[0,256])

H,S,V = cv2.split(img_HSV)                                        # Partição dos canais
hist_SM = cv2.calcHist([S],[0], None, [256],[0,256])              #histograma canal S

# Limiarização manual

limiar = 130
(L3, img_limiar_S) = cv2.threshold(S,limiar,255,cv2.THRESH_BINARY)
img_segmentada2 = cv2.bitwise_and(img_rgb,img_rgb,mask=img_limiar_S)          # Obtendo imagem segmentada

# Apresentar figuras
plt.figure('MANUAL')
plt.subplot(1,3,2)
plt.plot(hist_SM,color = 'black')
plt.axvline(x=L3,color = 'r')
plt.title("Histograma - S")
plt.xlim([0,256])
plt.xlabel("Valores Pixels")
plt.ylabel("Número de Pixels")

plt.subplot(1,3,3)
plt.imshow(img_segmentada2)
plt.title('Segmentada - RGB')
plt.xticks([])
plt.yticks([])

plt.subplot(1,3,1)
plt.imshow(img_limiar_S,cmap = 'gray')
plt.title('Binarizada')
plt.xticks([])
plt.yticks([])

plt.show()
print('-='*50)
print('')

"""
#Sistema Lab

hist_L = cv2.calcHist([img_Lab],[0],None,[256],[0,256])           #fiz os histogramas de todos os canais para selecionar o melhor para meu interesse;
hist_a = cv2.calcHist([img_Lab],[1],None,[256],[0,256])
hist_b = cv2.calcHist([img_Lab],[2],None,[256],[0,256])

L,a,b = cv2.split(img_Lab)                                        #partição dos canais
hist_a = cv2.calcHist([a],[0], None, [256],[0,256])               #histograma canal a, que é o que eu acho que permitiu uma boa segmentação dos objetos da imagem; O "0"no parâmetro é porque estamos utilizando apenas 1 canal.

##Limiarização- técnica de OTSU
(L2, img_limiar) = cv2.threshold(a,0,255,cv2.THRESH_BINARY+cv2.THRESH_OTSU)

#Segmentação
img_segmentada1 = cv2.bitwise_and(img_rgb,img_rgb,mask=img_limiar)

# Apresentar figuras
plt.figure('OTSU')
plt.subplot(1,3,2)
plt.plot(hist_a,color = 'black')                                  #no subplot, o histograma do canal escolhido da imagel Lab,
plt.axvline(x=L2,color = 'r')
plt.title("Histograma - a/Lab")
plt.xlim([0,256])
plt.xlabel("Valores Pixels")
plt.ylabel("Número de Pixels")

plt.subplot(1,3,1)
plt.imshow(img_segmentada1)                                       #a imagem segmentada com a máscara obtida pelo limiar OTSU;
plt.title('Segmentada - RGB')
plt.xticks([])
plt.yticks([])

plt.subplot(1,3,3)
plt.imshow(img_limiar,cmap = 'gray')
plt.title('Binarizada')                                           #a imagem limiarizada pela tecnica de OTSU.
plt.xticks([])
plt.yticks([])

plt.show()
print('-='*50)
print('')

## Segmentação Manual

Determinação do limiar e limiarização

limiar_a = 125
(L3, img_limiar_a) = cv2.threshold(a,limiar_a,255,cv2.THRESH_BINARY)   #limiar manual, escolhi com base no resultado anterior 115;

# Obtendo imagem segmentada
img_segmentada2 = cv2.bitwise_and(img_rgb,img_rgb,mask=img_limiar_a)   #obtenção da imagem segmentada com a imagem linearizada como mascara;

# Apresentar figuras
plt.figure('MANUAL')
plt.subplot(1,3,2)
plt.plot(hist_a,color = 'black')                                        #subplot, com histograma canal a;
plt.axvline(x=L3,color = 'r')
plt.title("Histograma - a/Lab")
plt.xlim([0,256])
plt.xlabel("Valores Pixels")
plt.ylabel("Número de Pixels")

plt.subplot(1,3,1)
plt.imshow(img_segmentada2)                                             #imagem segmentada;
plt.title('Segmentada - RGB')
plt.xticks([])
plt.yticks([])

plt.subplot(1,3,3)
plt.imshow(img_limiar_a,cmap = 'gray')                                  #imagem binarizada.
plt.title('Binarizada')
plt.xticks([])
plt.yticks([])

plt.show()
print('-='*50)
print('')
"""

print('01.I)  Obtenha o histograma de cada um dos canais da imagem em RGB, utilizando como mascara a imagem limiarizada'
      ' (binarizada) da letra h. ')
print('')

#histogramas dos canais R,G e B.

hist_seg_r = cv2.calcHist([img_segmentada1],[0],img_limiar,[256],[0,256])
hist_seg_g = cv2.calcHist([img_segmentada1],[1],img_limiar,[256],[0,256])
hist_seg_b = cv2.calcHist([img_segmentada1],[2],img_limiar,[256],[0,256])

# Apresentar figuras

plt.subplot(2,3,1)
plt.imshow(img_segmentada1[:,:,0],cmap = 'gray')                 #imagem canal R
plt.title('Segmentada - R')
plt.xticks([])
plt.yticks([])

plt.subplot(2,3,2)
plt.imshow(img_segmentada1[:,:,1],cmap = 'gray')                 #imagem canal G
plt.title('Segmentada - G')
plt.xticks([])
plt.yticks([])

plt.subplot(2,3,3)
plt.imshow(img_segmentada1[:,:,2],cmap = 'gray')                 #imagem canal B
plt.title('Segmentada - B')
plt.xticks([])
plt.yticks([])

plt.subplot(2,3,4)
plt.plot(hist_seg_r,color = 'r')                                 #histograma canal R
plt.title("Histograma - R")
plt.xlim([0,256])
plt.xlabel("Valores Pixels")
plt.ylabel("Número de Pixels")

plt.subplot(2,3,5)
plt.plot(hist_seg_g,color = 'black')                              #histograma canal G
plt.title("Histograma - G")
plt.xlim([0,256])
plt.xlabel("Valores Pixels")
plt.ylabel("Número de Pixels")

plt.subplot(2,3,6)
plt.plot(hist_seg_b,color = 'b')                                  #histograma canal B
plt.title("Histograma - B")
plt.xlim([0,256])
plt.xlabel("Valores Pixels")
plt.ylabel("Número de Pixels")

plt.show()
print('-='*50)
print('')


print('01.J) Realize operações aritméticas na imagem em RGB de modo a realçar os aspectos de seu interesse. '
      'Exemplo (2*R-0.5*G). Explique a sua escolha pelas operações aritméticas. Segue abaixo algumas sugestões.')
print('')

# Operações nos canais de uma imagem

img_opr_01 = 1.5*img_rgb[:,:,2] - 2*img_rgb[:,:,0]
img_opr_02 = 1.5*img_rgb[:,:,2] - 1.5*img_rgb[:,:,0]
img_opr_03 = 1.8*img_rgb[:,:,2] - 1.5*img_rgb[:,:,0] - img_rgb[:,:,1]                #A melhor para realçar as lesões de antracnose na nervura

print("Resultados das operações:")
print("Operação 1")
print(img_opr_01)
print("Operação 2")
print(img_opr_03)
print("Operação 3")
print(img_opr_03)

# Conversão para inteiro de 8 bits

img_opr_01 = img_opr_01.astype(np.uint8)
img_opr_02 = img_opr_02.astype(np.uint8)
img_opr_03 = img_opr_03.astype(np.uint8)

print("Operações padronizadas para inteiro de 8 bits:")
print("Operação 1")
print(img_opr_01)
print("Operação 2")
print(img_opr_02)
print("Operação 3")
print(img_opr_03)

# Apresentar imagens

# Figura das modificações

plt.figure('MODIFICAÇÕES')
plt.subplot(2,2,1)
plt.imshow(img_rgb,cmap='gray')                             #imagem RGB
plt.title("RGB")

plt.subplot(2,2,2)
plt.imshow(img_opr_01,cmap='gray')                          #imagem operação 1
plt.title("1.5B-2R")

plt.subplot(2,2,3)
plt.imshow(img_opr_02,cmap='gray')                          #imagem operação 2
plt.title("1.5B-1.5R")

plt.subplot(2,2,4)
plt.imshow(img_opr_03,cmap='gray')                          #imagem operação 3
plt.title("1.8B-1.5R-G")

plt.show()
print('-='*50)
print('')

#######################################################################################################################