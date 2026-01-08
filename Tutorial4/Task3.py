import numpy as np
import matplotlib.pyplot as plt

# Function to generate one sample (x, y)
def generate_xy():
    u1, u2 = np.random.rand(2)
    
    # Solve cubic for Y: 2y^3 + 3y - 5*u1 = 0
    coeffs_y = [2, 0, 3, -5*u1]
    roots_y = np.roots(coeffs_y)
    y = roots_y[np.isreal(roots_y)].real
    y = y[y >= 0][0]  # positive real root
    
    # Solve quadratic for X given Y: x^2 + 2y^2 x - u2*(1 + 2*y^2) = 0
    coeffs_x = [1, 2*y**2, -u2*(1 + 2*y**2)]
    roots_x = np.roots(coeffs_x)
    x = roots_x[np.isreal(roots_x)].real
    x = x[x >= 0][0]  # positive real root
    
    return x, y

# Generate samples
n = 1000
pairs = np.array([generate_xy() for _ in range(n)])
x_vals = pairs[:,0]
y_vals = pairs[:,1]

# Define the theoretical joint PDF
def f_xy(x, y):
    return 6/5*(x+y**2)

# Create meshgrid for contour plot
x_grid = np.linspace(0, 1, 100)
y_grid = np.linspace(0, 1, 100)
X, Y = np.meshgrid(x_grid, y_grid)
Z = f_xy(X, Y)

# Plot scatter + contour
plt.figure(figsize=(7,5))
plt.scatter(x_vals, y_vals, color='blue', alpha=0.5,s =3, )
contour = plt.contour(X, Y, Z, levels=10, colors='red')
plt.clabel(contour, inline=True, fontsize=8)
plt.xlabel("x")
plt.ylabel("y")
plt.title("Samples with theoretical PDF contour")
plt.legend()
plt.show()
