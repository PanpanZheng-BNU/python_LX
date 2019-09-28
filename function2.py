import math


def quadratic(a, b, c):
    x1 = (-b + math.sqrt(b**2 - 4 * a * c)) / (2 * a)
    x2 = (-b - math.sqrt(b**2 - 4 * a * c)) / (2 * a)
    return x1, x2
    pass


def enroll(name, gender, age=6, city='Beijing'):
    print('name:', name)
    print('gender:', gender)
    print('age:', age)
    print('city:', city)
    return
    pass


def add_end(L=None):
    if L is None:
        L = []
    L.append('END')
    return L
    pass


def calc(*numers):
    sum = 0
    for n in numers:
        sum = sum + n * n
    return sum
    pass


def person(name, age, **kw):
    print('name:', name, 'age:', age, 'other:', kw)
