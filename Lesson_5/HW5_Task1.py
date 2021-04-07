from math import sqrt


def is_prime(x):
    if x % 2 == 0:
        return x == 2
    divider = 3
    while divider <= sqrt(x) and x % divider != 0:
        divider += 2
    return divider > sqrt(x)


print(is_prime())
