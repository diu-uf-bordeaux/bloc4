## Fonctions de 1ère classe

- Les fonctions sont les briques de base pour composer les
  expressions. Elles peuvent apparaître&nbsp;:

	* dans des structures de données,

	* ou comme paramètres et retours d'autres fonctions.

- Une fonction est alors une petite **unité de code**, que l'on peut
  créer, transmettre et utiliser à la demande.

- Exemple fondamental : les **lambda-expressions**.

```python
lambda x: x+1         # <function <lambda> at 0x7>
```
<!-- .element: style="padding:20px; background-color: #3f3f3f" -->

  en tant qu'exemple de fonction **anonyme**.

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
<!-- .element: style="width:100%" -->

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
<!-- .element: style="width:100%" -->

</div>

- Caveat <span class="label">Python</span>&nbsp;: le corps d'une
  lambda doit être une expression.

- Les fonctions peuvent alors&nbsp;:

	* être stockées dans des variables (comme `lamb`)
   <!-- .element: style="margin-top:-10px" -->

	* apparaître dans des structures : `[func, lamb]`
   <!-- .element: style="margin-top:-20px" -->


--

## 1ère classe : Paramètre

- Une fonction peut être **paramétrée** par une autre fonction.

- Exemple : un algorithme de tri paramétré par un ordre de tri

<div class="half" style="width:51%">

```python
def sort(l, cmp): # Generic Bubble Sort
  n, nl = len(l), list(l)
  for i in range(n):
    for j in range(n - i - 1):
      if cmp(nl[j], nl[j + 1]):
        nl[j], nl[j+1] = nl[j+1], nl[j]
  return nl
```
<!-- .element: style="width:100%" -->

</div>

<div class="half" style="width:47%">

```python
sort(range(10), lambda x,y: x>y)
# -> [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]

sort(range(10), lambda x,y: x<y)
# -> [9, 8, 7, 6, 5, 4, 3, 2, 1, 0]
```
<!-- .element: style="width:100%" -->

</div>

- Idée : déléguer une partie d'un algorithme à l'appelant.

  De telles fonctions sont dites **génériques**.
  <!-- .element: style="margin-top:-15px" -->

- Exemples&nbsp;: `filter`, `map`, `min`, `max`, `sorted` (via `key`)

--

## 1ère classe : Retour

- Une fonction peut **renvoyer** une autre fonction&nbsp;:

- Exemple : un algorithme de dérivation de fonction

<div class="half" style="width:51%">

```python
def derivate(h, f):
    return lambda x: \
		(f(x+h) - f(x)) / h
```
<!-- .element: style="width:100%" -->

</div>

<div class="half" style="width:47%">

```python
c = derivate(0.01, np.sin)
c(0)     # 0.9999833334166665
c(np.pi) # -0.9999833334166452
```
<!-- .element: style="width:100%" -->

</div>

- Idée : créer un code paramétré applicable de manière différée

- Exemples :

	* spécialisation par application partielle (`partial`)

	 ```python
	 functools.partial(derivate, 0.01)   # derivation operator
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
	  (cf. [characteristic](../td/functional/td_characteristic.html)),

	* la parallèlisation automatique des calculs <br/>
	  (cf. [mapreduce](../td/functional/td_mapreduce.html)),

	* le contrôle de l'évaluation et la paresse<br/>
	  (cf. [laziness](../td/functional/td_laziness.html)).
