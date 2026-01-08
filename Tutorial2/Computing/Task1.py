from numpy import random 
import seaborn as sns
import numpy as np
import matplotlib.pyplot as plt
def runtest():
    athletes = {}
    for i in range(1,101):
        athletes[i] =(random.randint(1,11), random.randint(1,11),random.randint(1,11))


    failed_tests = []
    for i in range (1,101):
        if (athletes[i][0]==1 and athletes[i][1] >=3 and athletes[i][2]>=3 )or (athletes[i][0]>=2 and athletes[i][1] <=2 and athletes[i][2] <=2):
            failed_tests.append(i)

    drugtakers = 0
    for i in failed_tests:
        if athletes[i][0]==1:
            drugtakers +=1
            
    return drugtakers/len(failed_tests)

percentages = []
for i in range(1000):
    percentages.append(runtest())

bins = np.linspace(min(percentages), max(percentages), 30)
# np.histogram(df["waiting"], bins=bins)
sns.distplot(percentages, bins=bins) #histogram with a density plot
plt.xlabel('Percentage of drug takers among athletes who failed the test')
plt.show()