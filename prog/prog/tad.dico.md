## Cas particulier: les dictionnaires

- Ces structures contiennent des données comme les listes mais ces dernières sont stockées et accessibles grâce à des **clés**.

- Par exemple, les dictionnaires dans python ressemblent à ça:
```python
  dico = {
    'A': 2,
    'C': 5
  }

  print(dico['A']) # 2

  dico['F'] = 47 # Stocke 47 dans le dictionnaire avec la clé 'F'
```

--

## Type abstrait ```Dictionnaire```

1. Constructeurs :

```python
 dictionnaire : () -> Dictionnaire
    # produit le dictionnaire vide
```

2. Fonctions : <!-- .element: class="fragment" data-fragment-index="1" -->

```python
 insérer : (Valeur * Valeur * Dictionnaire) -> Dictionnaire
    # Première valeur: Clé
    # Deuxième valeur: valeur à insérer
    # Insère la valeur à l'emplacement correspondant à la clé

 supprimer : (Valeur * Dictionnaire) -> Dictionnaire
    # Supprime la valeur correspondant à la clé
```

<!-- .element: class="fragment" data-fragment-index="1" -->

2. Sélecteurs : <!-- .element: class="fragment" data-fragment-index="2" -->

```python
 valeur : (Valeur * Dictionnaire) -> Valeur
    # Renvoie la valeur correspondant à la clé correspondante
```

<!-- .element: class="fragment" data-fragment-index="2" -->

3. Prédicat : <!-- .element: class="fragment" data-fragment-index="3" -->

```python
 existe : (Valeur * Dictionnaire) -> bool
    # Renvoie un booléen exprimant si une valeur est stockée avec la clé fournie en paramètre
```

<!-- .element: class="fragment" data-fragment-index="3" -->
