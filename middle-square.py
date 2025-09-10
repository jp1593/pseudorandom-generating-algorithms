import matplotlib.pyplot as plt
from scipy.stats import chisquare
import numpy as np

# Middle Square function
def middle_square(seed, amount):
    if (len(str(seed)) < 4): 
        print("This algorithm requires 4 digits at least for execution")
    else:
        double_list = []
        x = seed
        for _ in range(amount):
            distribution = (len(str(seed)) + 2 - 1) // 2
            double_square = x * x
            double_square_str = str(double_square)
            double_square_str = double_square_str.rjust(len(str(seed)) * 2, '0')
            remove_digits = double_square_str[distribution:-distribution]
            x = int(remove_digits)
            double_list.append(x)
        return double_list
    
# Function call and print of values
random_number = middle_square(7604, 1000)
print(*random_number, sep="\n")

# Histogram
plt.figure(figsize=(8,5))
plt.hist(random_number, bins=150, color='skyblue', edgecolor='black', alpha=0.7)
plt.title("Histogram of Pseudo-random Numbers (Middle-Square)")
plt.xlabel("Value")
plt.ylabel("Frequency")
plt.grid(axis='y', alpha=0.3)
plt.show()

# Hypotesis test:
#Number normalization [0,1]
max_value = max(random_number)
normalized_number = [x / max_value for x in random_number]

bins = 35
n = len(normalized_number)
E = n / bins  # valor esperado por bin

# Conteo de observaciones por bin
counts, _ = np.histogram(normalized_number, bins=bins, range=(0.0, 1.0))

# Chi-cuadrado manual
chi2_manual = np.sum((counts - E)**2 / E)

# Prueba con scipy
chi2_stat, p_val = chisquare(counts, f_exp=[E]*bins)

# Valores críticos df = 34 (bins-1)
chi2_95 = 48.602
chi2_90 = 45.563

print("\n=== Prueba de Uniformidad (Chi-cuadrado sobre valores normalizados - Middle-Square) ===")
print(f"Chi² (manual)   = {chi2_manual:.4f}")
print(f"Chi² (scipy)    = {chi2_stat:.4f}")
print(f"p-value (scipy) = {p_val:.6f}")
print(f"Comparación con tabla:")
print(f"  chi²[0.95, 34] = {chi2_95}")
print(f"  chi²[0.90, 34] = {chi2_90}")

# Conclusión
if chi2_stat < chi2_95:
    print("\nA un nivel de confianza del 95%:")
    print("Según la prueba, no podemos rechazar la hipótesis nula de que los números generados provienen de una distribución uniforme.")
elif chi2_stat < chi2_90:
    print("\nA un nivel de confianza del 90%:")
    print("Según la prueba, no podemos rechazar la hipótesis nula de que los números generados provienen de una distribución uniforme,")
    print("pero sí se rechaza al 95%.")
else:
    print("\nConclusión general:")
    print("Según la prueba, se rechaza la hipótesis nula: los números generados no provienen de una distribución uniforme.")