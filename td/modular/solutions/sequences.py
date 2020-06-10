import functools
import math
import operator

def fibo_imp(n: int) -> int:
    fibPr, fib = 0, 1
    for num in range(1, n+1):
        fibPr, fib = fib, fib + fibPr
    return fibPr

def fibo_rec_double(n):
    if (n <= 1):
        return n
    else:
        return fibo_rec_double(n-1) + fibo_rec_double(n-2)

def fibo_tail_rec(n):
    def fib_help(a, b, n):
        return fib_help(b, a+b, n-1) if n > 0 else a
    return fib_help(0, 1, n)

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
