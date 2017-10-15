from dfh.dfhBase import *
from dfh.itens.penteado.classificador import *
from dfh.itens.figurabaixa.classificador import *
from dfh.itens.adaptacaocabelo.classificador import *
from dfh.itens.bocacortada.classificador import *
from dfh.itens.dedosjuntos.classificador import *
from dfh.itens.dificuldadeintegracao.classificador import *
from dfh.itens.enfaseface.classificador import *
from dfh.itens.linhapesada.classificador import *
from dfh.itens.linhatremida.classificador import *
from dfh.itens.problemarepresentacaoroupa.classificador import *
from dfh.itens.transparencia.classificador import *

def classificarEcDfhF912(path):
	return classificarItens(prepararImagem(path))
		
def classificarItens(img):
	resultado = ResultadoDfh()
	resultado.itens = []
	resultado.itens.append(avaliarAdaptacaoCabelo(img))
	resultado.itens.append(avaliarBocaCortada(img))
	resultado.itens.append(avaliarDedosJuntos(img))
	resultado.itens.append(avaliarDificuldadeIntegracao(img))
	resultado.itens.append(avaliarEnfaseFace(img))
	resultado.itens.append(avaliarFiguraBaixa(img))
	resultado.itens.append(avaliarLinhaPesada(img))
	resultado.itens.append(avaliarLinhaTremida(img))
	resultado.itens.append(avaliarPenteado(img))
	resultado.itens.append(avaliarProblemasRepresentacaoRoupa(img))
	resultado.itens.append(avaliarTransparencia(img))
	return resultado
	
def avaliarAdaptacaoCabelo(img):
	return avaliarResultadoItem(adaptacaoCabeloLabel, classificarAdaptacaoCabelo(img), 3, 'A');
	
def avaliarBocaCortada(img):
	return avaliarResultadoItem(bocaCortadaLabel, classificarBocaCortada(img), 3, 'P');
	
def avaliarDedosJuntos(img):
	return avaliarResultadoItem(dedosJuntosLabel, classificarDedosJuntos(img), 2, 'P');

def avaliarDificuldadeIntegracao(img):
	return avaliarResultadoItem(dificuldadeIntegracaoLabel, classificarDificuldadeIntegracao(img), 1, 'P');
	
def avaliarEnfaseFace(img):
	return avaliarResultadoItem(enfaseFaceLabel, classificarEnfaseFace(img), 1, 'P');

def avaliarFiguraBaixa(img):
	return avaliarResultadoItem(figuraBaixaLabel, classificarFiguraBaixa(img), 1, 'P');
	
def avaliarLinhaPesada(img):
	return avaliarResultadoItem(linhaPesadaLabel, classificarLinhaPesada(img), 1, 'P');
	
def avaliarLinhaTremida(img):
	return avaliarResultadoItem(linhaTremidaLabel, classificarLinhaTremida(img), 3, 'P');
	
def avaliarPenteado(img):
	return avaliarResultadoItem(penteadoLabel, classificarPenteado(img), 3, 'A');
	
def avaliarProblemasRepresentacaoRoupa(img):
	return avaliarResultadoItem(problemaRepresentacaoRoupaLabel, classificarProblemaRepresentacaoRoupa(img), 1, 'P');
	
def avaliarTransparencia(img):
	return avaliarResultadoItem(transparenciaLabel, classificarTransparencia(img), 2, 'P');


