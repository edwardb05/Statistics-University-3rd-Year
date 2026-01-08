import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from scipy.stats import norm, trim_mean
import pandas as pd

#Generat base sample
sample = pd.read_csv('Tutorial1/Computing/faithful.csv')['waiting'].values

# Parameters
pop_mean = np.mean(sample)
variance = np.var(sample, ddof=1)
std_dev = np.sqrt(variance)
median = np.median(sample)
k = 100000     # number of resamples

n = len(sample)

# Resample K times
resample_means = np.empty(k)
resample_medians = np.empty(k)
resample_trimmeans = np.empty(k)
for i in range(k):
    resample = np.random.choice(sample, size=n, replace=True)
    resample_means[i] = np.mean(resample)
    resample_medians[i] = np.median(resample) 
    resample_trimmeans[i] = trim_mean(resample, proportiontocut=0.05)


plt.figure(figsize=(15, 5))
# Plot KDE
plt.subplot(1, 3, 1)
sns.kdeplot(resample_means, fill=True, color='skyblue', label='Bootstrap KDE')

# Overlay theotrical pdf
x = np.linspace(min(resample_means), max(resample_means), 1000)
theoretical_pdf = norm.pdf(x, loc=pop_mean, scale=std_dev/np.sqrt(n))
plt.plot(x, theoretical_pdf, color='red', linestyle='--', label='Theoretical PDF')

plt.title(f'Bootstrap Distribution of Sample Mean (n={n}, k={k})')
plt.xlabel('Mean')
plt.ylabel('Density')
plt.legend()

# 2. Median
plt.subplot(1, 3, 2)
sns.kdeplot(resample_medians, fill=True, color='lightgreen', label='Bootstrap Median KDE')
plt.title('Bootstrap Distribution of Median')
plt.xlabel('Median')
plt.ylabel('Density')
plt.legend()

# 3. 5% Trimmed Mean
plt.subplot(1, 3, 3)
sns.kdeplot(resample_trimmeans, fill=True, color='salmon', label='Bootstrap 5% Trimmed Mean KDE')
plt.title('Bootstrap Distribution of 5% Trimmed Mean')
plt.xlabel('Trimmed Mean')
plt.ylabel('Density')
plt.legend()

plt.tight_layout()
plt.show()


