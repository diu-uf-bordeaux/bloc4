def pgcd_imp(a, b):
    if a > b:
        a, b = b, a
    while (a != 0) and (a != b) :
        a, b = b % a, a
    return b

def pgcd_rec(a, b):
    if a == 0:
        return b
    elif a == b:
        return b
    elif a > b:
        return pgcd_rec(b, a)
    else:
        return pgcd_rec(b % a, a)

def test_pgcd(pgcd_fun):
    test_values = [
        ((0,0), 0),
        ((4,4), 4),
        ((4,0), 4),
        ((3,5), 1),
        ((5,3), 1),
        ((12,42), 6),
    ]
    for ((a,b), c) in test_values:
        assert(pgcd_fun(a,b) == c)

test_pgcd(pgcd_imp)
test_pgcd(pgcd_rec)
