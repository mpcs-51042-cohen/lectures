# This file is for ad-hoc demonstrations
# I will push the final version of this file to Github after class

# Simple prime number detector
def is_prime(n):
    p = True
    for i in range(2, n):
        if n % i == 0:
            p = False
    return p

print(is_prime("9"))