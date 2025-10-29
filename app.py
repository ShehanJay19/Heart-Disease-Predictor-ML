from flask import Flask,render_template,request
import joblib
import numpy as np

model=joblib.load('heart_risk_prediction_regression_model.sav')

app(Flask(__name__))

@app.route('/')
def index():

    return render_template('index.html')


@app.route('/predict',methods=['POST'])
def predict():
    
    result=request.form
    
    name