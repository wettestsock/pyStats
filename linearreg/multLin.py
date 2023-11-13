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
MULTIPLE LINEAR REGRESSION

y = B0 + B1x1 + B2x2 ... Bkxk + e


assumptions:
mean of error is zero
variance = o^2 , constant variance
normal probability distribution
random errors are independent

'''

#data to practice on
data = pd.read_csv('linearreg\grandfatherclock.csv')

bids = data['NUMBIDS']
salesprice = data['PRICE']
print(spy.linregress(bids, salesprice).rvalue)

sns.regplot(data = data, x='NUMBIDS', y='PRICE')
plt.show()