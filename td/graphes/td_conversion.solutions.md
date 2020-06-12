---
layout: page_ext
title: "Passage d'une représentation à l'autre - solutions"
permalink: /td/graphes/conversions/solutions/
---

- [Retour aux exercices sur les graphes](../../)

- [Retour à l'exercice](../)

Les deux représentations étant implémentées dans leur module respectif :

```python
import graphe_listes as gl
import graphe_matrice as gm
```

- Passage des listes de successeurs à une matrice d'adjacence

```python
def gl2gm(graphe_listes):
  graphe_matrice = gm.creer_graphe(gl.sommets(graphe_listes))
  for s1 in gl.sommets(graphe_listes):
    for s2 in gl.voisins(graphe_listes, s1):
      gm.ajouter_arete(graphe_matrice, s1, s2)
  return graphe_matrice
```

- Passage d'une matrice d'adjacence à des listes de successeurs

```python
def gm2gl(graphe_matrice):
  graphe_listes = gl.creer_graphe(gm.sommets(graphe_matrice))
  for s1 in gm.sommets(graphe_matrice):
    print(gm.voisins(graphe_matrice, s1))
    for s2 in gm.voisins(graphe_matrice, s1):
      gl.ajouter_arete(graphe_listes, s1, s2)
  return graphe_listes
```