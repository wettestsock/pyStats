import pyFunctions as s


#testing and debugging purposes. anova.csv and anova2.csv is extra data. 

data1 = [85, 90, 94, 89, 90, 93, 95, 96, 92, 93, 93 ,95]
data2 = [13.3, 6.0, 20.0, 8.0, 14.0, 19.0, 18.0, 25.0, 16.0, 24.0, 15.0, 1.0, 15.0]
data3 = [22.0, 16.0, 21.7, 21.0, 30.0, 26.0, 12.0, 23.2, 28.0, 23.0]
data4 = [14, 15, 15, 15, 16, 18, 22, 23, 24, 25, 25]
data5 = [14, 15, 15, 15, 16, 18, 22, 23, 24, 25, 25]
data6 = [10, 12, 14, 15, 18, 22, 24, 27, 31, 33, 34, 34]
data7 = s.pd.read_csv("anova.csv")
data8 = s.pd.read_csv("anova2.csv")
anova1 = [[3.7,1.2,4.1,5.4,2.5], [5.1,2.1,4.5,4.3], [1.1,0.8,2.3]]
anova2 = [[3.7,1.2,4.1,5.4,2.5], [5.1,2.1,4.5,4.3,4.2], [1.1,0.8,2.3,2.2,1.9]]
  
s.VIntervalRaw(data1, 0.95) # (4.4711, 25.6849)
s.MIntervalRaw(data1, 0.95) # (90.3945, 93.7722)

s.MTest1SData(Smean = 44.9, comparison="!=", popMean=40, std=8.9,n=15,alpha =0.05) # (H0: mu = 40, HA: mu != 40,t: 2.1323, p: 0.0512, FTR)
s.MTest2SData(300,18.5,40,"!=",305,16.7,38) # SE: 3.9869, t: -1.2541, p: 0.2137, a: 0.05 ( default)
s.MTest2SData(252, 282, 20, "!=", 187,32,24)
s.MTest2SRaw(data4, "!=", data6)
s.MTestPRaw(data1, "!=", data6)


#prints the csv files as lists
print(s.csvFileToList("anova2.csv"))
print(s.dfToList(data7))


print(s.stats.tukey_hsd(*s.csvFileToList("anova.csv")))
#Comparison  Statistic  p-value  Lower CI  Upper CI
# (0 - 1)      4.426     0.540    -5.462    14.313
# (0 - 2)     15.512     0.001     5.915    25.110
# (1 - 0)     -4.426     0.540   -14.313     5.462
# (1 - 2)     11.087     0.026     1.056    21.117
# (2 - 0)    -15.512     0.001   -25.110    -5.915
# (2 - 1)    -11.087     0.026   -21.117    -1.056
