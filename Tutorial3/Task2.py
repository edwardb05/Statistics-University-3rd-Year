import numpy as np
from statsmodels.graphics.gofplots import qqplot
import matplotlib.pyplot as plt
from scipy.stats import poisson

N = 10000
mu = 3
u = np.random.random(N)

def inverseF(u):
    return poisson.ppf(u, mu)

PD = poisson(mu)
qqplot(inverseF(u), PD , line ='45')
plt.show()



