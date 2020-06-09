---
layout: page_ext
title: "Récursivité"
---

- [Retour aux exercices de programmation fonctionnelle](./td_functional.md)

- [Accès aux solutions](./td_recursivity.solutions.md)

Cette page contient un ensemble de fonctions qu'il est possible de
programmer de manière fonctionnelle pure, en utilisant des algorithmes
récursifs. A chaque fois, on insiste sur la description formelle de la
fonction à représenter, on discute les problèmes de terminaison, et de
complexité.

### 1ère partie : Calcul de puissance

Les deux définitions suivantes permettent de calculer la fonction
$\mathrm{pow}(a,n) = a^n$ &nbsp;:

$$
\begin{cases}
\mathrm{pow}_1(a, 0) & = 1 \\
\mathrm{pow}_1(a, n) & = a * \mathrm{pow}_1(a, n-1) \quad \textrm{si}~ n \geq 1
\end{cases}
$$

$$
\begin{cases}
\mathrm{pow}_2(a, 0) & = 1 \\
\mathrm{pow}_2(a, 1) & = a \\
\mathrm{pow}_2(a, 2*n) & = \mathrm{pow}_2(a, n)^2 \quad \textrm{si}~ n \geq 1 \\
\mathrm{pow}_2(a, 2*n+1) & = a * \mathrm{pow}_2(a, n)^2 \quad \textrm{si}~ n \geq 1
\end{cases}
$$

Écrire chacun de ces algorithmes en Python. Évaluer pour chacun leur
complexité. Expliquer pourquoi le second algorithme nécessite plus de
cas pour sa définition que le premier.

### 2ème partie : PGCD

Une façon de calculer le plus grand commun diviseur entre deux nombres
consiste à implémenter l'[algorithme
d'Euclide](https://fr.wikipedia.org/wiki/Algorithme_d%27Euclide), dont
on fournit une définition ici&nbsp;:

$$
\begin{cases}
\mathrm{pgcd}(0, b) & = b \\
\mathrm{pgcd}(b, b) & = b \\
\mathrm{pgcd}(a, b) & = \mathrm{pgcd}(b, a) \quad \textrm{si}~ a > b \\
\mathrm{pgcd}(a, b) & = \mathrm{pgcd}(b \mod a, a) \quad \textrm{sinon}
\end{cases}
$$

Dessiner sur un quart de plan le chemin réalisé par le calcul de
$\mathrm{pgcd}(7,5)$. Donner une borne supérieure de la complexité du
calcul de $\mathrm{pgcd}(a,b)$. Écrire cet algorithme en Python,
d'abord de manière récursive, et ensuite avec une boucle `for`.

### 3ème partie : suite de Syracuse

La suite de Syracuse est une suite d'entiers naturels paramétrée par
une valeur de départ donnée, qui peut être construite à l'aide de la
fonction suivante&nbsp;:

$$
\begin{cases}
\mathrm{syra}(1) & = 1 \\
\mathrm{syra}(n) & = \mathrm{syra}(n/2) \quad \textrm{si}~ n ~\textrm{est pair et} \geq 1\\
\mathrm{syra}(n) & = \mathrm{syra}(3*n+1) \quad \textrm{sinon}
\end{cases}
$$

Cette suite est connue pour la fameuse [conjecture de
Syracuse](https://fr.wikipedia.org/wiki/Conjecture_de_Syracuse) qui
lui est associée. En 2017, il a été vérifié que pour tout entier $n \leq
87×2^{60}$, $\mathrm{syra}(n) = 1$.

Écrire le code en Python calculant la fonction précédente. Écrire le
code calculant la liste des valeurs atteintes lors du calcul de
$\mathrm{syra}(n)$, aussi appelé $\mathrm{vol}(n)$. Par exemple, pour
$n=12$&nbsp;:

$$ \mathrm{vol}(12) = [12, 6, 3, 10, 5, 16, 8, 4, 2, 1] $$

<span class="label">Plus difficile</span>Calculer l'entier ayant le
vol le plus long compris entre $1$ et un entier $n$ donné.

### 4ème partie : récursivité et listes

Les listes sont des types de données que l'on peut appeler
**inductifs**, signifiant ainsi qu'ils peuvent être pensés d'une
manière récursive. En effet, une liste `l` est :

- soit la liste vide (`[]`),

- soit composée d'un premier élément (la tête, `l[0]`), et d'une
  sous-liste de taille plus petite (la queue, `l[1:]`).

Écrire un code en Python recherchant de manière récursive si un
élément appartient à une liste Python.

$$
\begin{cases}
\mathrm{search}([], x) & = False \\
\mathrm{search}(l, x)  & = True \quad \textrm{si}~ l ~\textrm{est non vide et}~ x = l[0] \\
\mathrm{search}(l, x)  & = \mathrm{search}(l[1:], x) \quad \textrm{sinon}
\end{cases}
$$

Comparer au code réalisant la même chose avec une boucle `for`.

Adapter ce code pour compter le nombre d'occurrences d'un élément
apparaissant dans une liste, cela d'abord de manière récursive, puis
avec une boucle `for`. Déterminer parmi les fonctions que vous venez
d'écrire celles qui sont pures et celles qui font des effets de bord.
