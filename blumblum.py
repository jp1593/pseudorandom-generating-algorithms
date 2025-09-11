import matplotlib.pyplot as plt
import numpy as np
from scipy.stats import chisquare

# Blum Blum Function
def BlumBlum(seed, p, q, amount):
    x = seed
    m=p*q
    random_numbers = [] 
    raw_numbers = [] 
    for _ in range(amount): 
        x = (x*x) % m 
        raw_numbers.append(x) 
        random_numbers.append(x / m) # Normalization between [0,1]
    return random_numbers, raw_numbers

# Function call and print data
blum_generation, raw_numbers = BlumBlum(123, 383, 503, 10000)
print(*blum_generation, sep='\n')

#Histogram
plt.figure(figsize=(8,5))
plt.hist(blum_generation, bins=35, color='skyblue', edgecolor='black', alpha=0.7)
plt.title("Histogram of Pseudo-random Numbers (BlumBlum)")
plt.xlabel("Value")
plt.ylabel("Frequency")
plt.grid(axis='y', alpha=0.3)
plt.show()

# Hypotesis test:
lsb_bits = [num & 1 for num in raw_numbers]

count_0 = lsb_bits.count(0)
count_1 = lsb_bits.count(1)
n = len(lsb_bits)
k = 2
E = n / k  # Expected values for 1's and 0's
print("\n=== Prueba de Uniformidad (Chi-cuadrado en LSB) ===")
print(f"Total bits: {n}")
print(f"Cantidad de 0's: {count_0}")
print(f"Cantidad de 1's: {count_1}")

# Stadistic Chi^2
counts = np.array([count_0, count_1])
chi2_stat, p_val = chisquare(counts, f_exp=[E, E])

# Chi^2 at 1 level of confidence
chi2_95 = 2.71
chi2_90 = 3.84

print(f"\nChi² (scipy) = {chi2_stat:.4f}")
print(f"\nComparación con tabla:")
print(f"  chi²[0.95, 29] = {chi2_95}")
print(f"  chi²[0.90, 29] = {chi2_90}")

if chi2_stat < chi2_95:
    print("\nA un nivel de confianza del 95%; no podemos rechazar la hipótesis nula que los números generados por Python vengan de una distribución uniforme")
elif chi2_stat < chi2_90:
    print("\nA un nivel de confianza del 90%; no podemos rechazar la hipótesis nula de que los números generados provienen de una distribución uniforme, pero sí se rechaza al 95%.")
else:
    print("\nSegún la prueba, debemos rechazar la hipótesis nula: los números generados no provienen de una distribución uniforme.")

# Autocorrelation Test
def autocorr(x, k):
    x = np.asarray(x)
    n = len(x)
    xbar = x.mean()
    num = np.dot(x[:n-k]-xbar, x[k:]-xbar)
    den = np.dot(x-xbar, x-xbar)
    return num/den

print("\n=== Prueba de Autocorrelación (LSB - BlumBlum) ===")
alpha = 0.05
z_alpha = 1.96  # 95% IC

for k in (1, 2, 5, 10):
    r = autocorr(lsb_bits, k)
    z = r * np.sqrt(n)
    margin = z_alpha / (12 * np.sqrt(n - k))
    IC_inf = r - margin
    IC_sup = r + margin
    print(f"Lag {k}: r={r:.4f}, z≈{z:.3f}, IC=[{IC_inf:.5f}, {IC_sup:.5f}]")
    if IC_inf <= 0 <= IC_sup:
        print("   -> No se rechaza independencia (0 en IC).")
    else:
        print("   -> Se detecta dependencia (0 fuera del IC).")
