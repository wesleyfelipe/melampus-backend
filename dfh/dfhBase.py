import cv2
import numpy as np

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
	
def avaliarResultadoItem(resultadoClassificacao, pesoItem, somarEscoreQuando):
	item = ResultadoItem()
	item.pesoItem = pesoItem
	item.resultadoClassificacao = resultadoClassificacao
	item.resultadoAvaliado = avaliarResultado(resultadoClassificacao, pontoDeCorteGlobal, toleranciaGlobal)
		
	if(item.resultadoAvaliado == somarEscoreQuando):
		item.escore = item.pesoItem
	else:
		item.escore = 0
		
	return item
	
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