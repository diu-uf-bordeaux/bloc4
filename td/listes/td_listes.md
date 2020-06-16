---
layout: page_ext
title: "Exercices sur les listes"
permalink: /td/listes/
---

[Retour à l'ensemble des exercices](../)

Pour travailler sur les listes, deux TDs sont disponibles, à l'aide des codes suivants :

- Classe `Cellule` : [code](./classe_cellule.py)

```python
class Cellule:
    liste_vide = None

    def __init__(self, etiquette, liste):
        self._valeur = etiquette
        self._suivant = liste

    def valeur(self):
        return self._valeur

    def suite(self):
        return self._suivant

    def est_vide(liste):
        return liste is Cellule.liste_vide
```

La classe s'utilise ainsi :

```python
from classe_cellule import Cellule

l1 = Cellule.liste_vide  # returns an empty list
l2 = Cellule(1, Cellule.liste_vide)
l3 = Cellule(2, l2)

Cellule.est_vide(l1) # -> True
Cellule.est_vide(l2) # -> False

l3.suite()                # -> returns a list
l3.suite() == l2          # -> True
```

- Code liste : [code](./code_liste.py)
{: .list}

Essayez d'implémenter les méthodes demandées dans différents paradigmes pour bien intégrer le fonctionnement d'une liste.

- [Opérations sur les listes](./operations/)

- [Représentation polynomiale](./polynome/)
