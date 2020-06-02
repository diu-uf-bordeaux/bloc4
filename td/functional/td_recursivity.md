
Cette page contient un ensemble de fonctions qu'il est possible de
programmer de manière fonctionnelle pure, en utilisant des algorithmes
récursifs. A chaque fois, on insiste sur la description formelle de la
fonction à représenter, on discute les problèmes de terminaison, et de
complexité.

### 1ère partie : PGCD

Une façon de calculer le plus grand commun diviseur entre deux nombres
consiste à implémenter l'[algorithme
d'Euclide](https://fr.wikipedia.org/wiki/Algorithme_d%27Euclide), dont
ou fournit une définition ici&nbsp;:

$$
\\begin{cases}
\mathrm{pgcd}(a, 0) & = a \\\\
\mathrm{pgcd}(a, a) & = a \\\\
\mathrm{pgcd}(a, b) & = \mathrm{pgcd}(b, a) \quad \textrm{si}~ a > b \\\\
\mathrm{pgcd}(a, b) & = \mathrm{pgcd}(b, a modulo b) \quad \textrm{sinon} \\\\
\end{cases}
$$
