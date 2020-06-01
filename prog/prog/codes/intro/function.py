def filter(f, l):
    return [item for item in l if f(item)]

def integrate(f, a, b, n):
    h = (b-a) / n
    return h*sum([f(a + k*h) for k in range(n)])

def derivate(f, h):
    return lambda x: (f(x+h) - f(x)) / h

def bubble_sort(l, f):
    nl = list(l)
    n = len(nl)
    for i in range(n):
        already_sorted = True
        for j in range(n - i - 1):
            if f(nl[j], nl[j + 1]):
                nl[j], nl[j + 1] = nl[j + 1], nl[j]
                already_sorted = False
        if already_sorted:
            break
    return nl
