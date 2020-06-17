---
layout: page_ext
title: "Fonctions caractéristiques"
---

- [Retour aux exercices de programmation sur les listes](./td_listes.md)

- [Retour aux exercices de programmation des opérations sur les listes](./td_operations.md)

### 1ère partie : implémentation objet, version avec ajout de fonctions

A partir du [code](./classe_cellule.py) de `Cellule` :

```python
def str_liste(l):
    if Cellule.est_vide(l):
        return "[]"
    else:
        return "[{},{}]".format(l.valeur(), str_liste(l.suite()))

def taille_liste(l):
    if Cellule.est_vide(l):
        return 0
    else:
        return 1 + taille_liste(l.suite())

def max_liste(l):
    if Cellule.est_vide(l):
        raise Exception("No max on an empty list")
    elif Cellule.est_vide(l.suite()):
        return l.valeur()
    else:
        return max(l.valeur(), max_liste(l.suite()))

def min_liste(l):
    if Cellule.est_vide(l):
        raise Exception("No min on an empty list")
    elif Cellule.est_vide(l.suite()):
        return l.valeur()
    else:
        return min(l.valeur(), min_liste(l.suite()))

def inserer_liste(x, l):
    if Cellule.est_vide(l):
        return Cellule(x, Cellule.liste_vide)
    elif x < l.valeur():
        return Cellule(x, l)
    else:
        return Cellule(l.valeur(), inserer_liste(x, l.suite()))

def trier_liste(l):
    if Cellule.est_vide(l):
        raise Exception("No min on an empty list")
    elif Cellule.est_vide(l.suite()):
        return l
    else:
        return inserer_liste(l.valeur(), trier_liste(l.suite()))
```

### 2ème partie : implémentation fonctionnelle

A partir du [code](./code_liste.py) fonctionnel :

```python
def str_liste(l):
    if lis.est_vide(l):
        return "[]"
    else:
        return "[{},{}]".format(lis.valeur(l), str_liste(lis.suite(l)))

def taille(l):
    if lis.est_vide(l):
        return 0
    else:
        return 1 + taille(lis.suite(l))

def max_liste(l):
    if lis.est_vide(l):
        raise Exception("No max on an empty list")
    elif lis.est_vide(lis.suite(l)):
        return lis.valeur(l)
    else:
        return max(lis.valeur(l), max_liste(lis.suite(l)))

def min_liste(l):
    if lis.est_vide(l):
        raise Exception("No min on an empty list")
    elif lis.est_vide(lis.suite(l)):
        return lis.valeur(l)
    else:
        return min(lis.valeur(l), min_liste(lis.suite(l)))

def inserer(x, l):
    if lis.est_vide(l):
        return lis.cellule(x, lis.liste_vide())
    elif x < lis.valeur(l):
        return lis.cellule(x, l)
    else:
        return lis.cellule(lis.valeur(l), inserer(x, lis.suite(l)))

def trier(l):
    if lis.est_vide(l):
        raise Exception("No min on an empty list")
    elif lis.est_vide(lis.suite(l)):
        return l
    else:
        return inserer(lis.valeur(l), trier(lis.suite(l)))
```

### 3ème partie : implémentation objet, version avec liste_vide objet

A partir du [code](./classe_liste.py) de `Liste` :

```python
def str_liste(l):
    if l.est_vide():
        return "[]"
    else:
        return "[{},{}]".format(l.valeur(), str_liste(l.suite()))

def taille(l):
    if l.est_vide():
        return 0
    else:
        return 1 + taille(l.suite())

def max_liste(l):
    if l.est_vide():
        raise Exception("No max on an empty list")
    elif l.suite().est_vide():
        return l.valeur()
    else:
        return max(l.valeur(), max_liste(l.suite()))

def min_liste(l):
    if l.est_vide():
        raise Exception("No min on an empty list")
    elif l.suite().est_vide():
        return l.valeur()
    else:
        return min(l.valeur(), min_liste(l.suite()))

def inserer(x, l):
    if l.est_vide():
        return Liste(x, Liste.liste_vide)
    elif x < l.valeur():
        return Liste(x, l)
    else:
        return Liste(l.valeur(), inserer(x, l.suite()))

def trier(l):
    if l.est_vide():
        raise Exception("No min on an empty list")
    elif l.suite().est_vide():
        return l
    else:
        return inserer(l.valeur(), trier(l.suite()))
```

### 4ème partie : implémentation objet, version avec ajout de méthodes

A partir du [code](./classe_liste.py) de `Liste` :

```python
def str_liste(self):
    if self.est_vide():
        return "[]"
    else:
        return "[{},{}]".format(self.valeur(), str_liste(self.suite()))
Liste.str_liste = str_liste

def taille(self):
    if self.est_vide():
        return 0
    else:
        return 1 + taille(self.suite())
Liste.taille = taille

def max_liste(self):
    if self.est_vide():
        raise Exception("No max on an empty list")
    elif self.suite().est_vide():
        return self.valeur()
    else:
        return max(self.valeur(), max_liste(self.suite()))
Liste.max_liste = max_liste

def min_liste(self):
    if self.est_vide():
        raise Exception("No min on an empty list")
    elif self.suite().est_vide():
        return self.valeur()
    else:
        return min(self.valeur(), min_liste(self.suite()))
Liste.min_liste = min_liste

def inserer(self, x):
    if self.est_vide():
        return Liste(x, Liste.liste_vide)
    elif x < self.valeur():
        return Liste(x, l)
    else:
        return Liste(self.valeur(), self.suite().inserer(x))
Liste.inserer = inserer

def trier(self):
    if self.est_vide():
        raise Exception("No min on an empty list")
    elif self.suite().est_vide():
        return self
    else:
        return trier(self.suite()).inserer(self.valeur())
Liste.trier = trier
```

Noter qu'ici on ajoute des méthodes à la classe `Liste` a
posteriori. On pourrait aussi bien écrire ces méthodes directement
dans la classe `Liste` si on le droit de la modifier.
