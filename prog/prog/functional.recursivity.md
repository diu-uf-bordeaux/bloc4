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
