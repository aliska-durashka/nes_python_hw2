
import numpy as np
from timeit import timeit

def wsum1(x, w):
    result = 0

    for i in range(len(x)):
        result += x[i] * w[i] ** 2

    return result

def wsum2(x, w):
    matrix = np.diag(w)
    return x @ matrix @ x

def wsum3(x,w):
    return np.sum(w*x**2)

def mytimeit(fun, x, y):
    n = 100
    t=timeit(lambda: fun(x,y), number=n)
    return t/n

x = np.linspace(0, 1, num=10000)
w = np.linspace(0, 1, num=10000)

print(wsum1(x, w))
print(wsum2(x, w))
print(wsum3(x, w))

print(mytimeit(wsum1, x, w))
print(mytimeit(wsum2, x, w))
print(mytimeit(wsum3, x, w))