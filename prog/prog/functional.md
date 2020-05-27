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

Un moyen de construire des expressions plus complexes

--

## Un if-then-else ?

```python
def abs(x):
	if (x > 0):
		return x
	else:
		return -x
```
<!-- .element: style="padding:20px; background-color: #3f3f3f" -->

![If-Then-Else](prog/images/functional/ifthenelse.svg)

--

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

- **Pureté**&nbsp;: le résultat de l'évaluation d'une fonction ne
  dépend que de la valeur de ses paramètres, et pas d'autre facteurs
  externes (comme par exemple le moment du calcul).

- **Fonctions de 1ère classe**&nbsp;: les fonctions sont les briques
  de base pour composer les expressions; elles peuvent apparaître en
  tant que paramètres, retours ou même données du calcul.

--

## Pureté (1/2)

- Revient à considérer les fonctions comme leurs homologues
  mathématiques : des **applications**.

<div class="half">

```python
i = 0

def f():
    global i
    i = i + 1
    return i

f() - f() # (1 - 2) ou (2 - 1) ?
```
</div>
<div class="half">

- En <span class="label">Python</span> : `-1`

- En <span class="label">C</span> : `1` ou `-1`

- En <span class="label">OCaml</span> : `1` ou `-1`

</div>

- Idée : rendre les calculs indépendants de toute influence externe

- Dans cet exemple, le résultat de l'appel à `f()` dépend du moment où
  on l'appelle.

Note:
- une application est telle qu'à un élément d'origine on associe un
unique élément d'arrivée.
- en C, la chose est plus facile à vérifier parce qu'il existe
plusieurs compilateurs. en OCaml, il y a deux compilateurs mais tous
les deux développés ensemble (bytecode et natif), et les versions
récentes ont unifié le comportement, mais il est l'opposé de Python.

--

## Pureté (2/2)

- Exemples d'influences externes&nbsp;:
	* les générateurs aléatoires,
	* les lectures/écritures de fichiers ou bases de données
	* les interrogations dans des capteurs &hellip;

- Parmi les facteurs entravant la pureté : la présence de **variables**.

  $\Rightarrow$ Idée : manipuler et transformer des objets constants

- Il n'est pas toujours simple d'écrire (uniquement) des fonctions
  pures.


--

Style récursif

Sans effets de bords, mutabilité

Exemple (genre exemple récurrent)

Exemple classique (pas trop effrayant, genre OCaml)
