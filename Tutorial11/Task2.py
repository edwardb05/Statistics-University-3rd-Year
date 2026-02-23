import matplotlib.pyplot as plt

#dataset
x = [5, 3, -1, 2, 7, 6, 4]
y = [4, 3, 0, 1, 8, 5, 3]

n = len(x)

# Create scatter plot
plt.scatter(x, y)

# Labels and title
plt.xlabel("X values")
plt.ylabel("Y values")


sum_x = sum(x)
sum_y = sum(y)
sum_xy = sum(x[i] * y[i] for i in range(n))
sum_x2 = sum(xi**2 for xi in x)

# Beta (slope) calculation
beta = (n * sum_xy - sum_x * sum_y) / (n * sum_x2 - sum_x**2)

#Means
x_bar = sum_x / n
y_bar = sum_y / n

# Intercept (alpha)
alpha = y_bar - beta * x_bar

print(f"Alpha (intercept): {alpha}")
print(f"Beta (slope): {beta}")  
plt.show()