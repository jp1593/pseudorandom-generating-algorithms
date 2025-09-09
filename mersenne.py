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


MersenneResult = MersenneTwister_Aleatorio(5489, 10)
print(*MersenneResult, sep="\n")

