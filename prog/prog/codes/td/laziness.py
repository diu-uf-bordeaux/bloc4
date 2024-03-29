def f(x):
        print("Using {}".format(x))
        return x+1

it = map(f, range(3))
try:
    for i in range(4):
        print(it.__next__())
except StopIteration:
    print("Exception raised : StopIteration")

it = filter(lambda x: (f(x) % 2 == 0), range(4))
try:
    for i in range(4):
        print(it.__next__())
except StopIteration:
    print("Exception raised : StopIteration")

def make_function():
    x = [0]
    def f():
        x[0] = x[0]+1
        return x[0]
    return f

def make_infinite_iter():
    return iter(make_function(), -1)

# This iterates through all positive integers
# for x in make_infinite_iter(): print(x)

def make_value(x):
    return lambda : x

def make_addition(a, b):
    return lambda : a() + b()

op = make_addition(make_value(5), make_value(6))
op()

def pgcd(a, b):
    if a == 0:
        return b
    elif a == b:
        return b
    elif a > b:
        return pgcd(b, a)
    else:
        return pgcd(b % a, a)

print(pgcd(7,5))

def pgcd_l(a, b):
    if a == 0:
        return lambda: b
    elif a == b:
        return lambda: b
    elif a > b:
        return lambda: pgcd_l(b, a)
    else:
        return lambda: pgcd_l(b % a, a)

f = pgcd_l(7,5)
print(f)
print(f())
print(f()())
print(f()()())
print(f()()()())
print(f()()()()())

def pgcd_s(a, b):
    dic = {"a":a, "b":b }
    if a == 0:
        return lambda: (b, dic)
    elif a == b:
        return lambda: (b, dic)
    elif a > b:
        return lambda: (pgcd_s(b, a), dic)
    else:
        return lambda: (pgcd_s(b % a, a), dic)

f = pgcd_s(7,5)
print(f)
print(f())
print(f()[0]())
print(f()[0]()[0]()[0]())
print(f()[0]()[0]()[0]()[0]())
