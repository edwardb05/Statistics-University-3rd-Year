import pandas as pd
import numpy as np
import matplotlib.pyplot as plt



df = pd.Series([15, 25, 22, 31, 25, 19, 8, 24, 44, 30, 34, 12, 7, 33, 19, 20, 19, 42, 38, 27])
plt.hist(df, bins=10, edgecolor='black')
plt.axvline(df.mean(), color = 'red', label = 'mean')
plt.axvline(df.var(), color = 'green', label = 'Sample Var') 
plt.axvline(df.median(), color = 'blue', label = 'Median')
plt.legend()
plt.show()

