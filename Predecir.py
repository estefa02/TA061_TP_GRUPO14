import pandas as pd
import pickle

#Cargamos el modelo
with open('/home/estefano/Escritorio/FIUBA/Ap. automatico/TP/modelos/modelo_svc.pkl', 'rb') as archivo:
    model = pickle.load(archivo)

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