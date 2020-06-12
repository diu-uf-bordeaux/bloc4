---
layout: page_ext
title: "Map &amp; Reduce"
---

- [Retour aux exercices de programmation fonctionnelle](./td_functional.md)

- [Retour aux exercices sur map &amp; reduce](./td_mapreduce.md)


### 1ère partie : les fonctions d'ordre supérieur

```python
def map_imp(f, l):
    res = []
    for x in l:
        res.append(f(x))
    return res

def map_rec(f, l):
    if (len(l) == 0):
        return []
    else:
        return [f(l[0])] + map_rec(f, l[1:])
```

```python
def filter_imp(f, l):
    res = []
    for x in l:
        if (f(x)):
            res.append(x)
    return res

def filter_rec(f, l):
    if (len(l) == 0):
        return []
    elif f(l[0]):
        return [l[0]] + filter_rec(f, l[1:])
    else:
        return filter_rec(f, l[1:])
```

```python
def sum_imp(f, l):
    res = 0
    for x in l:
        res += f(x)
    return res

def sum_rec(f, l):
    if (len(l) == 0):
        return 0
    else:
        return f(l[0]) + sum_rec(f, l[1:])
```

```python
def reduce_imp(f, acc, l):
    res = acc
    for x in l:
        res = f(res, x)
    return res

def reduce_rec(f, acc, l):
    if (len(l) == 0):
        return acc
    else:
        return reduce_rec(f, f(acc, l[0]), l[1:])
```

```python
def reverse_reduce(l):
    return reduce_rec(lambda acc, x: [x] + acc, [], l)
```

### 2ème partie : sagesse de l'Antiquité

```python
age = lambda s: s["death"] - s["birth"]

names = sorted(map_rec(lambda s: s["name"], sages))
names = sorted([s["name"] for s in sages])

most_ancient = sorted(sages, key=lambda s: s["birth"])[0]

most_longlived = sorted(sages, key=age, reverse=True)[0]

mean_age = sum(map_rec(age, sages)) / len(sages)
```

### 3ème partie : questions de parallélisation

Pas de code demandé dans cette partie.
