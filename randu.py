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
random = Randu(33, 100)
print(*random, sep='\n')
