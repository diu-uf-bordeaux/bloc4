---
layout: page_ext
title: "Piles"
permalink: /td/filesPiles/piles/
---

[Retour aux exercices sur les files et piles](../)

L'objectif de ce TD est de proposer de nouvelles méthodes pour le type `Pile` à l'aide des codes suivants:

- Classe `Pile` : [code](./classe_pile.py)
- Code `Pile` : [code](./code_pile.py)
{: .list}

Pour commencer, ajoutez le prédicat suivant :

```python
taille : Pile -> entier
  # à partir d'une pile P, renvoie le nombre d'éléments qu'elle contient
```

Nous pourrons ensuite ajouter deux autres prédicats :

```python
max: Pile -> entier
  # à partir d'une pile P, renvoie la valeur maximum

min: Pile -> entier
  # à partir d'une pile P, renvoie la valeur minimum
```

Ensuite, proposez une implémentation pour la méthode suivante :

```python
copie: Pile -> Pile
    # Renvoie une copie de la pile en paramètre dans une nouvelle pile
```

Nous allons maintenant nous intéresser à une opération un peu plus compliquée : à partir d'une file contenant des parenthèses, crochets et accolades, vérifier si le parenthésage est bon.
Vous aurez besoin d'une pile.
Exemple :

```python
["(", "[", "]", ")"] -> True
["(", "[", ")", "]"] -> False
```

Enfin, pour pousser un peu plus loin, proposez une implémentation de la méthode suivante :

```python
switch: Pile -> Pile
    # Inverse les éléments du sommet et du bas de la pile uniquement
```

- [Accès au code solution en objet](./solution_pile_operations_objet.py)
- [Accès au code solution en fonctionnel](./solution_pile_operations.py)