import matplotlib.pyplot as plt

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