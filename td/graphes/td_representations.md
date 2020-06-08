---
layout: page_ext
title: "Manipulation des représentations"
permalink: /td/graphes/representations/
---

[Retour aux exercices sur les graphes](../)

L'objectif des exercices de cette page est de manipuler les deux représentations des graphes vues en cours : les matrices d'adjacence et les listes de successeurs.

### 1ère partie : activités débranchées

1. Pour chaque graphe ci-dessous, donnez :
   - sa matrices d'adjacence,
   - ses listes de successeurs,
   - ses listes de prédécesseurs.
   {: .list}
   1. <img src="../images/graphe1.svg" width="225px"/>
   2. <img src="../images/graphe2.svg" width="225px"/>
   3. <img src="../images/graphe3.svg" width="225px"/>
   {: .list_alpha_inline}

2. Pour chaque tableau ci-dessous, tracez le graphe correspondant et donnez sa matrice d'adjacence.
   1. | **sommet**      | a | b    | c | d | e |
      |-------------|---|------|---|---|---|
      | **successeurs** | b | a,c,d| b | e |   |
      {: .graph}
   2. | **sommet**        | a | b    | c | d | e |
      |---------------|---|------|---|---|---|
      | **prédécesseurs** | b | a,c,d| b | e |   |
      {: .graph}
   3. | **sommet**        | a | b | c | d | e |
      |---------------|---|---|---|---|---|
      | **prédécesseurs** |   | a | b | c | d |
      {: .graph}
   {: .list_alpha_inline}

3. Pour chaque matrice d'adjacence ci-dessous, tracez le graphe associé et donnez ses listes de successeurs et de prédécesseurs.
   - $$\begin{pmatrix}
      0 & 1 & 1\\
      1 & 0 & 0\\
      0 & 0 & 1\\
      \end{pmatrix}$$ associée à l'ensemble de sommets $S=\\{a,b,c\\}$.
   - $$\begin{pmatrix}
      1 & 1 & 0 & 1\\
      1 & 0 & 0 & 1\\
      0 & 0 & 0 & 0\\
      0 & 1 & 1 & 1\\
      \end{pmatrix}$$ associée à l'ensemble de sommets $S=\\{a,b,c,d\\}$.
   {: .list_alpha}


### 2ème partie : implémentation en Python

Avec le type abstrait `Graphe simple` défini en cours, passer d'une représentation à l'autre consiste à énumérer les sommets et les voisins depuis une représentation tout en construisant l'autre représentation.

Écrivez deux fonctions Python permettant respectivement de passer des listes de successeurs à une matrice d'adjacence et réciproquement.