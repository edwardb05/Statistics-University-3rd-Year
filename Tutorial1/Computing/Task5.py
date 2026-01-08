
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import statsmodels.tsa.tsatools as ts
from sklearn.cluster import KMeans

df = pd.read_csv('Tutorial 1/Computing/faithful.csv')
n = len(df)
K=2 #Number of clusters

colors = ['red', 'green', 'blue', 'black', 'purple', 'orange'] #Colors for each cluster
lagduration = ts.lagmat(df["duration"],1).flatten() #Lagged duration shows duration of previous explosion, 1 is used to indicate one time step before, flatten to conver to a list
lagwaitingtime = ts.lagmat(df["waiting"],1).flatten() 

# X = pd.DataFrame({'lagduration': lagduration, 'waiting': df['waiting'] }) Create a new dataframe with lagged duration and waiting time
X = pd.DataFrame({ 'lagwaitingtime': lagwaitingtime, 'waiting': df['waiting'] })  #Create a new dataframe with lagged waiting time and waiting time
C = KMeans(n_clusters=K, random_state=0).fit(X) #Fit the model to the data, C will contain the cluster labels


# for i in range(K):
#     label_i = X.loc[C.labels_==i]
#     plt.scatter(x=label_i['lagduration'], y=label_i['waiting'], color = colors[i])

for i in range(K): #Loop over each cluster and find values in that cluster
    label_i = X.loc[C.labels_==i]
    plt.scatter(x=label_i['lagwaitingtime'], y=label_i['waiting'], color = colors[i])


# plt.xlabel('Lagged duration (duration of previous eruption)')

plt.xlabel('Lagged waiting time (waiting time of previous eruption)')
plt.ylabel('Waiting time (mins)')

plt.show()
