---
layout: page_ext
title: "Manipulation des représentations - solutions"
permalink: /td/graphes/representations/solutions/
---

- [Retour aux exercices sur les graphes](../../)

- [Retour à l'exercice](../)

### 1ère partie : activités débranchées

#### Question 1

- Matrices d'adjacence
   1. $$\begin{pmatrix}
       0 & 1 & 1 & 0 \\
       1 & 0 & 1 & 1 \\
       1 & 0 & 0 & 0 \\
       0 & 1 & 0 & 0 \\
      \end{pmatrix}$$
   2. $$\begin{pmatrix}
       0 & 1 & 0 & 0 \\
       0 & 0 & 0 & 0 \\
       1 & 1 & 0 & 0 \\
       0 & 1 & 0 & 0 \\
      \end{pmatrix}$$
   3. $$\begin{pmatrix}
       0 & 0 & 1 & 0 & 0 \\
       0 & 0 & 0 & 0 & 0 \\
       0 & 0 & 0 & 0 & 1 \\
       1 & 0 & 0 & 0 & 0 \\
       0 & 0 & 0 & 1 & 0 \\
      \end{pmatrix}$$
   {: .list_alpha_inline}

- Listes de successeurs :
  1. | **sommet**      | a   | b     | c   | d |
     |-----------------|-----|-------|-----|---|
     | **successeurs** | b,c | a,c,d | a,b | b |
     {: .graph}
  2. | **sommet**      | a | b | c   | d |
     |-----------------|---|---|-----|---|
     | **successeurs** | b |   | a,b | b |
     {: .graph}
  3. | **sommet**      | a | b | c | d | e |
     |-----------------|---|---|---|---|---|
     | **successeurs** | c |   | e | a | d |
     {: .graph}
  {: .list_alpha_inline}

- Listes de prédécesseurs :
  1. | **sommet**        | a   | b     | c   | d |
     |-------------------|-----|-------|-----|---|
     | **prédécesseurs** | b,c | a,c,d | a,b | b |
     {: .graph}
  2. | **sommet**        | a | b     | c | d |
     |-------------------|---|-------|---|---|
     | **prédécesseurs** | c | a,c,d |   |   |
     {: .graph}
  3. | **sommet**        | a | b | c | d | e |
     |-------------------|---|---|---|---|---|
     | **prédécesseurs** | d |   | a | e | c |
     {: .graph}
  {: .list_alpha_inline}


#### Question 2

- Graphes :
   1. <img src="../../images/graphe4.svg" width="225px"/>
   2. <img src="../../images/graphe5.svg" width="225px"/>
   3. <img src="../../images/graphe6.svg" width="225px"/>
   {: .list_alpha_inline}

- Matrices d'adjacence :
   1. $$\begin{pmatrix}
       0 & 1 & 0 & 0 & 0 \\
       0 & 0 & 1 & 1 & 0 \\
       0 & 0 & 0 & 1 & 0 \\
       0 & 0 & 0 & 0 & 1 \\
       0 & 0 & 0 & 0 & 0 \\
      \end{pmatrix}$$
   2. $$\begin{pmatrix}
       0 & 0 & 0 & 0 & 0 \\
       1 & 0 & 0 & 0 & 0 \\
       0 & 1 & 0 & 0 & 0 \\
       0 & 1 & 1 & 0 & 0 \\
       0 & 0 & 0 & 1 & 0 \\
      \end{pmatrix}$$
   3. $$\begin{pmatrix}
       0 & 1 & 1 & 1 \\
       1 & 0 & 1 & 0 \\
       1 & 1 & 0 & 1 \\
       1 & 0 & 1 & 0 \\
      \end{pmatrix}$$
   {: .list_alpha_inline}


#### Question 3

- Graphes :
   1. <img src="../../images/graphe7.svg" width="145px"/>
   2. <img src="../../images/graphe8.svg" width="225px"/>
   {: .list_alpha_inline}

- Listes de successeurs :
  1. | **sommet**      | a   | b | c |
     |-----------------|-----|---|---|
     | **successeurs** | b,c | a | a |
     {: .graph}
  2. | **sommet**      | a | b | c | d |
     |-----------------|---|---|---|---|
     | **successeurs** | d | a |   | a |
     {: .graph}
  {: .list_alpha_inline}

- Listes de prédécesseurs :
  1. | **sommet**        | a   | b | c |
     |-------------------|-----|---|---|
     | **prédécesseurs** | b,c | a | a |
     {: .graph}
  2. | **sommet**        | a | b | c | d |
     |-------------------|---|---|---|---|
     | **prédécesseurs** | b | d | d | a |
     {: .graph}
  {: .list_alpha_inline}


### 2ème partie : implémentation en Python

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