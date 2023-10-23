import numpy as npy
from numpy import array as arr
import pandas as pd
import scipy.stats as spy
import matplotlib.pyplot as plt


'''
SIMPLE LINEAR REGRESSION
H0: theres no slope (x has no effect on y)
Ha: theres a slope (x has effect on y)

r^2 = % of variability explained by the lsrl
r = strength of association


lots of matplotlib
'''

x = [29.8,30.3,22.6,18.7,14.8,4.1,4.4,2.8,3.8]
y= [67.5,70.6,72,78.2,87,89.9,91.2,93.1,96.7]


print(spy.linregress(x,y))
plt.scatter(x,y)
reg = spy.linregress(x,y)
plt.axline(xy1=(0,reg.intercept), slope =reg.slope)
plt.show()



plt.hist(x, bins = 20)
plt.show()