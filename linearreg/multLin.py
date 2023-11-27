import numpy as npy
from numpy import array as arr
import pandas as pd
import scipy.stats as spy
import matplotlib.pyplot as plt
import statsmodels.api as sm
from statsmodels.formula.api import ols
import seaborn as sns
from math import sqrt

'''
PREDICTS Y BY X 


MULTIPLE LINEAR REGRESSION

y = B0 + B1x1 + B2x2 ... Bkxk + e


assumptions:
mean of error is zero
variance = o^2 , constant variance
normal probability distribution
random errors are independent


df = n-2

note: confidence interval for regression and t test will be the same
with categorical variables can dummy code into a t test


'''

#data to practice on
data = pd.read_csv('linearreg\grandfatherclock.csv')

bids = data['NUMBIDS']
salesprice = data['PRICE']
age = data['AGE']
print(spy.linregress(bids, salesprice)) #predict salesprice by bids
print(spy.linregress(age
, salesprice)) # predict salesprice by age

sns.histplot(data, x='NUMBIDS5')
plt.show()

'''
interpolation - easy
predicting something in the present

extrapolation - hard
predicting something in the future

'''


'''
note: explanatory variables in mult LR just test for if theyre significant for the response
not whether or not interaction between the variables exists 
(do not conduct t tests) if the result is significant
(B1 + B3x2) represents rate of change


qualitative (categorical) variables can also be included in multiple linear regression
levels:
dummy variable: coding qualitative variables as quantitative 
ex:
x = 1 if male 0 if female
x = 1 if (gender == 'male') else 0


TODO: LEARN LINEAR REGRESSION 
'''