import numpy as np
import math
from scipy.stats import norm

# Montecarlo Method
def monte_carlo_integral(f, a, b, N=1000000):
    x = np.random.uniform(a, b, N)  
    fx = f(x)
    return (b - a) * np.mean(fx)

# Problema 1
f1 = lambda x: np.sin(np.pi * x)
a1, b1 = 0, 1
mc_est_1 = monte_carlo_integral(f1, a1, b1)
true_val_1 = 2/np.pi

print("Integral 1:")
print(f"Estimación Monte Carlo: {mc_est_1}")
print(f"Valor real: {true_val_1}")
print(f"Error absoluto: {abs(mc_est_1 - true_val_1)}\n")

# Problema 2
f2 = lambda x: (1/np.sqrt(2*np.pi)) * np.exp(-x**2/2)
a2, b2 = 0, 2
mc_est_2 = monte_carlo_integral(f2, a2, b2)
true_val_2 = norm.cdf(2) - norm.cdf(0)  

print("Integral 2:")
print(f"Estimación Monte Carlo: {mc_est_2}")
print(f"Valor real: {true_val_2}")
print(f"Error absoluto: {abs(mc_est_2 - true_val_2)}")
