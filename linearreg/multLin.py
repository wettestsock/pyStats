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
print(spy.linregress(age, salesprice)) # predict salesprice by age

sns.histplot(data, x='NUMBIDS5')
plt.show()