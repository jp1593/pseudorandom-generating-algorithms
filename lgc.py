import matplotlib.pyplot as plt
import numpy as np

# LGC Function
def LGC(seed, a, c, m, amount): 
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
pseudo_number = LGC(seed=10, a=22695477,c=1,m=2**31, amount=10)
# Print of list items in a iterative way
print(*pseudo_number, sep='\n')
# Histogram
data = pseudo_number
plt.hist(data, bins=10)
plt.show()

