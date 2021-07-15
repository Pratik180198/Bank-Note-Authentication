# -*- coding: utf-8 -*-
"""
Created on Mon Jul 12 12:46:09 2021

@author: Pratik
"""

from flask import Flask,request
import pandas as pd
import pickle
from flasgger import Swagger

app=Flask(__name__)
Swagger(app)
model=open('svc.pkl','rb')
classifier=pickle.load(model)
scale=open('Scaler.pkl','rb')
scaler=pickle.load(scale)

@app.route('/')
def welcome():
    return 'Welcome'

@app.route('/predict')
def predict():

    """Authenticate the Bank Note
    Data were extracted from images that were taken from genuine and forged banknote-like specimens. For digitization, an industrial camera usually used for print inspection was used. The final images have 400x 400 pixels. Due to the object lens and distance to the investigated object gray-scale pictures with a resolution of about 660 dpi were gained. Wavelet Transform tool were used to extract features from images.
    ---
    parameters:
        - name: variance
          in: query
          type: number
          required : true
        - name: skewness
          in: query
          type: number
          required : true
        - name: curtosis
          in: query
          type: number
          required : true
        - name: entropy
          in: query
          type: number
          required : true

    responses:
        200:
            description: True.
    """
    variance=request.args.get('variance')
    skewness=request.args.get('skewness')
    curtosis=request.args.get('curtosis')
    entropy=request.args.get('entropy')
    scaling=scaler.transform([[variance,skewness,curtosis,entropy]])
    prediction=classifier.predict(scaling)
    if prediction[0] == 0:
        return 'It is an Authentic Note'
    else:
        return "It is a fake note"

@app.route('/note',methods=['POST'])
def files():
    """ Authenticate the Bank Note with uploading csv file
    ---
    parameters:
        - name: fnm
          in: formData
          type: file
          required: true
    responses:
        200:
            description: True

    """
    fn=pd.read_csv(request.files.get('fnm'))
    scaling = scaler.transform(fn)
    prediction = classifier.predict(scaling)
    return 'Predictions'+ str(list(prediction))

if __name__ == '__main__':
    app.run(host='0.0.0.0',port=5000)
