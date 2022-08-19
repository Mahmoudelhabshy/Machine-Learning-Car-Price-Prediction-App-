import pickle

import numpy as np
import pandas as pd
from flask import Flask, render_template, request

app=Flask(__name__)
cors=CORS(app)

model = pickle.load(open('LinearRegressionModel.pkl', 'rb'))
df = pd.read_csv('Cleaned Car.csv')

@app.route('/',methods=['GET','POST'])
def index():
    companies = sorted(df['Company'].unique())
    car_models = sorted(df['Name'].unique())
    year = sorted(df['year'].unique(),reverse=True)
    fuel_type = df['fuel_type'].unique()
    return render_template('index2.html',companies=companies, car_models=car_models, years=year, fuel_type=fuel_type)


@app.route('/predict', methods=['POST'])
def predict():
    company = request.form.get('company')
    car_model = request.form.get('car_model')
    year = request.form.get('year')
    fuel_type = request.form.get('fuel_type')
    kms_driven = int(request.form.get('kilo_driven'))
    print(company, car_model, year, fuel_type, kms_driven)

    prediction = model.prdict(pd.DataFrame([[car_model, company, year, kms_driven, fuel_type]], columns=['name',
    'company', 'year', 'kms_driven', 'fuel_type']).reshape(1, 5))


    return str(np.roundprediction[0],2)


if __name__=='__main__':
    app.run(debug=True)