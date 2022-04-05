import json
from core import FileClassifier
from flask import Flask, flash, request, redirect, url_for
app = Flask(__name__)

@app.route('/')
def welcome():
    return 'File Classifier API'

@app.route('/upload', methods=['POST'])
def upload_file():
    f = request.files['file']
    fc = FileClassifier(f,2)
    print(fc.classify())
    return 'hi'

if __name__ == '__main__':
    app.debug = True
    app.run(host= '0.0.0.0', port=5000, threaded=True)