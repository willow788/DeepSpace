# Here we will explore the data and do some basic cleaning and visualization
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

#loading the dataset
df = pd.read_csv('nasa_apod_complete.csv')


#plotting the distribution of APOD extries per year

#converting date to datetime format
df['date'] = pd.to_datetime(df['date'])

#then extracting the year from the date
df['year'] = df['date'].dt.year

#then plotting the graph
plt.figure(figsize=(12,6))
sns.countplot(x='year', data=df, palette='viridis')
plt.xticks(rotation=90)
plt.title('Distribution of APOD entries per year')
plt.xlabel('Year')
plt.ylabel('Count')
plt.show()

#saving the output graph in the file
plt.savefig('apod_entries_per_year.png')



