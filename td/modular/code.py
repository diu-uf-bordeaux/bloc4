import functools
import math
import operator
import timeit

import matplotlib.pyplot as mp

def fibo_imp(n: int) -> int:
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

def plot_a_sequence(f, n) -> None:
    xs = range(n)
    ys = [ f(x) for x in xs ]
    mp.plot(xs, ys, 'o-')
    mp.show()

# plot_a_sequence(fibo, 10)

def plot_all_sequences(n) -> None:
    xs = range(n)
    fs = [
        (fibo,    "Fibonacci"),
        (catalan, "Catalan"),
        (rowland, "Rowland"),
        (log_2,   "Log 2"),
    ]
    sqrt_len = int(math.ceil(math.sqrt(len(fs))))
    fig, axs = mp.subplots(sqrt_len, sqrt_len)
    fig.subplots_adjust(wspace=0.3, hspace=0.4)
    (x, y) = (0, 0)
    for (fn, fstr) in fs:
        print((x,y))
        ys = [ fn(x) for x in xs ]
        ax = axs[x, y]
        ax.plot(xs, ys)
        ax.set_yscale('linear')
        ax.set_title(fstr)
        ax.grid(True)
        if (x + 1 == sqrt_len):
            (x, y) = (0, y+1)
        else:
            (x, y) = (x+1, y)
    mp.show()

# plot_all_sequences(10)

def fibo_rec_double(n):
    if (n <= 1):
        return n
    else:
        return fibo_rec_double(n-1) + fibo_rec_double(n-2)

def fibo_tail_rec(n):
    def fib_help(a, b, n):
        return fib_help(b, a+b, n-1) if n > 0 else a
    return fib_help(0, 1, n)

def plot_time_a_sequence(seq_fun):
    ns = range(10,100,2)
    ts = [timeit.timeit(lambda: seq_fun(n), number=100) for n in ns]
    mp.gca().set_xlabel('Valeur de $n$')
    mp.gca().set_ylabel('Temps de calcul de $fibo(n)$')
    mp.plot(ns, ts, 'o-')
    mp.show()

# plot_time_a_sequence(fibo_tail_rec)
# plot_time_a_sequence(fibo_rec_double)
