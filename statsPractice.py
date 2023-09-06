from asyncio.windows_events import NULL
import numpy as npy
import scipy.stats as stats
import matplotlib.pyplot as plt
import pandas as pd
import csv


data0 = [301, 305, 312, 315, 318, 319, 310, 318, 305, 313, 305, 305, 305]
data1 = pd.read_csv("anova.csv") # opens the csv file
data2 = pd.read_csv("anova2.csv")


with open("anova2.csv", 'r') as f:
    iterator = csv.reader(f) #csv.writer to write into the file
    
    next(iterator) # iterates over the column name for the loop
    

    #for line in iterator:  # iterator cycles through each row in tghe csv file
    #    print(line)

    for line in iterator:
        print(line[0], end=", ")  # iterates bjy column, if left blank iterates by row
        


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



univ = data2[data2["Group"] == "University students"]
print(univ)

print(data2.head())
print(data2.tail())

data2.boxplot("Stress_score", by="Group")   # .boxplot(y axis, x axis)

data2.plot.pie(y="Stress_score")
plt.show()

print(2*(1-stats.f.cdf(1.083646869,24,24))) # two tail f test


t = [[3.7,1.2,4.1,5.4,2.5], [5.1,2.1,4.5,4.3], [1.1,0.8,2.3]]

fStat, pVal = stats.f_oneway(t[0], t[1],t[2])


print(fStat, pVal)

