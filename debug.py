import pyFunctions as s


#testing and debugging purposes. anova.csv and anova2.csv is extra data. 


dataa = [301, 305, 312, 315, 318, 319, 310, 318, 305, 313, 305, 305, 305, 311] # 14 values
data0 = [301, 305, 312, 315, 318, 319, 310, 318, 305, 313, 305, 305, 305, 311,230,322] # 16 values
data1 = [85, 90, 94, 89, 90, 93, 95, 96, 92, 93, 93 ,95]
data2 = [13.3, 6.0, 20.0, 8.0, 14.0, 19.0, 18.0, 25.0, 16.0, 24.0, 15.0, 1.0, 15.0]
data3 = [22.0, 16.0, 21.7, 21.0, 30.0, 26.0, 12.0, 23.2, 28.0, 23.0]
data4 = [14, 15, 15, 15, 16, 18, 22, 23, 24, 25, 25]
data5 = [14, 15, 15, 15, 16, 18, 22, 23, 24, 25, 25]
data6 = [10, 12, 14, 15, 18, 22, 24, 27, 31, 33, 34, 34]
data7 = s.read_csv("anova.csv")
data8 = s.read_csv("anova2.csv")
anova1 = [[3.7,1.2,4.1,5.4,2.5], [5.1,2.1,4.5,4.3], [1.1,0.8,2.3]]
anova2 = [[3.7,1.2,4.1,5.4,2.5], [5.1,2.1,4.5,4.3,4.2], [1.1,0.8,2.3,2.2,1.9]]
anova3 = [[3.7,1.2,4.1,5.4,2.5], [5.1,2.1,4.5,4.3,4.2], [1.1,0.8,2.3,2.2,1.9,2.2]]

dataframe0 = [4.1,3.5,3.4,4.1,3.7,2.8,3.4,4.0,2.5,3.0,3.4,3.5,3.2,3.1,2.4, # violent, volunteer
        3.4,3.9,4.2,3.2,4.3,3.3,3.1,3.2,3.8,3.1,3.8,4.1,3.3,3.8,4.5, # violent physcology
        2.4,2.4,2.5,2.6,3.6,4.0,3.3,3.7,2.8,2.9,3.2,2.5,2.9,3.0,2.4,    #non violent volunteer
        2.5,2.9,2.9,3.0,2.6,2.4,3.5,3.3,3.7,3.3,2.8,2.5,2.8,2.0,3.1]    #non violent psychology
        #60 values 

dataframe1 = s.DataFrame({
    'video': s.npy.repeat(['Violent', 'Non-violent'], 30),
    'student type': s.npy.repeat(['Volunteer', 'Psychology', 'Volunteer', 'Psychology'], 15),
    'rating':
        [4.1,3.5,3.4,4.1,3.7,2.8,3.4,4.0,2.5,3.0,3.4,3.5,3.2,3.1,2.4, # violent, volunteer
        3.4,3.9,4.2,3.2,4.3,3.3,3.1,3.2,3.8,3.1,3.8,4.1,3.3,3.8,4.5, # violent physcology
        2.4,2.4,2.5,2.6,3.6,4.0,3.3,3.7,2.8,2.9,3.2,2.5,2.9,3.0,2.4,    #non violent volunteer
        2.5,2.9,2.9,3.0,2.6,2.4,3.5,3.3,3.7,3.3,2.8,2.5,2.8,2.0,3.1]    #non violent psychology
})    
print(dataframe1)
  
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

s.AOne(anova2)


s.PComparison(anova3, alpha = 0.05)

#s.ATwo(data0, horizontalGroupNum=4, verticalGroupNum=2)

#anova3 data:
#Comparison  Statistic  p-value  Lower CI  Upper CI
# (0 - 1)      4.426     0.540    -5.462    14.313
# (0 - 2)     15.512     0.001     5.915    25.110
# (1 - 0)     -4.426     0.540   -14.313     5.462
# (1 - 2)     11.087     0.026     1.056    21.117
# (2 - 0)    -15.512     0.001   -25.110    -5.915
# (2 - 1)    -11.087     0.026   -21.117    -1.056


# 2 WAY ANOVA PRACTICE

print(s.stats.f.ppf(q=1-0.01, dfn= 2, dfd= 18)) #f statistic critical value for treatment
print(1-s.stats.f.cdf(x=3.6, dfn= 2, dfd = 18)) # p value treatment given f statistic (x) 
                                                # df numerator = (a-1) df denominator = (a-1)(b-1)



print(s.stats.f.ppf(q=1-0.05, dfn= 2, dfd= 18)) #f statistic critical value  for block
print(1-s.stats.f.cdf(x=1.2, dfn= 9, dfd = 18)) # p value block given f statistic (x) 
                                                # df numerator = (b-1) df denominator = (a-1)(b-1)



print(s.stats.f.ppf(q=1-0.05, dfn= 2, dfd= 18)) #f statistic critical value  for block
print(1-s.stats.f.cdf(x=4, dfn= 9, dfd = 18)) # p value block given f statistic (x) 
              # df numerator = (b-1) df denominator = (a-1)(b-1)



# p value from chi square : 1-s.stats.chi2.cdf(chisq, df)



d = [1.64 ,1.47 ,1.8  ,1.37 ,1.71 ,1.71 ,1.81 ,1.51 ,1.63 ,1.65 ,1.35 ,1.45 ,1.66 ,1.44 ,2.35 ,2.84 ,2.97 ,2.05 ,2.54 ,2.82 ,2.93 ,2.93 ,2.63 ,2.72 ,2.61 ,2.99 ,2.64 ,2.19]
#s.ATwo(d,horizontalFName = 'diet', verticalFName = 'rat_size')


df = s.DataFrame({"diet": s.npy.repeat(['regular', 'vitamin', 'regular', 'vitamin'], 7),
                  "size": s.npy.repeat(['lean', 'obese'], 14),
                  "data": d})

model = s.ols("data ~ C(diet) + C(size) + C(diet):C(size)", data = df).fit()




print(df)
print(s.anova_lm(model, type=2))

name = input("type ur name: ")
print(name)


print('I GOT LINUX')