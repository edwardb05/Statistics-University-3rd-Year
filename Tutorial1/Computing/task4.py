import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import statsmodels.tsa.tsatools as ts

df = pd.read_csv('Computing/faithful.csv')
n = len(df)
print(n)

lagduration = ts.lagmat(df["duration"],1).flatten() #Lagged duration shows duration of previous explosion, 1 is used to indicate one time step before, flatten to conver to a list
slope, intercept = np.polyfit(lagduration,df['waiting'],deg=1) #Fits a 1st degree (linear) line to the data
waitingest = slope*lagduration + intercept #Estimated waiting time from the linear regression

plt.plot(lagduration,waitingest,color='red',label='Linear regression fit')
plt.scatter(lagduration,df['waiting'])
plt.xlabel('Lagged duration (duration of previous eruption)')
plt.ylabel('Waiting time (mins)')
plt.legend() #Show labels
plt.show()