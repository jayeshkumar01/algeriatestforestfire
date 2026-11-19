from flask import Flask, request, render_template
import pickle

application = Flask(__name__)
app = application

# FWI regression model (RidgeCV) + its scaler (9 features, incl. Classes + Region)
ridge_model = pickle.load(open('ridge.pkl', 'rb'))
standard_scalar = pickle.load(open('scaler.pkl', 'rb'))

# Fire / not-fire classifier (Decision Tree, max_depth=3, 5-fold CV)
# + its scaler (10 features: incl. DC, BUI. NO Classes, because Classes is the target)
fire_model = pickle.load(open('decisioncv.pkl', 'rb'))
fire_scalar = pickle.load(open('classification_scaler.pkl', 'rb'))


@app.route('/')
def home():
    return render_template("index.html")


@app.route("/predictdata", methods=["GET", "POST"])
def predict_data():
    if request.method == "POST":
        Temperature = float(request.form.get('Temperature'))
        RH = float(request.form.get('RH'))
        Ws = float(request.form.get('Ws'))
        Rain = float(request.form.get('Rain'))
        FFMC = float(request.form.get('FFMC'))
        DMC = float(request.form.get('DMC'))
        ISI = float(request.form.get('ISI'))
        Classes = float(request.form.get('Classes'))
        Region = float(request.form.get('Region'))
        newdata = standard_scalar.transform(
            [[Temperature, RH, Ws, Rain, FFMC, DMC, ISI, Classes, Region]])
        result = ridge_model.predict(newdata)
        return render_template("predict.html", result=round(float(result[0]), 2))
    else:
        return render_template("predict.html", result=None)


@app.route("/predictfire", methods=["GET", "POST"])
def predict_fire():
    if request.method == "POST":
        Temperature = float(request.form.get('Temperature'))
        RH = float(request.form.get('RH'))
        Ws = float(request.form.get('Ws'))
        Rain = float(request.form.get('Rain'))
        FFMC = float(request.form.get('FFMC'))
        DMC = float(request.form.get('DMC'))
        DC = float(request.form.get('DC'))
        ISI = float(request.form.get('ISI'))
        BUI = float(request.form.get('BUI'))
        Region = float(request.form.get('Region'))
        # 10 features, no Classes (it is what we are predicting)
        newdata = fire_scalar.transform(
            [[Temperature, RH, Ws, Rain, FFMC, DMC, DC, ISI, BUI, Region]])
        result = fire_model.predict(newdata)
        label = "Fire" if int(result[0]) == 1 else "Not fire"
        return render_template("predictfire.html", result=label)
    else:
        return render_template("predictfire.html", result=None)


if __name__ == "__main__":
    app.run(debug=True)