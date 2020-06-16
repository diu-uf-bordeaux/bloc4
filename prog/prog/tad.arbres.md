## Type abstrait ```Arbre Binaire```

1. Constructeurs : <!-- .element: class="fragment" data-fragment-index="0" -->

```python
 arbre_vide : () -> Arbre binaire
    # produit l'arbre vide
 noeud : (Etiquette * Arbre binaire * Arbre binaire) -> Arbre binaire
    # à partir d'un étiquette e et des arbres binaires g et d, 
    # produit l'arbre binaire (e, g, d)
```

<!-- .element: class="fragment" data-fragment-index="0" -->

2. Sélecteurs : <!-- .element: class="fragment" data-fragment-index="1" -->
  
```python
 etiquette : Arbre binaire -> Etiquette
    # à partir de l'arbre binaire (e, g, d), produit l'étiquette e
 gauche : Arbre binaire -> Arbre binaire
    # à partir de l'arbre binaire (e, g, d), produit l'arbre binaire g
 droit : Arbre binaire -> Arbre binaire
    # à partir de l'arbre binaire (e, g, d), produit l'arbre binaire d
```
<!-- .element: class="fragment" data-fragment-index="1" -->

3. Prédicat : <!-- .element: class="fragment" data-fragment-index="2" -->

```python
 est_vide : Arbre binaire -> bool
    # à partir de l'arbre binaire A, produit un booléen 
    # indiquant si A est l'arbre vide
```
<!-- .element: class="fragment" data-fragment-index="2" -->

--

## Mise en oeuvre en <span class="label">Python</span>

Plusieurs implémentations possibles :

1. **Listes de listes** <br/>&#x279E; paradigme fonctionnel

--

## Listes de listes
<!-- .slide: data-transition="fade" -->

1. Constructeurs : 
  ```python 
    def arbre_vide():
      return []

    def noeud(etiquette, gauche, droit):
      return [etiquette, gauche, droit]
  ```

2. Sélecteurs :

  ```python 
    def etiquette(arbre):
      return arbre[0]

    def gauche(arbre):
      return arbre[1]

    def droit(arbre):
      return arbre[2]
  ```

3. Prédicat :

  ```python 
    def est_vide(arbre):
      return arbre == arbre_vide()
  ```

--

## Listes de listes
<!-- .slide: data-transition="fade" -->

Exemple d'utilisation :

```python
 A1 = noeud('r', arbre_vide(), arbre_vide())
 print(A1) # ['r', [], []]
 print(est_vide(gauche(A1))) # True

 a = noeud('a', arbre_vide(), arbre_vide())
 b = noeud('b', arbre_vide(), arbre_vide())
 A2 = noeud('r', a, b)
 print(A2) # ['r', ['a', [], []], ['b', [], []]]
 print(etiquette(gauche(A2))) # a

 c = noeud('c', arbre_vide(), arbre_vide())
 b = noeud('b', c, arbre_vide())
 A3 = noeud('r', a, b)
 print(A3) # ['r', ['a', [], []], ['b', ['c', [], []], []]]
 print(etiquette(gauche(droit(A3)))) # c
```

--

## Mise en oeuvre en <span class="label">Python</span>

Plusieurs implémentations possibles :

1. **Listes de listes** <br/>&#x279E; paradigme fonctionnel

<br/>

2. **Classe Noeud** <br/>&#x279E; paradigme objet

--

## Classe Noeud
<!-- .slide: data-transition="fade" -->

1. Arbre vide représenté par `None`
2. Nœud représenté par la classe suivante :

  ```python
    class Noeud:
      arbre_vide = None

      def __init__(self, etiquette, gauche, droit):
          self._etiquette = etiquette
          self._gauche = gauche
          self._droit = droit
      
      def etiquette(self):
          return self._etiquette
      
      def gauche(self):
          return self._gauche

      def droit(self):
          return self._droit
      
      def est_vide(arbre):
          return arbre is Noeud.arbre_vide
  ```
<!-- .element: class="stretch" -->

--

## Classe Noeud
<!-- .slide: data-transition="fade" -->

Exemple d'utilisation :

```python
 A1 = Noeud('r', Noeud.arbre_vide, Noeud.arbre_vide)
 print(A1) # <__main__.Noeud object at 0x...>
 print(A1.etiquette()) # r
 print(Noeud.est_vide(A1.gauche())) # True

 a = Noeud('a', Noeud.arbre_vide, Noeud.arbre_vide)
 b = Noeud('b', Noeud.arbre_vide, Noeud.arbre_vide)
 A2 = Noeud('r', a, b)
 print(A2.gauche().etiquette()) # a
 print(Noeud.est_vide(a.gauche())) # True

 c = Noeud('c', Noeud.arbre_vide, Noeud.arbre_vide)
 b = Noeud('b', c, Noeud.arbre_vide)
 A3 = Noeud('r', a, b)
 print(A3.droit().gauche().etiquette()) # c
```

--

## Mise en oeuvre en <span class="label">Python</span>

Plusieurs implémentations possibles :

1. **Listes de listes** <br/>&#x279E; paradigme fonctionnel

<br/>

2. **Classe Noeud** <br/>&#x279E; paradigme objet

<br/>

3. **Liste unique** (méthode d'Eytzinger) <br/>&#x279E; paradigme impératif

--

## Liste unique (méthode d'Eytzinger)
<!-- .slide: data-transition="fade" -->

Liste dans laquelle les fils gauche et droit d'un nœud *i* sont rangés respectivement dans les cases 2*i*+1 et 2*i*+2.

![Eytzinger](prog/images/arbres/Eytzinger.svg)<!-- .element: class="stretch" style="max-width: 65%;" -->

Stockage mieux adapté aux **arbres complets**.
<!-- .element: class="fragment" data-fragment-index="0" -->

--

## Liste unique (méthode d'Eytzinger)
<!-- .slide: data-transition="fade" -->

Version simple où la profondeur de l'arbre est fixée *a priori*.

```python
 profondeur_max = 2

 def arbre_vide():
   return None

 arbre = [arbre_vide()] * (2**(profondeur_max+1)-1)

 def noeud(etiquette, i):
    arbre[i] = etiquette

 def etiquette(i):
    return arbre[i]

 def gauche(i): 
    return 2 * i + 1
 
 def droit(i): 
    return 2 * i + 2

 def est_vide(i):
    return arbre[i] == arbre_vide()
```
<!-- .element: class="stretch" -->

--

## Liste unique (méthode d'Eytzinger)
<!-- .slide: data-transition="fade" -->

Exemple d'utilisation :

```python
 noeud('r',0)
 print(arbre) # ['r', None, None, None, None, None, None]
 print(etiquette(0)) # r
 print(est_vide(gauche(0))) # True

 noeud('a', gauche(0))
 noeud('b', droit(0))
 print(arbre) # ['r', 'a', 'b', None, None, None, None]
 print(etiquette(gauche(0))) # a
 print(etiquette(droit(0))) # b

 noeud('c', gauche(droit(0)))
 print(arbre) # ['r', 'a', 'b', None, None, 'c', None]
 print(etiquette(gauche(droit(0)))) # c
```
