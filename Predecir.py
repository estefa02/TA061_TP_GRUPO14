import numpy as np
import pandas as pd
from sklearn.preprocessing import StandardScaler
from tensorflow.keras.models import load_model

#Cargamos el modelo
model = load_model('modelo_criptomonedas.h5')

def predecir_btc(date,open,high,low,close):

    datos_hoy = pd.DataFrame({
        'date': [date],
        'open': [open],
        'high': [high],
        'low':  [low],
        'close': [close]
    })

    datos_hoy = preprocesar(datos_hoy)

    prediccion = model.predict(datos_hoy)

    if prediccion == 1:
        print("Predicción: El precio subirá mañana.")
    else:
        print("Predicción: El precio bajará mañana.")
    return

def preprocesar(data):
    data['mean_day'] = data[['open', 'high', 'low', 'close']].mean(axis=1) #agrega la media

    #Agregamos target
    data['date'] = pd.to_datetime(data['date'])
    data['target'] = (data['mean_day'] > data['mean_day'].shift(1)).astype(int)

    #Agregamos variacion
    data['daily_variation'] = (data['high'] - data['low']) / data['mean_day']
    umbral = 0.1
    data['variation_category'] = data['daily_variation'].apply(
        lambda x: 1 if x > umbral else 0
    )

    #Convertimos las fechas
    data['day_of_week'] = pd.to_datetime(data['date']).dt.dayofweek
    data['month'] = pd.to_datetime(data['date']).dt.month
    data['year'] = pd.to_datetime(data['date']).dt.year
    data = data.drop(columns=['date'])

    return data
    
