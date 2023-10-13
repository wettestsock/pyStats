print("hello")

import numpy as npy
import pandas as pd
import scipy.stats as spy
import statsmodels.stats as sm
from matplotlib import pyplot as plt
from math import sqrt

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
#print(spy.wilcoxon(chimps[0]-chimps[1], alternative='greater', zero_method='????'))


'''

wtf ??

additive = npy.array([[36.4,36.4,36.6,36.6,36.8,36.9,37  ,37.1,37.2,37.2,36.7,37.5,37.6,37.8,37.9,37.9,38.1,38.4,40.2,40.5,40.9,35  ,32.7,33.6,34.2,35.1,35.2,35.3,35.5,35.9,36  ,36.1,37.2],[36.7,36.9,37  ,37.5,38  ,38.1,38.4,38.7,38.8,38.9,36.3,38.9,39  ,39.1,39.4,39.4,39.5,39.8,40  ,40  ,40.1,36.3,32.8,34.2,34.7,34.9,34.9,35.3,35.9,36.4,36.6,36.6,38.3]])
print(spy.shapiro(additive[0]), spy.shapiro(additive[1]), sep='\n')
print(spy.wilcoxon(additive[0]-additive[1], alternative='greater'))
'''

associate = npy.array([[21 ,22 ,21 ,19 ,18 ,25 ,16 ,18 ,21 ,24 ,21],[14, 21, 24, 16, 18 ,20 ,15 ,20, 17, 16, 18]])
print(spy.wilcoxon(associate[0]-associate[1], alternative = 'greater'))


'''
--------------------------------------
NONPARAMETRIC ANOVA TEST
COMPLETELY RANDOMIZED DESIGN

aka krustal wallis h -test

H0: the k probabiltiy distributions are identical.
Ha: at least 2 of the k probability distributions differ in location

assumptions: 
- k samples are random and independent
- n>= 5 for each sample
- continuous data (can be broken sometimes)
'''

#ex

pties=npy.array([[149,139,139,49,59.0],[98,35,35,37,29.0],[104.0,99,99,29.97,142]])

print(spy.kruskal(*pties))


stay = [[1,3,4,6,7,7,7,9,9,13],[1,4,4,5,5,5,6,7,8,10],[1,1,5,5,5,7,8,8],[2,3,3,4,5,5,6,6,6]]

print(spy.kruskal(*stay, nan_policy='omit'))
#MAY NOT GIVE THE EXACT P VALUE, BE CAREFUL

'''
NONPARAMETRIC ANOVA TEST
RANDOMIZED BLOCK DESIGN
FRIEDSMAN SQUARE TEST

reduces variability as compared to completely randomized
df = k+1
     ^^^^^ df is +1 instead of -1

CONDITIONS:
treatments randomly assigned to experimental units within the blocks
measurements ranked within blocks
continuous data (to prevent ties)

HYPOTHESES: 
H0: probability distributions for the treatments are identical.
Ha: At least 2 of the probability distributions differ in location.

CHI SQUARE DISTRIBUTION  X^2
if Fr (test statistic) > X^2 reject null
'''

#INPUT THE TREATMENTS ONLY
rats = pd.DataFrame({1:[6,9,6,5,7,5,6,6],2:[5,8,9,8,8,7,7,5],3:[3,4,3,6,9,6,5,7]})


#treatments
print(spy.friedmanchisquare(list(rats[1]),list(rats[2]),list(rats[3])))
print(spy.levene(rats[1], rats[1],rats[2]))

month = npy.array([[12,16,18,8],[15,17,16,12],[18,15,22,10],[20,12,19,16]])
print(spy.friedmanchisquare(*month))

heartRate= npy.array([[124,100,103,94,125,103,98,119],[124,98,98,91,123,98,82,87],[109,98,100,98,106,100,99,106],[107,99,106,95,110,103,105,111]])
print(spy.friedmanchisquare(*heartRate))



#sample boxplots (for dataframes)
#rats.boxplot()
#plt.show()


'''
BOOTSTRAPPING:
takes small sample of data and simulate the sampling distribution
that should be gotten from the entire population

for loops !!!!!!!!!!!!!
a lot of samples
( usually 8 to 10000 )

repeat sample means a few thousand times
find a mean of all the sample means 
final standard error = sd of all means


^^^ DO MORE RESEARCH ON THIS
'''



'''
---------------------------------------------------
CHAPTER 13 NONPARAMETRIC CATEGORICAL TESTING


'''

'''
---------------
MULTINOMIAL EXPERIMENT

properties: 
n identical trials
k possible outcomes to each trial (usually classes, categories, or cells)
probabilities always equal 1 
trials are independent

basically binomial distribution but has mor ethan 2 categories
'''

#EX LEVEL OF EDUCATION BY EACH CANADIAN ACTORS
#categories: some hs, completed hs, some college, undergrad degree, and grad degree
 #   ^ 5 categories
 # 1 qualitative variable (# of actors)

obs = [30,25,20,5,6,4]


#print(spy.chisquare(obs))


#-------------------
'''
CHI SQUARE CONTINGENCY TABLE

IF THE TABLE IS A 2X2 YOU CAN USE FISHERS EXACT TEST

expected for Eij (i is row, j is column) = (row total * col total)/all total


conditions:
1: samples are randomly sampled
2: n>= 5 for every sample

hypotheses:
H0: 2 classifications are independent (usually row and column)
Ha: 2 classifications are dependent
2 qualitative variables
'''
data = npy.array([[39,25],[54,70]])

def sum(array2d):
     try:
          return sum([sum(x) for x in zip(*array2d)])
     except:
          return "not 2d array"
     


print("SUM OF A 2D ARRAY IS:", sep='\n')
      
print(spy.chi2_contingency(data))


extraci = npy.array([[9,17,7],[30,25,12]])
# GOES BY ROW COLUMN
print(spy.chi2_contingency(extraci))

#is there an association between categorical var a and b?
id = npy.array([[95,41],[50,114]])
print(spy.chi2_contingency(id, correction = True))
#SIMULATED P VALUE
print("fijsiofjhiodjhiudfhgufiughduk")

print("chi2 critical value: ", spy.chi2.ppf(1-0.05,12-1)) 
#confidence = (1-alpha) and df = (col-1)*(row-1)


def chi2_interval(givenn, samplen, confidence=0.95,):
    muP= givenn/float(samplen)
    std= sqrt(muP*(1-muP)/samplen) #estimate of std based on p
    return spy.norm.interval(confidence=confidence, loc=muP, scale=std)

print(chi2_interval(30,60))