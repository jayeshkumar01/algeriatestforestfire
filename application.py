from flask import Flask, jsonify ,request,render_template

import pandas as pd
import numpy as np
import pickle 
import sklearn
from sklearn.preprocessing import StandardScaler
application=Flask(__name__)
app=application
#import ridge pickle model
ridge_model=pickle.load(open('ridge.pkl','rb'))
standard_scalar=pickle.load(open('scaler.pkl','rb'))
@app .route('/')
def home():
    return render_template("index.html")
@app.route("/predictdata",methods=["GET","POST"])
def predict_data():
    if request.method=="POST":
         Temperature = float(request.form.get('Temperature'))
         RH = float(request.form.get('RH'))
         Ws = float(request.form.get('Ws'))
         Rain = float(request.form.get('Rain'))
         FFMC = float(request.form.get('FFMC'))
         DMC = float(request.form.get('DMC'))
         ISI = float(request.form.get('ISI'))
         Classes = float(request.form.get('Classes'))
         Region = float(request.form.get('Region'))
         newdata=standard_scalar.transform([[Temperature,RH,Ws,Rain,FFMC,DMC,ISI,Classes,Region]])
         result=ridge_model.predict(newdata)
         return render_template("predict.html",result=result[0])
    else:

        return render_template("predict.html")
    
if __name__=="__main__":
    app.run(debug=True)