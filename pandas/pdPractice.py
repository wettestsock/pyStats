import pandas as pd
import numpy as npy
import re 
#REGEX 
#regular expressions - allow for a lot of powerful string sorting in python
#learn more later ^^^^^

# PANDAS LIBRARY INTRODUCTION 

df = pd.DataFrame(pd.read_csv('pokemon_data.csv'))
df_txt= pd.DataFrame(pd.read_csv('pokemon_data.txt', delimiter='\t')) # delimeter (tab in txt file)
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



# FILTERING DATA

new_df = df.loc[(df['Type 1'] == 'Grass') & (df['Type 2'] == 'Poison') & (df['HP']>70)]
#new_df = new_df.reset_index(drop = True)  # resets the index, assigns to new df
new_df.reset_index(drop = True, inplace=True)  # inplace just sets the new df, no need to reassign it


new_df = df.loc[df['Name'].str.contains('Mega')]  # strings that CONTAIN word Mega
new_df.reset_index(drop=True, inplace=True)

new_df = df.loc[df['Type 1'].str.contains('fire|grass', flags = re.I, regex=True)]  # regex , find Fire or Grass , IGNORE CASE

new_df = df.loc[df['Name'].str.contains('^pi[a-z]*', flags = re.I, regex = True)] # regex, start of line (^), pi followed by [a-z], repeated multiple times
#LEARN REGEX

df.loc[df['Type 1'] == 'Fire', 'Type 1'] = 'Flamer'  # df type 1 is fire, type 1 of the fire, assign it to flamer

print(df)

new_df.to_csv('modified.csv', index = False)  # dont save the annoying dataframe index
print(new_df) 

 # convention of pytohn pandas library : 
    # & for and
    # | for or
    # ~ for not



#GROUPBY FUNCTION TO DO AGGREGATE STATS

df3 = pd.DataFrame(pd.read_csv('pokemon_data.csv'))

df3['count'] =1 # adds count column 
print(df3.groupby(by = 'Type 1').count()['count'])  #amount of stuff sorted by type 1
# watch more on this, very buggy


print(df3.boxplot())
