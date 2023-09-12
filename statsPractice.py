from asyncio.windows_events import NULL
import pandas as pd
import matplotlib.pyplot as plt
import scipy.stats as stats 
import statsmodels as s
#import statsmodels.stats.multitest as m
import numpy as npy #has : 
    #npy.mean (mean) 
    #npy.std (standard deviation) 
    #npy.var (variance) 
    #npy.sem (standard error)
    #stats.norm.interval (CI for mean) parameters: confidence = (confidence), loc = (mean), scale = (standard error)
    #note : standard error formula : std/m.sqrt(n)

import math as m

import csv
import statsmodels
import pyFunctions as s



data0 = [301, 305, 312, 315, 318, 319, 310, 318, 305, 313, 305, 305, 305, 311]
data1 = pd.read_csv("anova.csv") # opens the csv file
data2 = pd.read_csv("anova2.csv")
univ = data2[data2["Group"] == "University students"]
anova1 = [[3.7,1.2,4.1,5.4,2.5], [5.1,2.1,4.5,4.3], [1.1,0.8,2.3]]
anova2 = [[3.7,1.2,4.1,5.4,2.5], [5.1,2.1,4.5,4.3,4.2], [1.1,0.8,2.3,2.2,1.9]]
anova3 = [[3.7,1.2,4.1,5.4,2.5], [5.1,2.1,4.5,4.3,4.2], [1.1,0.8,2.3,2.2,1.9], [1.2,2.5,3.4,1.1,1.5]]
anova2Way = [[3.7,1.2,4.1,5.4,2.5], [5.1,2.1,4.5,4.3,4.2], [1.1,0.8,2.3,2.2,1.9], [1.2,2.5,3.4,1.1,1.5], [3.2,2.1,4.5,4.3,4.2], [5.1,1.9,4.5,2.2,4.2]]
#anovaDF = pd.DataFrame({'sample 1': anova1[0], 'sample 2': anova1[1], 'sample 3': anova1[2]})
dataframe1 = pd.DataFrame({'Fertilizer': npy.repeat(['daily', 'weekly'], 15),
                          'Watering': npy.repeat(['daily', 'weekly'], 15),
                          'height': [14, 16, 15, 15, 16, 13, 12, 11, 14, 
                                     15, 16, 16, 17, 18, 14, 13, 14, 14, 
                                     14, 15, 16, 16, 17, 18, 14, 13, 14, 
                                     14, 14, 15]})

dataframe2 = pd.DataFrame({
    'video': npy.repeat(['Violent', 'Non-violent'], 30),
    'student type': npy.repeat(['Volunteer', 'Psychology', 'Volunteer', 'Psychology'], 15),
    'rating':
        [4.1,3.5,3.4,4.1,3.7,2.8,3.4,4.0,2.5,3.0,3.4,3.5,3.2,3.1,2.4, # violent, volunteer
        3.4,3.9,4.2,3.2,4.3,3.3,3.1,3.2,3.8,3.1,3.8,4.1,3.3,3.8,4.5, # violent physcology
        2.4,2.4,2.5,2.6,3.6,4.0,3.3,3.7,2.8,2.9,3.2,2.5,2.9,3.0,2.4,    #non violent volunteer
        2.5,2.9,2.9,3.0,2.6,2.4,3.5,3.3,3.7,3.3,2.8,2.5,2.8,2.0,3.1]    #non violent psychology
})    


    


# 2 WAY ANOVAAAAAAAAAAAAAAAAAAAAAAA

print(dataframe1)

model = statsmodels.formula.api.ols('height ~ C(Fertilizer) + C(Watering) + C(Fertilizer):C(Watering)', data = dataframe1).fit()
result = statsmodels.stats.anova.anova_lm(model, type=2) #p vals: 0.9133, .99, .904

pVals = result.loc[:, 'PR(>F)'].values.tolist()
pVals.pop()


print(result, '\n', pVals)

#-------------------
    
    

print(dataframe2)

final = []
final.append([])
data3 = pd.read_csv("anova.csv").values.tolist()
#print(data3)


#key = data3[0][0]
#value = 0
#for rowName, data in data3:
#    if key != rowName:
#        value = value +1
#        final.append([])
#        key = rowName
#    
#    print(key)
#    final[value] += [data]  
#
#print(final)


with open("anova2.csv", 'r') as f:
    iterator = csv.reader(f) #csv.writer to write into the file
    
    next(iterator) # iterates over the column name for the loop
    

    #for line in iterator:  # iterator cycles through each row in tghe csv file
    #    print(line)

    #for line in iterator:
        #print(line[0], end=", ")  # iterates bjy column, if left blank iterates by row
        


#makes a new csv file and adds a tab delimiter 
#with open("pStat/anova2.csv", 'r') as f:
#    iterator = csv.reader(f)
#    
#    next(iterator)
#    
#    with open("new.csv", 'w') as file:
#        writeIt = csv.writer(file, delimiter='\t')
#        
#        for line in iterator:
#            writeIt.writerow(line)
        


#prints the boxplot out !!
#plt.show() top 5 lines, can be changed to any value
#plt.tail() bottom lines, can be changed to any value



#print(univ)
#
#print(data2.head())
#print(data2.tail())

data2.boxplot("Stress_score", by="Group")   # .boxplot(y axis, x axis)

#data2.plot.pie(y="Stress_score")
#plt.show()

print(2*(1-stats.f.cdf(1.083646869,24,24))) # two tail f test


#f.oneway method. only gives fstatistic and p value
fStat, pVal = stats.f_oneway(*anova1)  #asterisk specifies unlimited args, can input a list and itll open lists within that list
print(f"f stat:{fStat} \t p-value: {pVal}")
print(stats.tukey_hsd(*anova2))
#print(data1.values.tolist())
#stats.false_discovery_control()

dict = {}
for i, item in enumerate(anova2Way):
    dict.update({i: item})


df = pd.DataFrame(dict)
print(df)

df = pd.DataFrame(anova2, columns = ["high school", "fetus", "observer"])
print(df)

#2 WAY ANOVA TEST 


print(npy.repeat(['Violent', 'Non-violent'], 30))



