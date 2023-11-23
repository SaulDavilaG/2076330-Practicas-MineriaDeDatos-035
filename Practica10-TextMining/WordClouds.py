from wordcloud import WordCloud, STOPWORDS
import matplotlib.pyplot as plt
import pandas as pd

stop_words = ''
path = "../Proyectomineria/Practica10-TextMining/stop_words_spanish.txt"
with open(path, "r", encoding="utf-8") as file:
    custom_stopwords = set(line.strip() for line in file)
#print(custom_stopwords)
stop_words = STOPWORDS.union(custom_stopwords)

def lluviadetextoDirectores():
    path = "../Proyectomineria/Practica10-TextMining/twitterfeed.txt"
    text = open(path, mode='r', encoding='utf-8').read()
    wordcloud = WordCloud(width=800, height=400, background_color="white", stopwords=stop_words).generate(text)
    #Se genera la lluvia de texto
    plt.figure(figsize=(10, 5))
    plt.imshow(wordcloud, interpolation="bilinear")
    plt.axis("off")
    #plt.show()
    plt.savefig('../Proyectomineria/Practica10-TextMining/'+'TwitterWordCloud.png', bbox_inches='tight')

def lluviadetextoFeedTwitter():
    df = pd.read_csv("../Proyectomineria/recogiendo_tomates_2.csv")
    directores = df['Director']
    directores = directores.str.replace(","," ")
    directores = directores.str.replace('-','')
    #Se crea el archivo de texto 'directores'
    with open('../Proyectomineria/Practica10-TextMining/directores.txt', 'w', encoding='utf-8') as file:
        for director in directores:
            file.write(str(director) + '\n')
    #Se lee dicho archivo
    text2 = open('../Proyectomineria/Practica10-TextMining/directores.txt', mode='r', encoding='utf-8').read()
    wordcloud = WordCloud(width=800, height=400, background_color="white", stopwords=stop_words).generate(text2)
    #Se crea la lluvia de texto
    plt.figure(figsize=(10, 5))
    plt.imshow(wordcloud, interpolation="bilinear")
    plt.axis("off")
    #plt.show()
    plt.savefig('../Proyectomineria/Practica10-TextMining/'+'DirectorsWordCloud.png', bbox_inches='tight')    

lluviadetextoDirectores()
lluviadetextoFeedTwitter()
