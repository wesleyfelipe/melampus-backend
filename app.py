import os
from flask import Flask, request, redirect, url_for, send_from_directory, jsonify
from werkzeug.utils import secure_filename

#from keras.models import model_from_json
import cv2
import numpy as np

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
	messageFileNotFound = jsonify({'message' : 'Nenhum arquivo encontrado.'})
	messageWrongFileFormat = jsonify({'message' : 'Formato de arquivo não suportado.'})

	if 'file' not in request.files:
		return messageFileNotFound
		
	file = request.files['file']
	if file.filename == '':
		return messageFileNotFound
		
	if file and allowed_file(file.filename):
		filename = secure_filename(file.filename)
		file.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))
		path = os.path.join(app.config['UPLOAD_FOLDER'], filename)
		return jsonify(classificarEcDfhF912(path).__dict__)
	else:
		return messageWrongFileFormat

def allowed_file(filename):
    return '.' in filename and \
           filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS
							   
app.run(debug=True)