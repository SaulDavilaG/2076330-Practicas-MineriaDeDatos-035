import pandas as pd
import statsmodels.api as sm
from statsmodels.formula.api import ols

def anovaPromedio_Generos(input_file):
    # Se lee el dataframe con pandas
    df_peliculas = pd.read_csv(input_file)

    # Se cuenta el numero de peliculas que tiene cada genero
    conteo_generos = df_peliculas['Genre'].value_counts()

    # Se crea una lista con aquellos generos que tienen menos de 30 peliculas
    generos_menos_de_30 = conteo_generos[conteo_generos < 30].index.tolist()

    # Aquellos generos que estén dentro de la lista anterior son cambiados por 'other' para agruparlos mejor 
    df_peliculas.loc[df_peliculas['Genre'].isin(generos_menos_de_30), 'Genre'] = 'other'    

    # Se realiza el modelo para el ANOVA
    modelo = ols('TomatometerScore ~ C(Genre)', data=df_peliculas).fit()

    # Se obtienen los resultados del ANOVA
    resultado_anova = sm.stats.anova_lm(modelo, typ=2)

    # Se imprimen dichos resultados
    print(resultado_anova)

    # En caso de este dataframe, los datos indican que hay diferencias significativas 
    # entre al menos dos géneros en términos de las puntuaciones de las películas (TomatometerScore) 
    # La estadística F es mucho mayor que 1, y el valor de p es extremadamente pequeño, lo que 
    # dice que al menos un par de géneros son significativamente diferentes en términos de puntuaciones

# Se manda a llamar a la función :p
anovaPromedio_Generos("../Proyectomineria/recogiendo_tomates_2.csv")
