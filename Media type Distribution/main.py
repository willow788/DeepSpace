import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

#loading the dataset
df = pd.read_csv('nasa_apod_complete.csv')

#plottting how many entries are images and how many are videos
plt.figure(figsize=(8,6))
sns.countplot(x='media_type', data=df, palette='viridis')
plt.title('Distribution of media types in APOD entries')

plt.xlabel('Media Type')
plt.ylabel('Count')
plt.show()
