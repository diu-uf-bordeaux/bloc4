---
layout: page_ext
title: "Représentation visuelle - solutions"
permalink: /td/arbres/representation/solutions/
---

[Retour à l'exercice](../)

### Solution pour la mise en oeuvre avec des listes de listes :

```python
def represente(arbre, p = 0) :
  if est_vide(arbre): 
    print('*')
  else:
    print(etiquette(arbre))
    p += 1
    print('-' * p, end ='')
    represente(gauche(arbre), p)
    print('-' * p, end ='')
    represente(droit(arbre), p)
```

### Solution pour la mise en oeuvre avec la classe Noeud :

```python
def represente (arbre, p=0):
  if Noeud.est_vide(arbre):
    print('*')
  else :
      print(arbre.etiquette())
      p += 1
      print('-' * p, end ='')
      Noeud.represente(arbre.gauche(), p)
      print('-' * p, end ='')
      Noeud.represente(arbre.droit(), p)
```