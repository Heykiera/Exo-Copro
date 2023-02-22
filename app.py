from flask import Flask, request, render_template
import requests
import pandas as pd
import json
from statistics import mean 

data = pd.read_csv('./dataset_annonces.csv')

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')


@app.route('/exo', methods=['GET','POST'])
def stats():
    print("on est la")
    # Get the type of localisation
    type_loc = request.form.get('type_loc')
    print(type_loc)
    # Get the location from the form data
    location = request.form.get('localisation')
    print(location)
    # Search panda by type charges de copropriétés moyennes, les quantiles 10%, 90%  sur un département, une ville ou code postal
    try:
        result = data.query(f'{type_loc} == {str(location)} and CONDOMINIUM_EXPENSES > 0')
        print(result[['DEPT_CODE','ZIP_CODE','CITY','CONDOMINIUM_EXPENSES']])
        try:
            avg = mean(result['CONDOMINIUM_EXPENSES']) 
            ChargesCopro = f'Charge de copropriétées moyennes a/au {str(location)} sont de ' + str(round(avg,2)) + '€'
            print(ChargesCopro)
        except:
            ChargesCopro = f'An exception occurred for {str(location)}'
            print(ChargesCopro) 
    except:
        ChargesCopro = 'test'
    # Get url
    bienici_url = request.form.get('ad_url')
    # Split the URL at the last / character, and then split the second part at the ? character.
    path_id, bienici = bienici_url.rsplit('/', 1)[-1].split('?')
    print('https://www.bienici.com/realEstateAd.json?id=' + path_id)
    df = pd.read_json('https://www.bienici.com/realEstateAd.json?id=' + path_id)
    print(df)
    try:
        df.to_csv()
    except:
        print('no url bienivi.com')

    # Return the statistics
    return render_template('index.html', type_loc = type_loc ,location = location, bienici_url = bienici_url, ChargesCopro = ChargesCopro)

# AD_URLS,PROPERTY_TYPE,DEPT_CODE,ZIP_CODE,CITY, PRICE