from numpy import random
import numpy as np
from scipy.stats import norm
#Set random seed without leading 0 in CID
random.seed(2399744)

# Generate 10000 samples using the normal distribution approx
N = 10000
m = 50
theta = 0.45

def run_simulation(N, m, theta):
    samples = []
    for i in range(N):
        samples.append(random.binomial(1, theta, m))
        
    # Method 1 for confidence interval
        
    Z = norm.ppf(0.975)  # Z value for 95% confidence interval

    correct_samples = 0
    for i in range(N):
        theta_hat = np.mean(samples[i])
        upper_bound =(2*theta_hat+ Z**2/m + Z*np.sqrt(4*theta_hat/m + Z**2/m**2 - 4*(theta_hat**2)/m))/(2*(1+Z**2/m))
        lower_bound =(2*theta_hat+ Z**2/m - Z*np.sqrt(4*theta_hat/m + Z**2/m**2 - 4*(theta_hat**2)/m))/(2*(1+Z**2/m))
        if lower_bound <= theta <= upper_bound:
            correct_samples += 1

    print("Method 1: Proportion of confidence intervals containing theta:", correct_samples/N)

    # Method 2 for confidence interval

    #Fix Z value for 95% confidence interval
    Z = 1.96

    correct_samples = 0
    for i in range(N):
        theta_hat = np.mean(samples[i])
        upper_bound =(theta_hat + Z*np.sqrt((1/m) *theta_hat*(1-theta_hat)))
        lower_bound =(theta_hat - Z*np.sqrt((1/m) *theta_hat*(1-theta_hat)))
        if lower_bound <= theta <= upper_bound:
            correct_samples += 1

    print("Method 2: Proportion of confidence intervals containing theta:", correct_samples/N)

print("Running simulation with m =", m)
run_simulation(N, m, theta)

m = 20
print("Running simulation with m =", m)
run_simulation(N, m, theta)

m = 100
print("Running simulation with m =", m)
run_simulation(N, m, theta)