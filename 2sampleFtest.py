import numpy as npy
import scipy.stats as stats

#needs 2 degrees of freedom along with a probability 
#to calculate the value

data1 = [1,2,3,4,5]
data2=[6,7,8,9,10]

stats.f(data1,data2).pvalue