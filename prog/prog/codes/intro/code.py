import functools
import itertools
import math
import operator
import timeit

import matplotlib.pyplot as mp

def fibo(n: int) -> int:
    fibPr, fib = 0, 1
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

def next_conway(l):
    result = []

    repeat = l[0]
    l.pop(0)
    times = 1

    for actual in l:
        if actual != repeat:
            result += [times, repeat]
            times = 1
            repeat = actual
        else:
            times += 1
    result += [times, repeat]

    return result

def conway(n):
    if (n <= 1):
        return 1
    else:
        result = [1]
        for i in range(n):
            result = next_conway(result)
        return int("".join([str(r) for r in result]))

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

def test_conway():
    tab = [1, 1, 21, 1211, 111221, 312211, 13112221, 1113213211,
           31131211131221, 13211311123113112211]
    for i in range(1, 10):
        assert(conway(i) == tab[i])

test_fibo()
test_rowland()
test_conway()

def plot_sequence(f, n) -> None:
    xs = range(n)
    ys = [ f(x) for x in xs ]
    mp.plot(xs, ys, 'o-')
    mp.show()

def fibo(n):
    if (n <= 1):
        return n
    else:
        return fibo(n-1) + fibo(n-2)

def fibo(n):
    def fib_help(a, b, n):
        return fib_help(b, a+b, n-1) if n > 0 else a
    return fib_help(0, 1, n)

def plot_time_fibo():
    # ns = range(10,33,2)
    ns = range(10,100,2)
    ts = [timeit.timeit(lambda: fibo(n), number=100) for n in ns]
    mp.gca().set_xlabel('Valeur de $n$')
    mp.gca().set_ylabel('Temps de calcul de $fibo(n)$')
    mp.plot(ns, ts, 'o-')
    mp.show()

# plot_time_fibo()
