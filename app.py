import os
from flask import Flask, request, redirect, url_for, send_from_directory, jsonify, make_response
from werkzeug.utils import secure_filename

import cv2
import numpy as np
import jsonpickle

from dfh.ecdfhf912 import *

UPLOAD_FOLDER = './upload'
ALLOWED_EXTENSIONS = set(['bmp', 'png', 'jpg', 'jpeg'])

app = Flask(__name__)
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER

@app.route('/uploads/<filename>')
def uploaded_file(filename):
    return send_from_directory(app.config['UPLOAD_FOLDER'], filename)

@app.route('/ec-dfh-f-9-12', methods=['POST'])
def avaliar_ec_dfh_f_9_12():

	validacaoResult = validarRequest(request)
	if(validacaoResult != None):
		return validacaoResult

	path = uploadFile(getFileFromRequest(request))
	result = classificarEcDfhF912(path)
	return prepareSuccessResponse(result)
	
	
	
		
def getFileFromRequest(request):
	return request.files['file']
	
def parseResultToJson(result):
	responseJson = jsonpickle.encode(result, unpicklable=False)
	return responseJson
	
def prepareSuccessResponse(body):
	resp = make_response(parseResultToJson(body), 200)
	resp.headers['content-type'] = 'application/json'
	return resp
		
def validarRequest(request):
	if 'file' not in request.files:
		return fileNotFoundResponse()
		
	file = getFileFromRequest(request)
	if file.filename == '':
		return fileNotFoundResponse()
	
	if file and allowed_file(file.filename):
		return None
	else:
		return wrongFileFormatResponse()
	

def uploadFile(file):
	filename = secure_filename(file.filename)
	file.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))
	path = os.path.join(app.config['UPLOAD_FOLDER'], filename)
	return path
		
def fileNotFoundResponse():
	messageFileNotFound = jsonify({'message' : 'Nenhum arquivo encontrado.'})
	return (messageFileNotFound, 409, [])

def wrongFileFormatResponse():
	messageWrongFileFormat = jsonify({'message' : 'Formato de arquivo não suportado.'})
	return (messageWrongFileFormat, 409, [])
		
def allowed_file(filename):
    return '.' in filename and \
           filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS

app.run(host='0.0.0.0', debug=True)
#app.run(debug=True)
#app.run()