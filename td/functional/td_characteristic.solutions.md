---
layout: page_ext
title: "Fonctions caractéristiques"
---

- [Retour aux exercices de programmation fonctionnelle](./td_functional.md)

- [Retour aux exercices sur les fonctions caractéristiques](./td_characteristic.md)


### 1ère partie : les fonctions caractéristiques

```python
def set_all(x):
    return True

def set_empty(x):
    return False

def set_single(x):
    return lambda y: (x == y)

def belongs(s, x):
    return s(x)

def set_complement(s):
    return lambda y: not(s(y))

def set_union(s1, s2):
    return lambda y: s1(y) or s2(y)

def set_intersection(s1, s2):
    return lambda y: s1(y) and s2(y)

def set_add(s, x):
    return lambda y: s(y) or y == x
```

### 2ème partie : les ensembles de points du plan

```python
def dist(p1, p2):
    return np.sqrt((p1[0] - p2[0])**2 + (p1[1] - p2[1])**2)

def set_circle(c, r):
    return lambda y: dist(y, c) <= r

def set_square(p1, p2):
    return lambda y: y[0] >= p1[0] and y[0] <= p2[0] and \
        y[1] >= p1[1] and y[1] <= p2[1]
```

```python
c1 = set_circle((5,5), 3)
c2 = set_complement(set_circle((7.5,3.5), 1))
r  = set_square((4,0),(10,10))
s = set_intersection(set_intersection(c1,c2), r)

set_display_2d(s)
```

Fonctions de transformation géométriques :


```python
def translate(deltax, deltay):
    return lambda p: (p[0] + deltax, p[1] + deltay)

def scale(a, b):
    return lambda p: (p[0] * a, p[1] * b)

def rotate(theta):
    costheta = math.cos(theta)
    sintheta = math.sin(theta)
    return lambda p: (p[0] * costheta - p[1] * sintheta, \
                      p[1] * costheta + p[0] * sintheta)

def set_translate(s, deltax, deltay):
    return lambda p: s(translate(-deltax, -deltay)(p))

def set_scale(s, a, b):
    return lambda p: s(scale(1./a,1./b)(p))

def set_rotate(s, theta):
    return lambda p: s(rotate(-theta)(p))

def set_rotate_rel(s, theta, p):
    cen_x = p[0]
    cen_y = p[1]
    return lambda p: s(translate(cen_x, cen_y)(rotate(theta)(translate(-cen_x,-cen_y)(p))))
```


### 3ème partie : les listes de lectures

```python
r1 = lambda m: "rock" in m["genre"]
r2 = lambda m: m["title"].startswith("Don't")

def generate_playlist(req, n):
    res = []
    valid_songs = [ s for s in songs if req(s) ]
    if len(valid_songs) == 0:
        return res
    for i in range(n):
        res.append(random.choice(valid_songs))
    return res
```
