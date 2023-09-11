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


data0 = [301, 305, 312, 315, 318, 319, 310, 318, 305, 313, 305, 305, 305]
data1 = pd.read_csv("anova.csv") # opens the csv file
data2 = pd.read_csv("anova2.csv")
univ = data2[data2["Group"] == "University students"]
anova1 = [[3.7,1.2,4.1,5.4,2.5], [5.1,2.1,4.5,4.3], [1.1,0.8,2.3]]
anova2 = [[3.7,1.2,4.1,5.4,2.5], [5.1,2.1,4.5,4.3,4.2], [1.1,0.8,2.3,2.2,1.9]]
#anovaDF = pd.DataFrame({'sample 1': anova1[0], 'sample 2': anova1[1], 'sample 3': anova1[2]})


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


df = pd.DataFrame(anova2, columns = ["high school", "fetus", "observer"])
print(df)



