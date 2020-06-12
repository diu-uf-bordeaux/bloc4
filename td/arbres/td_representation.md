---
layout: page_ext
title: "Représentation visuelle"
permalink: /td/arbres/representation/
---

- [Retour aux exercices sur les arbres binaires](../)

- [Accès aux solutions](./solutions/)

Dans cet exercice nous aimerions produire une représentation visuelle lors de l'affichage de l'arbre sur le terminal. 

Par exemple, l'arbre <img src="../images/racine.svg" width="50px"/> sera affiché par :

```python
r
-*
-*
```

où le symbole ```-``` indique la profondeur et ```*``` désigne l'arbre vide.

L'arbre <img src="../images/arbre.svg" width="125px"/> sera visualisé ainsi :

```python
r
-a
--*
--*
-b
--*
--*
```

et l'arbre <img src="../images/arbre2.svg" width="125px"/> ainsi :

```python
r
-a
--*
--*
-b
--c
---*
---*
--*
```

Écrire une fonction `represente` permettant cette représentation textuelle. Dans le cas de la classe `Noeud`, cette fonction sera une méthode statique. Vous réalisez ainsi une **parcours préfixe** de l'arbre.

_Remarque_ : le comportement de la fonction Python `print` en fin de ligne peut être modifié à l'aide du paramètre `end` (par défaut égal à `'\n'`).