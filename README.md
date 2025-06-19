# 📈 Trabajo Práctico - Aprendizaje Automático: Predicción del Valor de Bitcoin

Este proyecto fue realizado para la materia **Aprendizaje Automático** y consiste en el desarrollo de un modelo de machine learning capaz de predecir el comportamiento del valor del Bitcoin (BTC) a partir de datos históricos.

## 🎯 Objetivo

Diseñar y evaluar un modelo de clasificación que prediga si el precio de Bitcoin subirá o bajará al día siguiente, basándose en características extraídas del comportamiento histórico de la criptomoneda.

## 📁 Estructura del repositorio

- `TA061_TP_GRUPO14.ipynb`: notebook principal con el análisis exploratorio, selección de variables, entrenamiento y evaluación del modelo.
- `Pruebas.ipynb`: pruebas complementarias y análisis adicionales.
- `Predecir.py`: script de uso práctico que permite realizar predicciones usando el modelo entrenado.
- `datasets/BTC.csv`: dataset con precios históricos de BTC utilizado para entrenar y validar el modelo.
- `modelos/modelo_svc.pkl`: modelo entrenado con `Support Vector Classifier` guardado con `pickle`.

## 🧪 Tecnologías y Herramientas utilizadas

- Python 3
- Pandas, NumPy
- Scikit-learn
- Matplotlib, Seaborn
- Pickle
- Jupyter Notebooks

## ✅ Metodología

1. **Análisis exploratorio de datos**: visualización de tendencias, medias móviles, y volatilidad.
2. **Transformación de variables**: ingeniería de características derivadas del precio.
3. **Entrenamiento del modelo**: se utilizó un **Support Vector Classifier (SVC)**.
4. **Evaluación**: análisis de métricas de precisión, recall y matriz de confusión.
5. **Pruebas adicionales**: se exploraron distintas configuraciones y umbrales de decisión.

## 🧠 Conclusiones

- El modelo logró capturar patrones en el comportamiento del BTC, aunque la naturaleza volátil de las criptomonedas representa un gran desafío para modelos supervisados.
- Se destaca la importancia de una buena selección de features y del preprocesamiento para mejorar el rendimiento.

## 👨‍🏫 Modalidad Académica

Este trabajo fue realizado en grupo como parte de la materia **Aprendizaje Automático** y tiene fines exclusivamente académicos.

---

