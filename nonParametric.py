import numpy as npy
import pandas as pd
import scipy.stats as spy
import statsmodels.stats as sm

# SIGN TEST IN PYTHON ( 1 sample)


data = npy.array([0.78,0.51,3.79,0.23,0.77,0.98,0.96,0.89])
null = 1.0

#shapiro wilk test in python
print(spy.shapiro(data))
# tests for normality

# TEST STATISTIC = # of measurements less or greater (depending the right or left tailed)
#           ^^^^^^ for two-tailed, it's whichever has more measurements on left or right , the biggest of the 2 
print(spy.binomtest(k=8-7,n=8, alternative='less'))  # k = # of measurements that dont fit the alternative

# k = # of successes (opposite of the alternative)
# n = sample size


#gives test statistic n p value
# FTR 

#---------------------

'''
 INDEPENDENT SAMPLES WILCOXON TEST

 D = probability distribution
 HYPOTHESES:
 D1= D2 (D1 is identical to D2)
 D1 ><!= D2 (D1 is shifted left/right/from D2)

TEST STATISTIC 
 w = sum of ranks - mean of the rank
'''

aug18, aug19= npy.array([87,88,91,92,92,93,93,95]), npy.array([88,89,90,92,93,94,95,96,97])
print(spy.shapiro(aug18))
print(spy.shapiro(aug19))

print(spy.ranksums(aug18, aug19, alternative='two-sided'))


S13,S17 = npy.array([38,34,25,38,62,19,39,23,17,52]), npy.array([61,38,51,63,31,73,31,45,49,37])
print(spy.shapiro(S13), spy.shapiro(S17), sep='\n')

print(spy.ranksums(S13,S17,alternative='less'))

'''
-------------------

 PAIRED WILCOXON TEST

 hypotheses:
 H0: D1-D2 or D1 is identical to D2
 Ha: D1<>!=D2 is shifted to the left/right/from D2 

 test statistic : sum of the ranks or    n(n+1)/2
 TS for 2 tail : sum of ranks - mean of rank
'''

# ex 1, gives small sample size warning
chimps=npy.array([[23,22,21,23,19,19,19],[21,22,23,21,18,16,19]])
print(spy.shapiro(chimps[0]), spy.shapiro(chimps[1]), sep='\n')
print(spy.wilcoxon(chimps[0]-chimps[1], alternative='greater', zero_method='????'))


'''

wtf ??

additive = npy.array([[36.4,36.4,36.6,36.6,36.8,36.9,37  ,37.1,37.2,37.2,36.7,37.5,37.6,37.8,37.9,37.9,38.1,38.4,40.2,40.5,40.9,35  ,32.7,33.6,34.2,35.1,35.2,35.3,35.5,35.9,36  ,36.1,37.2],[36.7,36.9,37  ,37.5,38  ,38.1,38.4,38.7,38.8,38.9,36.3,38.9,39  ,39.1,39.4,39.4,39.5,39.8,40  ,40  ,40.1,36.3,32.8,34.2,34.7,34.9,34.9,35.3,35.9,36.4,36.6,36.6,38.3]])
print(spy.shapiro(additive[0]), spy.shapiro(additive[1]), sep='\n')
print(spy.wilcoxon(additive[0]-additive[1], alternative='greater'))
'''

associate = npy.array([[21 ,22 ,21 ,19 ,18 ,25 ,16 ,18 ,21 ,24 ,21],[14, 21, 24, 16, 18 ,20 ,15 ,20, 17, 16, 18]])
print(spy.wilcoxon(associate[0]-associate[1], alternative = 'greater'))