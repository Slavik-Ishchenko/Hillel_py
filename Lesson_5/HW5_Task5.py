from math import sqrt


def square(x):
    s = set()
    s.add(x*4)
    s.add(x**2)
    s.add((2**0.5)*x)
    return s


print(square(25))

