import pandas as pd
import numpy as np
import re
from io import StringIO
from datetime import datetime

ruta_csv = "../Proyectomineria/recogiendo_tomates.csv"

def eliminar_registros_con_mal_formato(input_file):
    # Aquí se lee el archivo CSV
    df = pd.read_csv(input_file)
    # Se nombra a la primer columna (no tenía)
    df.rename(columns={df.columns[0]: "Number"}, inplace = True)
    # Remover registros que tengan valores en la columna titulo (fuera de formato)
    df = df[df['Title'].isna()]
    # Se crea un archivo nuevo sin los registros que depreciamos
    df.to_csv("../Proyectomineria/recogiendo_tomates_1.csv", index=False) 

def ordenar_columnas_depuradas_a_csv(input_file):
    # Se carga el archivo CSV
    df = pd.read_csv(input_file)
    # Pasar a una lista todos los valores de la columna "Number"
    ColumnaALista = df['Number'].tolist()
    # String que ayudará a reordenar los datos
    lineas_completas = ""

    # Ciclo loop para añadir al string anterior todos los datos de la lista ColumnaALista
    for linea in ColumnaALista:
        lineas_completas = lineas_completas + '\n' + linea

    # Utiliza StringIO para convertir el string en un objeto tipo archivo
    archivo_csv = StringIO(lineas_completas)
    # Crea un DataFrame de Pandas a partir de las líneas de datos
    df1 = pd.read_csv(archivo_csv, header=None, quotechar='"')
    # Guarda el DataFrame en un archivo CSV nuevo ya ordenado
    df1.to_csv("../Proyectomineria/recogiendo_tomates_2.csv", index=False)

def renombrar_Columnas(input_file):
    # Se carga el archivo CSV
    df = pd.read_csv(input_file)
    # Se renombran todas las columnas
    df.rename(columns={df.columns[0]: "Number", df.columns[1]: "Title", df.columns[2]: "TomatometerScore", 
                       df.columns[3]: "AudienceScore", df.columns[4]: "Rating", df.columns[5]: "Genre",
                       df.columns[6]: "Director", df.columns[7]: "Producer", df.columns[8]: "Writer",
                       df.columns[9]: "R. Date (Theaters)", df.columns[10]: "R. Date (Streaming)", df.columns[11]: "Runtime",
                       df.columns[12]: "Prod. Company"}, inplace = True)
    # Se elimina la primer columna (no es importante y está mal numerada)
    df.drop(['Number'], axis= 1, inplace = True)
    # Actualizamos el archivo en el que se encontraba la información
    df.to_csv(input_file, index=False)

def formato_A_Fechas(input_file):
    # Se carga el archivo CSV
    df = pd.read_csv(input_file)
    # Se reemplazan algunos caracteres que estorban en el formato de las fechas
    df['R. Date (Theaters)'] = df['R. Date (Theaters)'].str.replace(' limited','')
    df['R. Date (Theaters)'] = df['R. Date (Theaters)'].str.replace(' wide','')
    # Se aplica la función convertir_fecha() de abajo de este método
    df['R. Date (Streaming)'] = df['R. Date (Streaming)'].apply(convertir_fecha)
    df['R. Date (Theaters)'] = df['R. Date (Theaters)'].apply(convertir_fecha)
    df.to_csv(input_file, index=False)

def convertir_fecha(fecha_str):
    # Si el campo no es nulo, se entra a la condición
    if pd.notna(fecha_str):
        # Se quita la coma
        fecha_str = fecha_str.replace(',', '').strip()
        # Se usa la función strptime() para cambiar la fecha con base en un formato ya establecido por la librería datetime 
        # y solo se extrae la fecha de eso, sin la hora
        return datetime.strptime(fecha_str, '%b%d%Y').date()

def formato_A_Horas(input_file):
    # Se carga el archivo CSV
    df = pd.read_csv(input_file)
    df['Runtime'] = df['Runtime'].map(funcion_ejemplo)
    df.to_csv(input_file, index=False)

def funcion_ejemplo(hora):
    if (pd.isna(hora)):
        return np.nan
    elif 'h' in hora and 'm' in hora:
        partes = hora.split("h")
        horas = int(partes[0])*60
        minutos = partes[1].replace("m","")
        duracion = horas+int(minutos)
        return duracion
    elif 'h' in hora and not 'm' in hora:
        hora = hora.replace('h','')
        duracion = int(hora)*60
        return duracion
    elif 'm' in hora and not 'h' in hora:
        minutos = hora.replace('m','')
        duracion = int(minutos)
        return duracion
    else:
        return 0
    
def formato_A_Score(input_file):
    # Se carga el archivo CSV
    df = pd.read_csv(input_file)
    # Se guardan los datos de las puntuaciones en variables diferentes
    columnaTomatometerScore = df['TomatometerScore']
    columnaAudienceScore = df['AudienceScore']
    # Se itera a través de las listas/Arrays
    for i in range(len(columnaAudienceScore)):
        #Si el valor es no nulo, se le quita el signo de porcentaje
        if pd.notna(columnaTomatometerScore[i]):
            columnaTomatometerScore[i] = columnaTomatometerScore[i][:-1]
        #Lo mismo aquí, pero para el otro array de score
        if pd.notna(columnaAudienceScore[i]):
            columnaAudienceScore[i] = columnaAudienceScore[i][:-1]
    df['TomatometerScore'] = columnaTomatometerScore
    df['AudienceScore'] = columnaAudienceScore
    df.to_csv(input_file, index=False)

def formato_A_Rating(input_file):
    # Se carga el archivo CSV
    df = pd.read_csv(input_file)
    # Se guarda la columna rating en un array
    columna_rating = df.iloc[:,3]
    # Se reemplazan los valores nulos con NR (Not Rated)
    columna_rating = columna_rating.replace(np.NaN,"NR")
    # Se deja la categoría con forma estandarizada del "Film Rating System"
    columna_rating = columna_rating.map(categorizar_ratings)
    # Se actualiza la columna en el dataframe y el csv
    df['Rating'] = columna_rating
    df.to_csv(input_file, index=False)
        
def categorizar_ratings(cadena):
    # Se usa una expresión regular para buscar y eliminar los paréntesis y su contenido.
    # La ER r'\([^)]*\)' coincide con cualquier texto entre paréntesis.
    # r'\(' coincide con el paréntesis izquierdo "(",
    # [^)]* coincide con cualquier caracter que no sea un paréntesis derecho ")",
    # y r'\)' coincide con el paréntesis derecho ")".
    return re.sub(r'\([^)]*\)', '', cadena)

def eliminar_columnas(input_file):
    # Se carga el archivo CSV
    df = pd.read_csv(input_file)
    df.drop(columns=['Producer','Writer','Prod. Company'], inplace=True)
    df.to_csv(input_file, index=False)

def formato_A_Generos(input_file):
    # Se carga el archivo CSV
    df = pd.read_csv(input_file)
    generos = df['Genre']
    # Se recortan por comas los generos
    primeras_partes = [str(cadena).split(',')[0] for cadena in generos]
    # Se agrega al dataframe original
    df['Genre'] = primeras_partes
    # Se guarda en un archivo
    df.to_csv(input_file, index=False)

# Se ejecutan todas las funciones (que crearán y modificarán archivos csv en una ruta específica)
# Si intentas descargar todo el proyecto, borra los archivos 'recogiendo_tomates_1.csv' y 'recogiendo_tomates_2.csv'
# para que se vuelvan a crear
eliminar_registros_con_mal_formato("../Proyectomineria/recogiendo_tomates.csv")
ordenar_columnas_depuradas_a_csv("../Proyectomineria/recogiendo_tomates_1.csv")
renombrar_Columnas("../Proyectomineria/recogiendo_tomates_2.csv")
formato_A_Fechas("../Proyectomineria/recogiendo_tomates_2.csv")
formato_A_Rating("../Proyectomineria/recogiendo_tomates_2.csv")
formato_A_Score("../Proyectomineria/recogiendo_tomates_2.csv")
formato_A_Horas("../Proyectomineria/recogiendo_tomates_2.csv")
eliminar_columnas("../Proyectomineria/recogiendo_tomates_2.csv")
formato_A_Generos("../Proyectomineria/recogiendo_tomates_2.csv")

# Obtener generos diferentes
"""df = pd.read_csv("../Proyectomineria/recogiendo_tomates_2.csv")
unique_elements = set(df['Genre'])
unique_list = list(unique_elements)
print(unique_list)"""
