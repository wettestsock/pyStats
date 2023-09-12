from pandas import read_csv, DataFrame
from math import sqrt
from pandas._libs.lib import is_integer
from statsmodels.stats.anova import anova_lm
from statsmodels.formula.api import ols
from itertools import product
import matplotlib.pyplot as plt
import scipy.stats as stats 
import numpy as npy #has : 
    #npy.mean (mean) 
    #npy.std (standard deviation) 
    #npy.var (variance) 
    #npy.sem (standard error)
    #stats.norm.interval (CI for mean) parameters: confidence = (confidence), loc = (mean), scale = (standard error)
    #note : standard error formula : std/m.sqrt(n)  

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
    SE = stdDiff/sqrt(n)
    tStat = SmeanDiff/SE   
    pVal = stats.t.cdf(tStat, n-1)
    sign = "!="
    
    print("---------------------")
    if comparison== "less" or comparison == "<":
        sign = "<"
    elif comparison =="greater" or comparison == ">":
        pVal = 1- pVal
        sign = ">"
    elif comparison == "not equal" or comparison == "!=": 
        pVal = 2*min(pVal, 1-pVal)
        
    else:
        print("   No parameter or wrong comparison. Assumed \"not equal\"\n   Acceptable inputs: \"less\", \"greater\", or \"not equal\".\n   ")
        pVal = 2*min(pVal, 1-pVal)
        
    
    tStat = round(tStat, ROUND)
    pVal = round(pVal, ROUND)
    SE = round(SE, ROUND)
    
    
    print(f"   PAIRED T TEST\n   Rounded to the {ROUND}{POSITION} decimal.\n   \t      H0:\tmd = 0\n   \t      Ha:\tmu {sign} 0")
    print(f"             df:\t{n-1}\n standard error:\t{SE}\n    t-statistic:\t{tStat}\n        p-value:\t{pVal}")

    if (pVal<alpha):
        print(f"   We reject the null because the p-value of {pVal} is less than a = {alpha}.\n   Therefore, we have convincing evidence that...")
    else:
        print(f"   We fail to reject the null because the p-value of {pVal} is greater than a = {alpha}.\n   Therefore, we have do not have convincing evidence that...")
    print("---------------------\n")

def MTest1SRaw(data, comparison, popMean=0, alpha=0.05) :
    #1 sample t test raw data
    MTest1SData(npy.mean(data), comparison, popMean, npy.std(data), len(data), alpha)
    #print(stats.ttest_1samp(a = data, popmean = popMean, alternative= comp))

def MTest1SData(Smean, std, comparison, popMean, n, alpha=0.05):
    #1 sample t test
    SE = std/sqrt(n)
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
        print("   No parameter or wrong comparison. Assumed \"not equal\"\n   Acceptable inputs: \"less\", \"greater\", or \"not equal\".\n   ")
        pVal = 2*min(pVal, 1-pVal)
        
    
    tStat = round(tStat, ROUND)
    pVal = round(pVal, ROUND)
    SE = round(SE, ROUND)
    
    
    print(f"   1 SAMPLE T TEST\n   Rounded to the {ROUND}{POSITION} decimal.\n   \t     H0:\tmu = {popMean}\n   \t     Ha:\tmu {sign} {popMean}")
    print(f"             df:\t{n-1}\n standard error:\t{SE}\n    t-statistic:\t{tStat}\n        p-value:\t{pVal}")

    if (pVal<alpha):
        print(f"   We reject the null because the p-value of {pVal} is less than a = {alpha}.\n   Therefore, we have convincing evidence that...")
    else:
        print(f"   We fail to reject the null because the p-value of {pVal} is greater than a = {alpha}.\n   Therefore, we do NOT have convincing evidence that...")
    print("---------------------\n")

def MTest2SRaw(data1, comparison, data2, alpha=0.05) :
    # 2 sample t test raw data
    MTest2SData(npy.mean(data1), npy.std(data1), len(data1), comparison, npy.mean(data2), npy.std(data2), len(data2), alpha)
            

def MTest2SData(Smean1, std1, n1, comparison, Smean2, std2, n2, alpha=0.05):
    #2 sample t test
    #df = (pow(pow(std1,2)/n1 + pow(std2,2)/n2 ,2))/((1/(n1-1))*(pow(std1,2)/n1)+(1/(n2-1))*(pow(std2,2)/n2))   #??? 
    SE1 = std1*std1/n1
    SE2 = std2*std2/n2
    SE = sqrt(SE1+SE2)
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
        print("   No parameter or wrong comparison. Assumed \"not equal\"\n   Acceptable inputs: \"less\", \"greater\", or \"not equal\".\n   ")
        pVal = 2*min(pVal, 1-pVal)
        
    
    df = round(df, ROUND)
    tStat = round(tStat, ROUND)
    pVal = round(pVal, ROUND)
    SE = round(SE, ROUND)
    
    print(f"   WELCH'S 2 SAMPLE T TEST\n   Rounded to the {ROUND}{POSITION} decimal.\n   \t     H0:\tm1 = m2\n   \t     Ha:\tm1 {sign} m2")
    print(f"             df:\t{df}\n standard error:\t{SE}\n    t-statistic:\t{tStat}\n        p-value:\t{pVal}")
    if (pVal<alpha):
        print(f"   We reject the null because the p-value of {pVal} is less than a = {alpha}.\n   Therefore, we have convincing evidence that...")
    else:
        print(f"   We fail to reject the null because the p-value of {pVal} is greater than a = {alpha}.\n   Therefore, we do NOT have convincing evidence that...")
    print("---------------------\n")




#---------------------------------


#INTERVALS -----------------------

def MIntervalRaw(data, confidence) :
    #raw data mean interval 
    MIntervalData(npy.mean(data), npy.std(data), len(data), confidence)

def MIntervalData(Smean, std, n, confidence):
    #mean interval
    #ME = stats.t.ppf(confidence/2, n-1 ) #ppf -> inverse cdf (cumulative density function )
    lBound, uBound = stats.norm.interval(confidence = confidence, loc = Smean, scale = std/sqrt(n)) # steps :
    # stats.norm.interval , returns a tuple
    # assigns to lBound and uBound
    
    print("---------------------")
    print(f"   We are {int(100*confidence)}% confident that the the true mean is between {round(lBound, ROUND)} and {round(uBound, ROUND)}.")
    print("---------------------\n")

def VIntervalRaw(data, confidence) :
    #variance interval with raw data
    VIntervalData(npy.var(data), len(data)-1, confidence)

def VIntervalData(Svar, df, confidence):
    #variance interval 
    lBound = (df*Svar)/stats.chi2.ppf(1-(1-confidence)/2, df)
    uBound = (df*Svar)/stats.chi2.ppf(((1-confidence)/2), df)
    print("---------------------")
    print(f"   We are {int(100*confidence)}% confident that the true variance is between {round(lBound,ROUND)} and {round(uBound,ROUND)}.")
    print("---------------------\n")

#----------------------------------

#ANOVA AND PAIRWISE -------------

def AOne(twoDimensionalList, alpha = 0.05):
    #one way anova , not rly necessary (already included) but is nice to have 
    #note: anova can be used for a 2 sample test, so the exception is handled in the interpretations
    #i code in the interpretation
    fStat, pVal = stats.f_oneway(*twoDimensionalList)
    null, alternate, final = "= ... =", "At least two treatment means differ", " the mean difference between at least two populations is not 0."
    if len(twoDimensionalList)==2:
        null, alternate, final = "=", "m1 != m2", "..."
    
    fStat = round(fStat,ROUND)
    pVal = round(pVal, ROUND)
    
    print("---------------------")
    print(f"   ONE-WAY ANOVA TEST\n   Rounded to the {ROUND}{POSITION} decimal.\n   \t     H0:\tm1 {null} m2\n   \t     Ha:\t{alternate}")
    print(f"    f-statistic:\t{fStat}\n        p-value:\t{pVal}")
    if (pVal<alpha):
        print(f"   We reject the null because the p-value of {pVal} is less than a = {alpha}.\n   Therefore, we have convincing evidence that{final}")
    else:
        print(f"   We fail to reject the null because the p-value of {pVal} is greater than a = {alpha}.\n   Therefore, we do NOT have convincing evidence that{final}")
    print("---------------------\n")
    
def ATwo(values, horizontalFName= "treatment", horizontalFNum=2, verticalFName = "block", verticalFNum=2, alpha=0.05):
    #WIP
    l = len(values)
    print("---------------------")
    if l == horizontalFNum*verticalFNum:
        print("ERROR: EACH CELL CONTAINS 1 SAMPLE.\n Samples are being compared, not means. >:(")
        print("---------------------\n")
        return
    if l%2 != 0:
        print("ERROR: ODD SAMPLE SIZE. CHOOSING TO NOT CUT OFF.")
        print("---------------------\n")
        return
    if not (l/(horizontalFNum*verticalFNum)).is_integer():
        print("NUCLEAR ALARM: INVALID HORIZONTAL/VERTICAL FACTOR AMOUNTS.\nHorizontal times vertical factor groups DO NOT evenly split the values.")
        print("---------------------\n")
        return
    #i did it

    f1Groups, f2Groups = [], []
    for i in range(verticalFNum):
        f2Groups.append(f'({verticalFName} - {str(i+1)})')
    for i in range(horizontalFNum):
        f1Groups.append(f'({horizontalFName} - {str(i+1)})')
    
    df = DataFrame({
    horizontalFName : npy.repeat(f1Groups,l/horizontalFNum),
    verticalFName: npy.repeat(f2Groups, l/verticalFNum/2),
    'data': values
    })

    #l/(horizontalFName*verticalFName)
    
    #c = list(product([horizontalFName + ' - '+ str(x+1) for x in range(horizontalFNum)], [verticalFName + ' - '+ str(i+1) for i in range(verticalFNum)]))
    #c = [npy.repeat(i, l/(horizontalFNum*verticalFNum)) for i in c]
    #
    #df = DataFrame({
    #horizontalFName : [i[0] for i in c],
    #verticalFName: [i[1] for i in c],
    #'data': values
    #})
    
    model = ols('data ~ C({0}) + C({1}) + C({0}):C({1})'.format(horizontalFName , verticalFName ), data = df).fit()
    result = anova_lm(model, type=2) #p vals: 0.9133, .99, .904
    
    pVals = result.loc[:, 'PR(>F)'].values.tolist()
    pVals.pop()
    pVals = [round(n, ROUND) for n in pVals]
    
    print(df)
    print(f"\n   2-WAY ANOVA\n   OR A FACTORIAL EXPERIMENT\n   OR A RANDOMIZED   BLOCK DESIGN\n    Rounded to the {ROUND}{POSITION} decimal.")
    
    print(result, '\n', pVals)
    
    #print(npy.repeat(f1Groups,l/horizontalFNum))
    #print(npy.repeat(f2Groups,l/verticalFNum))
    #print(f1Groups)    
    #print(f2Groups)


def PComparison(twoDimensionalList, alpha =0.05):
    #pairwise comparison using tukey method
    #works for unequal sample sizes too
    
    result = stats.tukey_hsd(*twoDimensionalList)
    result.confidence_interval(confidence_level = 1-alpha)
    conf = result.confidence_interval(confidence_level = 1-alpha)
    
    print("---------------------")
    print(f"   PAIRWISE COMPARISON TEST\n   Rounded to the {ROUND}{POSITION} decimal.\n{result}")
    
    for ((i,j), pVal) in npy.ndenumerate(result.pvalue):
        if i==j:
            continue
        print(f" ({i} - {j}): ", end = "")
        if pVal < alpha and 0 not in npy.arange(conf.low[i,j], conf.high[i,j]):
            print(f"REJ the null ({i} = {j}). Therefore DIFFERENT, alt is true ({i} != {j})")
        else:
            print(f"FTR the null ({i} = {j}). Therefore NO DIFFERENCE, alt is false ({i} != {j})")
    print("---------------------\n")
        
        
     


    



#-----------------------------

#OTHER FUNCTIONS ---------------


def csvFileToList(relativePath):
    #quick conversion from csv file to list
    return dfToList(read_csv(relativePath))

def dfToList(DataFrame): 
    #DataFrame object to a List (not dictionary)
    #essential for anova and whatever
    data = DataFrame.values.tolist()
    final = []
    final.append([])
    key = data[0][0]
    value = 0
    for rowName, val in data:
        if key != rowName:
            value = value +1
            final.append([])
            key = rowName
      
        
        final[value] += [val] 
    return final

def listToDF(twoDimensionalList):
    #converts list to a dictionary before converting to a dataframe 
    #list to a dataframe takes each list in the list as a row
    #this one makes each list a column with columns 0 through n-1
    #where n is the # of columns 
    return DataFrame(listToDict(twoDimensionalList))

def listToDict(twoDimensionalList):
    #list to dataframe object, where each list within the list represents a column (starting index 0)
    dict = {}
    for i, item in enumerate(twoDimensionalList):
        dict.update({i: item})
    return dict
    


#idk not yet 

#---------------------


