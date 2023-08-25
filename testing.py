import json
import pandas as pd
from flask import Flask, render_template


app = Flask(__name__)
carDataset = pd.read_csv("cleaned_car_data.csv")
carCompanies = list(carDataset['name'])
carModels = list(carDataset['company'])


@app.route('/')
def home():
    return render_template('testing.html', carCompanies=json.dumps(carCompanies), carModels=json.dumps(carModels))


print(carCompanies)
print(carModels)

if __name__ == '__main__':
    app.run(debug=True, port=2000)