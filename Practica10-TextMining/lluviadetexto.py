from wordcloud import WordCloud
import matplotlib.pyplot as plt

# Ejemplo de texto
texto = """
Python es un lenguaje de programación popular. Es fácil de aprender y versátil. 
Python se utiliza en una variedad de aplicaciones, desde desarrollo web hasta inteligencia artificial.
La comunidad de Python es grande y activa.
"""

# Crear un objeto WordCloud
wordcloud = WordCloud(width=800, height=400, background_color="white").generate(texto)

# Mostrar la imagen generada
plt.figure(figsize=(10, 5))
plt.imshow(wordcloud, interpolation="bilinear")
plt.axis("off")
plt.show()
