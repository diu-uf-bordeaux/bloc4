---
layout: page_ext
title: "Expressions arithmétiques"
permalink: /td/arbres/expression/
---

- [Retour aux exercices sur les arbres binaires](../)

- [Accès aux solutions](./solutions/)

Une expression arithmétique construite avec des opérateurs binaires (c'est-à-dire à deux opérandes telles l'addition, la soustraction, la multiplication, la division) peut être représentée par un arbre binaire dont les nœuds internes portent les opérateurs et les feuilles des symboles de variables ($x$, $y$, $z$, etc.) ou des constantes ($6$, $14$, etc.)

Ainsi, l'arbre suivant représente l'expression $6(x+y)+(y−14)$.

<img src="../images/expression.svg" width="250px"/>

En utilisant l'implémentation à base de listes, cet arbre peut être construits avec l'instruction suivante :
```python
expression = noeud('+', 
                   noeud('*', 
                         noeud(6,arbre_vide(),arbre_vide()), 
                         noeud('+', 
                              noeud('x',arbre_vide(),arbre_vide()), 
                              noeud('y',arbre_vide(),arbre_vide()))), 
                   noeud('-', 
                         noeud('y',arbre_vide(),arbre_vide()), 
                         noeud(14,arbre_vide(),arbre_vide())))
```

1. Proposez une fonction `affiche` qui prend en paramètre un arbre représentant une expression arithmétique et affiche cette expression sur le terminal. Vous réalisez ainsi une **parcours infixe** de l'arbre.

2. Proposez une fonction `evalue` qui prend en paramètre un arbre représentant une expression arithmétique et renvoie la valeur de cette expression. 
<br/>
Il est nécessaire de fournir à cette fonction les valeurs associées à chacune des variables présentes dans l'expression.
Quelle structure de données proposez-vous d'utiliser pour mémoriser ces associations ?

3. Proposez une fonction `affichePolonaise` qui prend en paramètre un arbre représentant une expression arithmétique et affiche cette expression en utilisant la [notation polonaise inverse](https://fr.wikipedia.org/wiki/Notation_polonaise_inverse). Vous réalisez ainsi une **parcours postfixe** de l'arbre.
<br/>
Remarquez que cette expression non-ambiguë ne nécessite pas de parenthèses.