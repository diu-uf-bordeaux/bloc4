---
layout: page_ext
title: "Opérations sur les graphes"
permalink: /td/graphes/operations/
---

- [Retour aux exercices sur les graphes](../)

- [Accès aux solutions](./solutions/)

L'objectif de cet exercice est d'étendre le TAD `Graphe simple` avec de nouvelles opérations dont vous proposerez une implémentation pour les deux représentations vues en cours : les matrices d'adjacence ([code](./graphe_matrice.py)) et les listes de successeurs ([code](./graphe_listes.py)). Pour plus de simplicité, on considéra des graphes **non-orientés**.

Tout d'abord, on souhaite pouvoir calculer le degré d'un sommet du graphe :

```python
 degre : Graphe * Sommet -> int
  # à partir d'un graphe simple G et d'un sommet s, produit un entier indiquant le degré de s
```

À partir de cette opération, on veut ajouter le prédicat :

```python
 est_isole : Graphe * Sommet -> bool
  # à partir d'un graphe simple G et d'un sommet s, produit un booléen indiquant si s est isolé
```

On souhaite maintenant calculer le degré moyen des sommets du graphe :

```python
 degre_moyen : Graphe -> int
  # à partir d'un graphe simple G, produit un entier indiquant le degré moyen des sommets de G
```

Enfin, on veut ajouter le prédicat :

```python
 sont_voisins : Graphe * Sommet * Sommet -> bool
  # à partir d'un graphe simple G et de deux sommets s1 et s2, 
  # produit un booléen indiquant si s1 est voisin de s2
```
