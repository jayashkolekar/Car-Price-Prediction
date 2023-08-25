import json

from flask import Flask, render_template, request
import pandas as pd
import pickle
app = Flask(__name__)

car_model = pickle.load(open('CarModel.pkl', 'rb'))

carDataset = pd.read_csv("cleaned_car_data.csv")
carCompanies = list(carDataset['name'])
carModels = list(carDataset['company'].unique())

@app.route("/")
def home():
    return render_template('index.html')


@app.route("/prediction", methods=['GET', 'POST'])
def prediction():
    if request.method=='POST':
        company = request.form.get('company')
        model = str(request.form.get('model')).replace('"', '')
        year = request.form.get('year')
        fueltype = request.form.get('fueltype')
        driven = request.form.get('driven')

        predicted_value = car_model.predict(pd.DataFrame([[model, company, year, driven, fueltype]],
                                  columns=['name', 'company', 'year', 'kms_driven', 'fuel_type']))
        print(company, model, year, fueltype, driven)
        return render_template('prediction.html', prediction_price=f"Predicted Price is ₹{round(predicted_value[0], 2)}", carCompanies=json.dumps(carCompanies), carModels=json.dumps(carModels), companies=carModels, models=carCompanies)
    return render_template('prediction.html', prediction_price="", carCompanies=json.dumps(carCompanies), carModels=json.dumps(carModels), companies=carModels, models=carCompanies)


@app.route('/about')
def about():
    return render_template("about.html")

@app.route("/contact")
def contact():
    return render_template("contact.html")

if __name__ == '__main__':
    app.run(debug=True)