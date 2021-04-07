from math import sqrt


def square(x):
    s = set()
    s.add(x*4)
    s.add(x**2)
    s.add(sqrt(2)*x)
    return s


print(square())
