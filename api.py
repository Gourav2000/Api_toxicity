# -*- coding: utf-8 -*-
"""
Created on Wed Jul 15 19:55:37 2020

@author: goura
"""
from unittest import result
import flask
from flask import render_template, request, jsonify

import tensorflow.keras as tf
import pickle
from tensorflow.keras.preprocessing.text import Tokenizer
from tensorflow.keras.preprocessing.sequence import pad_sequences
from keras.models import load_model
from tensorflow.keras.applications.resnet50 import decode_predictions, preprocess_input
from keras import backend as K
import os
from tensorflow.keras.preprocessing import image
# from keras.utils import load_img, img_to_array
import tensorflow as tff
import numpy as np
from PIL import Image

model=tf.models.load_model("D:/doc/project-8-sem/Api_toxicity/Toxicity.h5")
with open("D:/doc/project-8-sem/Api_toxicity/tokenizer.pickle","rb") as file:
    l=pickle.load(file)

names = ['drugs','normal','pornographic','unpleasant visuals']
model_img=load_model('D:/doc/project-8-sem/Api_toxicity/image_classificationDR32.h5')

app = flask.Flask(__name__,template_folder="templates")
app.config["DEBUG"] = True

# Create some test data for our catalog in the form of a list of dictionaries.


@app.route('/', methods=['GET'])
def home():
    return render_template("main.html")





@app.route('/toxicity_check', methods=['GET'])
def api_id():
    
    if 'text' in request.args:
        text = str(request.args['text'])
    else:
        return "Error: No text field provided. Please specify a text feild to evaluate !!!."

    # Create an empty list for our results
    results = []
    z=dict()
    z['text']=text
    
    
    g=l.texts_to_sequences([text])
    g=pad_sequences(g,maxlen=120,padding="post",truncating="post")
    pred=model.predict(g)
    f=0
    Identity=0
    if pred[0][0]>0.5:
        f=1
    else:
        f=0
    if pred[0][-1]>0.35:
        Identity=1
    else:
        Identity=0
    if(f and not Identity):
        z['toxic']='yes'
    elif(f and Identity):
        z['toxic']='yes'
    else:
        z['toxic']='no'
        
    results.append(z)


    # Use the jsonify function from Flask to convert our list of
    # Python dictionaries to the JSON format.
    return jsonify(results)

@app.route('/toxicity_image_text', methods=['POST'])
def t_img():
    result_img=""
    result_text=""
    # print(request.files['toxic_image'])
    if request.files.__contains__('toxic_image') and request.files['toxic_image'].filename!='':
        uploaded_file_img = request.files['toxic_image'] 
        uploaded_file_img.save(uploaded_file_img.filename)
        img_path=uploaded_file_img.filename
        img = image.load_img(img_path,target_size=(224,224))
        x = image.img_to_array(img)
        x = np.expand_dims(x, axis=0)
        x = preprocess_input(x)
        predic = model.predict(x)
        value=np.argmax(predic)
        print('predictions is- {}\n'.format(names[value]))
        if value == 2:
            print("image under review warning")
        elif value == 1:
            im = Image.open(img_path)
            im.show()
        else :
            print("see with caution may contain violent or addictive content")
            im = Image.open(img_path)
            im.show()
            result_img=result
    if request.form.__contains__('tox_text') and request.form.get("tox_text")!='':
        text=request.form.get("tox_text")
        results = []
        z=dict()
        z['text']=text
        g=l.texts_to_sequences([text])
        g=pad_sequences(g,maxlen=120,padding="post",truncating="post")
        pred=model.predict(g)
        f=0
        Identity=0
        if pred[0][0]>0.5:
            f=1
        else:
            f=0
        if pred[0][-1]>0.35:
            Identity=1
        else:
            Identity=0
        if(f and not Identity):
            z['toxic']='yes'
            result_text="text given is toxic"
        elif(f and Identity):
            z['toxic']='yes'
            result_text="text given is toxic"
        else:
            z['toxic']='no'
            result_text="text given is not toxic"
        
    if result_img=='' and result_text=='':
        return 'no file uploaded and no text given'
    elif result_img=='':
        return result_text
    elif result_text=='':
        return result_img
    else:
        return result_img + '\n' + result_text
app.run()