#plotting the word cloud of the APOD titles
from wordcloud import WordCloud, STOPWORDS
import matplotlib.pyplot as plt
import pandas as pd
import re

# loading the dataset
df = pd.read_csv('nasa_apod_complete.csv')

# cleaning the text data
stopwords = set(STOPWORDS)

# remove stopwords per-word after cleanup
df['title'] = df['title'].astype(str)
df['title'] = df['title'].apply(lambda x: re.sub(r'[^\w\s]', '', x))
df['title'] = df['title'].apply(lambda x: re.sub(r'\d+', '', x))
df['title'] = df['title'].str.lower()

text = ' '.join(df['title'].tolist())

# generating the word cloud
wordcloud = WordCloud(
    width=800,
    height=400,
    background_color='black',
    colormap='Greens',
    stopwords=stopwords
).generate(text)

plt.figure(figsize=(10, 5))
plt.imshow(wordcloud, interpolation='bilinear')
plt.axis('off')
plt.title('Word Cloud of APOD Titles')
plt.show()
