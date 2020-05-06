## Listes, piles et files

- Structures de données :
  - **linéaires**
  - **séquentielles**

<br />

- TADs **très proches** les uns des autres :
  - Structures **identiques**
  - Différents sur leur **fonctionnement**

<!-- .element: class="fragment" -->

<br />

- Largement utilisés dans les **algorithmes** :
  - Tri
  - Ordonnancement
  - Gestion mémoire (appels de fonctions)

<!-- .element: class="fragment" -->

--

## Exemple: file d'impression

![File d'impression](prog/images/listes/file.svg)<!-- .element: class="stretch" style="max-width: 80%;" -->

<br />

<!-- pictures credits at the end of piles, listes, files: Gregor Cresnar, Freepik, DinosoftLabs, Becris -->

Une imprimante ne pouvant pas imprimer plusieurs documents en même temps, les requêtes doivent être stockées et organisées avant d'être traitées.

--

## Exemple: CTRL-Z

![Undo Redo](prog/images/listes/undoRedo.svg)<!-- .element: class="stretch" style="max-width: 80%;" -->

Certaines implémentations d'annulation/rétablissement d'actions utilisent une structure sous forme de pile.

--

## Terminologie

--

## Définition récursive

- Une **liste** c'est:
  - soit une **liste vide**, notée ∆ ;
  - soit un **couple** (*e*, *L*), appelé cellule, avec :
    - *e* l'étiquette de la cellule (la valeur stockée)
    - *L* le reste de la liste

- <!-- .element: class="fragment" -->Définition <strong>récursive</strong> car une liste est définie par d'autres listes.
- <!-- .element: class="fragment" -->La première partie de la définition assure l’arrêt et donc la cohérence de la définition.

## Type abstrait ```Liste```

1. Constructeurs :

```python
 liste_vide : () -> Liste
    # produit la liste vide
 cellule : (Etiquette * Liste) -> Liste
    # à partir d'une étiquette e et d'une liste L,
    # produit la liste (e, L)
```

2. Sélecteurs : <!-- .element: class="fragment" data-fragment-index="1" -->

```python
 valeur : Liste -> Etiquette
    # à partir d'une liste (e, L), produit l'étiquette e
 suite : Liste -> Liste
    # à partir d'une liste (e, L), produit la liste L
```

<!-- .element: class="fragment" data-fragment-index="1" -->

3. Prédicat : <!-- .element: class="fragment" data-fragment-index="2" -->

```python
 est_vide : Liste -> bool
    # à partir d'une liste L, produit un booléen
    # indiquant si L est la liste vide
```

<!-- .element: class="fragment" data-fragment-index="2" -->
