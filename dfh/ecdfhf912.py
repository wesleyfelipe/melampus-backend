import cv2
import numpy as np

from dfh.itens.penteado.classificador import classificarPenteado

pontoDeCorte = 0.5
tolerancia = 0.05

def classificarEcDfhF912(path):

	img = prepararImagem(path)
	
	results = classificarItens(path)
	
	return "Resultado: "
	
def classificarItens(img):
	result = avaliarPenteado(img)
	
	print(result)
	
def prepararImagem(path):
	img = cv2.imread(path)
	img = cv2.resize(img,(299,299))
	img = np.reshape(img,[1,299,299,3])
	return img
	
def avaliarPenteado(img):
	return avaliarResultado(classificarPenteado(img))

		
def avaliarResultado(result):
	if(result >= pontoDeCorte + tolerancia):
		return 1.0
	elif(result <= pontoDeCorte - tolerancia):
		return 0.0
	else:
		return -1.0