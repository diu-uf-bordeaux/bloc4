---
layout: page_ext
title: "Opérations"
permalink: /td/listes/operations/
---

[Retour aux exercices sur les listes](../)

L'objectif de ce TD est de proposer de nouvelles méthodes pour le type `Liste`.

Pour commencer, ajoutez les prédicats suivants :

```python
str_liste : Liste -> str
  # à partir d'une liste L, produit une chaîne de caractères décrivant L

taille_liste : Liste -> entier
  # à partir d'une liste L, renvoie le nombre d'éléments qu'elle contient
```

Nous pourrons ensuite ajouter deux autres prédicats :

```python
max_liste: Liste -> entier
  # à partir d'une liste L, renvoie la valeur maximum ou une exception si L est vide

min_liste: Liste -> entier
  # à partir d'une liste L, renvoie la valeur minimum ou une exception si L est vide
```

Enfin, pour poussez encore plus loin, essayez d'implémenter le transformateur suivant :

```python
trier_liste: Liste -> Liste
  # à partir d'une liste L, renvoie cette liste avec les valeurs triées (tri au choix)
```

- [Accès aux solutions au format web](./td_operations.solutions.md)
- [Accès au code solution en objet (classe Cellule)](./solution_liste_operations_objet_cellule.py)
- [Accès au code solution en fonctionnel](./solution_liste_operations.py)
- [Accès au code solution en objet (classe Liste)](./solution_liste_operations_objet_liste.py)