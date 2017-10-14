import cv2
import numpy as np

pontoDeCorteGlobal = 0.5
toleranciaGlobal = 0.05

dedosJuntosLabel = 'Dedos Juntos'
adaptacaoCabeloLabel = 'Adaptação do Cabelo'
bocaCortadaLabel = 'Boca Cortada'
penteadoLabel = 'Penteado'
figuraBaixaLabel = 'Figura Baixa'
dificuldadeIntegracaoLabel = 'Dificuldade Integracao'
enfaseFaceLabel = 'Ênfase da Face'
linhaPesadaLabel = 'Linha Pesada'
linhaTremidaLabel = 'Linha Tremida'
problemaRepresentacaoRoupaLabel = 'Problema de Representação de Roupa'
transparenciaLabel = 'Transparência'

class ResultadoItem:
	item = None
	resultadoClassificacao = None #resultado emitido pelo pela ConvNet
	resultadoAvaliado = None #A para ausente, P para presente, I para indeterminado
	pesoItem = None # peso deste item para a composição na composição da escala
	escore = None # resultado final, quanto somar no escore final do desenho avaliado 

class ResultadoDfh:
	itens = None
	escoreFinal = None
	
def avaliarResultadoItem(nomeItem, resultadoClassificacao, pesoItem, somarEscoreQuando):
	item = ResultadoItem()
	item.item = nomeItem
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