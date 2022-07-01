## Le paradigme fonctionnel

* Brique élémentaire : l'**expression**

* Idée générale :
  - partir d'un ensemble de valeurs (nombres, listes &hellip;)
  - utiliser un ensemble de moyens de les composer en expressions complexes (opérateurs, fonctions &hellip;)

* Exemple simpliste : `sin(2*pi*x) + cos(2*pi*y)`

* Représentants historiques : Lisp (1958), Scheme (1975)

* Exemple emblématique : **Haskell** (1990, dernière norme: 2010)


--

## Qu'est-ce qu'une expression ?

<code class="hljs python">sin(<span class="hljs-number">2</span><span>*</span>pi<span>*</span>x) + cos(<span class="hljs-number">2</span><span>*</span>pi<span>*</span>y)</code>
<!-- .element: style="background-color:black" -->

![Expression](prog/images/functional/expression.svg)

- L'expression est la représentation arborescente d'un calcul.

- **Évaluer** une expression permet d'obtenir le résultat du calcul.


--

## Qu'est-ce qu'une fonction alors ?

```python
def f(x,y):
	return sin(2*pi*x) + cos(2*pi*y)
```
<!-- .element: style="padding:10px; background-color: #3f3f3f; font-size: 24px" -->

![Fonction](prog/images/functional/function.svg)

Un moyen de construire des expressions plus complexes.


--

## Un if-then-else ?

<div class="half" style="width:47%">

```python
def abs(x):
	if (x > 0):
		return x
	else:
		return -x
```
<!-- .element: style="padding:10px; background-color: #3f3f3f; font-size: 24px" -->

</div>

<div class="half" style="width:51%">

```python
def abs(x):
	return (                  \
		x if (x > 0) else -x  \
	)
```
<!-- .element: style="padding:10px; background-color: #3f3f3f; font-size: 24px" -->

</div>

![If-Then-Else](prog/images/functional/ifthenelse.svg)

--

## Un exemple plus compliqué
<!-- .element: style="display:none" -->

```python
def fibo(n):
    fibPr, fib = 0, 1
    for num in range(1, n):
        fibPr, fib = fib, fib + fibPr
    return fib
```
<!-- .element: style="padding:10px; background-color: #3f3f3f; font-size: 24px" -->

![Fibonacci](prog/images/functional/fibonacci.svg)

--

## De l'importance des fonctions

- Les fonctions se **composent** pour produire des résultats :

```python
# Mathematical functions
p = { 'x': 0, 'y': 1 };
q = { 'x': 1, 'y': 0 }
math.sqrt((p['x'] - q['x'])**2 + (p['y']-q['y'])**2)

# Functions on lists
data = [1, 2, 3, 4]
list(filter(lambda x: x%2==0, map(lambda x: x*x, data)))
```

- Les fonctions structurent le code en blocs **paramétrables**
  et **réutilisables**.

--

## Fonctions et portées (1/2)

<div class="half">

Générateur aléatoire de Lehmer <!-- .element: class="title" -->

```python
seed = 12345
M = 65537
A = 75

def rand():
	global seed
	seed = (A * seed) % M
	return seed
```
<!-- .element: style="width: 100%" -->

</div>

<div class="half" style="vertical-align: bottom">

```python
for i in range(6):
	print(rand())

# -> [ 8357, 36942, 18096,
# ___ 46460, 11039, 41481 ]
```

&nbsp;

</div>

- La fonction `rand` utilise une variable `seed` qui lui est
  extérieure (mot-clé `global`).

- Cette variable a une **portée globale** au code : il est possible de
  la lire et la modifier en tout point après sa définition.

- Cela pose évidemment des problèmes de sécurité.

--

## Fonctions et portées (2/2)

<div class="half">

```python
def make_rand():
    iseed = 12345
    iM = 65537
    iA = 75
    def irand():
        nonlocal iseed
        iseed = (iA * iseed) % iM
        return iseed
    return irand
```
<!-- .element: style="width: 100%" -->

</div>

<div class="half">

```python
new_rand = make_rand()
for i in range(6):
    print(new_rand())

# -> [ 8357, 36942, 18096,
#     46460, 11039, 41481 ]
```

</div>

- Ici, on enferme le code dans une fonction `make_rand`, qui renvoie
  une fonction `irand` définie à l'intérieur.

- La variable `iseed` a une **portée locale** à la fonction
  `make_rand` et est inaccessible de l'extérieur.

- La fonction `irand` enferme dans son code le lien vers `iseed` et y
  accède en dehors de `make_rand` : c'est une **fermeture**.

--

## Propriétés

La programmation fonctionnelle s'appuie sur deux principes&nbsp;:

- <a href="#/functional.purity">**Pureté**</a>&nbsp;: le résultat de
  l'évaluation d'une fonction ne dépend que de la valeur de ses
  paramètres, pas de facteurs externes;

- <a href="#/functional.firstclass">**Fonctions de 1ère
  classe**</a>&nbsp;: les fonctions sont les briques de base pour
  composer les expressions; elles peuvent apparaître comme
  paramètres, retours ou données d'un programme.
