import numpy as np
import matplotlib.pyplot as plt
from scipy.stats import poisson, norm
import seaborn as sns
#Produce plot for the probality mass function and cumulative distribution function for lambda

lambda_poisson = 3
x_poisson = np.arange(0, 10)
pmf_poisson = poisson.pmf(x_poisson, lambda_poisson)
cdf_poisson = poisson.cdf(x_poisson, lambda_poisson)

y = np.random.poisson(lambda_poisson, 10000)
print("Mean of generated Poisson values:", np.mean(y))
print("Variance of generated Poisson values:", np.var(y))x
y = y[y <= 10]

counts, _ = np.histogram(y, bins=np.arange(-0.5, 10.5, 1))
freqs = counts / counts.sum()  # normalize to make it sum to 1
plt.figure(figsize=(12,5))
plt.subplot(1,2,1)
#Draws a stem for poisson pmf
plt.stem(x_poisson, pmf_poisson, linefmt='b-') 
plt.stem(x_poisson, freqs, linefmt='r-') 
plt.title('Poisson PMF (λ=3)')

#Draw a step for poisson cdf
plt.subplot(1,2,2)
plt.step(x_poisson, cdf_poisson, where='mid')
plt.title('Poisson CDF (λ=3)')
plt.show()

#Conitnius normal distrivution func
mu, sigma = 0, 2
x_normal = np.linspace(-10, 10, 200)

#shows pdf and cdf for normal distribution
pdf_normal = norm.pdf(x_normal, mu, sigma)
cdf_normal = norm.cdf(x_normal, mu, sigma)

# verifying identity by generating random normal values
x = np.random.normal(mu, sigma, 1000000)

var = np.var(x)
print("Variance of generated normal values:", var)
# plotting probability density function and cumulative distribution function
plt.subplot(1,2,1)
plt.plot(x_normal, pdf_normal, color='blue', label='Theoretical PDF')
sns.kdeplot(x=x, color='red', label='Empirical KDE', fill=True, alpha=0.3)
plt.title('Normal PDF (μ=0, σ=2)')
plt.xlabel('x')
plt.ylabel('Density')
plt.legend()

plt.subplot(1,2,2)
plt.plot(x_normal, cdf_normal)
plt.title('Normal CDF (μ=0, σ=2)')
plt.show()
