import pandas as pd
import numpy as npy

# PANDAS LIBRARY INTRODUCTION 

df = pd.DataFrame(pd.read_csv('pandas/pokemon_data.csv'))
df_txt= pd.DataFrame(pd.read_csv('pandas/pokemon_data.txt', delimiter='\t')) # delimeter (tab in txt file)
print(df.head(6), '', df_txt, sep='\n') #top 5 rows,  .tail gives bottom rows


#reading headers

print(df.columns)

#reading column 

print(df['Name'][0:10], '\n')   # column named 'name' [] row, column
                   # specified rows 0 to 5 (exclusive)

print(df[['Name', 'HP', 'Attack']][0:10]) # can get multiple columns 


# read each row !!

#  .iloc integer location
print(df.iloc[1])  # row 2
print(df.iloc[2:10])  # row 2 through 10 (exclusive)

#read specific location
print(df.iloc[2, 1].upper()) # row, column


#  .loc for non integer stuff

print(df.loc[df['Type 1'] == 'Fire'])  # gives all type 1 fire 