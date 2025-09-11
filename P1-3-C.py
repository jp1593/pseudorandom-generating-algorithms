import matplotlib.pyplot as plt
from scipy.stats import chisquare
import random
import numpy as np

# Randu function
def Randu(seed, amount): 
    m = 2**31
    x = seed
    random_numbers = []
    for _ in range(amount): 
        x = (65539 * x) % m
        normalize  = x / m
        random_numbers.append(normalize) #Normalizarion between 0 and 1
    return random_numbers

# Usage of same seed and amount of numbers to be generated with both of them
randu = Randu(33, 1000)
random.seed(33)
python_random_numbers = [random.random() for _ in range(1000)]

#Histogram
plt.figure(figsize=(12,5))

plt.subplot(1,2,1)
plt.hist(randu, bins=35, color='salmon', edgecolor='black', alpha=0.7)
plt.title("Histogram - Randu")
plt.xlabel("Value")
plt.ylabel("Frequency")
plt.grid(axis='y', alpha=0.3)

plt.subplot(1,2,2)
plt.hist(python_random_numbers, bins=35, color='skyblue', edgecolor='black', alpha=0.7)
plt.title("Histogram - Python random")
plt.xlabel("Value")
plt.ylabel("Frequency")
plt.grid(axis='y', alpha=0.3)

plt.tight_layout()
plt.show()


# Hypothesis Functions: 
def chi_square_test(numbers, bins=35):
    n = len(numbers)
    E = n / bins
    counts, _ = np.histogram(numbers, bins=bins, range=(0.0, 1.0))
    chi2_stat, p_val = chisquare(counts, f_exp=[E]*bins)
    return chi2_stat, p_val

# Chisquare test for both type of numbers
chi2_randu, p_randu = chi_square_test(randu)
chi2_python, p_python = chi_square_test(python_random_numbers)

# Critical values for df = 34
chi2_95 = 48.602
chi2_90 = 45.563

print("\n=== Valores de Chi^2 a un grado de libertad de 34 ===")
print(f"Comparación con tabla:")
print(f"  chi²[0.95, 34] = {chi2_95}")
print(f"  chi²[0.90, 34] = {chi2_90}")

print("\n=== Chi-cuadrado (Randu) ===")
print(f"Chi² = {chi2_randu:.4f}, p = {p_randu:.4f}")
if chi2_randu < chi2_95:
    print("\nA un nivel de confianza del 95%: no podemos rechazar la hipótesis nula de que los números generados provienen de una distribución uniforme.")
elif chi2_randu < chi2_90:
    print("\nA un nivel de confianza del 90%: no podemos rechazar la hipótesis nula de que los números generados provienen de una distribución uniforme, pero sí se rechaza al 95%.")
else:
    print("\nSegún la prueba, se rechaza la hipótesis nula: los números generados no provienen de una distribución uniforme.")

print("\n=== Chi-cuadrado (Python random) ===")
print(f"Chi² = {chi2_python:.4f}, p = {p_python:.4f}")
if chi2_python < chi2_95:
    print("\nA un nivel de confianza del 95%: no podemos rechazar la hipótesis nula de que los números generados provienen de una distribución uniforme.")
elif chi2_python < chi2_90:
    print("\nA un nivel de confianza del 90%: no podemos rechazar la hipótesis nula de que los números generados provienen de una distribución uniforme, pero sí se rechaza al 95%.")
else:
    print("\nSegún la prueba, se rechaza la hipótesis nula: los números generados no provienen de una distribución uniforme.")