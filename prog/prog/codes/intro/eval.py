i = 0

def f():
    global i
    i = i + 1
    return i

def g():
    global i
    i = i + 2
    return i

print("Returns -2 = 1 - 3 : {}".format(f() - g()))

class SideEffect():
    def __init__(self):
        self.i = 0

    def f(self):
        self.i += 1
        return self.i

    def g(self):
        self.i += 2
        return self.i

    def h(self, z, t):
        self.i += 3
        return self.i

s = SideEffect()
print("Returns -2 = 1 - 3 : {}".format(s.f() - s.g()))
s = SideEffect()
print("Returns 6 = 1 + 2 + 3 : {}".format(s.h(s.f(), s.g())))
