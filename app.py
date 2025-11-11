from flask import Flask,render_template,request
import joblib
import numpy as np

model=joblib.load('heart-risk-reg-model.sav')

app=(Flask(__name__))

@app.route('/')
def index():

    return render_template('index.html')


@app.route('/predict',methods=['POST'])
def predict():
    
    result=request.form
    
    name=result['name'] 
    gender=float(result['sex'])
    age=float(result['age'])
    tc=float(result['total_cholesterol'])
    hdl=float(result['HDL'])
    smoker=float(result['smoker'])
    bp_medicine=float(result['bp_medicine'])
    diabetic=float(result['diabetic'])
    
    test_data=np.array([gender,age,tc,hdl,smoker,bp_medicine,diabetic]).reshape(1,-1)
    
    prediction=model.predict(test_data)
    pred_arr = np.asarray(prediction).ravel()
    if pred_arr.size == 0:
        risk_value = float(prediction)
    else:
        risk_value = float(pred_arr[0])

    
    
    resultDict={"name":name,"risk":round(risk_value,2)}
    
    return render_template('result.html',result=resultDict)

app.run(debug=True,port=5001)