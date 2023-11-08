import numpy as npy
from numpy import array as arr
from pandas import DataFrame as df
import pandas as pd
import scipy.stats as spy
import matplotlib.pyplot as plt
import statsmodels.api as sm
from statsmodels.formula.api import ols
import seaborn as sns



d1 = pd.read_csv('linearreg\AP_Top_25_2018.csv')
d2 = pd.read_excel('linearreg\Brand DAta RBD in Excel.xlsx')
d3 = pd.read_csv('linearreg\STA4163 Enrollment.csv')

print(d1,d2,d3)

'''
SPEARMAN NONPARAMETRIC RANK CORRELATION TEST

basically doesnt make sense on a graph
ordinal level data - where multiplying and dividing doesnt make sense

conditions:
1 - sample of experimental units is randomly assigned
2 - probability distributions of 2 variables are continuous ( ??? ) 

meausring probabilities, denoted by p 
measures if no association


test statistic: rs 
basically sum of the error square


basically gives the R value (in a linear regression)
'''


#ex

ex1 = df({'on-time': [87.3, 79.4, 86.5, 79.8, 76.0, 91.1,75.0, 82.3, 80.8, 74.3, 81.7, 76.2], 
'complaints': [0.50, 2.49, 0.68, 0.51, 5.94, 1.16,0.75, 0.49, 0.47, 6.74, 2.27, 1.85]})

#print(ex1.iloc[:(len(ex1.index)//2)])
print(ex1)
print(spy.spearmanr(ex1.iloc[:,0], ex1.iloc[:,1], alternative='less'))
# p value isnt that necessary were only looking at the test statistic (r)
print('At the 5 percent level of significance, we see a moderate negative relationship in the ranking between x and y because r = -0.556')
print('as on time percentage goes up, there is a trend for the complaints is downward')