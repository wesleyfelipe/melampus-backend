from keras.models import model_from_json
from keras.optimizers import Adam

def loadModel(pathModel, pathWeights):
	file = open(pathModel, 'r') 
	model = model_from_json(file.read())
	model.load_weights(pathWeights)
	adam = Adam(lr=0.0001)
	model.compile(loss='binary_crossentropy', optimizer=adam, metrics=['binary_accuracy'])
	return model