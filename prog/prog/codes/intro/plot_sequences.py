import functools
import math
import operator
import timeit

import matplotlib.pyplot as mp

def plot_a_sequence(f, n) -> None:
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

plot_time_fibo()
