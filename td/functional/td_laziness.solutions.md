---
layout: page_ext
title: "Programmation paresseuse"
---

- [Retour aux exercices de programmation fonctionnelle](./td_functional.md)

- [Retour aux exercices sur la programmation paresseuse](./td_laziness.md)

### 1ère partie : les itérateurs Python

```python
it = map(f, range(3))
try:
    for i in range(4):
        print(it.__next__())
except StopIteration:
    print("Exception raised : StopIteration")
```

```python
it = filter(lambda x: (f(x) % 2 == 0), range(4))
try:
    for i in range(4):
        print(it.__next__())
except StopIteration:
    print("Exception raised : StopIteration")
```

```python
def make_function():
    x = [0]
    def f():
        x[0] = x[0]+1
        return x[0]
    return f

def make_infinite_iter():
    return iter(make_function(), -1)

for i in make_infinite_iter():
	print(i) # Infinite loop
	if i >= 10000:
		break
```

### 2ème partie : les expressions congelées

```python
def make_value(x):
    return lambda : x

def make_addition(a, b):
    return lambda : a() + b()

op = make_addition(make_value(5), make_value(6))
op()
```

### 3ème partie : le contrôle de l'évaluation

- La version de base

```python
def pgcd(a, b):
    if a == 0:
        return b
    elif a == b:
        return b
    elif a > b:
        return pgcd(b, a)
    else:
        return pgcd(b % a, a)
```

```python
print(pgcd(7,5))
```

- La version avec contrôle des calculs

```python
def pgcd_lazy(a, b):
    if a == 0:
        return lambda: b
    elif a == b:
        return lambda: b
    elif a > b:
        return lambda: pgcd_lazy(b, a)
    else:
        return lambda: pgcd_lazy(b % a, a)
```

```python
f = pgcd_lazy(7,5)
print(f)
print(f())
print(f()())
print(f()()())
print(f()()()())
print(f()()()()())
```

- La version avec affichage des valeurs intermédiaires

```python
def pgcd_dbg(a, b):
    dic = {"a":a, "b":b }
    if a == 0:
        return lambda: (b, dic)
    elif a == b:
        return lambda: (b, dic)
    elif a > b:
        return lambda: (pgcd_dbg(b, a), dic)
    else:
        return lambda: (pgcd_dbg(b % a, a), dic)
```

```python
f = pgcd_dbg(7,5)
print(f)
print(f())
print(f()[0]())
print(f()[0]()[0]()[0]())
print(f()[0]()[0]()[0]()[0]())
```
