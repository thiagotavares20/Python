######   REO3   ######

# DATA: 17/08/2020
# DISCIPLINA: VISÃO COMPUTACIONAL NO MELHORAMENTO DE PLANTAS
# PROFESSOR: VINÍCIUS QUINTÃO CARNEIRO
# ALUNOS:
# CAROLINE MARCELA DA SILVA
# EWERTON LÉLYS RESENDE
# MARIANA ANDRADE DIAS
# THIAGO TAVARES BOTELHO

################################################################################################
# Importar pacotes:

import cv2  # Importa o pacote opencv
from matplotlib import pyplot as plt # Importa o pacote matplotlib
import numpy as np
from skimage.measure import label, regionprops
from skimage.feature import peak_local_max
from skimage.segmentation import watershed
from scipy import ndimage
import pandas as pd
########################################################################################################################
# Leitura da imagem:
nome_arquivo = 'trabalho.png' # determina a variável para carregar a imagem
img_bgr = cv2.imread(nome_arquivo,1) # carrega a imagem no sistema bgr e depois converte para RGB.
img_rgb = cv2.cvtColor(img_bgr,cv2.COLOR_BGR2RGB) # faz a conversão para a RGB.

########################################################################################################################
print('1-Selecione uma imagem a ser utilizada no trabalho prático e realize os seguintes processos utilizando\n'
      'as bibliotecas OPENCV e Scikit-Image do Python:')

print('a) Aplique o filtro de média com cinco diferentes tamanhos de kernel e compare os resultados\n'
      'com a imagem original; ')

#Filtros de média
img_fmedia_1 =  cv2.blur ( img_rgb , ( 11 , 11 ))
img_fmedia_2 =  cv2.blur ( img_rgb , ( 21 , 21 ))
img_fmedia_3 =  cv2.blur ( img_rgb , ( 31 , 31 ))
img_fmedia_4 =  cv2.blur ( img_rgb , ( 41 , 41 ))
img_fmedia_5 =  cv2.blur ( img_rgb , ( 51 , 51 ))

# Apresentação das figuras
plt.figure('Filtros')
plt.subplot(2,3,1)
plt.imshow(img_rgb)
plt.xticks([])
plt.yticks([]) #
plt.title("ORIGINAL")

plt.subplot(2,3,2)
plt.imshow(img_fmedia_1)
plt.xticks([])
plt.yticks([])
plt.title("5x5")

plt.subplot(2,3,3)
plt.imshow(img_fmedia_2)
plt.xticks([])
plt.yticks([])
plt.title("11x11")

plt.subplot(2,3,4)
plt.imshow(img_fmedia_3)
plt.xticks([])
plt.yticks([])
plt.title("21x21")

plt.subplot(2,3,5)
plt.imshow(img_fmedia_4)
plt.xticks([])
plt.yticks([])
plt.title("31x31")

plt.subplot(2,3,6)
plt.imshow(img_fmedia_5)
plt.xticks([])
plt.yticks([])
plt.title("41x41")

plt.show()
print('-'*50)
print('')

print('b) Aplique diferentes tipos de filtros com pelo menos dois tamanhos de kernel e compare os\n'
      'resultados entre si e com a imagem original.')

# Filtro de média
img_filtro_media1 = cv2.blur(img_rgb,(33,33))
img_filtro_media2 = cv2.blur(img_rgb,(61,61))

# Filtro gaussiano
img_filtro_gaussiano1 = cv2.GaussianBlur(img_rgb,(33,33),0)
img_filtro_gaussiano2 = cv2.GaussianBlur(img_rgb,(61,61),0)

# Filtro de mediana
img_filtro_mediana1 = cv2.medianBlur(img_rgb,33)
img_filtro_mediana2 = cv2.medianBlur(img_rgb,61)

# Filtro bilateral
img_filtro_bilateral1 = cv2.bilateralFilter(img_rgb,33,33,21)
img_filtro_bilateral2 = cv2.bilateralFilter(img_rgb,61,61,21)

#Apresentação das imagens

#Filtros - kernel 31x31
plt.figure('Imagens- Diferentes filtros')
plt.subplot(231)
plt.imshow(img_rgb)
plt.title("RGB")
plt.xticks([])
plt.yticks([])

plt.subplot(232)
plt.imshow(img_filtro_media1)
plt.title("MÉDIA 33x33")
plt.xticks([])
plt.yticks([])

plt.subplot(233)
plt.imshow(img_filtro_gaussiano1)
plt.title("GAUSSIANO 33x33")
plt.xticks([])
plt.yticks([])

plt.subplot(235)
plt.imshow(img_filtro_mediana1)
plt.title("MEDIANA 33X33")
plt.xticks([])
plt.yticks([])

plt.subplot(236)
plt.imshow(img_filtro_bilateral1)
plt.title("BILATERAL 33X33")
plt.xticks([])
plt.yticks([])

plt.show()

#Filtros - kernel 61x61
plt.figure('Imagens- Diferentes filtros')
plt.subplot(231)
plt.imshow(img_rgb)
plt.title("RGB")
plt.xticks([])
plt.yticks([])

plt.subplot(232)
plt.imshow(img_filtro_media2)
plt.title("MÉDIA 61X61")
plt.xticks([])
plt.yticks([])

plt.subplot(233)
plt.imshow(img_filtro_gaussiano2)
plt.title("GAUSSIANO 61X61")
plt.xticks([])
plt.yticks([])

plt.subplot(235)
plt.imshow(img_filtro_mediana2)
plt.title("MEDIANA 61X61")
plt.xticks([])
plt.yticks([])

plt.subplot(236)
plt.imshow(img_filtro_bilateral2)
plt.title("BILATERAL 61X61")
plt.xticks([])
plt.yticks([])

plt.show()

######=#####

# Filtros de borda

#Laplacian
img_1 = cv2.Laplacian(img_rgb,cv2.CV_64F) #Função para aplicação do filtro em imagem 64b.
abs_164f = np.absolute(img_1)             #Transormando em numeros inteiros.
img_1 = np.uint8(abs_164f)                #Transformando para inteiro de 8b.

#Sobel
img_sx = cv2.Sobel(img_rgb,cv2.CV_64F,0,1,ksize=5)  #Função para aplicação do filtro (imagem, ident.64b, eixoy,eixo x e kernel).
abs_sx64f = np.absolute(img_sx)
img_sx = np.uint8(abs_sx64f)

img_sy = cv2.Sobel(img_rgb,cv2.CV_64F,1,0,ksize=5)
abs_sy64f = np.absolute(img_sy)
img_sy = np.uint8(abs_sy64f)

#Bordas Canny
edges = cv2.Canny(img_rgb, 100,200)                 #Função (imagem rgb, minimo e maximo do gradiente de borda (delimitação da borda). Os valores intermediários também são processados pelo algoritmo por conectividade com as de valores acima de 200.

#Apresentação das imagens
plt.figure('Imagens- Filtros de Bordas')
plt.subplot(231)
plt.imshow(img_rgb)
plt.title("RGB")
plt.xticks([])
plt.yticks([])

plt.subplot(232)
plt.imshow(img_1)
plt.title("Laplacian")
plt.xticks([])
plt.yticks([])

plt.subplot(233)
plt.imshow(img_sx)
plt.title("Sobel eixo X")
plt.xticks([])
plt.yticks([])

plt.subplot(235)
plt.imshow(img_sy)
plt.title("Sobel eixo Y")
plt.xticks([])
plt.yticks([])

plt.subplot(236)
plt.imshow(edges)
plt.title("Canny")
plt.xticks([])
plt.yticks([])

plt.show()
print('-='*50)
print('')

print('c) Realize a segmentação da imagem utilizando o processo de limiarização. Utilizando o\n'
      'reconhecimento de contornos, identifique e salve os objetos de interesse. Além disso, acesse\n'
      'as bibliotecas Opencv e Scikit-Image, verifique as variáveis que podem ser mensuradas e\n'
      'extraia as informações pertinentes (crie e salve uma tabela com estes dados). Apresente todas\n'
      'as imagens obtidas ao longo deste processo.')

# Conversão para o sistema HSV
img_HSV = cv2.cvtColor(img_bgr,cv2.COLOR_BGR2HSV)

# Partição dos canais
H,S,V = cv2.split(img_HSV)

#Filtro de média
S = cv2.medianBlur(S,5)

# Histograma do canal informativo S
hist_S = cv2.calcHist([S],[0], None, [256],[0,256])

# Limiarização - Thresholding
(L, img_limiar) = cv2.threshold(S,0,255,cv2.THRESH_BINARY+cv2.THRESH_OTSU)
(Linv, img_limiar_inv) = cv2.threshold(S,0,255,cv2.THRESH_BINARY_INV+cv2.THRESH_OTSU)

# Obtendo imagem segmentada
img_segmentada = cv2.bitwise_and(img_rgb,img_rgb,mask=img_limiar)

#Apresentando limiarização da imagem

plt.figure('Imagem HSV')
plt.subplot(2,2,1)
plt.imshow(img_HSV)
plt.xticks([])
plt.yticks([])
plt.title('Canal S- HSV')

plt.subplot(2,2,2)
plt.plot(hist_S)
plt.title('Histograma S')

plt.subplot(2,2,3)
plt.imshow(img_limiar, cmap='gray')
plt.xticks([])
plt.yticks([])
plt.title('Limiarização')

plt.subplot(2,2,4)
plt.imshow(img_segmentada)
plt.xticks([])
plt.yticks([])
plt.title('Segmentada')

plt.show()

# Objetos
mascara = img_limiar.copy()
cnts,h = cv2.findContours(mascara, cv2.RETR_TREE,cv2.CHAIN_APPROX_SIMPLE)
dimen = []

# Obtenção dos contornos dos objetos

for (i, c) in enumerate(cnts):

	(x, y, w, h) = cv2.boundingRect(c)
	obj = img_limiar[y:y+h,x:x+w]
	obj_rgb = img_segmentada[y:y+h,x:x+w]
	obj_bgr = cv2.cvtColor(obj_rgb,cv2.COLOR_RGB2BGR)
	cv2.imwrite('folha'+str(i+1)+'.png',obj_bgr)
	cv2.imwrite('Imagem Binaria' + str(i + 1) + '.png', obj)

# Características das medidas dos objetos

	area = cv2.contourArea(c)
	razao = round((h/w), 2)
	perim = round(cv2.arcLength(c, True), 2)
	tam_ret = np.shape(obj)

	regiao = regionprops(obj)
	rm = round(regiao[0].minor_axis_length, 2)
	rmai = round(regiao[0].major_axis_length, 2)
	cen = regiao[0].centroid
	dimen += [[str(i + 1), str(h), str(w), str(area), str(razao),
			   str(perim), str(tam_ret), str(rm), str(rmai), str(cen)]]

#Caracterização- medidas de cor	dos objetos

	print('Medidas de Cor')
	min_val_r, max_val_r, min_loc_r, max_loc_r = cv2.minMaxLoc(obj_rgb[:,:,0], mask=obj)
	print('Valor Mínimo no R: ', min_val_r, ' - Posição: ', min_loc_r)
	print('Valor Máximo no R: ', max_val_r, ' - Posição: ', max_loc_r)
	med_val_r = cv2.mean(obj_rgb[:,:,0], mask=obj)
	print('Média no Vermelho: ', med_val_r)

	min_val_g, max_val_g, min_loc_g, max_loc_g = cv2.minMaxLoc(obj_rgb[:, :, 1], mask=obj)
	print('Valor Mínimo no G: ', min_val_g, ' - Posição: ', min_loc_g)
	print('Valor Máximo no G: ', max_val_g, ' - Posição: ', max_loc_g)
	med_val_g = cv2.mean(obj_rgb[:,:,1], mask=obj)
	print('Média no Verde: ', med_val_g)

	min_val_b, max_val_b, min_loc_b, max_loc_b = cv2.minMaxLoc(obj_rgb[:, :, 2], mask=obj)
	print('Valor Mínimo no B: ', min_val_b, ' - Posição: ', min_loc_b)
	print('Valor Máximo no B: ', max_val_b, ' - Posição: ', max_loc_b)
	med_val_b = cv2.mean(obj_rgb[:,:,2], mask=obj)
	print('Média no Azul: ', med_val_b)

#confecção da tabela

dados_folhas = pd.DataFrame(dimen)
dados_folhas = dados_folhas.rename(columns={0: 'FOLHA', 1: 'ALTURA', 2: 'LARGURA', 3: 'AREA', 4: 'RAZAO',
											5: 'PERIMETRO', 6: 'TAMANHO RET', 7:'EIXO MENOR', 8:'EIXO MAIOR',
											9:'CENTROIDE'})
dados_folhas.to_csv('medidas.csv', index=False)

print('Total de objetos: ', len(cnts))
print('-'*50)

#Apresentando os contornos
seg = img_segmentada.copy()
cv2.drawContours(seg,cnts,-1,(0,255,0),2)

plt.figure('Objetos')
plt.subplot(1,2,1)
plt.imshow(seg)
plt.xticks([])
plt.yticks([])
plt.title('Objetos')

plt.subplot(1,2,2)
plt.imshow(obj_rgb)
plt.xticks([])
plt.yticks([])
plt.title('Objetos')
plt.show()

print('-='*50)
print('')

print('d) Utilizando máscaras, apresente o histograma somente dos objetos de interesse.')

#Conversão da imagem para HSV
img_segmentada_backup = img_segmentada.copy()
img_segmentada2 = cv2.cvtColor(img_segmentada,cv2.COLOR_RGB2HSV)

#Recorte dos objetos
plt.figure('Objetos')
for (i, c) in enumerate(cnts):
	(x,y,w,h) = cv2.boundingRect(c)
	print('Objeto #%d' % (i+1))
	print(cv2.contourArea(c))
	obj = img_limiar[y:y+h,x:x+w]
	obj_rgb = img_segmentada2[y:y+h,x:x+w]

#Criação dos histogramas
	grafico = True
	if grafico == True:

		hist_segmentada_r = cv2.calcHist([obj_rgb], [0], obj, [256], [0, 256])
		hist_segmentada_g = cv2.calcHist([obj_rgb], [1], obj, [256], [0, 256])
		hist_segmentada_b = cv2.calcHist([obj_rgb], [2], obj, [256], [0, 256])
		# obj = img_rgb[y:y + h, x:x + w]

#Apresentando as imagens
		plt.subplot(3,3,2)
		plt.imshow(obj_rgb)
		plt.title('Objeto: ' + str(i+1))

		plt.subplot(3, 3, 4)
		plt.imshow(obj_rgb[:,:,0],cmap='gray')
		plt.title('Objeto: ' + str(i + 1))

		plt.subplot(3, 3, 5)
		plt.imshow(obj_rgb[:,:,1],cmap='gray')
		plt.title('Objeto: ' + str(i + 1))

		plt.subplot(3, 3, 6)
		plt.imshow(obj_rgb[:,:,2],cmap='gray')
		plt.title('Objeto: ' + str(i + 1))

		plt.subplot(3, 3, 7)
		plt.plot(hist_segmentada_r, color='r')
		plt.title("Histograma - R")
		plt.xlim([0, 256])
		plt.xlabel("Valores Pixels")
		plt.ylabel("Número de Pixels")

		plt.subplot(3, 3, 8)
		plt.plot(hist_segmentada_g, color='g')
		plt.title("Histograma - G")
		plt.xlim([0, 256])
		plt.xlabel("Valores Pixels")
		plt.ylabel("Número de Pixels")

		plt.subplot(3, 3, 9)
		plt.plot(hist_segmentada_b, color='b')
		plt.title("Histograma - B")
		plt.xlim([0, 256])
		plt.xlabel("Valores Pixels")
		plt.ylabel("Número de Pixels")
		plt.show()

	else:
		pass

print('-'*50)

print('e) Realize a segmentação da imagem utilizando a técnica de k-means. Apresente as imagens\n'
      'obtidas neste processo.')

# Formatação da imagem para uma matriz de dados
pixel_values = img_rgb.reshape((-1, 3))

# Conversão para Decimal (para transformar inteiro de 8 bites para decimal)
pixel_values = np.float32(pixel_values)

print('Dimensão Matriz: ',pixel_values.shape)
print('-'*50)

# K-means (Processo iterativo)

# Critério de Parada
criteria = (cv2.TERM_CRITERIA_EPS + cv2.TERM_CRITERIA_MAX_ITER, 100, 0.2)

# Número de Grupos (k)
k = 2
dist, labels, (centers) = cv2.kmeans(pixel_values, k, None, criteria, 10, cv2.KMEANS_RANDOM_CENTERS)

print('SQ das Distâncias de Cada Ponto ao Centro: ', dist)
print('-'*50)

print('Dimensão labels: ', labels.shape)
print('Valores únicos: ',np.unique(labels))
print('Tipo labels: ', type(labels))
# flatten the labels array
labels = labels.flatten()
print('-'*50)

print('Dimensão flatten labels: ', labels.shape)
print('Tipo labels (f): ', type(labels))
print('-'*50)

# Valores dos labels
val_unicos,contagens = np.unique(labels,return_counts=True)
val_unicos = np.reshape(val_unicos,(len(val_unicos),1))
contagens = np.reshape(contagens,(len(contagens),1))
hist = np.concatenate((val_unicos,contagens),axis=1)

print('Histograma')
print(hist)
print('-'*50)
print('Centroides Decimais')
print(centers)
print('-'*50)

# Conversão dos centroides para valores de interos de 8 digitos
centers = np.uint8(centers)

print('Centroides uint8')
print(centers)
print('-'*50)

# Conversão dos pixels para a cor dos centroides
matriz_segmentada = centers[labels]

print('Dimensão Matriz Segmentada: ',matriz_segmentada.shape)
print('Matriz Segmentada')
print(matriz_segmentada[0:5,:])
print('-'*50)

# Reformatar a matriz na imagem de formato original
img_segmentada1 = matriz_segmentada.reshape(img_rgb.shape)

# Grupo 1
original_01 = np.copy(img_rgb)
matriz_or_01 = original_01.reshape((-1, 3))
matriz_or_01[labels != 0] = [0, 0, 0]
img_final_01 = matriz_or_01.reshape(img_rgb.shape)

# Grupo 2
original_02 = np.copy(img_rgb)
matriz_or_02 = original_02.reshape((-1, 3))
matriz_or_02[labels != 1] = [0, 0, 0]
img_final_02 = matriz_or_02.reshape(img_rgb.shape)

# Apresentar Imagem
plt.figure('Imagens')
plt.subplot(2,2,1)
plt.imshow(img_rgb)
plt.title('ORIGINAL')
plt.xticks([])
plt.yticks([])

plt.subplot(2,2,2)
plt.imshow(img_segmentada1)
plt.title('ROTULOS')
plt.xticks([])
plt.yticks([])

plt.subplot(2,2,3)
plt.imshow(img_final_01)
plt.title('Grupo 1')
plt.xticks([])
plt.yticks([])

plt.subplot(2,2,4)
plt.imshow(img_final_02)
plt.title('Grupo 2')
plt.xticks([])
plt.yticks([])

plt.show()
print('-'*50)
print('')

print('f) Realize a segmentação da imagem utilizando a técnica de watershed. Apresente as\n'
      ' imagens obtidas neste processo.')

#Conversão sistema de cor
img_HSV = cv2.cvtColor(img_bgr,cv2.COLOR_BGR2HSV)

#Partição dos canais
h,s,v = cv2.split(img_HSV)

#Segmentação
limiar, mascara = cv2.threshold(s,0,255,cv2.THRESH_BINARY+cv2.THRESH_OTSU)

#Picos
img_dist = ndimage.distance_transform_edt(mascara)
max_local = peak_local_max(img_dist, indices=False, min_distance=100, labels=mascara)

print('Número de Picos')
print(np.unique(max_local,return_counts=True))
print('-'*50)

#Marcadores
marcadores,n_marcadores = ndimage.label(max_local, structure=np.ones((3, 3)))

print('Análise de conectividade - Marcadores')
print(np.unique(marcadores,return_counts=True))
print('-'*50)

#Segmentação Watershed
img_ws = watershed(-img_dist, marcadores, mask=mascara)

print('Imagem Segmentada - Watershed')
print(np.unique(img_ws,return_counts=True))
print("Número de Folhas: ", len(np.unique(img_ws)) - 1)

#Acessando um objeto
img_final = np.copy(img_rgb)
img_final[img_ws != 2] = [0,0,0] # Acessando a folha 2

#Apresentação das imagens
plt.figure('Watershed')
plt.subplot(2,3,1)
plt.imshow(img_rgb)
plt.xticks([])
plt.yticks([])
plt.title('IMAGEM ORIGINAL')

plt.subplot(2,3,2)
plt.imshow(s,cmap='gray')
plt.xticks([])
plt.yticks([])
plt.title('IMAGEM - S')

plt.subplot(2,3,3)
plt.imshow(mascara,cmap='gray')
plt.xticks([])
plt.yticks([])
plt.title('IMAGEM BINÁRIA - MÁSCARA')

plt.subplot(2,3,4)
plt.imshow(img_dist,cmap='jet')
plt.xticks([])
plt.yticks([])
plt.title('IMAGEM DE DIST NCIAS')

plt.subplot(2,3,5)
plt.imshow(img_ws,cmap='jet')
plt.xticks([])
plt.yticks([])
plt.title('IMAGEM FOLHA - SEGMENTADA')

plt.subplot(2,3,6)
plt.imshow(img_final)
plt.xticks([])
plt.yticks([])
plt.title('IMAGEM FINAL SEM O VALOR 2')

plt.show()

print('-'*50)
print('g) Compare os resultados das três formas de segmentação (limiarização, k-means e watershed\n'
      'e identifique as potencialidades de cada delas.')

# Apresentando as imagens das três segmentações
plt.figure('Imagens')
plt.subplot(1,3,1)
plt.imshow(img_ws)
plt.xticks([])
plt.yticks([])
plt.title('Segmentada Wathershed')

plt.subplot(1,3,2)
plt.imshow(img_segmentada)
plt.xticks([])
plt.yticks([])
plt.title('Segmentada OTSU')

plt.subplot(1,3,3)
plt.imshow(img_final_02)
plt.title('Segmentada K-MEANS')
plt.xticks([])
plt.yticks([])

plt.show()
########################################################################################################################