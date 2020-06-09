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
	sin(2*pi*x) + cos(2*pi*y)
```
<!-- .element: style="padding:20px; background-color: #3f3f3f" -->

![Fonction](prog/images/functional/function.svg)

Un moyen de construire des expressions plus complexes.


--

## Un if-then-else ?

<div class="half">

```python
def abs(x):
	if (x > 0):
		return x
	else:
		return -x
```
<!-- .element: style="padding:20px; background-color: #3f3f3f" -->

</div>

<div class="half">

```python
def abs(x):
	return (                     \
		x if (x > 0) else -x     \
	)
```
<!-- .element: style="padding:25px 20px 25px 20px; background-color: #3f3f3f" -->

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
<!-- .element: style="padding:20px; background-color: #3f3f3f" -->

![Fibonacci](prog/images/functional/fibonacci.svg)


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
