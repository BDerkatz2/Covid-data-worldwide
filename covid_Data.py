import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

url = 'https://covid.ourworldindata.org/data/owid-covid-data.csv'
df = pd.read_csv(url)

# Select the columns we are interested in
cols = ['iso_code', 'location', 'date', 'total_cases', 'total_deaths']
df = df[cols]

# Convert date to datetime format
df['date'] = pd.to_datetime(df['date'])

# Remove rows with missing values
df = df.dropna()

df['new_cases'] = df.groupby('location')['total_cases'].diff().fillna(0)
df['new_deaths'] = df.groupby('location')['total_deaths'].diff().fillna(0)

df_country = df.groupby(['iso_code', 'location'])[['total_cases', 'total_deaths']].max().reset_index()

# Plot the top 10 countries with the most total cases
top10_cases = df_country.sort_values('total_cases', ascending=False).head(10)
plt.figure(figsize=(10, 6))
sns.barplot(x='location', y='total_cases', data=top10_cases, palette='Blues_r')
plt.title('Top 10 Countries with the Most Total Cases')
plt.ylabel('Total Cases (millions)')
plt.xticks(rotation=45)
plt.show()

# Plot the top 10 countries with the most total deaths
top10_deaths = df_country.sort_values('total_deaths', ascending=False).head(10)
plt.figure(figsize=(10, 6))
sns.barplot(x='location', y='total_deaths', data=top10_deaths, palette='Reds_r')
plt.title('Top 10 Countries with the Most Total Deaths')
plt.ylabel('Total Deaths (thousands)')
plt.xticks(rotation=45)
plt.show()
