def is_prime(x):
    if x % 2 == 0:
        return x == 2
    divider = 3
    while divider <= x**0.5 and x % divider != 0:
        divider += 2
    return divider > x**0.5


print(is_prime())
