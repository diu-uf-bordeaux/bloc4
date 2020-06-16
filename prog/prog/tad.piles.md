## Pile

- Les piles sont omniprésentes en informatique :
- Par exemple :
  - L'annulation de commande (CTRL-Z) est gérée par une pile.
  - Vérifier si une expression est bien parenthésée nécessite une pile.
  - Évaluer une expression arithmétique peut être fait avec une pile.

--

## Type abstrait `Pile`

1. Constructeurs :

```python
 pile_vide : () -> Pile
    # produit la pile vide
 pile : (Valeur * Pile) -> Pile
    # produit une pile à partir d'une valeur et d'une autre pile
```

2. Fonctions : <!-- .element: class="fragment" data-fragment-index="1" -->

```python
 push : (Valeur * Pile) -> Pile
    # ajoute une valeur dans la Pile
 pop : Pile -> (Valeur * Pile)
    # extrait la valeur du sommet de la pile
    # puis renvoi la Pile sans cette valeur
    # Attention: La Pile ne doit pas être vide
```

<!-- .element: class="fragment" data-fragment-index="1" -->

3. Prédicat : <!-- .element: class="fragment" data-fragment-index="2" -->

```python
 est_vide : Pile -> bool
    # indique si la Pile est vide
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
  def pile_vide():
    return []

  def pile(valeur, pile):
    return [valeur, pile]
```

2. Fonctions : <!-- .element: class="fragment" data-fragment-index="1" -->

```python 
  # Nous considérons que le sommet de la Pile est la première case
  def push(valeur, pile):
    return [valeur, pile]

  def pop(pile):
    return (pile[0], pile[1])
```

<!-- .element: class="fragment" data-fragment-index="1" -->

3. Prédicat : <!-- .element: class="fragment" data-fragment-index="2" -->

```python 
  def est_vide(pile):
    return pile == pile_vide()
```

<!-- .element: class="fragment" data-fragment-index="2" -->

--

## Récursive
<!-- .slide: data-transition="fade" -->

Exemple d'utilisation :

```python
  1. P1 = pile_vide()
  2. P1 = push(3, P1)
  3. print(P1) # [3, []]
  4.
  5. P1 = push(6, P1)
  6. print(P1) # [6, [3, []]]
  7.
  8. resultat = pop(push(9, P1))
  9. print(resultat) # (9, [6, [3, []]])
 10.
 11. # Nous pouvons inverser une pile en la dépilant dans une autre pile
 11. P2 = pile_vide()
 12. while not est_vide(P1):
 13.   (val, P1) = pop(P1)  # res[0] contient la valeur, res[1] contient la pile restante
 14.   P2 = push(val, P2)
 15. print(P2)  # [3, [6, []]]
```

--

## Mise en oeuvre en <span class="label">Python</span>

Plusieurs implémentations possibles :

1. **Récursive** <br/>&#x279E; paradigme fonctionnel

<br/>

2. **Classe Pile** <br/>&#x279E; paradigme objet

--

## Classe Pile
<!-- .slide: data-transition="fade" -->

La classe Pile est implémentée de la même façon que la classe `File` :

```python
  class Pile:
    pile_vide = None

    def __init__(self, valeur, pile):
        self._valeur = valeur
        self._suite = pile
    
    def push(self, valeur):
        return Pile(valeur, self)
    
    def pop(self):
        return (self._valeur, self._suite)
    
    def est_vide(pile):
        return pile is Pile.pile_vide
```

--

## Classe Pile
<!-- .slide: data-transition="fade" -->

Exemple d'utilisation :

```python
   1. P1 = Pile(3, Pile.pile_vide)
   2. print(P1.pop()) # (3, None)
   3.
   4. P2 = Pile(3, Pile.pile_vide)
   5. P2.push(6).push(9)
   6.
   7. P3 = Pile(P2.pop(), Pile.pile_vide)
   8. while not Pile.est_vide(P2):
   9.   (val, P2) = P2.pop()
   9.   P3.push(val)
  10. # P3: [3, 6, 9]
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

Pile stockée dans un tableau.

```python 
  def pile_vide():
    return []

  def pile(valeur, pile):
    return [valeur] + pile

  pile = pile_vide()

  def push(valeur, pile):
    return [valeur] + pile

  def pop(pile):
    return (pile[0], pile[1:])

  def est_vide(pile):
    return pile == pile_vide()
```

--

## Tableau
<!-- .slide: data-transition="fade" -->

Exemple d'utilisation :

```python
   1. pile = pile_vide()
   2. pile = push(3, pile)
   3. print(pop(pile)) # (3, [])
   4.
   5. pile = pile_vide()
   6. pile = push(3, pile)
   7. pile = push(6, pile)
   8. pile = push(9, pile)
   9. print(pile) # [9, 6, 3]
  10. rev = pile_vide()
  11.
  12. while not est_vide(pile):
  13.   (val, pile) = pop(pile)
  14.   rev = push(val, rev)
  15. print(rev) # [3, 6, 9]
```
