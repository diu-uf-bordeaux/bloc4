---
layout: page_ext
title: "Récursivité"
---

- [Retour aux exercices de programmation fonctionnelle](./td_functional.md)

- [Retour aux exercices sur la récursivité](./td_recursivity.md)

Cette page contient un ensemble de fonctions qu'il est possible de
programmer de manière fonctionnelle pure, en utilisant des algorithmes
récursifs. A chaque fois, on insiste sur la description formelle de la
fonction à représenter, on discute les problèmes de terminaison, et de
complexité.

### 1ère partie : Exponentiation

- La version linéaire

```python
def power_lin(a, n):
    if (n == 0):
        return 1
    else:
        return a * power_lin(a, n-1)
```

- La version binaire

```python
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
```


### 2ème partie : PGCD

- La version récursive

```python
def pgcd_rec(a, b):
    if a == 0:
        return b
    elif a == b:
        return b
    elif a > b:
        return pgcd_rec(b, a)
    else:
        return pgcd_rec(b % a, a)
```

- La version impérative (avec boucle for)

```python
def pgcd_imp(a, b):
    if a > b:
        a, b = b, a
    while (a != 0) and (a != b) :
        a, b = b % a, a
    return b
```

- La page [Rosetta
Code](https://rosettacode.org/wiki/Greatest_common_divisor) contenant
un ensemble d'écritures différentes pour la fonction PGCD.

- Un exemple de fonction pour tester les différentes fonctions de
  calcul de PGCD&nbsp;:

```python
def test_pgcd(pgcd_fun):
    test_values = [
        ((0,0), 0),
        ((4,4), 4),
        ((4,0), 4),
        ((3,5), 1),
        ((5,3), 1),
        ((12,42), 6),
    ]
    for ((a,b), c) in test_values:
        assert(pgcd_fun(a,b) == c)
```

### 3ème partie : suite de Syracuse

```python
def syra(n):
    if (n == 1):
        return 1
    elif (n % 2 == 0):
        return syra(n // 2)
    else:
        return syra(3*n + 1)
```

```python
def flight(n):
    if (n == 1):
        return [1]
    elif (n % 2 == 0):
        return [n] + flight(n // 2)
    else:
        return [n] + flight(3*n + 1)
```

```python
def flight_len(n):
    if (n == 1):
        return 1
    elif (n % 2 == 0):
        return 1 + flight_len(n // 2)
    else:
        return 1 + flight_len(3*n + 1)
```

```python
def max_flight(flight_fun, n):
    max_s  = 1
    imax_s = 1
    for i in range(2, n+1):
        l = flight_fun(i)
        if (l > max_s):
            max_s  = l
            imax_s = i
    return imax_s
```

Une autre implémentation d'une fonction qui calcule la longueur d'un
vol, avec *mémoïsation* des calculs : on garde les calculs déjà faits
dans une variable (nommée ici `mem`). Dans l'exemple suivant, la
fonction `flight_mem` renvoie une fonction. Et cette fonction
permet de calculer plus rapidement les valeurs avec `max_flight`.

```python
def flight_mem():
    mem = { 1: 1 }  # stores computed flight lengths
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
```
Exemples d'utilisation des deux fonctions pour comparaison :

```python
n = 6
f = flight_mem()
# Comparaison des temps de calcul de f et de flight_len :
print(max_flight(flight_len, 10**n))
print(max_flight(f, 10**n))
```


### 4ème partie : récursivité et listes

```python
def search_rec(l, x):
    if (l == []):
        return False
    elif (l[0] == x):
        return True
    else:
        return search_rec(l[1:], x)
```

```python
def search_for(l, x):
    for y in l:
        if (x == y):
            return True
    return False
```

```python
def count_rec(l, x):
    if (l == []):
        return 0
    elif (l[0] == x):
        return 1 + count_rec(l[1:], x)
    else:
        return count_rec(l[1:], x)
```

```python
def count_for(l, x):
    res = 0
    for y in l:
        if (y == x):
            res += 1
    return res
```
