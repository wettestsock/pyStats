import numpy as npy
import pandas as pd
import scipy.stats as spy
import statsmodels as sm



data = npy.array([0.78,0.51,3.79,0.23,0.77,0.98,0.96,0.89])


#shapiro wilk test in python
print(spy.shapiro(data))
# tests for normality


# SIGN TEST IN PYTHON
null = 1.0

# TEST STATISTIC = # of measurements less or greater (depending the right or left tailed)
#           ^^^^^^ for two-tailed, it's whichever has more measurements on left or right , the biggest of the 2 
print(spy.binomtest(k=7,n=8, alternative='greater'))

#gives test statistic n p value
# FTR 
