def smallest_factor(n):
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return i
    return n

def all_factors(n):
    for i in range(2, n + 1):
        val = smallest_factor(i)
        print("The smallest factor of " + str(i) + " is " + str(val))

# Calling the function for numbers up to 30
all_factors(30)