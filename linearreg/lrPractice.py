import numpy as npy
from numpy import array as arr
import pandas as pd
import scipy.stats as spy
import matplotlib.pyplot as plt
import statsmodels.api as sm
from statsmodels.formula.api import ols
import seaborn as sns


#annoying
def pp():
    print('\n\n')
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
plt.axline(xy1=(0,reg.intercept + 2*reg.stderr), slope =reg.slope)
plt.axline(xy1=(0,reg.intercept - 2*reg.stderr), slope =reg.slope)
plt.show()
pp()


'''
PROBABILISTIC MODELS

model with exact relationship between variables

y = 3x, y = 10x-2, etc
there will always be some unexplained variation in the data caused by random phenomena

general model :
Y = deterministic component + random error

first order probabilistic model:
y = B0 + B1X + e
B0: y intercept
B1: slope
e: random error component
assumed mean of the error is zero, hope its zero

expected value of y = B0 + B1X
|E|Y| or y^hat (AP STATS REFERENCE)
y^hat = a+bx         MRS MAGULICKKKKKKKKKKKKKKKKKKKKKKK


LSRL TABLE IS LITERALLY ANOVA TABLE
one way anova gives same p value as lsrl 

slope isnt really meaningful

df for parameter estimate = n - # of parameters (intercept and slope)
df is n-2 

'''


#NUMPY ARRAYS ARE GOOD, A LOT MORE CONTROL OVER DATA
x = arr([6,7,1,10,6,4,8])
y=arr([2,9,4,9,3,10,7])




pp()

reg2 = spy.linregress(x,y)
print(pow(x,2))
print(x*y)
print(sum(x))
pp()

print(reg)

#MAKING THE GRAPH
plt.scatter(x,y)
plt.axline(xy1=(0, reg2.intercept), slope = reg2.slope)
plt.axline(xy1=(0, reg2.intercept+2*reg.stderr), slope = reg2.slope)
plt.show()
# SSxy

SSxy = sum(x*y)-((sum(x)*sum(y))/len(x))

# SSxx 

SSxx = sum(pow(x,2))-(pow(sum(x),2)/len(x))

# x bar = sum of x / n
# y bar = sum of y / n

xbar = sum(x)/len(x)
ybar = sum(y)/len(y)

# mean of x and y = pivot point
#theres a confidence interval for the slope
# hourglass shape pivoting around the mean

# 95% CI for mean (model)
# and 95% CI for data points

# is independent, y is dependent
print(x,y)
h = pd.read_csv('linearreg\AP_Top_25_2018.csv', usecols=['Total Yards', 'Passing Yards'])
print(h.iloc[:, 0])
output = spy.linregress(h.iloc[:,0],h.iloc[:,1])
print(output)
plt.show()

sns.residplot(x='Total Yards', y='Passing Yards', data = h)
plt.show()
sns.histplot(h, x='Total Yards')
plt.show()




# regression plot
# SEABORN IS A GODSEND
out = sns.regplot(data = h, x='Total Yards', y='Passing Yards')
print(out)
plt.show()

plt.scatter(h.iloc[:,0], h.iloc[:,1])
plt.axline(xy1=(0, output.intercept), slope=(output.slope))
plt.show()