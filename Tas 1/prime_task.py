# -*- coding: utf-8 -*-
"""Prime_task.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1a2eA6ARndd8w8X-sBhxPiK_Tj9N-ZVC4
"""

import numpy as np
import pandas as pd

df=pd.read_csv('/content/prime.csv')

df.isnull().sum()

df.head(10)

from typing_extensions import DefaultDict
from IPython.core.display import display_pdf
df['director'].fillna('Unknown', inplace=True)
df['cast'].fillna('Unknown', inplace=True)
df['country'].fillna('Unknown', inplace=True)
df['date_added'].fillna('Unknown', inplace=True)
df['rating'].fillna(df['rating'].mode()[0], inplace=True)
df['duration'].fillna(df['duration'].mode()[0], inplace=True)

df.isnull().sum()

df['director'].unique()

df['director'].value_counts()

df['director'].value_counts().sort_values(ascending=False)

df['type'].value_counts().plot(kind='bar')

import seaborn as sns
import matplotlib.pyplot as plt

df = df.sort_values(by=['rating'], ascending=False)
plt.bar(df['director'], df['rating'])
plt.xlabel('Director')
plt.ylabel('Rating')
plt.title('Bar Graph of Director by Rating')
plt.show()

df = df.sort_values(by=['rating'], ascending=False)
print(df['director'].iloc[0])

df = df.sort_values(by=['rating'], ascending=False)
print(df['title'].iloc[0])

movie_name = "You Don't Mess with the Zohan"
rating = df[df['title'] == movie_name]['rating'].iloc[0]
director = df[df['title'] == movie_name]['director'].iloc[0]
print(f"Rating: {rating}")
print(f"Director: {director}")

highest_rating = df['rating'].max()
top_rated_movies = df[df['rating'] == highest_rating]
top_rated_movie_durations = top_rated_movies['duration']
for duration in top_rated_movie_durations:
    print(f"Movie duration: {duration}")

cast_with_highest_rating_and_country = df.groupby('cast')['rating'].max().reset_index().sort_values(by=['rating'], ascending=False).iloc[0]
print(f"Cast with highest rating and country: {cast_with_highest_rating_and_country}")

df_pie = df['type'].copy().value_counts()
plt.figure(figsize=(6,6))
plt.pie(
    x=df_pie.values,labels=df_pie.index,autopct='%.1f%%',
    wedgeprops={'linewidth':2.0,'edgecolor':'white'}
    )
plt.title('Movie and TV Shows Ratio')
plt.legend(labels=[f"{label} ({count})" for label, count in zip(df_pie.index, df_pie.values)],loc='best')
plt.show()

fig =plt.figure(figsize=(16,6))
bins = []
for i in range(1920,2022,10):
    if(i==2020):
        i = 2021
    bins.append(i)
df_count = df[['type','release_year']].copy()
df_count.loc[:,'release_year_bins'] = pd.cut(df_count['release_year'],bins)
sns.countplot(data=df_count,x='release_year_bins',hue='type',width=0.8)
plt.xticks(rotation=45)
plt.title('Distribution of Movie and Tv Shows per 10 Year')
plt.ylabel('Shows Released')
plt.xlabel('Release Year')
fig.set_tight_layout(True)
plt.show()

df_count1 = df['rating'].value_counts().reset_index()
plt.figure(figsize=(16,6))
sns.countplot(x='rating', data=df,hue='type', order=df['rating'].value_counts().index)
plt.xticks(rotation=90)
plt.title('Distribution of Shows Rating')
plt.xlabel('Rating')
plt.ylabel('Number of Shows')
plt.show()

df_barh = df['listed_in'].str.split(', ').explode().value_counts()
plt.figure(figsize=(14,7))
sns.barplot(y=df_barh.index,x=df_barh.values,orient='horizontal')
plt.ylabel('Category')
plt.xlabel('Number of Shows')
plt.title('Shows Categories Available in Amazon Prime')
plt.show()

df_bar_mov = df[df['type']=='Movie'].copy()
df_bar_tv = df[df['type']=='TV Show'].copy()

df_bar_mov['duration_num'] = df_bar_mov.duration.str.split().str[0].astype('Int64')
df_bar_tv['duration_num'] = df_bar_tv.duration.str.split().str[0].astype('Int64')

df_bar_mov = df_bar_mov[['title','duration_num']].sort_values('duration_num',ascending=False)
df_bar_tv = df_bar_tv[['title','duration_num']].sort_values('duration_num',ascending=False)
plt.figure(figsize=(8,12))
plt.subplot(2,1,1)
sns.barplot(data=df_bar_mov.head(10),y='title',x='duration_num',orient='horizontal')
plt.title('Top 10 Longest Movie Duration')
plt.xlabel('Duration (min)')
plt.ylabel('Movie Title')
plt.show()
plt.figure(figsize=(8,12))
plt.subplot(2,1,2)
sns.barplot(data=df_bar_tv.head(10),y='title',x='duration_num',orient='horizontal')
plt.title('Top 10 TV Show with the Most Seasons')
plt.xlabel('Number of Seasons')
plt.ylabel('Tv Show Title')
plt.show()

plt.figure(figsize=(12,2))
plt.title("Value Counts of The Country Variable")
sns.set(style="darkgrid")
ax = sns.countplot(x="country", data=df, palette="Pastel2", order=df.country.value_counts().iloc[:4].index)
ax.bar_label(ax.containers[0])