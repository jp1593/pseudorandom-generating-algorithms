import matplotlib.pyplot as plt
from scipy.stats import chisquare
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

# Call of function and number display
random = Randu(33, 1000)
print(*random, sep='\n')

#Histogram
plt.figure(figsize=(8,5))
plt.hist(random, bins=35, color='skyblue', edgecolor='black', alpha=0.7)
plt.title("Histogram of Pseudo-random Numbers (RANDU)")
plt.xlabel("Value")
plt.ylabel("Frequency")
plt.grid(axis='y', alpha=0.3)
plt.show()

# Hypothesis test: 
bins = 35
n = len(random)
E = n / bins  

# Stadistic Chi^2
counts, _ = np.histogram(random, bins=bins, range=(0.0, 1.0))
chi2_stat, p_val = chisquare(counts, f_exp=[E]*bins)

# Critical values for df = 34
chi2_95 = 48.602
chi2_90 = 45.563

print("\n=== Prueba de Uniformidad (Randu) ===")
print(f"Chi² (scipy) = {chi2_stat:.4f}")
print(f"\nComparación con tabla:")
print(f"  chi²[0.95, 34] = {chi2_95}")
print(f"  chi²[0.90, 34] = {chi2_90}")

if chi2_stat < chi2_95:
    print("\nA un nivel de confianza del 95%: no podemos rechazar la hipótesis nula de que los números generados provienen de una distribución uniforme.")
elif chi2_stat < chi2_90:
    print("\nA un nivel de confianza del 90%: no podemos rechazar la hipótesis nula de que los números generados provienen de una distribución uniforme, pero sí se rechaza al 95%.")
else:
    print("Según la prueba, se rechaza la hipótesis nula: los números generados no provienen de una distribución uniforme.")

# Autocorrelation test
def autocorr(x, k):
    x = np.asarray(x)
    n = len(x)
    xbar = x.mean()
    num = np.dot(x[:n-k]-xbar, x[k:]-xbar)
    den = np.dot(x-xbar, x-xbar)
    return num/den

print("\n=== Prueba de Autocorrelación (Randu) ===")
alpha = 0.05
z_alpha = 1.96  # 95%
for k in (1,2,5,10):
    r = autocorr(random, k)
    z = r * np.sqrt(n)

    # Confidence Interval
    margin = z_alpha / (12 * np.sqrt(n-k))
    CI_inf = r - margin
    CI_sup = r + margin
    
    print(f"{k}: r = {r:.4f}, z ≈ {z:.3f}, CI = [{CI_inf:.5f}, {CI_sup:.5f}]")
    if CI_inf <= 0 <= CI_sup:
        print("   -> No se rechaza independencia (0 está en el IC).")
    else:
        print("   -> Se detecta dependencia (0 fuera del IC).")