import matplotlib.pyplot as plt

# Blum Blum Function
def BlumBlum(seed, p, q, amount):
    x = seed
    m=p*q
    random_numbers = [] 
    for _ in range(amount): 
        x = (x*x) % m 
        random_numbers.append(x / m) # Normalization between [0,1]
    return random_numbers

# Function call and print data
blum_generation = BlumBlum(123, 383, 503, 10000)
print(blum_generation)

#Histogram
plt.figure(figsize=(8,5))
plt.hist(blum_generation, bins=35, color='skyblue', edgecolor='black', alpha=0.7)
plt.title("Histogram of Pseudo-random Numbers (BlumBlum)")
plt.xlabel("Value")
plt.ylabel("Frequency")
plt.grid(axis='y', alpha=0.3)
plt.show()

