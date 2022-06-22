---
layout: page_ext
title: "Manipulation des représentations"
permalink: /td/graphes/representations/
---

[Retour aux exercices sur les graphes](../)

L'objectif des exercices de cette page est de manipuler sur papier les deux représentations des graphes vues en cours : les matrices d'adjacence et les listes de successeurs.

1. Pour chaque graphe ci-dessous, donnez :
   - sa matrices d'adjacence,
   - ses listes de successeurs,
   - ses listes de prédécesseurs.
   {: .list}
   1. <img src="../images/graphe1.svg" width="225px" height="115px"/>
   2. <img src="../images/graphe2.svg" width="225px" height="115px"/>
   3. <img src="../images/graphe3.svg" width="225px" height="115px"/>
   {: .list_alpha_inline}

2. Pour chaque tableau ci-dessous, tracez le graphe correspondant et donnez sa matrice d'adjacence.
   1. | **sommets**     | a | b   | c | d | e |
      |-----------------|---|-----|---|---|---|
      | **successeurs** | b | c,d | d | e |   |
      {: .graph}
   2. | **sommets**       | a | b   | c | d | e |
      |-------------------|---|-----|---|---|---|
      | **prédécesseurs** | b | c,d | d | e |   |
      {: .graph}
   3. | **sommet**        | a     | b   | c     | d   |
      |-------------------|-------|-----|-------|-----|
      | **prédécesseurs** | b,c,d | a,c | b,a,d | a,c |
      {: .graph}
   {: .list_alpha_inline}

3. Pour chaque matrice d'adjacence ci-dessous, tracez le graphe associé et donnez ses listes de successeurs et de prédécesseurs.
   - $$\begin{pmatrix}
      0 & 1 & 1\\
      1 & 0 & 0\\
      1 & 0 & 0\\
      \end{pmatrix}$$ associée à l'ensemble de sommets $S=\\{a,b,c\\}$.
   - $$\begin{pmatrix}
      0 & 0 & 0 & 1\\
      1 & 0 & 0 & 0\\
      0 & 0 & 0 & 0\\
      0 & 1 & 1 & 0\\
      \end{pmatrix}$$ associée à l'ensemble de sommets $S=\\{a,b,c,d\\}$.
   {: .list_alpha}

   [Accès aux solutions au format web](./solutions/)