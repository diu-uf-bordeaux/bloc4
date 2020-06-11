---
layout: page_ext
title: "Opérations sur les graphes - solutions"
permalink: /td/graphes/operations/solutions/
---

- [Retour aux exercices sur les graphes](../../)

- [Retour à l'exercice](../)

### Solutions avec les matrices d'adjacence

```python
def degre(graphe, sommet):
  i = sommets(graphe).index(sommet)
  c = 0
  for j in range(len(sommets(graphe))):
    c += graphe[1][i][j]
  return len(voisins(graphe, sommet))

def est_isole(graphe, sommet):
  return degre(graphe, sommet) == 0

def degre_moyen(graphe):
  c = 0
  for s in sommets(graphe):    
        c += degre(graphe,s)
  return c/len(sommets(graphe))

def sont_voisins(graphe, s1, s2):
  i = sommets(graphe).index(s1)
  j = sommets(graphe).index(s2)
  return graphe[1][i][j] == 1
```

### Solutions avec les listes de successeurs

```python
import functools
import operator

def degre(graphe, sommet):
  return len(voisins(graphe, sommet))
  
def est_isole(graphe, sommet):
  return degre(graphe, sommet) == 0

def degre_moyen(graphe):
  S = sommets(graphe)
  # c = 0
  # for s in S:
  #   c += degre(graphe, s)
  # return c / len(S)
  return functools.reduce(operator.add, [ degre(graphe,s) for s in S ]) / len(S)

def sont_voisins(graphe, s1, s2):
  return s2 in voisins(graphe, s1)
```