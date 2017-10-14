import cv2
import numpy as np

from dfh.itens.penteado.classificador import classificarPenteado

pontoDeCorte = 0.5
tolerancia = 0.05

class ResultadoItem:
	resultadoClassificacao = None
	resultadoNormatizado = None
	peso = None	

class EcDfhF912Results:
	adaptacaoCabelo = None
	bocaCortada = None
	dedosJuntos = None
	dificuldadeIntegracao = None
	enfaseFace = None
	figuraBaixa = None
	linhaPesada = None
	linhaTremida = None
	penteado = None
	problemaRepresentacaoRoupa = None
	transparencia = None

def classificarEcDfhF912(path):
	img = prepararImagem(path)
	return classificarItens(path)
		
def classificarItens(img):
	results = EcDfhF912Results()
	penteado = ResultadoItem()
	penteado.resultadoClassificacao = avaliarPenteado(img)
	results.penteado = penteado
	
	return results
	
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
	
	
