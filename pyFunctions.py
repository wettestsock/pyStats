import pandas as pd
import matplotlib.pyplot as plt
import scipy.stats as stats 
import numpy as npy #has : 
    #npy.mean (mean) 
    #npy.std (standard deviation) 
    #npy.var (variance) 
    #npy.sem (standard error)
    #stats.norm.interval (CI for mean) parameters: confidence = (confidence), loc = (mean), scale = (standard error)
    #note : standard error formula : std/m.sqrt(n)

import math as m

ROUND = 4   #decimal place to round, default 4, can make whatever
POSITION = "th"
match ROUND%10:
    case 1:
        POSITION = "st"
    case 2:
        POSITION = "nd"
    case 3:
        POSITION = "rd"
    


#TESTS ---------------------------

def MTestPRaw(data1, comparison, data2, alpha=0.05):
    # WIP. DOIESNTY WORK YET
    if len(data1)!=len(data2):
        print("This is not a paired t-test because the sample size is different.\n Consider using a 2 sample t test instead.\n")
        return
    
    difference = []
    
    
    

def MTestPData(SmeanDiff, stdDiff, comparison, n, alpha = 0.05):
    # STILL A WIP. DOESNT WORK YET. 
    SE = stdDiff/m.sqrt(n)
    tStat = SmeanDiff/SE   
    pVal = stats.t.cdf(tStat, n-1)
    sign = "!="
    
    print("---------------------")
    if comparison== "less" or comparison == "<":
        sign = "<"
    elif comparison == "greater" or comparison == ">":
        pVal = 1- pVal
        sign = ">"
    elif comparison == "not equal" or comparison == "!=": 
        pVal = 2*min(pVal, 1-pVal)
        
    else:
        print("|   No parameter or wrong comparison. Assumed \"not equal\"\n|   Acceptable inputs: \"less\", \"greater\", or \"not equal\".\n|   ")
        pVal = 2*min(pVal, 1-pVal)
        
    
    tStat = round(tStat, ROUND)
    pVal = round(pVal, ROUND)
    SE = round(SE, ROUND)
    
    
    print(f"|   PAIRED T TEST\n|   Rounded to the {ROUND}{POSITION} decimal.\n|   \t      H0:\tmd = 0\n|   \t      Ha:\tmu {sign} 0")
    print(f"|             df:\t{n-1}\n| standard error:\t{SE}\n|    t-statistic:\t{tStat}\n|        p-value:\t{pVal}")

    if (pVal<alpha):
        print(f"|   We reject the null because the p-value of {pVal} is less than a = {alpha}.\n|   Therefore, we have convincing evidence that...")
    else:
        print(f"|   We fail to reject the null because the p-value of {pVal} is greater than a = {alpha}.\n|   Therefore, we have do not have convincing evidence that...")
    print("---------------------\n")

def MTest1SRaw(data, comparison, popMean=0, alpha=0.05) :
    MTest1SData(npy.mean(data), comparison, popMean, npy.std(data), len(data), alpha)
    #print(stats.ttest_1samp(a = data, popmean = popMean, alternative= comp))

def MTest1SData(Smean, std, comparison, popMean, n, alpha=0.05):
    SE = std/m.sqrt(n)
    tStat = (Smean-popMean)/SE   
    pVal = stats.t.cdf(tStat, n-1)
    sign = "!="
    
    print("---------------------")
    if comparison== "less" or comparison == "<":
        sign = "<"
    elif comparison == "greater" or comparison == ">":
        pVal = 1- pVal
        sign = ">"
    elif comparison == "not equal" or comparison == "!=": 
        pVal = 2*min(pVal, 1-pVal)
        
    else:
        print("|   No parameter or wrong comparison. Assumed \"not equal\"\n|   Acceptable inputs: \"less\", \"greater\", or \"not equal\".\n|   ")
        pVal = 2*min(pVal, 1-pVal)
        
    
    tStat = round(tStat, ROUND)
    pVal = round(pVal, ROUND)
    SE = round(SE, ROUND)
    
    
    print(f"|   1 SAMPLE T TEST\n|   Rounded to the {ROUND}{POSITION} decimal.\n|   \t      H0:\tmu = {popMean}\n|   \t      Ha:\tmu {sign} {popMean}")
    print(f"|             df:\t{n-1}\n| standard error:\t{SE}\n|    t-statistic:\t{tStat}\n|        p-value:\t{pVal}")

    if (pVal<alpha):
        print(f"|   We reject the null because the p-value of {pVal} is less than a = {alpha}.\n|   Therefore, we have convincing evidence that...")
    else:
        print(f"|   We fail to reject the null because the p-value of {pVal} is greater than a = {alpha}.\n|   Therefore, we have do not have convincing evidence that...")
    print("---------------------\n")

def MTest2SRaw(data1, comparison, data2, alpha=0.05) :
    MTest2SData(npy.mean(data1), npy.std(data1), len(data1), comparison, npy.mean(data2), npy.std(data2), len(data2), alpha)
            

def MTest2SData(Smean1, std1, n1, comparison, Smean2, std2, n2, alpha=0.05):
    #df = (pow(pow(std1,2)/n1 + pow(std2,2)/n2 ,2))/((1/(n1-1))*(pow(std1,2)/n1)+(1/(n2-1))*(pow(std2,2)/n2))   #??? 
    SE1 = std1*std1/n1
    SE2 = std2*std2/n2
    SE = m.sqrt(SE1+SE2)
    tStat = (Smean1-Smean2)/SE
    df=int((SE1+SE2)**2/((SE1**2)/(n1-1) + (SE2**2)/(n2-1)))
    pVal = stats.t.cdf(tStat, df) # calculates pValue from (-9e999 to t statistic)
    8

    sign = "!="

    print("---------------------")
    if comparison== "less" or comparison == "<":
        sign = "<"
    elif comparison == "greater" or comparison == ">":
        pVal = 1-pVal
        sign = ">"
    elif comparison == "not equal" or comparison == "!=": 
        pVal = 2*min(pVal, 1-pVal)
        
    else:
        print("|   No parameter or wrong comparison. Assumed \"not equal\"\n|   Acceptable inputs: \"less\", \"greater\", or \"not equal\".\n|   ")
        pVal = 2*min(pVal, 1-pVal)
        
    
    df = round(df, ROUND)
    tStat = round(tStat, ROUND)
    pVal = round(pVal, ROUND)
    SE = round(SE, ROUND)
    
    print(f"|   WELCH'S 2 SAMPLE T TEST\n|   Rounded to the {ROUND}{POSITION} decimal.\n|   \t      H0:\tm1 = m2\n|   \t      Ha:\tm1 {sign} m2")
    print(f"|             df:\t{df}\n| standard error:\t{SE}\n|    t-statistic:\t{tStat}\n|        p-value:\t{pVal}")
    if (pVal<alpha):
        print(f"|   We reject the null because the p-value of {pVal} is less than a = {alpha}.\n|   Therefore, we have convincing evidence that...")
    else:
        print(f"|   We fail to reject the null because the p-value of {pVal} is greater than a = {alpha}.\n|   Therefore, we have do not have convincing evidence that...")
    print("---------------------\n")




#---------------------------------


#INTERVALS -----------------------

def MIntervalRaw(data, confidence) :
    MIntervalData(npy.mean(data), npy.std(data), len(data), confidence)

def MIntervalData(Smean, std, n, confidence):
    #ME = stats.t.ppf(confidence/2, n-1 ) #ppf -> inverse cdf (cumulative density function )
    lBound, uBound = stats.norm.interval(confidence = confidence, loc = Smean, scale = std/m.sqrt(n)) # steps :
    # stats.norm.interval , returns a tuple
    # assigns to lBound and uBound
    
    print("---------------------")
    print(f"|   We are {int(100*confidence)}% confident that the the true mean is between {round(lBound, ROUND)} and {round(uBound, ROUND)}.")
    print("---------------------\n")

def VIntervalRaw(data, confidence) :
    VIntervalData(npy.var(data), len(data)-1, confidence)

def VIntervalData(Svar, df, confidence):
    lBound = (df*Svar)/stats.chi2.ppf(1-(1-confidence)/2, df)
    uBound = (df*Svar)/stats.chi2.ppf(((1-confidence)/2), df)
    print("---------------------")
    print(f"|   We are {int(100*confidence)}% confident that the true variance is between {round(lBound,ROUND)} and {round(uBound,ROUND)}.")
    print("---------------------\n")

#----------------------------------

#OTHER FUNCTIONS ---------------

#idk not yet 

#---------------------


