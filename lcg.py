import matplotlib.pyplot as plt
from scipy.stats import chisquare
import numpy as np

# LGC Function
def LCG(seed, a, c, m, amount): 
    """
    Generador de Congruencia Lineal (LCG)
    """
    pseudo_list = []
    x = seed
    for _ in range(amount): 
        prev_x = (a * x + c) % m
        pseudo_list.append(prev_x / m)
        x = prev_x
    return pseudo_list
    
# Using the Borland C/C++ parameters
pseudo_number = LCG(seed=20, a=22695477,c=1,m=2**31, amount=1000)

# Print of list items in a iterative way
print(*pseudo_number, sep='\n')

# Histogram
plt.figure(figsize=(8,5))
plt.hist(pseudo_number, bins=35, color='skyblue', edgecolor='black', alpha=0.7)
plt.title("Histogram of Pseudo-random Numbers (LCG)")
plt.xlabel("Value")
plt.ylabel("Frequency")
plt.grid(axis='y', alpha=0.3)
plt.show()

# Hypotesis test:
bins = 35
n = len(pseudo_number)
E = n / bins  

# Stadistic Chi^2
counts, _ = np.histogram(pseudo_number, bins=bins, range=(0.0, 1.0))
chi2_stat, p_val = chisquare(counts, f_exp=[E]*bins)

# Critic values at df=34
chi2_95 = 48.602
chi2_90 = 45.563

print("\n=== Prueba de Uniformidad (LCG) ===")
print(f"Chi² (scipy) = {chi2_stat:.4f}")
print(f"\nComparación con tabla:")
print(f"  chi²[0.95, 29] = {chi2_95}")
print(f"  chi²[0.90, 29] = {chi2_90}")

if chi2_stat < chi2_95:
    print("\nA un nivel de confianza del 95%; no podemos rechazar la hipótesis nula que los números generados por Python vengan de una distribución uniforme")
elif chi2_stat < chi2_90:
    print("\nA un nivel de confianza del 90%; no podemos rechazar la hipótesis nula de que los números generados provienen de una distribución uniforme, pero sí se rechaza al 95%.")
else:
    print("\nSegún la prueba, debemos rechazar la hipótesis nula: los números generados no provienen de una distribución uniforme.")

