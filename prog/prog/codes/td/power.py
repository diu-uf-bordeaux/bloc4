def power_for(a, n):
    res = 1
    for i in range(n):
        res *= a
    return res

def power_lin(a, n):
    if (n == 0):
        return 1
    else:
        return a * power_lin(a, n-1)

def power_bin(a, n):
    if (n == 0):
        return 1
    elif (n == 1):
        return a
    elif (n % 2 == 0):
        b = power_bin(a, n // 2)
        return b*b
    else:
        b = power_bin(a, n // 2)
        return a * b * b

def test_power(power_fun):
    test_values = [
        ((0,0), 1),
        ((4,4), 256),
        ((4,0), 1),
        ((3,5), 243),
        ((5,3), 125),
        ((12,12), 8916100448256),
    ]
    for ((a,b), c) in test_values:
        assert(power_fun(a,b) == c)

test_power(power_for)
test_power(power_lin)
test_power(power_bin)
