# def pgcd(a, b):
#     if a > b:
#         a, b = b, a
#     while (a != 0) and (a != b) :
#         a, b = b % a, a
#     return b

def pgcd(a, b):
    if a == 0:
        return b
    if a == b:
        return b
    if a > b:
        return pgcd(b, a)
    return pgcd(b % a, a)

assert(pgcd(4,4) == 4)
assert(pgcd(4,0) == 4)
assert(pgcd(3,5) == 1)
assert(pgcd(5,3) == 1)
assert(pgcd(12,42) == 6)
