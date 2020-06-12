---
layout: page_ext
title: "Opérations"
permalink: /td/arbres/operations/
---

- [Retour aux exercices sur les arbres binaires](../)

- [Accès aux solutions](./solutions/)

L'objectif de cet exercice est d'étendre le TAD `Arbre binaire` avec de nouvelles opérations dont vous proposerez une implémentation pour la mise en oeuvre à base de listes de listes ([code](./arbre_listes.py)) et avec la classe `Noeud` ([code](./arbre_classe.py)).

Pour commencer, on souhaite étendre le TAD avec le prédicat suivant :

```python
est_feuille : Arbre binaire -> bool
  # à partir d'un arbre binaire A, produit un booléen indiquant si A est une feuille
```

En utilisant ce prédicat, on veut ensuite ajouter l'opération suivante :

```python
compte_feuilles : Arbre binaire -> int
  # à partir d'un arbre binaire A, produit un entier indiquant le nombre de feuilles de A
```

Avec une simple modification, vous pourrez calculer la taille d'un arbre, c'est-à-dire son nombre de nœuds :

```python
taille : Arbre binaire -> int
  # à partir d'un arbre binaire A, produit un entier indiquant la taille de A
```

On souhaite enfin calculer la hauteur d'un arbre, c'est-à-dire sa profondeur maximale :

```python
hauteur : Arbre binaire -> int
  # à partir d'un arbre binaire A, produit un entier indiquant la hauteur de A
```