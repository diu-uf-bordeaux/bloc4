---
layout: page_ext
title: "Exercices sur la programmation modulaire"
permalink: /td/modular/
---

- [Retour à l'ensemble des exercices](../)

- [Accès aux solutions](./td_modular.solutions.md)


### Une application monolithique

Supposons partir du [code suivant](./code.py) qui permet de manipuler
des suites de nombres. Ce code est complètement monolithique, et donc
difficile à faire évoluer. Pire, les fonctions à l'intérieur sont
mises à plat, mélangées, et contiennent des morceaux de code en
commentaire. Enfin, les standards de codage sont faibles, il manque
des indications de types à plusieurs endroits.

Proposer une décomposition du code en plusieurs fichiers Python
indépendants. On s'assurera des choses suivantes :

- chaque fichier est du code Python valide, ce qui signifie que l'on
  peut les exécuter avec `python` sans erreur (même s'ils ne font
  aucun calcul)

- il est possible d'exécuter les tests, ou de choisir un affichage
  (sans les autres), et cela de manière indépendante.

Remarque : le code utilise la bibliothèque `matplotlib` pour dessiner
les suites. Si jamais cela posait difficulté d'installation, il est
possible de faire l'exercice en supprimant l'ensemble des fonctions
commençant par `code_` et le chargement de la bibliothèque
`matplotlib`.
