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

Y PREDICTS X 

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


NOTE:
x is independent variable (explanatory variable), input
y is dependent variable (response variable), output

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
h = pd.read_csv('AP_Top_25_2018.csv', usecols=['Passing Yards/Game', 'Points/Game'])
print(h.iloc[:, 0])
output = spy.linregress(h.iloc[:,0],h.iloc[:,1])
print(output)
plt.show()

sns.histplot(h, x='Passing Yards/Game')
plt.show()




# regression plot
# SEABORN IS A GODSEND
out = sns.regplot(data = h, x='Passing Yards/Game', y='Points/Game')
print(out)
plt.show()

plt.scatter(h.iloc[:,0], h.iloc[:,1])
plt.axline(xy1=(0, output.intercept), slope=(output.slope))
plt.show()



sns.residplot(x=h.columns[0], y=h.columns[1], data = h)
plt.show()



df = pd.DataFrame({'age':[16,17,18,19,20,21,22,23,24,25],'insurance':[7203,5924,5242,3874,3532,2864,2593,2415,2267,2010]})
dfout = spy.linregress(df.iloc[:,0], df.iloc[:,1])

print(df.iloc[:,1])
print([[dfout.intercept+ dfout.slope*i] for i in df.iloc[:,0]])

sns.regplot(df, x=df.columns[0], y = df.columns[1])
plt.show()


'''
WHAT MAKES LR NOT LINERA

NOTE: will make non linear relationships in methods 3

1 - regression function isnt linear
2 - error terms dont have constant variance
3 - error tersm arent independent
4 - model fits all but one or a few outlier observations
5 - error tersm arent normally distributed
6 - 1 or several predictor vars haev been omitted

'''


'''
SLOPE -
B1 (slope) = SSxy/SSxx 
B0 (y intercept) = predicted y - slope * predicted x

SSE = SSyy - B1 * SSxy
S^2 = SSE/ n-2

conf int. = y^hat +- t a/2 * s * sqrt(1/n + (xp - x predicted)^2/SSxx)
t a/2 with n-2 df 
'''

'''
to predict avergae for a single point - use prediction interval
to predict mean of average for all points - use confidence interval

'''

data = pd.DataFrame({'x':[50,45,50,60,50,60,55,60,50,50,70,45,40,40,50], 'y':[77.51,72.03,48.79,41.93,68.15,54.11,57.09,20.79,60.36,68.15,28.87,72.03,35.06,33.95,43.93] })

out = spy.linregress(data.iloc[:,0], data.iloc[:,1])
print(out, out.slope-2*out.intercept_stderr, out.slope+2*out.intercept_stderr)

out = sns.regplot(data, x='x', y='y')
plt.show()