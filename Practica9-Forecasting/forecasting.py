import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

# Leer el dataset de películas (asegúrate de tener un archivo CSV válido)
data = pd.read_csv('tu_archivo.csv')

# Seleccionar las columnas de interés
X = data['Runtime'].values
y = data['TomatometerScore'].values

# Calcular las medias de X y y
mean_x = np.mean(X)
mean_y = np.mean(y)

# Calcular los coeficientes de la regresión
numerator = 0
denominator = 0
n = len(X)

for i in range(n):
    numerator += (X[i] - mean_x) * (y[i] - mean_y)
    denominator += (X[i] - mean_x) ** 2

b1 = numerator / denominator
b0 = mean_y - (b1 * mean_x)

# Imprimir los coeficientes
print(f'Coeficiente b1 (pendiente): {b1}')
print(f'Coeficiente b0 (intersección): {b0}')

# Realizar predicciones
y_pred = b0 + b1 * X

# Graficar las predicciones
plt.scatter(X, y, color='blue', label='Datos reales')
plt.plot(X, y_pred, color='red', label='Predicciones')
plt.xlabel('Runtime')
plt.ylabel('TomatometerScore')
plt.legend()
plt.show()

# Calcular el coeficiente de determinación R^2
ssr = 0
sst = 0

for i in range(n):
    y_pred_i = b0 + b1 * X[i]
    ssr += (y[i] - y_pred_i) ** 2
    sst += (y[i] - mean_y) ** 2

r2 = 1 - (ssr / sst)
print(f"Coeficiente de determinación R^2: {r2}")

# Hacer predicciones para nuevas películas
new_runtimes = np.array([120, 140])  # Ejemplos de duración de películas en minutos
predicted_scores = b0 + b1 * new_runtimes
print(f"Pronóstico de calificaciones para nuevas películas: {predicted_scores}")
