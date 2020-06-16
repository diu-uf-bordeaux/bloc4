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

<!-- pictures credits at the end of piles, listes, files: Gregor Cresnar, Freepik, DinosoftLabs, Becris -->

Une imprimante ne pouvant pas imprimer plusieurs documents en même temps, les requêtes doivent être stockées et organisées avant d'être traitées.

--

## Exemple: Historique des actions

![Undo Redo](prog/images/listes/history.jpg)<!-- .element: class="stretch" style="max-width: 80%;" -->

Certaines implémentations d'annulation/rétablissement d'actions utilisent une structure sous forme de pile.

--

## Liste: Terminologie

![Liste](prog/images/listes/liste_terminologie.svg)<!-- .element: class="stretch" style="width: 50%;" -->

- Une **liste** est caractérisée par un ensemble de **cellules**
- Chaque **cellule** contient une valeur et un **lien** vers la cellule suivante
- Une **liste** peut être vide

--

## Définition récursive

- Une **liste** c'est :
  - soit une **liste vide**, notée ∆ ;
  - soit un **couple** (*e*, *L*), appelé cellule, avec :
    - *e* l'étiquette de la cellule (la valeur stockée)
    - *L* le reste de la liste

- <!-- .element: class="fragment" -->Définition <strong>récursive</strong>&nbsp;: une liste est construite à partir d'un élément et d'une sous-liste.

- <!-- .element: class="fragment" -->La première partie de la définition assure l’arrêt et donc la cohérence de la définition.

--

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

--

## Mise en oeuvre en <span class="label">Python</span>

Plusieurs implémentations possibles :

1. **Récursive** <br/>&#x279E; paradigme fonctionnel

--

## Récursive

1. Constructeurs :

```python 
  def liste_vide():
    return []

  def cellule(etiquette, liste):
    return [etiquette, liste]
```

2. Sélecteurs : <!-- .element: class="fragment" data-fragment-index="1" -->

```python 
  def valeur(liste):
    return liste[0]

  def suite(liste):
    return liste[1]
```

<!-- .element: class="fragment" data-fragment-index="1" -->

3. Prédicat : <!-- .element: class="fragment" data-fragment-index="2" -->

```python 
  def est_vide(liste):
    return liste == liste_vide()
```

<!-- .element: class="fragment" data-fragment-index="2" -->

--

## Récursive
<!-- .slide: data-transition="fade" -->

Exemple d'utilisation :

```python
 1. L1 = cellule(3, liste_vide())
 2. print(L1) # [3, []]
 3. print(est_vide(suite(L1))) # True
 4. 
 5. L2 = cellule(3, cellule(6, cellule(9, liste_vide())))
 6. print(L2) # [3, [6, [9, []]]]
 7. print(valeur(suite(suite(L2)))) # 9
```

--

## Mise en oeuvre en <span class="label">Python</span>

Plusieurs implémentations possibles :

1. **Récursive** <br/>&#x279E; paradigme fonctionnel

<br/>

2. **Classe Cellule** <br/>&#x279E; paradigme objet

--

## Classe Cellule
<!-- .slide: data-transition="fade" -->

1. Liste vide représenté par `None`
2. Liste représentée par la classe suivante :

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
<!-- .element: class="stretch" -->

--

## Classe Cellule
<!-- .slide: data-transition="fade" -->

Exemple d'utilisation :

```python
  1. L1 = Cellule(3, Cellule.liste_vide)
  2. print(L1) # <__main__.Cellule object at 0x...>
  3. print(L1.valeur()) # 3
  4. print(Cellule.est_vide(L1)) # False
  5. 
  6. c1 = Cellule(9, Cellule.liste_vide)
  7. c2 = Cellule(6, c1)
  8. L2 = Cellule(3, c2)
  9. print(L2.suite().valeur()) # 6
 10. print(Cellule.est_vide(L2.suite().suite().suite())) # True
```

--

## Mise en oeuvre en <span class="label">Python</span>

Plusieurs implémentations possibles :

1. **Récursive** <br/>&#x279E; paradigme fonctionnel

<br/>

2. **Classe Cellule** <br/>&#x279E; paradigme objet

<br/>

3. **Tableau** <br/>&#x279E; paradigme impératif

--

## Tableau
<!-- .slide: data-transition="fade" -->

Liste stockée dans un tableau de taille fixe. Les opérations se font sur des cellules et non plus sur la liste entière :

```python 
  taille_max = 8

  def liste_vide():
    return None

  liste = [liste_vide()] * taille_max

  def cellule(etiquette, numero_cellule):
    liste[numero_cellule] = etiquette

  def valeur(numero_cellule):
    return liste[numero_cellule]

  def suite(numero_cellule):
    return liste[numero_cellule:]

  def est_vide(numero_cellule):
    return liste[numero_cellule] == liste_vide()
```

--

## Tableau
<!-- .slide: data-transition="fade" -->

Exemple d'utilisation :

```python
  1. cellule(3, 0)
  2. 
  3. print(liste) # [3, None, None, None, None, None, None, None]
  4. 
  5. cellule(6, 1)
  6. cellule(9, 2)
  7. 
  8. print(liste) # [3, 6, 9, None, None, None, None, None]
  9. print(valeur(1)) # 6
 10. print(est_vide(4)) # True
```
