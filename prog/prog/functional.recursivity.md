## Récursivité

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
		return 1
	else:
		return fibo(n-1) + fibo(n-2)
```

</div>

- La version récursive repose sur la définition mathématique&nbsp;:

$$
\begin{cases}
f_0 = 1 \\\\
f_1 = 1 \\\\
f_n = f_{n-1} + f_{n-2} \quad \textrm{si}~n \geq 2
\end{cases}
$$
<!-- .element: style="margin-top:-20px" -->


--

## Récursivité : cas d'application

- Quand écrire des fonctions récursives&nbsp;?

	* pour des calculs mettant en jeu des structures de données
      récursives (listes, arbres &hellip;)

	* pour des algorithmes du type "diviser pour régner"

- Toute boucle est convertible en appel récursif et vice versa.

<div class="half" style="width:44%">

```python
def fun_with_loop(n):
	res = 0
	for i in range(n):
		res += i
	return res
```

</div>

<div class="half" style="width:53%">

```python
def fun_with_rec(n):
    def f_rec(res, i):
        if (i < n):
            return f_rec(res+i, i+1)
        else:
            return res
    return f_rec(0, 0)
```

</div>


--

## Récursivité : débordements de pile

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

- En pratique, il s'agit de faire attention en construisant `fibo`&nbsp;:

<div class="half" style="width:51%">

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

<div class="half" style="width:47%">

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

## Une structure récursive : la liste

Les <a href="#/tad.listes">listes</a> sont un type de données
construit de manière **récursive**. Une liste peut prendre deux formes
différentes :

- soit elle est vide (appelée par la suite **liste vide**),

- soit elle est constituée d'une valeur initiale (la **tête**) et d'une
  autre liste (la **queue**).


![Liste](prog/images/functional/listes.png)<!-- .element: class="stretch" style="width: 44%;" -->


--

## Structure récursive, algos récursifs

- Lorsqu'un type de données est conçu de manière récursive, les
  algorithmes qui l'utilisent sont naturellement récursifs.

<div class="half">

```python
def cons(x, l):
    return { "hd": x, "tl": l }

def head(l): return l["hd"]
def tail(l): return l["tl"]

def empty(): return cons(None, None)
def is_empty(l):
	return (head(l) is None) and \
           (tail(l) is None)
```

</div>

<div class="half">

```python
def length(l):
    if is_empty(l):
        return 0
    else:
        return 1 + length(tail(l))
```

```python
l = cons(1, cons(2, cons(3, empty())))
length(l)       # -> 3
length(tail(l)) # -> 2
length(empty()) # -> 0
```

</div>

- Structure canonique :

```python
if is_empty(l):
    # Do something for the empty list
else:
    # Now l is not empty, do something with is head and tail
```
