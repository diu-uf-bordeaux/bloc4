---
layout: page_ext
title: "Expressions arithmétiques - solutions"
permalink: /td/arbres/expression/solutions/
---

- [Retour aux exercices sur les arbres binaires](../../)

- [Retour à l'exercice](../)

### Question 1

```python
def affiche(expression):
  if est_feuille(expression):
    print(etiquette(expression), end ='')
  else:
    print('(', end ='')
    affiche(gauche(expression))
    print(etiquette(expression), end ='')
    affiche(droit(expression))
    print(')', end ='')
```

### Question 2

```python
def evalue(expression, valeurs):
    if est_vide(expression): 
        return 0
    if est_feuille(expression):
        v = etiquette(expression)
        if v in valeurs:
          return valeurs[v]
        return v
    a=evalue(gauche(expression), valeurs)
    b=evalue(droit(expression), valeurs)
    o=etiquette(expression)
    if o=='+':
        return a+b
    if o=='*':
        return a*b
    if o=='-':
        return a-b
    if o=='/':
        return a/b
```

### Question 3

```python
def affichePolonaise(expression):
  if est_feuille(expression):
    print(etiquette(expression), end =' ')
  else:
    affichePolonaise(gauche(expression))
    affichePolonaise(droit(expression))
    print(etiquette(expression), end =' ')
```