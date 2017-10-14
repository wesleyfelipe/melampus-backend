from dfh.dfhBase import ResultadoItem, ResultadoDfh, prepararImagem, avaliarResultado, avaliarResultadoItem
from dfh.itens.penteado.classificador import classificarPenteado
from dfh.itens.figurabaixa.classificador import classificarFiguraBaixa

def classificarEcDfhF912(path):
	return classificarItens(prepararImagem(path))
		
def classificarItens(img):
	resultado = ResultadoDfh()
	resultado.itens = []
	resultado.itens.append(avaliarPenteado(img))
	return resultado
	
def avaliarPenteado(img):
	return avaliarResultadoItem(classificarPenteado(img), 3, 'A');

