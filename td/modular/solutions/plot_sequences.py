import math
import matplotlib.pyplot as mp
import sequences as seq
import timeit

def plot_a_sequence(f, n) -> None:
    xs = range(n)
    ys = [ f(x) for x in xs ]
    mp.plot(xs, ys, 'o-')
    mp.show()

def plot_all_sequences(n) -> None:
    xs = range(n)
    fs = [
        (seq.fibo_tail_rec, "Fibonacci"),
        (seq.catalan,       "Catalan"),
        (seq.rowland,       "Rowland"),
        (seq.log_2,         "Log 2"),
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

def plot_time_a_sequence(seq_fun):
    ns = range(5,24,1)
    ts = [timeit.timeit(lambda: seq_fun(n), number=100) for n in ns]
    mp.gca().set_xlabel('Valeur de $n$')
    mp.gca().set_ylabel('Temps de calcul de $fibo(n)$')
    mp.plot(ns, ts, 'o-')
    mp.show()
