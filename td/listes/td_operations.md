---
layout: page_ext
title: "Opérations"
permalink: /td/listes/operations/
---

- [Retour aux exercices sur les listes](../)

L'objectif de ce TD est de proposer de nouvelles méthodes pour le type `Liste`.

Pour commencer, ajoutez le prédicat suivant:

```python
taille : Liste -> entier
  # à partir d'une liste L, renvoi le nombre d'éléments qu'elle contient
```

Nous pourrons ensuite ajouter deux autres prédicats:

```python
max: Liste -> entier
  # à partir d'une liste L, renvoi la valeur maximum

min: Liste -> entier
  # à partir d'une liste L, renvoi la valeur minimum
```

Enfin, pour poussez encore plus loin, essayer d'implémenter le transformateur suivant:

```python
trier: Liste -> Liste
  # à partir d'une liste L, renvoi cette liste avec les valeurs triées (tri au choix)
```