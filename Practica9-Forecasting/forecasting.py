import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv('../Proyectomineria/recogiendo_tomates_2.csv')
df = df.dropna(subset=['TomatometerScore', 'AudienceScore'])

X = df['TomatometerScore'].values
y = df['AudienceScore'].values

mean_X = np.mean(X)
mean_y = np.mean(y)

#Coeficientes de la regresión lineal
numerador = np.sum((X - mean_X) * (y - mean_y))
denominador = np.sum((X - mean_X)**2)

# Caso en que el denominador sea cero (evitar la indeterminación)
if denominador != 0:
    b1 = numerador / denominador
    b0 = mean_y - b1 * mean_X

    # Función de predicción
    def predict(x):
        return b0 + b1 * x

    # Predicciones
    predicted_y = predict(X)

    # Imprimir los coeficientes y la precisión
    print("Coeficiente b1:", b1)
    print("Coeficiente b0:", b0)

    # Por ejemplo, para predecir AudienceScore para un nuevo valor de TomatometerScore
    new_tomatometer_score = 75
    predicted_audience_score = predict(new_tomatometer_score)
    print(f"Predicción de AudienceScore para TomatometerScore {new_tomatometer_score}: {predicted_audience_score}")

    # Crear un rango de valores para TomatometerScore
    x_range = np.linspace(min(X), max(X), 100)

    # Calcular los valores predichos correspondientes a ese rango
    y_pred = b0 + b1 * x_range

    plt.figure(figsize=(10, 6))
    plt.scatter(X, y, label='Películas Puntuadas', color='black', s=10)
    plt.plot(x_range, y_pred, label='Línea de Regresión', color='red')

    # Etiquetas y título
    plt.xlabel('TomatometerScore')
    plt.ylabel('AudienceScore')
    plt.title('Regresión Lineal TomatometerScore vs AudienceScore')

    # Mostrar la leyenda
    plt.legend()

    # Mostrar la gráfica
    plt.show()
else:
    print("El denominador es cero, por lo que no se puede calcular la regresión lineal")