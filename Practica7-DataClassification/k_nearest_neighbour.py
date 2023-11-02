import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import statistics

# Carga tu dataset de películas
data = pd.read_csv("../Proyectomineria/recogiendo_tomates_2.csv")  # Asegúrate de especificar la ubicación de tu archivo CSV

# Cálculo del promedio para rellenar espacios vacíos
mean = int(data['AudienceScore'].mean(skipna=True))
data['AudienceScore'] = data['AudienceScore'].replace(np.NaN, mean)

# Se crea una nueva columna 'Quality'. Por defecto, todas las películas con calidad buena
data['Quality'] = 'Buena'

# A cada fila se le asigna una clasificación de acuerdo al promedio de su puntuación de la audiencia y de Tomatometer
data.loc[((data['TomatometerScore'] + data['AudienceScore']) / 2 < 70), 'Quality'] = 'Regular'
data.loc[((data['TomatometerScore'] + data['AudienceScore']) / 2 < 50), 'Quality'] = 'Mala'

color_mapping = {"Buena": "green", "Regular": "blue", "Mala": "red"}

# Crear un DataFrame solo con las características
X = data[['TomatometerScore', 'AudienceScore','Quality']]

# Función para calcular la distancia euclidiana entre dos puntos
def euclidean_distance(punto1, punto2):
    punto1 = np.array(punto1)  # Convierte las tuplas en arrays NumPy
    punto2 = np.array(punto2)
    return np.sqrt(np.sum((punto1 - punto2) ** 2))

def k_nearest_neighbour(punto, dfaux):
    dfaux['Distance']=0
    for index, row in dfaux.iterrows():
        dfaux.at[index, 'Distance'] = round(euclidean_distance(punto,(row['TomatometerScore'],row['AudienceScore'])),4)
    arr = np.array(dfaux['Distance']) # Guarda en un arreglo las distancias calculadas con la función euclidean_distance
    indArrOrdenado = np.argsort(arr) # Guarda los índices del arreglo ordenado (de menor a mayor) antes de ordenarlo
    primeros_tres_indices = indArrOrdenado[:3]
    filas_seleccionadas = dfaux.iloc[primeros_tres_indices]
    clasificaciones_filas_seleccionadas = filas_seleccionadas['Quality']
    moda = statistics.mode(clasificaciones_filas_seleccionadas)
    return moda

# Crear una gráfica de dispersión con las predicciones de K-NN
plt.figure(figsize=(8, 6))
for clasificacion in color_mapping:
    subset = data[data['Quality'] == clasificacion]
    plt.scatter(subset['TomatometerScore'], subset['AudienceScore'], c=color_mapping[clasificacion], label=clasificacion, alpha=0.5, s=10)

punto_x=20
punto_y=50
genero= k_nearest_neighbour((punto_x,punto_y), X)

plt.scatter(punto_x,punto_y, marker='x', c='black', label= f'Punto Nuevo ({genero})', s=100)

# Etiquetas de ejes
plt.xlabel('TomatometerScore')
plt.ylabel('AudienceScore')

# Leyenda
plt.legend()

# Título
plt.title('Gráfica de Dispersión TomatometerScore vs. AudienceScore KNN')

# Guardar la gráfica
plt.savefig('../Proyectomineria/Practica7-DataClassification/'+'k_nearest_neighbour_1.png')
