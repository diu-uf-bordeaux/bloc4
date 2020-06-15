---
layout: page_ext
title: "Opérations"
permalink: /td/filesPiles/files/
---

- [Retour aux exercices sur les files et piles](../)

L'objectif de ce TD est de proposer de nouvelles méthodes pour le type `File`.

Pour commencer, ajoutez le prédicat suivant:

```python
taille : File -> entier
  # à partir d'une file F, renvoi le nombre d'éléments qu'elle contient
```

Nous pourrons ensuite ajouter deux autres prédicats:

```python
max: File -> entier
  # à partir d'une file F, renvoi la valeur maximum

min: File -> entier
  # à partir d'une file F, renvoi la valeur minimum
```

Ensuite, proposez une implémentation pour la méthode suivante:

```python
inverse: File -> File
    # Renvoi une copie de la file en paramètre avec l'ordre des éléments inversé
```

Nous allons maintenant nous intéresser à des opérations un peu plus compliquées:

```python
trier: File -> File
  # Tri une liste donnée en paramètre

fusionne: (File * File) -> File
  # Fusionne deux files triées en une seule (bien triée)
```

Enfin, pour pousser un peu plus loin, proposez une implémentation pour la méthode suivante:

```python
popValeur: (Valeur * File) -> File
    # Enlève d'une file tout les éléments dont la valeur est passée en paramètre
```