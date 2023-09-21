import pandas as pd
from io import StringIO

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
    df.rename(columns={df.columns[0]: "Number", df.columns[1]: "Title", df.columns[2]: "Tomatometer Score", 
                       df.columns[3]: "Audience Score", df.columns[4]: "Rating", df.columns[5]: "Genre",
                       df.columns[6]: "Director", df.columns[7]: "Producer", df.columns[8]: "Writer",
                       df.columns[9]: "R. Date (Theaters)", df.columns[10]: "R. Date (Streaming)", df.columns[11]: "Runtime",
                       df.columns[12]: "Prod. Company"}, inplace = True)
    # Se elimina la primer columna (no es importante y está mal numerada)
    df.drop(['Number'], axis= 1, inplace = True)
    # Actualizamos el archivo en el que se encontraba la información
    df.to_csv("../Proyectomineria/recogiendo_tomates_2.csv", index=False)

#eliminar_registros_con_mal_formato("../Proyectomineria/recogiendo_tomates.csv")
#ordenar_columnas_depuradas_a_csv("../Proyectomineria/recogiendo_tomates_1.csv")
renombrar_Columnas("../Proyectomineria/recogiendo_tomates_2.csv")