import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from scipy.stats import norm

# Parameters
pop_mean = 1
variance = 2
std_dev = np.sqrt(variance)
n = 1000       # original sample size
k = 100000     # number of resamples

#Generat base sample
sample = np.random.normal(loc=pop_mean, scale=std_dev, size=n)

# Resample K times
resample_means = []
for i in range(k):
    resample = np.random.choice(sample, size=n, replace=True)
    resample_means[i] = np.mean(resample)
resample_means = np.array(resample_means)

# Plot KDE
plt.figure(figsize=(8, 6))
sns.kdeplot(resample_means, fill=True, color='skyblue', label='Bootstrap KDE')

# Overlay theotrical pdf
x = np.linspace(min(resample_means), max(resample_means), 1000)
theoretical_pdf = norm.pdf(x, loc=pop_mean, scale=std_dev/np.sqrt(n))
plt.plot(x, theoretical_pdf, color='red', linestyle='--', label='Theoretical PDF')

plt.title(f'Bootstrap Distribution of Sample Mean (n={n}, k={k})')
plt.xlabel('Mean')
plt.ylabel('Density')
plt.legend()
plt.show()
