def cons(x, l): return { "hd": x, "tl": l }

def head(l): return l["hd"]
def tail(l): return l["tl"]
def empty(): return cons(None, None)
def is_empty(l): return (head(l) is None) and \
                        (tail(l) is None)

def length(l):
    if is_empty(l):
        return 0
    else:
        return 1 + length(tail(l))

l = cons(1, cons(2, cons(3, empty())))
length(l)       # -> 3
length(tail(l)) # -> 2
length(empty()) # -> 0
