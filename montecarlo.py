import numpy as np
import random
from scipy.stats import norm
import math
from math import erf

# Blum Blum Generator
def BlumBlum(seed, p, q, amount):
    x = seed
    m = p * q
    random_numbers = []
    for _ in range(amount):
        x = (x * x) % m
        random_numbers.append(x / m)  # normalizamos en [0,1]
    return random_numbers

# Montecarlo Blum Blum
def monte_carlo_blum(f, a, b, N=10000, seed=123, p=383, q=503):
    u = BlumBlum(seed, p, q, N)           
    x = a + (b - a) * np.array(u)        
    fx = f(x)                             
    return (b - a) * np.mean(fx)

# MonteCarlo Method with numpy
def monte_carlo_numpy(f, a, b, N=100000):
    x = np.random.uniform(a, b, N)   
    fx = f(x)
    return (b - a) * np.mean(fx)

# Integration functions
f1 = lambda x: np.sin(np.pi * x)   
f2 = lambda x: (1/np.sqrt(2*np.pi)) * np.exp(-x**2/2) 

# Amount of simulation
N = 100000  

# Integral 1
numpy_est_1 = monte_carlo_numpy(f1, 0, 1, N)
true_val_1 = 2/np.pi # Symbolab result
est_1 = monte_carlo_blum(f1, 0, 1, N=50000)

# Integral 2
numpy_est_2 = monte_carlo_numpy(f2, 0, 2, N)
true_val_2 = (1/math.sqrt(math.pi)) * erf(math.sqrt(2)) # Symbolab result
est_2 = monte_carlo_blum(f2, 0, 2, N=50000)

# Results
print("Integral 1:")
print(f"Estimación Blum Blum: {est_1:.6f}")
print(f"Monte Carlo (NumPy):   {numpy_est_1}")
print(f"Valor real:             {true_val_1}\n")

print("Integral 2:")
print(f"Estimación Blum Blum: {est_2:.6f}")
print(f"Monte Carlo (NumPy):   {numpy_est_2}")
print(f"Valor real:             {true_val_2}")
