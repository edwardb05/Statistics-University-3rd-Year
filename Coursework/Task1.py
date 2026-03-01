from numpy import random
import numpy as np
from scipy.stats import multivariate_normal 
from scipy.optimize import minimize

#Set random seed without leading 0 in CID
random.seed(2399744)

# Part 2 generate 100 x1 and x2 using the distributions worked out in the report
x1 = np.random.normal(0, np.sqrt(2), 100)
x2 = np.random.normal(1 - x1/2, np.sqrt(7/2))

# stack these together to get the data matrix
X = np.column_stack((x1, x2))


def negative_log(params):
    mu1, mu2, a, b, c = params
    
    L = np.array([
        [np.exp(a), 0],
        [b, np.exp(c)]
    ])
    
    cov_matrix = L @ L.T
    
    return -np.sum(
        multivariate_normal.logpdf(
            X,
            mean=[mu1, mu2],
            cov=cov_matrix
        )
    )


# initial guess for the parameters
initial_params = [0, 0, 0, 0, 0]

result = minimize(negative_log, initial_params)
L = np.array([
    [np.exp(result.x[2]), 0],
    [result.x[3], np.exp(result.x[4])]
])
    
cov_matrix = L @ L.T
print("MLE Estimates:")
print("mu1:", result.x[0])
print("mu2:", result.x[1])
print("Sigma:")
print(cov_matrix)