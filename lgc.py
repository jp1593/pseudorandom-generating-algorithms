# LGC Function
def LGC(seed, a, c, m): 
    """
    Generador de Congruencia Lineal (LCG)
    """
    x = seed
    prev_x = (a * x + c) % m
    prev_x = (a * prev_x + c) % m

    return prev_x
    
# Using the Borland C/C++ parameters
pseudo_number = LGC(seed=10, a=22695477,c=1,m=2**31)
print(pseudo_number)

