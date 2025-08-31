import matplotlib.pyplot as plt

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
pseudo_number = LGC(seed=20, a=22695477,c=1,m=2**31, amount=1000)

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

