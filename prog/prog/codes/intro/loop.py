def fun_with_loop(n):
        res = 0
        for i in range(n):
                res += i
        return res

def fun_with_rec(n):
    def f_int(res, i):
            return (res+i, i+1)
    def f_rec(res, i):
            if (i < n):
                    return f_rec(*f_int(res, i))
            else:
                    return res
    return f_rec(0, 0)

def fun_with_rec2(n):
    def f_rec(res, i):
            if (i < n):
                    return f_rec(res+i, i+1)
            else:
                    return res
    return f_rec(0, 0)

n = 100;
print([fun_with_loop(n), fun_with_rec(n), fun_with_rec2(n)])
