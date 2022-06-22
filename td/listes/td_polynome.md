---
layout: page_ext
title: "Polynômes avec des listes"
permalink: /td/listes/polynome/
---

- [Retour aux exercices sur les listes](../)

L'objectif de ce TD est de proposer une gestion de polynômes à l'aide de listes.

Les cellules, triées par ordre décroissant, représenteront chaque degré du polynôme et la valeur de ces cellules sera le multiplicateur. Par exemple, le polynôme $3x^3+x+6$ sera représenté par la liste suivante :

```python
[3]-[0]-[1]-[6]
```

Proposez une méthode qui calcule pour un $x$ donné en paramètre, la valeur du polynôme :

```python
calcul: (Valeur * Liste) -> Valeur
    # Pour une valeur et un polynome donné, renvoi la valeur calculée du polynôme.
```

Proposez ensuite plusieurs méthodes, d'abord d'addition et de soustraction :

```python
addition: (Liste * Liste) -> Liste
    # Pour deux polynômes donnés, renvoi la somme des deux

soustraction: (Liste * Liste) -> Liste
    # Pour deux polynômes donnés, renvoi la soustraction du premier par le deuxième
```

Enfin, proposez une méthode pour multiplier deux polynômes entre eux :

```python
multiplier: (Liste * Liste) -> Liste
    # Pour deux polynômes donnés, renvoi le polynôme résultant de la multiplication des ces derniers
```

Pour aller encore plus loin :

```python
diviser: (Liste * Liste) -> Liste
    # Renvoi la division des deux polynômes en paramètres
```

- [Accès au code solution en objet (classe Cellule)](./solution_liste_poly_objet.py)
- [Accès au code solution en fonctionnel](./solution_liste_poly.py)