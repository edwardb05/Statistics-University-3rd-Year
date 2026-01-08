import numpy as np
from statsmodels.graphics.gofplots import qqplot
from scipy.stats import norm
import matplotlib.pyplot as plt

N = 10000
mu = 0 
sigmasqrd = 1


z = np.sqrt(-2*np.log(np.random.random(N))) * np.cos(2*np.pi*np.random.random(N))
x = mu + np.sqrt(sigmasqrd) * z

qqplot(x, norm , line ='45')
plt.show()