---
layout: page_ext
title: "Tchisla"
---

- [Retour aux exercices de programmation fonctionnelle](./td_functional.md)

- [Retour aux exercices sur Tchisla](./td_tchisla.md)

```python
import math
```


### 1ère partie

```python
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
```

### 2ème partie : un peu de programmation fonctionnelle

```python
# "0"-ary operations
def make_value(e):
    return Value(e)

# Unary operations
def make_sqrt_op(e):
    return UnaryOp(lambda x: int(math.sqrt(x)), "int_sqrt", e)

def make_fact_op(e):
    return UnaryOp(lambda x: math.factorial(x), "fact", e)

unary_ops = [
    make_sqrt_op,
    make_fact_op,
    ]

# Binary operations
def make_add_op(e1,e2):
    return BinaryOp(lambda a,b: a+b, "plus", e1, e2)

def make_sub_op(e1,e2):
    return BinaryOp(lambda a,b: a-b, "minus", e1, e2)

def make_mul_op(e1,e2):
    return BinaryOp(lambda a,b: a*b, "times", e1, e2)

def make_div_op(e1,e2):
    return BinaryOp(lambda a,b: a//b, "div", e1, e2)

def make_pow_op(e1,e2):
    return BinaryOp(lambda a,b: a**b, "pow", e1, e2)

# Commutative binary operations
binary_comm_ops = [
    make_add_op,
    make_mul_op,
    ]

# Non-commutative binary operations
binary_not_comm_ops = [
    make_sub_op,
    make_div_op,
    make_pow_op,
    ]
```

### 3ème partie : un algorithme d'énumération

Le programme final est donné en 4ème partie.

### 4ème partie : des optimisations possibles

```python
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
                for a in range(0, math.ceil(sizerec / 2)):
                    res = res + [ b(a1, a2) for a1 in generate_rec(a)
                                  for a2 in generate_rec(sizerec-a-1) ]
            cache[sizerec] = res
            return res
    return generate_rec(size)

def find_solution_of_size(size, number, goal):
    trees  = generate_trees(size, number)
    print(len(trees))
    res = []
    for t in trees:
        if t.eval() == goal:
            res.append(t)
    return res
```

### 5ème partie : recherche d'une unique solution


```python
def generate_values(size, c):
    """Generate all expressions of size up to `size` internal operations,
       and leaves valued by `c`, one per evaluated value.
       The expressions are memoized.
    """
    cache = { 0 : { c: make_value(c) } }
    def generate_rec(sizerec):
        if (sizerec) in cache:
            return cache[(sizerec)]
        else:
            print(f"Generate rec of size {sizerec}")
            s = {}
            for u in unary_ops:
                for lu in generate_rec(sizerec-1).values():
                    e = u(lu)
                    s[e.eval()] = e
            for b in binary_not_comm_ops:
                for a in range(0, sizerec):
                    # print(f"Generating size {a},{sizerec-a-1} for {b.__name__}")
                    for la in generate_rec(a).values():
                        for lb in generate_rec(sizerec-a-1).values():
                            e = b(la, lb)
                            s[e.eval()] = e
            for b in binary_comm_ops:
                for a in range(0, math.ceil(sizerec / 2)):
                    # print(f"Generating size {a},{sizerec-a-1} for {b.__name__}")
                    for la in generate_rec(a).values():
                        for lb in generate_rec(sizerec-a-1).values():
                            e = b(la, lb)
                            s[e.eval()] = e
            cache[sizerec] = s
            return s
    return generate_rec(size)
```
