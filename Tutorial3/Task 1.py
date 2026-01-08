import numpy as np
from statsmodels.graphics.gofplots import qqplot
import matplotlib.pyplot as plt
import scipy.stats

N = 10000
lam = 1
u = np.random.random(N)

def inverseF(u, lam):
    return np.log(1-u)/(-lam)

PD = scipy.stats.expon
qqplot(inverseF(u, lam), PD , line ='45')
plt.show()


print (inverseF(u, lam))


