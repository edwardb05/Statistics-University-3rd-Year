import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

df = pd.read_csv('Tutorial 1/faithful.csv')
min_wait = np.min(df["waiting"])
max_wait = np.max(df["waiting"])
for i in range (3):
    bins = np.linspace(min_wait, max_wait, (i**2+1)*10)
    # np.histogram(df["waiting"], bins=bins)
    sns.distplot(df["waiting"], bins=bins) #histogram with a density plot
    plt.xlabel('Waiting time between eruptions (in mins)')
    plt.show()
sns.kdeplot(df["waiting"])
sns.kdeplot(df["waiting"], bw_adjust=0.75)
sns.kdeplot(df["waiting"], bw_adjust=2) #visualizes the distribution of points, the bandwidth controls the smoothness
plt.xlabel('Waiting time between eruptions (in mins)')
plt.show()
