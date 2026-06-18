import numpy as np
import scipy.io
import matplotlib.pyplot as plt

def generate_integral_data(num_samples, grid_size):
    """
    Generates 1D analytical integral data.
    Input a(x): sin(c * 2 * pi * x)
    Output u(x): integral of a(x) from 0 to x
    """
    x = np.linspace(0, 1, grid_size)
    a = np.zeros((num_samples, grid_size))
    u = np.zeros((num_samples, grid_size))
    
    for i in range(num_samples):
        # Generate a random multiplier
        c = np.random.uniform(1, 5)
        
        a[i, :] = np.sin(c * 2 * np.pi * x)
        u[i, :] = (1 - np.cos(c * 2 * np.pi * x)) / (c * 2 * np.pi)
        
    return x, a, u

# Training data
grid_size_train = 64
x_train, a_train, u_train = generate_integral_data(800, grid_size_train)
scipy.io.savemat('integral_train_R64.mat', {'a': a_train, 'u': u_train})

# Testing data
grid_size_test = 1024
x_test, a_test, u_test = generate_integral_data(200, grid_size_test)
scipy.io.savemat('integral_test_R1024.mat', {'a': a_test, 'u': u_test})

print("Datasets generated and saved as .mat files successfully.")

plt.figure(figsize=(10, 4))

plt.subplot(1, 2, 1)
plt.plot(x_train, a_train[0, :], marker='o', markersize=3, label="Input a(x)")
plt.title("Observation 1\nInitial Condition (N=64)")
plt.xlabel("x")
plt.ylabel("a")

plt.subplot(1, 2, 2)
plt.plot(x_train, u_train[0, :], color='orange', label="Output u(x)")
plt.title("Analytic Integral Solution (N=64)")
plt.xlabel("x")
plt.ylabel("u")

plt.tight_layout()
plt.savefig("example_plot.png")
print("Example plot saved as example_plot.png")
