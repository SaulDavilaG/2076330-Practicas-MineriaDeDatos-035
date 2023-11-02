import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import statistics
import math

# Carga tu dataset de películas
data = pd.read_csv("../Proyectomineria/recogiendo_tomates_2.csv")  # Asegúrate de especificar la ubicación de tu archivo CSV

#Elimino del dataset aquellas peliculas de los siguientes géneros para tener unicamente 20 y utilizar
#la función plt.get_cmap
data = data[data['Genre'] != 'sportsandfitness']
data = data[data['Genre'] != 'anime']

k = round(math.sqrt(len(data)))

# Cálculo del promedio para rellenar espacios vacíos (irrelevante para esta clasificacion)
mean = int(data['AudienceScore'].mean(skipna=True))
data['AudienceScore'] = data['AudienceScore'].replace(np.NaN, mean)

color_mapping = {
    'action': 'red',
    'adventure': 'orange',
    'animation': 'yellow',
    'biography': 'green',
    'comedy': 'lightblue',
    'crime': 'darkblue',
    'documentary': 'gray',
    'drama': 'purple',
    'fantasy': 'pink',
    'history': 'brown',
    'horror': 'darkred',
    'kidsandfamily': 'lightgreen',
    'music': 'lightpink',
    'musical': 'violet',
    'mysteryandthriller': 'darkgreen',
    'other': 'lightgray',
    'romance': 'pink',
    'scifi': 'blue',
    'war': 'darkgray',
    'western': 'sienna'
}

# Crear un DataFrame solo con las características
X = data[['TomatometerScore', 'Runtime','Genre']]

# Función para calcular la distancia euclidiana entre dos puntos
def euclidean_distance(punto1, punto2):
    punto1 = np.array(punto1)  # Convierte las tuplas en arrays NumPy
    punto2 = np.array(punto2)
    return np.sqrt(np.sum((punto1 - punto2) ** 2))

def k_nearest_neighbour(punto, dfaux):
    dfaux['Distance']=0
    for index, row in dfaux.iterrows():
        dfaux.at[index, 'Distance'] = round(euclidean_distance(punto,(row['TomatometerScore'],row['Runtime'])),4)
    arr = np.array(dfaux['Distance']) # Guarda en un arreglo las distancias calculadas con la función euclidean_distance
    indArrOrdenado = np.argsort(arr) # Guarda los índices del arreglo ordenado (de menor a mayor) antes de ordenarlo
    primeros_tres_indices = indArrOrdenado[:k]
    filas_seleccionadas = dfaux.iloc[primeros_tres_indices]
    clasificaciones_filas_seleccionadas = filas_seleccionadas['Genre']
    print(filas_seleccionadas)
    moda = statistics.mode(clasificaciones_filas_seleccionadas)
    return moda

# Crear una gráfica de dispersión con las predicciones de K-NN
plt.figure(figsize=(8, 6))
for clasificacion in color_mapping:
    subset = data[data['Genre'] == clasificacion]
    plt.scatter(subset['Runtime'], subset['TomatometerScore'], c=color_mapping[clasificacion], label=clasificacion, alpha=0.5, s=5)

punto_x= 50
punto_y= 90
genero= k_nearest_neighbour((punto_x,punto_y), X)

plt.scatter(punto_x,punto_y, marker='x', c='black', label= f'Punto Nuevo ({genero})', s=100)

# Etiquetas de ejes
plt.xlabel('Runtime')
plt.ylabel('TomatometerScore')

# Leyenda
plt.legend()

# Título
plt.title('Gráfica de Dispersión de TomatometerScore vs. Runtime con Clasificación K-NN')

# Mostrar la gráfica
plt.savefig('../Proyectomineria/Practica7-DataClassification/'+'k_nearest_neighbour_por_categorias.png')
