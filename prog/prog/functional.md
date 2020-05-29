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

<div class="half" style="width:47%; margin-top:10px">

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

<div class="half" style="width:52%; margin-top:10px">

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

- Chaque intermédiaire peut être considérée comme constant.


--

## Pureté : un exemple (2/2)

- Transformation de code impératif $\rightarrow$ fonctionnel

<div class="half" style="margin-top:10px">

Avec effet de bord <!-- .element: class="title" -->

```python
global_board = Board()  # global state

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
<!-- .element: class="title" style="font-size:22px; text-align:center" -->

![Arbre d'appel pour fibo(5)](prog/images/functional/fiboexpcall.svg)

</div>

- Nombre d'appels exponentiel $\Rightarrow$ débordements de pile.


--

- En pratique, il s'agit de faire attention en construisant `fibo`&nbsp;:

<div class="half" style="margin-top:20px">

```python
def fibo(n):
    def fib_rec(a, b, n):
		if n == 0:
			return a
		else:
			return fib_rec(b, a+b, n-1)
    return fib_rec(0, 1, n)
```

![Temps de calcul de fibo(n)](prog/images/functional/fibo_lin.png)
<!-- .element: class="stretch" style="max-width: 70%;margin-left: 15%;margin-top: -20px" -->

</div>

<div class="half" style="margin-top:20px">

Arbre des appels pour `fibo(5)`
<!-- .element: class="title" style="font-size:22px; text-align:center" -->

![Arbre d'appel pour fibo(5)](prog/images/functional/fibolincall.svg)
<!-- .element: style="max-width:60%; margin-left:20%" -->

</div>

- Nombre d'appels linéaire <span style="color:green">✔</span>
<!-- .element: style="margin-top:-20px" -->

- Pas de duplication des calculs <span style="color:green">✔</span>


--

## Intérêts de la pureté

- **Portabilité** de la fonction : indépendance du moment et de lieu
  de l'appel.

- Facilitation des tests : pas de nécessité de préparer un contexte
  particulier à chaque fois.

- Parallélisation possible du code : des appels indépendants peuvent
  être faits sur des machines différentes.

Il ne s'agit pas d'être dogmatique : on peut mélanger les styles purs
et impurs.  <!-- .element: class="title" style="margin-top:50px" -->

--

## Fonctions de 1ère classe
