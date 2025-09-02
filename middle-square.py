import matplotlib.pyplot as plt

# Middle Square function
def middle_square(seed, amount):
    if (len(str(seed)) < 4): 
        print("This algorithm requires 4 digits at least for execution")
    else:
        double_list = []
        x = seed
        for _ in range(amount):
            distribution = (len(str(seed)) + 2 - 1) // 2
            double_square = x * x
            double_square_str = str(double_square)
            double_square_str = double_square_str.rjust(len(str(seed)) * 2, '0')
            remove_digits = double_square_str[distribution:-distribution]
            x = int(remove_digits)
            double_list.append(x)
        return double_list
    
# Function call and print of values
random_number = middle_square(7604, 1000)
print(*random_number, sep="\n")

# Histogram
plt.figure(figsize=(8,5))
plt.hist(random_number, bins=150, color='skyblue', edgecolor='black', alpha=0.7)
plt.title("Histogram of Pseudo-random Numbers (Middle-Square)")
plt.xlabel("Value")
plt.ylabel("Frequency")
plt.grid(axis='y', alpha=0.3)
plt.show()
