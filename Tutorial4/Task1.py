import numpy as np
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt


# Plotting Multivariate Normal Samples - can see how different means and sigmas affect the distribution
def generatex():
    #Vector of 3 random normal variables
    Z =np.array([ np.random.randn(), np.random.randn(), np.random.randn()])

    #Mean vector and covariance matrix
    mu = np.array([ -1, 0, 2])
    Sigma = np.array([ [1, 0.5, 0], [0.5,2,0], [0,0,0.5]])

    x = mu + np.linalg.cholesky(Sigma)@(Z)   
    return x

#Run the function multiple times to generate samples
n=1000
samples = np.array([generatex() for _ in range(n)])

df = pd.DataFrame(samples, columns=['X1', 'X2', 'X3'])
#plot a pairplot
sns.pairplot(df)
plt.show()