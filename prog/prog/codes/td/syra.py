def syra(n):
    if (n == 1):
        return 1
    elif (n % 2 == 0):
        return syra(n // 2)
    else:
        return syra(3*n + 1)

def test_syra():
    max = 50
    for i in range(max):
        assert(syra(i) == 1)

def flight(n):
    if (n == 1):
        return [1]
    elif (n % 2 == 0):
        return [n] + flight(n // 2)
    else:
        return [n] + flight(3*n + 1)

print(flight(12))

def flight_len(n):
    if (n == 1):
        return 1
    elif (n % 2 == 0):
        return 1 + flight_len(n // 2)
    else:
        return 1 + flight_len(3*n + 1)

def flight_mem():
    mem = { 1: 1 }
    def flight_rec(n):
        if n in mem:
            return mem[n]
        elif (n % 2 == 0):
            l = flight_rec(n // 2)
            mem[n] = l+1
            return l+1
        else:
            l = flight_rec(3*n + 1)
            mem[n] = l+1
            return l+1
    return flight_rec

def max_flight(flight_fun, n):
    max_s  = 1
    imax_s = 1
    for i in range(2, n+1):
        l = flight_fun(i)
        if (l > max_s):
            max_s  = l
            imax_s = i
    return imax_s

n = 6
print(max_flight(flight_len, 10**n))
print(max_flight(flight_mem(), 10**n))
