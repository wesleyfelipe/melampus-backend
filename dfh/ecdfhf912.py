import cv2
import numpy as np

from dfh.itens.penteado.classificador import classificarPenteado

pontoDeCorteGlobal = 0.5
toleranciaGlobal = 0.05

class ResultadoItem:
	resultadoClassificacao = None #resultado emitido pelo pela ConvNet
	resultadoAvaliado = None #A para ausente, P para presente, I para indeterminado
	pesoItem = None # peso deste item para a composição na composição da escala
	escore = None # resultado final, quanto somar no escore final do desenho avaliado 

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
	results.penteado = avaliarPenteado(img)
	return results
	
def avaliarPenteado(img):
	penteado = ResultadoItem()
	penteado.resultadoClassificacao = classificarPenteado(img)
	penteado.resultadoAvaliado = avaliarResultado(penteado.resultadoClassificacao, pontoDeCorteGlobal, toleranciaGlobal)
	penteado.pesoItem = 3
	
	if(penteado.resultadoAvaliado == 'A'):
		penteado.escore = penteado.pesoItem
	else:
		penteado.escore = 0
		
	return penteado

def prepararImagem(path):
	img = cv2.imread(path)
	img = cv2.resize(img,(299,299))
	img = np.reshape(img,[1,299,299,3])
	return img
		
def avaliarResultado(result, pontoDeCorte, tolerancia):
	if(result >= pontoDeCorte + tolerancia):
		return 'P'
	elif(result <= pontoDeCorte - tolerancia):
		return 'A'
	else:
		return 'I'
	
	
