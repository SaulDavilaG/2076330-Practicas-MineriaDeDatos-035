import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

#data = data[data['Genre'] != 'sportsandfitness']
#data = data[data['Genre'] != 'anime'
#print(data.iloc[2375:2385])
#print(np.random.rand(1))

data = pd.read_csv("../Proyectomineria/recogiendo_tomates_2.csv")  # Asegúrate de especificar la ubicación de tu archivo CSV
data = data[data['Title'] != 'Bunt. Delo Litvinenko (Poisoned By Polonium: The Litvinenko File) (Rebellion: The Litvinenko Case)']
promedioDuracion = int(data['Runtime'].mean(skipna=True))
data['Runtime'] = data['Runtime'].replace(np.NaN, promedioDuracion)
promedioTomatometer = int(data['TomatometerScore'].mean(skipna=True))
data['TomatometerScore'] = data['TomatometerScore'].replace(np.NaN, promedioTomatometer)
data['Nearest Centroid']='nada'
data['Distance']=0

def obtener_min_max(df):
    x_menor = y_menor = float('inf')
    x_mayor = y_mayor = float('-inf')
    
    x_menor = df['Runtime'].min()
    y_menor = df['TomatometerScore'].min()
    
    x_mayor = df['Runtime'].max()
    y_mayor = df['TomatometerScore'].max()

    #print(x_menor, "," , y_menor)
    #print(x_mayor, "," , y_mayor)
    return ((x_menor, y_menor),(x_mayor,y_mayor)) #Lista de listas, x(0)(0) llama al elemento en x menor

def calcular_centroides(menor, mayor):
    return menor + (mayor - menor) * np.random.rand(1)

def inicializar_centroides(df, k):
    x = obtener_min_max(df)

    centroides = []
    for i in range(k):
        x1 = float(calcular_centroides(x[0][0], x[1][0])) # [0][0]=x_min, [0][1]=y_min
        x2 = float(calcular_centroides(x[0][1], x[1][1])) # [1][0]=x_max, [1][1])=y_max
        centroides.append([x1, x2])
    # centroides = [[172.4844694179541, 66.67592355890987], [98.50260033305285, 85.9973172956993], [48.47951913986416, 68.04147286136384]]
    # Ejemplo que me sirvió para arreglar errores
    return centroides

def distancia_euclidiana(punto1, punto2):
    punto1 = np.array(punto1)  # Convierte las tuplas en arrays NumPy
    punto2 = np.array(punto2)
    return np.sqrt(np.sum((punto1 - punto2) ** 2))

def centroide_mas_cercano(dfaux, centroides):
    for index, row in dfaux.iterrows():
        punto_x = row['Runtime']
        punto_y = row['TomatometerScore']
        distancia_minima = float('inf')
        centroide_mas_cercano = 0
        for i, centroid in enumerate(centroides):
            distancia = distancia_euclidiana(centroid, (punto_x,punto_y))
            if(distancia<distancia_minima):
                distancia_minima=distancia
                centroide_mas_cercano = i
        dfaux.loc[index, 'NearestCentroid'] = centroide_mas_cercano # Centroide: 0=grupo 1, 1=grupo2, 2=grupo3...
        dfaux.loc[index, 'Distance'] = distancia_minima
    return dfaux

def imprimir_graficas(data, centroides, iteracion, colors):
    plt.figure(figsize=(10, 6))

    for i, centroid in enumerate(unique_centroids):
        subset = data[data['NearestCentroid'] == centroid]
        plt.scatter(subset['Runtime'], subset['TomatometerScore'], label=f'Grupo{int(centroid)}', color=colors[i], alpha=0.5, s=5)

    for i, centroide in enumerate(centroides):
        x, y = centroide
        plt.scatter(x, y, marker='x', color="black", s=100)

    plt.title('Gráfica de Dispersión: Runtime vs. TomatometerScore')
    plt.xlabel('Runtime')
    plt.ylabel('TomatometerScore')
    plt.title(f'Grafica {iteracion} k_means')
    plt.savefig('../Proyectomineria/Practica8-DataClustering/'+f'Grafica {iteracion} k_means.png')
    plt.legend()

def nuevos_centroides(data):
    grouped = data.groupby('NearestCentroid')
    average_runtime = grouped['Runtime'].mean()
    average_tomatometer_score = grouped['TomatometerScore'].mean()

    result_df = pd.DataFrame({
        'Average_Runtime': average_runtime,
        'Average_TomatometerScore': average_tomatometer_score
    })
    return result_df

i=0
centroides = inicializar_centroides(data, 5) # En este caso, k se trabaja como 5 para tener 5 grupos
data = centroide_mas_cercano(data,centroides)
unique_centroids = data['NearestCentroid'].unique()
colors = plt.cm.viridis(np.linspace(0, 1, len(unique_centroids)))
imprimir_graficas(data, centroides, i, colors)
for i in range(16):
    if(i!=0): #aqui tuve un problemita con el primer ciclo para nombrar las figuras, entonces lo omití con este if
        centroides_actualizados = nuevos_centroides(data)
        centroides_actualizados = centroides_actualizados.reset_index()
        centroides_actualizados = centroides_actualizados.drop('NearestCentroid', axis=1)
        centroides_actualizados = centroides_actualizados.values
        data = centroide_mas_cercano(data, centroides_actualizados)
        imprimir_graficas(data, centroides_actualizados, i, colors)