# -*- coding: utf-8 -*-
"""
Created on Wed Jul 15 19:55:37 2020

@author: goura
"""
import flask
from flask import request, jsonify

import tensorflow.keras as tf
import pickle
from tensorflow.keras.preprocessing.text import Tokenizer
from tensorflow.keras.preprocessing.sequence import pad_sequences

model=tf.models.load_model("Toxicity.h5")
with open("tokenizer.pickle","rb") as file:
    l=pickle.load(file)

app = flask.Flask(__name__)
app.config["DEBUG"] = True

# Create some test data for our catalog in the form of a list of dictionaries.


@app.route('/', methods=['GET'])
def home():
    return '''<h1>Distant Reading Archive</h1>
<p>A prototype API for toxic text detection</p>'''





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

app.run(host='0.0.0.0')