import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

# Función para calcular la distancia euclidiana entre dos puntos
def euclidean_distance(punto1, punto2):
    punto1 = np.array(punto1)  # Convierte las tuplas en arrays NumPy
    punto2 = np.array(punto2)
    return np.sqrt(np.sum((punto1 - punto2) ** 2))

distancia = euclidean_distance([1,2],[3,4])

def k_nearest_neighbour(dfaux, punto):
    dfaux['Distance']=0
    for index, row in dfaux.iterrows():
        dfaux.at[index, 'Distance'] = round(euclidean_distance(punto,(row['TomatometerScore'],row['AudienceScore'])),4)
    arr = np.array(dfaux['Distance']) # Guarda en un arreglo las distancias calculadas con la función euclidean_distance
    indArrOrdenado = np.argsort(arr) # Guarda los índices del arreglo ordenado (de menor a mayor) antes de ordenarlo
    primeros_tres_indices = indArrOrdenado[:3]
    filas_seleccionadas = dfaux.iloc[primeros_tres_indices]
    print(filas_seleccionadas)


    # print(dfaux.at[indArrOrdenado[0],'TomatometerScore']) Hacer lo anterior ejecutará el 'TomatometerScore' del valor con menos distancia al punto dado

data = {
    'TomatometerScore': [80, 60, 90, 70],
    'AudienceScore': [75, 55, 92, 68],
    'Quality': ["Buena","Mala","Buena","Regular"]
}

df = pd.DataFrame(data)
k_nearest_neighbour(df, [60,80])
