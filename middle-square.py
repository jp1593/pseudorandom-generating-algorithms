def middle_square(seed, amount):
    if (len(str(seed)) < 4): 
        print("Debe de introducir minimo 4 digitos")
    else:
        double_list = []
        x = seed
        # for _ in range(amount):
        distribution = (len(str(seed)) + 2 - 1) // 2
        double_square = x * x
        double_square_str = str(double_square)
        remove_digits = double_square_str[distribution:-distribution]
        x = int(remove_digits)
        double_list.append(x)
        return double_list
    
random_number = middle_square(12345, 10)
print(random_number)


