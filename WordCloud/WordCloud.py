import matplotlib.pyplot as plt
from wordcloud import WordCloud, STOPWORDS
import sys
import os
os.chdir(sys.path[0])
text = open("Hey.txt", mode='r', encoding='utf-8').read()
stopwords = STOPWORDS
wc = WordCloud(
    background_color='#ffffff',
    stopwords=stopwords,
    height=396,
    width=1584
)
wc.generate(text)
wc.to_file("Kalua.png")
