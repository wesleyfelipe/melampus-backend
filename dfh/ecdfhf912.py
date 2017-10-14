from dfh.dfhBase import ResultadoItem, EcDfhF912Results, prepararImagem, avaliarResultado, avaliarResultadoItem
from dfh.itens.penteado.classificador import classificarPenteado

def classificarEcDfhF912(path):
	return classificarItens(prepararImagem(path))
		
def classificarItens(img):
	results = EcDfhF912Results()
	results.penteado = avaliarPenteado(img)
	return results
	
def avaliarPenteado(img):
	return avaliarResultadoItem(classificarPenteado(img), 3, 'A');

