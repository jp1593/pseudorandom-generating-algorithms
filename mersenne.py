import matplotlib.pyplot as plt
import numpy as np
from scipy.stats import chisquare


# Constantes del Mersenne Twister
n = 624
m = 397
w = 32
r = 31
a = 0x9908b0df
u = 11
s = 7
t = 15
l = 18
b = 0x9d2c5680
c = 0xefc60000
f = 1812433253
UMASK = (0xffffffff << r) & 0xffffffff  # bits altos
LMASK = (0xffffffff >> (w - r)) & 0xffffffff  # bits bajos

def MersenneTwister_Inicializar(semilla):
    """
    Inicializador del Mersenne Twister
    """
    estado = [0] * n
    estado[0] = semilla & 0xffffffff

    for i in range(1, n):
        estado[i] = (f * (estado[i - 1] ^ (estado[i - 1] >> (w - 2))) + i) & 0xffffffff

    indice = 0
    return estado, indice

def MersenneTwister_Generar(estado, indice):
    """
    Generador del Mersenne Twister
    """
    k = indice
    j = (k - (n - 1)) % n

    # Combinar bits altos y bajos
    x = (estado[k] & UMASK) | (estado[j] & LMASK)

    xA = x >> 1
    if x & 1: 
        xA ^= a

    # Combinar un estado anterior
    j = (k - (n - m)) % n
    x = estado[j] ^ xA
    estado[k] = x

    k = (k + 1) % n
    indice = k

    # Tempering
    y = x
    y ^= (y >> u)
    y ^= ((y << s) & b)
    y ^= ((y << t) & c)
    z = y ^ (y >> l)

    return z & 0xffffffff, estado, indice


def MersenneTwister_Aleatorio(semilla, cantidad):
    """
    Genera 'cantidad' números pseudoaleatorios a partir de una semilla
    """
    estado, indice = MersenneTwister_Inicializar(semilla)
    resultados = []

    for _ in range(cantidad):
        numero, estado, indice = MersenneTwister_Generar(estado, indice)
        resultados.append(numero)

    return resultados

MersenneResult = MersenneTwister_Aleatorio(5489, 1000)
print(*MersenneResult, sep="\n")

#Histogram
plt.figure(figsize=(8,5))
plt.hist(MersenneResult, bins=35, color='skyblue', edgecolor='black', alpha=0.7)
plt.title("Histogram of Pseudo-random Numbers (MersenneTwister)")
plt.xlabel("Value")
plt.ylabel("Frequency")
plt.grid(axis='y', alpha=0.3)
plt.show()


# Hypotesis test:
# Number normalization [0,1]
normalized_mt = [x / 2**32 for x in MersenneResult]

bins = 35
n = len(normalized_mt)
E = n / bins  

# Stadistic Chi^2
counts, _ = np.histogram(normalized_mt, bins=bins, range=(0.0, 1.0))
chi2_stat, p_val = chisquare(counts, f_exp=[E]*bins)

# Critic Values (df = 34)
chi2_95 = 48.602
chi2_90 = 45.563

print("\n=== Prueba de Uniformidad (Chi-cuadrado - Mersenne Twister) ===")
print(f"Chi² (scipy)    = {chi2_stat:.4f}")
print(f"\nComparación con tabla:")
print(f"  chi²[0.95, 34] = {chi2_95}")
print(f"  chi²[0.90, 34] = {chi2_90}")

if chi2_stat < chi2_95:
    print("\nA un nivel de confianza del 95%: no podemos rechazar la hipótesis nula de que los números generados provienen de una distribución uniforme.")
elif chi2_stat < chi2_90:
    print("\nA un nivel de confianza del 90%: no podemos rechazar la hipótesis nula de que los números generados provienen de una distribución uniforme, pero sí se rechaza al 95%.")
else:
    print("Según la prueba, se rechaza la hipótesis nula: los números generados no provienen de una distribución uniforme.")

# Autocorrelation Test
def autocorr(x, k):
    x = np.asarray(x)
    n = len(x)
    xbar = x.mean()
    num = np.dot(x[:n-k]-xbar, x[k:]-xbar)
    den = np.dot(x-xbar, x-xbar)
    return num/den

print("\n=== Prueba de Autocorrelación (Mersenne Twister) ===")
alpha = 0.05
z_alpha = 1.96  # 95% IC

for k in (1, 2, 5, 10):
    r = autocorr(normalized_mt, k)
    z = r * np.sqrt(n)
    margin = z_alpha / (12 * np.sqrt(n-k))
    IC_inf = r - margin
    IC_sup = r + margin
    print(f"{k}: r={r:.4f}, z≈{z:.3f}, IC=[{IC_inf:.5f}, {IC_sup:.5f}]")
    if IC_inf <= 0 <= IC_sup:
        print("   -> No, se rechaza independencia (0 en IC).")
    else:
        print("   -> Se detecta dependencia (0 fuera del IC).")

