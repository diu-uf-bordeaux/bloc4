---
layout: page_ext
title: "Opérations - solutions"
permalink: /td/arbres/operations/solutions/
---

- [Retour aux exercices sur les arbres binaires](../../)

- [Retour à l'exercice](../)

### Solutions pour la mise en oeuvre avec des listes de listes :

```python
def est_feuille(arbre):
  return est_vide(gauche(arbre)) and est_vide(droit(arbre))

def compte_feuille (arbre):
  if est_vide(arbre):
    return 0
  if est_feuille(arbre):
    return 1 
  return compte_feuille(gauche(arbre)) + compte_feuille(droit(arbre))

def taille (arbre):
  if est_vide(arbre):
    return 0
  return 1 + taille(gauche(arbre)) + taille(droit(arbre)) 

def hauteur (arbre):
  if est_vide(arbre):
    return -1
  h1 = 1 + hauteur(gauche(arbre))
  h2 = 1 + hauteur(droit(arbre))
  return max(h1,h2)
```

### Solutions pour la mise en oeuvre avec la classe `Noeud` :

```python
def est_feuille(self):
  return Noeud.est_vide(self.gauche()) and Noeud.est_vide(self.droit())

def compte_feuille (self):
  if Noeud.est_vide(self):
    return 0
  if self.est_feuille():
    return 1 
  return self.gauche().compte_feuille() + self.droit().compte_feuille()

def taille (self):
  if Noeud.est_vide(self):
    return 0
  if self.est_feuille():
    return 1 
  return 1 + self.gauche().taille() + self.droit().taille()

def hauteur (self):
  if Noeud.est_vide(self):
    return -1
  if self.est_feuille():
    return 0
  h1 = 1 + self.gauche().hauteur()
  h2 = 1 + self.droit().hauteur()
  return max(h1,h2)
```