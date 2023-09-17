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
                   # specified rows 0 to 10

print(df[['Name', 'HP', 'Attack']][0:10]) # can get multiple columns 


# read each row !!

#  .iloc integer location
print(df.iloc[1])  # row 2
print(df.iloc[2:11])  # row 2 through 10 (exclusive)

#read specific location
print(df.iloc[2, 1].upper()) # row, column


#  .loc for non integer stuff

print(df.loc[df['Type 1'] == 'Fire'])  # gives all type 1 fire 

print(df['HP'].describe()) # gives summary statistics for the data 

print(df.sort_values('Name', ascending = False))  # sorts the values


print(df.sort_values(['Type 1', 'HP'], ascending = False))  # sorts the values for multiple parameters



# MAKING CHANGES TO THE DATA

df['Total'] = df['HP'] + df['HP'] + df['HP'] + df['Defense']  # makes a new column named total 


df = df.drop(columns=['Total'])  # drops the column
print(df)  

df['Total'] = df.iloc[:, 4:10].sum(axis=1)  # all rows, columns 4 through 9 , sum by axis horizontally

print(df) 

cols = npy.array(df.columns)  #columns
print(cols)


#   SAVING TO A CSV FILE

df.to_csv('modified.csv', index = False)  # dont save the annoying dataframe index
df.to_csv()
