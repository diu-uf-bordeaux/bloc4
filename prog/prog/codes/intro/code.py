import functools
import math
import operator

import matplotlib.pyplot as mp

def fibo(n: int) -> int:
    fibPr = 0
    fib = 1
    for num in range(1, n+1):
        fibPr, fib = fib, fib + fibPr
    return fibPr

def choose(n, r):
    r = min(r, n-r)
    if r == 0: return 1
    numer = functools.reduce(operator.mul, range(n, n-r, -1))
    denom = functools.reduce(operator.mul, range(1, r+1))
    return numer//denom

def catalan(n):
    return choose(2*n, n)//(n+1)

def rowland(n):
    if (n <= 1):
        return 7
    else:
        row = 7
        for i in range(2, n+1):
            row += math.gcd(i, row)
        return row

def log_2(n):
    lg = 0
    while (n >= 2):
        lg += 1
        n /= 2
    return lg

def test_fibo() -> None:
    tab = [0, 1, 1, 2, 3, 5, 8, 13, 21, 34]
    for i in range(10):
        assert(fibo(i) == tab[i])

def test_rowland():
    tab = [7, 7, 8, 9, 10, 15, 18, 19, 20, 21]
    for i in range(10):
        assert(rowland(i) == tab[i])

def plot_sequence(f, n) -> None:
    xs = range(n)
    ys = [ f(x) for x in xs ]
    mp.plot(xs, ys, 'o-')
    mp.show()
