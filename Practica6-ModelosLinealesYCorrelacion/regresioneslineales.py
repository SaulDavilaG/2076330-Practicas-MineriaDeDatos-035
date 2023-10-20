import pandas as pd
import statsmodels.api as sm
import matplotlib.pyplot as plt

def regresion_runtime_tomatometerscore(input_file):
    data  = pd.read_csv(input_file)

    data['Runtime'].fillna(data['Runtime'].mean(), inplace=True)
    data['TomatometerScore'].fillna(data['TomatometerScore'].mean(), inplace=True)

    X = data['Runtime']  # Variable independiente
    Y = data['TomatometerScore']  # Variable dependiente
    data['AudienceScore'].fillna(data['AudienceScore'].mean(), inplace=True)

    X = sm.add_constant(X)  # constante intercept del modelo

    model = sm.OLS(Y, X).fit()  # Ajusta el modelo
    print(model.summary())

    plt.scatter(data['Runtime'], data['TomatometerScore'], label='Datos', s=10)
    plt.plot(data['Runtime'], model.predict(X), color='red', label='Regresión')
    plt.xlabel('Runtime')
    plt.ylabel('TomatometerScore')
    plt.legend()
    plt.title('Regresión Lineal entre duración de una pelicula y su puntuación Tomatometer')
    plt.show()

def regresion_runtime_audiencescore(input_file):
    data  = pd.read_csv(input_file)

    data['Runtime'].fillna(data['Runtime'].mean(), inplace=True)
    data['AudienceScore'].fillna(data['AudienceScore'].mean(), inplace=True)

    X = data['Runtime']  # Variable independiente
    Y = data['AudienceScore']  # Variable dependiente

    X = sm.add_constant(X)  # constante intercept del modelo

    model = sm.OLS(Y, X).fit()  # Ajusta el modelo
    print(model.summary())

    plt.scatter(data['Runtime'], data['AudienceScore'], label='Datos', s=10)
    plt.plot(data['Runtime'], model.predict(X), color='red', label='Regresión')
    plt.xlabel('Runtime')
    plt.ylabel('AudienceScore')
    plt.legend()
    plt.title('Regresión Lineal entre duración de una pelicula y su puntuación de la audiencia')
    plt.show()

def regresion_TomatometerScore_AudienceScore(input_file):
    data  = pd.read_csv(input_file)

    data['AudienceScore'].fillna(data['AudienceScore'].mean(), inplace=True)
    data['TomatometerScore'].fillna(data['TomatometerScore'].mean(), inplace=True)

    X = data['TomatometerScore']  # Variable independiente
    Y = data['AudienceScore']  # Variable dependiente
    X = sm.add_constant(X)  # Agrega una constante al modelo

    model1 = sm.OLS(Y, X).fit()  # Ajusta el modelo
    print(model1.summary())

    plt.scatter(data['TomatometerScore'], data['AudienceScore'], label='Datos', s=10)
    plt.plot(data['TomatometerScore'], model1.predict(X), color='red', label='Regresión')
    plt.xlabel('TomatometerScore')
    plt.ylabel('AudienceScore')
    plt.legend()
    plt.title('Regresión Lineal entre puntuación Tomatometer y puntuación de la audiencia')
    plt.show()

#No aparece la linea de la regresión
"""def regresion_DiasLanzamiento_AudienceScore(input_file):
    data  = pd.read_csv(input_file)

    data['TomatometerScore'].fillna(data['TomatometerScore'].mean(), inplace=True)

    data['R. Date (Streaming)'] = pd.to_datetime(data['R. Date (Streaming)'])
    data['DaysSinceRelease'] = (data['R. Date (Streaming)'] - data['R. Date (Streaming)'].min()).dt.days
    data['DaysSinceRelease'].fillna(data['DaysSinceRelease'].mean(), inplace=True)

    X = data['DaysSinceRelease']  # Variable independiente
    Y = data['AudienceScore']  # Variable dependiente
    X = sm.add_constant(X)  # Constante intercept del modelo

    model = sm.OLS(Y, X).fit()  # Ajusta el modelo
    print(model.summary())

    plt.scatter(data['DaysSinceRelease'], data['AudienceScore'], label='Datos', s=10)  # Ajusta el valor de 's' para cambiar el tamaño de los puntos
    plt.plot(data['DaysSinceRelease'], model.predict(X), color='red', label='Regresión')
    plt.xlabel('Días desde su lanzamiento en streaming')
    plt.ylabel('AudienceScore')
    plt.legend()
    plt.title('Regresión Lineal entre Días desde el lanzamiento y AudienceScore')
    plt.show()

regresion_DiasLanzamiento_AudienceScore("../Proyectomineria/recogiendo_tomates_2.csv")"""

regresion_runtime_audiencescore("../Proyectomineria/recogiendo_tomates_2.csv")
regresion_TomatometerScore_AudienceScore("../Proyectomineria/recogiendo_tomates_2.csv")
regresion_runtime_tomatometerscore("../Proyectomineria/recogiendo_tomates_2.csv")