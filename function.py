import math


def quadratic(a, b, c):
    x1 = (-b + math.sqrt(b**2 - 4 * a * c)) / (2 * a)
    x2 = (-b - math.sqrt(b**2 - 4 * a * c)) / (2 * a)
    return x1, x2


def enroll(name, gender, age=6, city='Beijing'):
    print('name:', name)
    print('gender:', gender)
    print('age:', age)
    print('city:', city)
    return


def add_end(L):
    L.append('END')
    return L


def calc(numers):
    sum = 0
    for n in numers:
        sum = sum + n * n
    return sum
    pass
