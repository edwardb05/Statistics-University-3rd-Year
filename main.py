import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

df = pd.read_csv('faithful.csv')
print(df.head())
waiting = df["waiting"]
mean = np.mean(waiting)
sns.boxplot(y=df['waiting'], x = df['day'], whis= 2)
plt.xlabel('Day')
plt.ylabel('Waiting time between eruptions (in mins)')
plt.show()
print(mean)