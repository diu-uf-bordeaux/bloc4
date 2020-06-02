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

- **Pureté**&nbsp;: le résultat de l'évaluation d'une fonction ne
  dépend que de la valeur de ses paramètres, et pas d'autre facteurs
  externes (comme par exemple le moment de l'appel).

- **Fonctions de 1ère classe**&nbsp;: les fonctions sont les briques
  de base pour composer les expressions; elles peuvent apparaître en
  tant que paramètres, retours ou même données d'un programme.


--

## Pureté (1/2)

- Revient à considérer les fonctions comme leurs homologues
  mathématiques : des **applications**.

- Dans l'exemple suivant, le résultat de l'appel à `f()` dépend du
  moment où on l'appelle&nbsp;:

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
  (moment de l'appel, disponibilité des ressources &hellip;)

Note:
- une application est telle qu'à un élément d'origine on associe un
unique élément d'arrivée.
- en C, la chose est plus facile à vérifier parce qu'il existe
plusieurs compilateurs. en OCaml, il y a deux compilateurs mais tous
les deux développés ensemble (bytecode et natif), et les versions
récentes ont unifié le comportement, mais il est l'opposé de Python.


--

## Pureté (2/2)

- Exemples d'influences externes ou **effets de bord**&nbsp;:
	* les générateurs aléatoires,
	* les lectures/écritures de fichiers ou bases de données
	* les mesure de capteurs électroniques &hellip;

- Parmi les facteurs entravant la pureté : la présence de
  **variables** ou de **boucles** (plus généralement la notion d'état).

  $\Rightarrow$ Idée : manipuler et transformer des objets **constants**

- Mais il n'est pas toujours simple d'écrire (uniquement) des
  fonctions pures, il faut parfois transiger.


--

## Pureté : un exemple (1/2)

- Transformation de code impératif $\rightarrow$ fonctionnel

<div class="half" style="width:46%; margin-top:10px">

Avec effet de bord <!-- .element: class="title" -->

```python
cpt = 0       # global state

def count_calls():
	global cpt
	cpt += 1
	print("calls={}".format(cpt))

count_calls() # calls=1
count_calls() # calls=2
```

</div>

<div class="half" style="width:53%; margin-top:10px">

Sans effet de bord <!-- .element: class="title" -->

```python
def count_calls(cpt):
	new_cpt = cpt + 1
	return new_cpt

cpt1 = 0
cpt2 = count_calls(cpt1)
print("calls={}".format(cpt2)) # calls=1
cpt3 = count_calls(cpt2)
print("calls={}".format(cpt3)) # calls=2
```

</div>

- Idée : transformer le `cpt` global en plusieurs intermédiaires.

- Chaque intermédiaire peut être considéré comme constant.


--

## Pureté : un exemple (2/2)

- Transformation de code impératif $\rightarrow$ fonctionnel

<div class="half" style="margin-top:10px">

Avec effet de bord <!-- .element: class="title" -->

```python
global_board = Board() # global state

def play(board, color):
	m = board.get_move(color)
	# Modify board 'in place'
	board.moves.append(m)

play(global_board, Color.WHITE)
play(global_board, Color.BLACK)
```

</div>

<div class="half" style="margin-top:10px">

Sans effet de bord <!-- .element: class="title" -->

```python
def play(board, color):
	m = board.get_move(color)
	# Return new independent board
	return Board(moves = \
                   board.moves + [m])

board1 = Board()
board2 = play(board1, Color.WHITE)
board3 = play(board2, Color.BLACK)
```

</div>

- La version sans effet de bord permet facilement de&nbsp;:

	* conserver les états intermédiaires, <!-- .element: style="margin-top:-15px" -->
	* jouer des coups et revenir en arrière,
	* envisager la construction de stratégies &hellip;


--

## Récursivité

- Comment réaliser des calculs complexes sans effets de bords&nbsp;?
  Solution classique&nbsp;: utiliser la récursivité.

- Une fonction est **récursive** si son code fait appel à elle-même.

<div class="half">

Version impérative <!-- .element: class="title" -->

```python
def fibo(n):
    fibPr, fib = 0, 1
    for num in range(1, n+1):
        fibPr, fib = fib, fib + fibPr
    return fibPr
```

</div>

<div class="half">

Version récursive <!-- .element: class="title" -->

```python
def fibo(n):
	if (n <= 1):
		return n
	else:
		return fibo(n-1) + fibo(n-2)
```

</div>

- La version récursive repose sur la définition mathématique&nbsp;:

$$
\begin{cases}
f_0 = 0 \\\\
f_1 = 1 \\\\
f_n = f_{n-1} + f_{n-2} \quad \textrm{si}~n \geq 2
\end{cases}
$$
<!-- .element: style="margin-top:-20px" -->


--

## Récursivité : débordements de pile
<!-- .element: style="display:none" -->

- Toute boucle est convertible en appel récursif et vice versa.

- Problème : les appels récursifs parfois trop nombreux

<div class="half">

```python
def fibo(n):
    if (n <= 1):
        return n
    else:
        return fibo(n-1) + fibo(n-2)
```

![Temps de calcul de fibo(n)](prog/images/functional/fibo_exp.png)
 <!-- .element: class="stretch" style="max-width: 70%;margin-top: -20px" -->


</div>

<div class="half">

Arbre des appels pour `fibo(5)`
<!-- .element: class="title" style="font-size:24px; text-align:center" -->

![Arbre d'appel pour fibo(5)](prog/images/functional/fiboexpcall.svg)

</div>

- Nombre d'appels exponentiel en `n` $\Rightarrow$ débordements de pile.


--

## Récursivité terminale
<!-- .element: style="display:none" -->

- En pratique, il s'agit de faire attention en construisant `fibo`&nbsp;:

<div class="half" style="width:51%; margin-top:20px">

```python
def fibo(n):
    def fib_rec(a, b, n):
		if n == 0:
			return a
		else:
			return fib_rec(b,a+b,n-1)
    return fib_rec(0, 1, n)
```

![Temps de calcul de fibo(n)](prog/images/functional/fibo_lin.png)
<!-- .element: class="stretch" style="max-width: 70%;margin-left: 15%;margin-top: -20px" -->

</div>

<div class="half" style="width:47%; margin-top:20px">

Arbre des appels pour `fibo(5)`
<!-- .element: class="title" style="font-size:24px; text-align:center" -->

![Arbre d'appel pour fibo(5)](prog/images/functional/fibolincall.svg)
<!-- .element: style="max-width:60%; margin-left:20%" -->

Version **récursive-terminale**
<!-- .element: class="title" style="font-size:24px; text-align:center; margin-top:-30px" -->

</div>

- Nombre d'appels linéaire en `n` <span style="color:green">✔</span>
<!-- .element: style="margin-top:-20px" -->

- Pas de duplication des calculs <span style="color:green">✔</span>
<!-- .element: style="margin-top:-20px" -->


--

## Intérêts de la pureté

- **Portabilité** de la fonction : indépendance du moment et de lieu
  de l'appel.

- Facilitation des **tests** : pas de nécessité de préparer un
  contexte particulier à chaque fois.

- **Parallélisation** possible du code : des appels indépendants
  peuvent être faits sur des machines différentes.

Il ne s'agit pas d'être dogmatique : on peut mélanger les styles purs
et impurs, si on prend soin des effets de bords.
<!-- .element: class="title" style="margin-top:50px" -->

--

## Fonctions de 1ère classe

- Considérer les fonctions comme des valeurs à part entière&nbsp;:

	* apparaissant dans des structures de données,

	* ou comme paramètres et retours d'autres fonctions.

- Une fonction est alors une petite **unité de code**, que l'on peut
  créer, transmettre et utiliser à la demande.

- Exemple fondamental : les **lambda-expressions**.

```python
lambda x: x+1         # <function <lambda> at 0x7>
```
<!-- .element: style="padding:20px; background-color: #3f3f3f" -->


--

## 1ère classe : création

- Construire des fonctions en <span class="label">Python</span>&nbsp;:

	* https://docs.python.org/3/reference/compound_stmts.html#function
	<!-- .element: style="font-size:large" -->

	* https://docs.python.org/3/reference/expressions.html#lambda
	<!-- .element: style="font-size:large" -->

<div class="half">

Version nommée
<!-- .element: class="title" -->

```python
def func(param1, param2):
	return param1 - param2

func         # <function func at 0x7>
func(34,23)  # 11
```

</div>

<div class="half">

Version anonyme
<!-- .element: class="title" -->

```python
lamb = lambda param1, param2: \
	        param1 - param2

lamb    # <function <lambda> at 0x7>
lamb(34,23)  # 11
```

</div>

- Caveat&nbsp;: le corps d'une lambda doit être une expression.

- Les fonctions peuvent alors&nbsp;:

	* être stockées dans des variables (comme `lamb`)
   <!-- .element: style="margin-top:-10px" -->

	* apparaître dans des structures : `[func, lamb]`
   <!-- .element: style="margin-top:-20px" -->


--

## 1ère classe : Paramètre

- Une fonction peut être paramétrée par une autre fonction.

- Exemple : un algorithme de tri paramétrée par un ordre de tri

<div class="half" style="width:51%">

```python
def sort(l, cmp): # generic Bubble Sort
  n, nl = len(l), list(l)
  for i in range(n):
    for j in range(n - i - 1):
      if cmp(nl[j], nl[j + 1]):
        nl[j], nl[j+1] = nl[j+1], nl[j]
  return nl
```

</div>

<div class="half" style="width:47%">

```python
sort(range(10), lambda x,y: x>y)
# -> [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]

sort(range(10), lambda x,y: x<y)
# -> [9, 8, 7, 6, 5, 4, 3, 2, 1, 0]
```

</div>

- Idée : déléguer une partie d'un algorithme à l'appelant.

  De telles fonctions sont dites **génériques**.
  <!-- .element: style="margin-top:-15px" -->

- Exemples&nbsp;: `filter`, `map`, `min`, `max`, `sorted` (via `key`)

--

## 1ère classe : Retour

- Une fonction peut renvoyer une autre fonction&nbsp;:

- Exemple : un algorithme de dérivation de fonction

<div class="half" style="width:51%">

```python
def derivate(f, h):
    return lambda x: \
		(f(x+h) - f(x)) / h
```

</div>

<div class="half" style="width:47%">

```python
c = derivate(np.sin, 0.01)
c(0)     # 0.9999833334166665
c(np.pi) # -0.9999833334166452
```

</div>

- Idée : créer un code paramétré applicable de manière différée

- Exemples :

	* spécialisation par application partielle (`partial`)

	 ```python
	 functools.partial(derivate, np.sin)
	 ```
	   <!-- .element: style="margin-top:-20px" -->

	* contrôle de l'évaluation / évaluation paresseuse

	 ```python
	 timeit.timeit(lambda: fibo(100))
	 ```
	   <!-- .element: style="margin-top:-20px" -->


--

## Intérêts de la 1ère classe

- Considérer les fonctions comme des valeurs ayant les mêmes
  possibilités d'utilisation que les entiers, les objets&hellip;

- Leur vocation : représenter des calculs paramétrés.

- Exemples d'application :

	* la représentation des données par les fonctions <br/>
	  (cf. `characteristic`)

	* la parallèlisation automatique des calculs <br/>
	  (cf. `mapreduce`)

	* le contrôle de l'évaluation et la paresse<br/>
	  (cf. `laziness`)
