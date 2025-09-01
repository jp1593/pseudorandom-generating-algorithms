def BlumBlum(seed, p, q, amount):
    x = seed
    m=p*q
    random_numbers = [] 
    for _ in range(amount): 
        x = (x*x) % m 
        random_numbers.append(x)
    return random_numbers

blum_generation = BlumBlum(3, 11, 19, 10)
print(blum_generation)