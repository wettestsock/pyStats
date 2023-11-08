import numpy as npy
from numpy import array as arr
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


'''
