import functools
import math
import operator

class Expr:
    def eval(self):
        raise Exception("Cannot evaluate abstract expression")

class Value(Expr):
    def __init__(self, v):
        self.value = v
    def __repr__(self):
        return "{}".format(self.value)
    def eval(self):
        return self.value

class UnaryOp(Expr):
    def __init__(self, op, op_name, arg):
        self.op  = op
        self.op_name = op_name
        self.arg = arg
    def __repr__(self):
        return "{}({})".format(self.op_name, self.arg)
    def eval(self):
        try:
            return self.op(self.arg.eval())
        except:
            return None

class BinaryOp(Expr):
    def __init__(self, op, op_name, arg1, arg2):
        self.op  = op
        self.op_name = op_name
        self.arg1 = arg1
        self.arg2 = arg2
    def __repr__(self):
        return "{}({},{})".format(self.op_name, self.arg1, self.arg2)
    def eval(self):
        try:
            return self.op(self.arg1.eval(), self.arg2.eval())
        except:
            return None

def fact(x):
    if x < 0 or x > 100:
        return None
    else:
        return functools.reduce(operator.mul, range(1, x))

def sqrt(x):
    res = int(math.sqrt(x))
    if res*res == x:
        return res
    else:
        return None

def div(x, y):
    res = x // y
    if res * y == x:
        return res
    else:
        return None

def pow(x, y):
    if y < 0 or y > 100:
        return None
    else:
        return x**y

def make_value(e): return Value(e)

def make_sqrt_op(e): return UnaryOp(sqrt, "sqrt", e)
def make_fact_op(e): return UnaryOp(fact, "fact", e)

def make_add_op(e1,e2): return BinaryOp(lambda a,b: a+b, "plus", e1, e2)
def make_sub_op(e1,e2): return BinaryOp(lambda a,b: a-b, "minus", e1, e2)
def make_mul_op(e1,e2): return BinaryOp(lambda a,b: a*b, "times", e1, e2)
def make_div_op(e1,e2): return BinaryOp(div, "div", e1, e2)
def make_pow_op(e1,e2): return BinaryOp(pow, "pow", e1, e2)

unary_ops = [
    make_sqrt_op,
    make_fact_op,
    ]

binary_comm_ops = [
    make_add_op,
    make_mul_op,
    ]

binary_not_comm_ops = [
    make_sub_op,
    make_div_op,
    make_pow_op,
    ]

def generate_trees(size, c):
    cache = { 0: [ make_value(c) ] }
    def generate_rec(sizerec):
        if sizerec in cache:
            return cache[sizerec]
        else:
            res = []
            for u in unary_ops:
                res = res + list(map(u, generate_rec(sizerec-1)))
            for b in binary_not_comm_ops:
                for a in range(0, sizerec):
                    res = res + [ b(a1, a2) for a1 in generate_rec(a)
                                  for a2 in generate_rec(sizerec-a-1) ]
            for b in binary_comm_ops:
                for a in range(0, sizerec // 2):
                    res = res + [ b(a1, a2) for a1 in generate_rec(a)
                                  for a2 in generate_rec(sizerec-a-1) ]
            cache[sizerec] = res
            return res
    return generate_rec(size)

size   = 2
number = 6
trees  = generate_trees(size, number)
print("Found {} trees for size={} and c={}".format(len(trees), size, number))

def find_solution_of_size(size, number, goal):
    trees  = generate_trees(size, number)
    print(len(trees))
    res = []
    for t in trees:
        if t.eval() == goal:
            res.append(t)
    return res

print(find_solution_of_size(6, 4, 2020))
