import pandas as pd

def promedio_score_por_genero(input_file):
    # Aquí se lee el archivo CSV
    df = pd.read_csv(input_file)

    # Se agrupan los datos en 'df' por la columna 'Genre'
    # y se calcula el promedio de las columnas 'Tomatometer Score' y 'Audience Score'
    df_genero = df.groupby('Genre')[['Tomatometer Score', 'Audience Score']].mean().round(2)

    # Se imprime el dataframe resultante
    print("\n\nPromedio de puntuaciones por genero y tipo (sobre 100)")
    print(df_genero)

def conteo_peliculas_por_genero(input_file):
    # Aquí se lee el archivo CSV
    df = pd.read_csv(input_file)

    # Se agrupan los datos en 'df' por la columna 'Genre'
    # y se cuentan los registros de las columnas 'Tomatometer Score' y 'Audience Score'
    df_genero = df.groupby('Genre')[['Tomatometer Score', 'Audience Score']].count()

    # Se imprime el dataframe resultante
    print("\n\nConteo de puntuaciones por genero y tipo")
    print(df_genero)

def conteo_peliculas_por_clasificacion(input_file):
    # Aquí se lee el archivo CSV
    df = pd.read_csv(input_file)

    # Se agrupan los datos en 'df' por la columna 'Rating' y 'Genre'
    # y se cuentan los registros de las columnas 'Titulo'
    conteo_por_clasificacion = df.groupby(['Genre','Rating']).agg({'Title': ['count']})

    # Se imprime el dataframe resultante
    print("\n\nConteo de puntuaciones por genero y tipo de clasificacion")
    print(conteo_por_clasificacion.to_string())

def pelicula_mejor_y_peor_puntuada(input_file):
    # Aquí se lee el archivo CSV
    df = pd.read_csv(input_file)
    print('\n\nPelicula mejor puntuada por las criticas')

    # Aquí se busca mediante la función idxmax() el índice de la pelicula que tiene el menor score,
    # se busca con la función .loc('Aqui pasamos el indice') y se imprime 
    print(df.loc[df['Tomatometer Score'].idxmax()])
    print('\n\nPelicula peor puntuada por las criticas')

    # Se hace el mismo proceso de arriba, solo que se cambia .idxmax() por .idxmin()
    print(df.loc[df['Tomatometer Score'].idxmin()])
    print('\n\nPelicula mejor puntuada por la audiencia')

    # Los siguientes dos pasos son los dos mismos pasos de arriba, solo que se cambia 'Tomatometer Score' 
    # por 'Audience Score'
    print(df.loc[df['Audience Score'].idxmax()])
    print('\n\nPelicula peor puntuada por la audiencia')
    print(df.loc[df['Audience Score'].idxmin()])

def pelicula_mas_larga_y_mas_corta(input_file):
    # Aquí se lee el archivo CSV
    df = pd.read_csv(input_file)

    # Se elimina un registro que estaba causando problemas
    df = df[df['Title'] != 'Bunt. Delo Litvinenko (Poisoned By Polonium: The Litvinenko File) (Rebellion: The Litvinenko Case)']

    # Funcion para encontrar la película que dura más
    indice_max_duracion = df['Runtime'].idxmax()

    # Funcion para encontrar la película que dura menos
    indice_min_duracion = df['Runtime'].idxmin()

    # Acceso a los registros de las películas que duran más y menos
    pelicula_max_duracion = df.loc[indice_max_duracion]
    pelicula_min_duracion = df.loc[indice_min_duracion]

    # Impresión de la información de las películas
    print("\n\nPelícula que dura más:")
    print(pelicula_max_duracion)
    print("\n\nPelícula que dura menos:")
    print(pelicula_min_duracion)
    
def fechas_lanzamiento(input_file):
    # Aquí se lee el archivo CSV
    df = pd.read_csv(input_file)

    # Se elimina un registro que estaba causando problemas
    df = df[df['Title'] != 'Mope']
    df = df[df['Title'] != 'Bunt. Delo Litvinenko (Poisoned By Polonium: The Litvinenko File) (Rebellion: The Litvinenko Case)']

    # Las fechas que aparecen en la columna 'R. Date (Theaters)' se acomodan a un formato fecha
    df['R. Date (Theaters)'] = pd.to_datetime(df['R. Date (Theaters)'], format= '%d/%m/%Y')
    df['R. Date (Streaming)'] = pd.to_datetime(df['R. Date (Streaming)'], format= '%d/%m/%Y')

    # Se utilizan funciones de agregacion en la columna 'R. Date (Theaters)' 
    # para obtener la fecha más antigua y reciente dicha columna 
    peli_cine_min = df['R. Date (Theaters)'].min()
    peli_cine_max = df['R. Date (Theaters)'].max()

    # Se buscan en el dataframe los registros con base en las fechas que se arrojó
    # anteriormente (pueden coincidir varios valores)
    pelicula_Cines_Antigua = df[df['R. Date (Theaters)'] == peli_cine_min]
    pelicula_Cines_Reciente = df[df['R. Date (Theaters)'] == peli_cine_max]

    # Se utilizan funciones de agregacion en la columna 'R. Date (Streaming)' 
    # para obtener la fecha más antigua y reciente dicha columna 
    peli_streaming_min = df['R. Date (Streaming)'].min()
    peli_streaming_max = df['R. Date (Streaming)'].max()

    # Se buscan en el dataframe los registros con base en las fechas que se arrojó
    # anteriormente (pueden coincidir varios valores)    
    pelicula_streaming_Antigua = df[df['R. Date (Streaming)'] == peli_streaming_min]
    pelicula_streaming_Reciente = df[df['R. Date (Streaming)'] == peli_streaming_max]

    # Se realiza la impresión de resultados
    print("\n\nPelículas más antiguas estrenadas en cine:")
    print(pelicula_Cines_Antigua)
    print("\n\nPelículas más recientes estrenadas en cine:")
    print(pelicula_Cines_Reciente)

    print("\n\nPelículas más antiguas estrenadas en plataforma:")
    print(pelicula_streaming_Antigua)
    print("\n\nPelículas más recientes estrenadas en plataforma:")
    print(pelicula_streaming_Reciente)


# Se mandan a llamar a las funciones con base en la direccion en la que están
# dentro del equipo
promedio_score_por_genero("../Proyectomineria/recogiendo_tomates_2.csv")
conteo_peliculas_por_genero("../Proyectomineria/recogiendo_tomates_2.csv")
#Si molesta mucho la funcion de abajo, solo comentala (es mucho texto)
conteo_peliculas_por_clasificacion("../Proyectomineria/recogiendo_tomates_2.csv")
pelicula_mejor_y_peor_puntuada("../Proyectomineria/recogiendo_tomates_2.csv")
pelicula_mas_larga_y_mas_corta("../Proyectomineria/recogiendo_tomates_2.csv")
fechas_lanzamiento("../Proyectomineria/recogiendo_tomates_2.csv")