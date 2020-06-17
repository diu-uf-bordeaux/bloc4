---
layout: page_ext
title: "Exercices sur les listes"
permalink: /td/listes/
---

[Retour à l'ensemble des exercices](../)

### Implémentations disponibles

Pour travailler sur les listes, deux implémentations sont disponibles,
dans les codes suivants :

- Classe `Cellule` : [code](./classe_cellule.py), une implémentation
  orientée objet
{: .list}

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

La classe `Cellule` s'utilise ainsi :

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

Note : dans cette implémentation, `Cellule.liste_vide` *n'est pas* une
instance de `Cellule`, et donc on *ne peut pas* appeler de méthodes
dessus.

- Code liste : [code](./code_liste.py), une implémentation orientée
fonctionnelle
{: .list}

```python
def liste_vide():
    return []

def cellule(etiquette, liste):
    return [etiquette, liste]

def valeur(liste):
    return liste[0]

def suite(liste):
    return liste[1]

def est_vide(liste):
    return liste == liste_vide()
```

Cette implémentation s'utilise ainsi :

```python
import code_list as lis

l1 = lis.liste_vide()  # returns an empty list
l2 = lis.cellule(1, lis.liste_vide)
l3 = lis.cellule(2, l2)

lis.est_vide(l1) # -> True
lis.est_vide(l2) # -> False

lis.suite(l3)       # -> returns a list
lis.suite(l3) == l2 # -> True
```

### Exercices

Implémenter les méthodes demandées dans les exercices suivants à
l'aide des deux implémentations précédentes, pour bien intégrer le
fonctionnement d'une liste.

- [Opérations sur les listes](./operations/)

- [Représentation polynomiale](./polynome/)
