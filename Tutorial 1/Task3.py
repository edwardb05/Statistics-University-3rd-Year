import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

df = pd.read_csv('Tutorial 1/faithful.csv')
fig, axes = plt.subplots(3, 5, figsize=(6, 3)) #Initialize a 3x5 grid of subplots
axes = axes.flatten() #Flat to allow easier iteration
for day in range(1,16):
    subset = df.loc[df["day"] == day, "waiting"].reset_index(drop=True) #Select a subset for specific day and reset its index
    axes[day-1].plot(subset) #Plot the subset for that day on the axes
    axes[day-1].set_title(f'Day {day}')
    axes[day-1].set_xlim(0,16) #Set  constant x and y lims
    axes[day-1].set_ylim(40,120)

for i in range(10,15):
    axes[i].set_xlabel('Eruption number') #Add x labels to all graphs on the bottom
for i in range (0,3):
    axes[i*5].set_ylabel('Waiting time (mins)') #Add y labels to all graphs on the left

plt.tight_layout(pad=0.4) #Adjust spacing between plots using pad
plt.show()