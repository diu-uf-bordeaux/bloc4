
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
