import pandas as pd
import matplotlib.pyplot as plt
import sys
sys.path.append('../Proyectomineria/Practica3-EstadisticaDescriptiva/')
import FuncionesDeAgregacion


def conteoDePeliculasPorGenero():
    df_conteo = FuncionesDeAgregacion.conteo_peliculas_por_genero("../Proyectomineria/recogiendo_tomates_2.csv")

    # Personalización del grafico    
    ax = df_conteo.plot(kind='bar', figsize=(12, 7))
    plt.title('Número de Películas por Género')
    plt.xlabel('Genero')
    plt.ylabel('Número de Películas')
    plt.legend(labels=[])
    plt.xticks(rotation=90)  # Se rotan las etiquetas del eje X para que sean legibles
    
    for p in ax.patches:
        ax.annotate(f'{p.get_height()}', (p.get_x() + p.get_width() / 2., p.get_height()), ha='center', va='center', fontsize=10, color='black', xytext=(0, 5), textcoords='offset points')

    # Esto nos ayuda a mostrar el número exacto de altitud de cada barra

    plt.savefig('../Proyectomineria/graficas/'+'Conteo de Peliculas por Genero', bbox_inches='tight')
    # Mostrar el gráfico (opcional)
    plt.show()

def graficaPuntuacionPromedioPorGenero():
    df_genero = FuncionesDeAgregacion.promedio_score_por_genero("../Proyectomineria/recogiendo_tomates_2.csv")

    # Esto me salvó la vida, no sabría como manipular un dataframe con funciones de agregacion incluidas
    df_genero = df_genero.reset_index()

    # Se toman los generos para colocarlos como nombre en las barras
    generos = df_genero['Genre']

    # Lo mismo con las puntuaciones de tomatometer y de la audiencia
    promedios_tomatometer = df_genero['Tomatometer Score']
    promedios_audience = df_genero['Audience Score']

    # Personalización de la grafica
    plt.figure(figsize=(12, 7))
    plt.bar(generos, promedios_tomatometer, label='Tomatometer Score', alpha=0.7)
    plt.bar(generos, promedios_audience, label='Audience Score', alpha=0.7)
    plt.xlabel('Género')
    plt.ylabel('Promedio de Puntuación (sobre 100)')
    plt.title('Promedio de Puntuaciones por Género y Tipo')
    plt.legend()
    plt.xticks(rotation=90)

    plt.savefig('../Proyectomineria/graficas/'+'Promedio de Puntuación de Peliculas por Genero', bbox_inches='tight')

    # Mostrar el grafico (Opcional)
    # plt.show()

def conteoDePeliculasPorGeneroYClasificacion():
    df_clasificacion = FuncionesDeAgregacion.conteo_peliculas_por_clasificacion("../Proyectomineria/recogiendo_tomates_2.csv")

    # Obtener la lista de géneros únicos
    generos = df_clasificacion.index.get_level_values('Genre').unique()

    # Se escribe la lista de clasificaciones únicas (se hizo mediante la función unique() también)
    # Primero se imprimió en consola el arreglo / lista, pero luego se ordenó de la siguiente manera
    # para ordenar las clasificaciones por edad
    clasificaciones = ['G', 'PG', 'PG-13', 'R', 'NC-17', 'TVG', 'TVPG', 'TV14', 'TVMA', 'NR']

    # Se crea un gráfico de barras para cada género
    for genero in generos:
        df_genero = df_clasificacion.loc[genero]
        
        # Rellenar con ceros las clasificaciones faltantes
        df_genero = df_genero.reindex(clasificaciones, fill_value=0)
        
        ax = df_genero.plot(kind='bar', figsize=(12, 6))
        
        # Personalización del grafico
        plt.title(f'Número de Películas por Clasificación en el Género {genero}')
        plt.xlabel('Clasificación')
        plt.ylabel('Número de Películas')
        plt.ylim(0,1200)
        plt.legend(labels=[])
        plt.xticks(rotation=0)  # Se rotan las etiquetas del eje X para que sean legibles


        # Esto nos ayuda a mostrar el número exacto de altitud de cada barra
        for p in ax.patches:
            ax.annotate(f'{p.get_height()}', (p.get_x() + p.get_width() / 2., p.get_height()), ha='center', va='center', fontsize=10, color='black', xytext=(0, 5), textcoords='offset points')

        nombre_archivo = f'grafica {genero} clasificacion.png'
        plt.savefig('../Proyectomineria/graficas/'+nombre_archivo, bbox_inches='tight')

        # Se muestra el grafico (opcional)
        # plt.show()


graficaPuntuacionPromedioPorGenero()
conteoDePeliculasPorGenero()
conteoDePeliculasPorGeneroYClasificacion()