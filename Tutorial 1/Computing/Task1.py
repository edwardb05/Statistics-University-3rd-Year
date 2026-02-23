import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

df = pd.read_csv('Computing/faithful.csv')
waiting = df["waiting"]
mean = np.mean(waiting)
sns.boxplot(y=df['waiting'], x = df['day'], whis= 2) #Plots box plot and whis changes max len of whiskers it is that value times the IQR
plt.xlabel('Day')
plt.ylabel('Waiting time between eruptions (in mins)')
plt.show()
print(mean)