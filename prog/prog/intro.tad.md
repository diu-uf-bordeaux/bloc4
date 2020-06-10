## Type abstrait de données
<!-- .element: style="margin-bottom: 5%;" -->

- Un **type abstrait de données** (aussi appelé TAD) consiste en :

	1. un **ensemble de valeurs** possibles (aussi appelé type)

	2. un **ensemble d'opérations** agissant sur ces valeurs

- Il s'agit d'un exemple classique de composant modulaire.

--

## Exemple de TAD : le livre

1. L'ensemble des livres possibles : encyclopédie, bande dessinée,
   journal, prospectus &hellip;

2. Un ensemble d'opérations pour manipuler les livres :

	```python
	open  : book -> book
		  # à partir d'un livre, produit un livre ouvert
	close : book -> book
		  # à partir d'un livre, produit un livre fermé
    pages : book -> [number]
	      # à partir d'un livre, produit la liste de ses pages
	read  : (book * number) -> string
	      # à partir d'un livre ouvert et d'un numéro de page
		  # produit le texte sur une page
	```

- <!-- .element: style="list-style-type:'⇒ '" -->
Abstraction &nbsp;: les fonctions `open`, `close` &hellip;
permettent de manier n'importe quel livre, sans connaître ses
particularités.

- <!-- .element: style="list-style-type:'⇒ '" -->
Modularité&nbsp;: l'implémentation du livre et son utilisation sont
clairement séparées.


<!-- NB : la notation "&rarr;" ainsi que le verbe "produit" permettent de -->
<!-- dénoter à la fois un paradigme impératif et fonctionnel, selon que -->
<!-- l'on estime que l'on a un état avant / après ou un passage -->
<!-- paramètre / retour -->

--

## Exemple de TAD : `sequence`  en <span class="label">Python</span>


1. L'ensemble des suites possibles : <br/>
   `list` (`[]`, `[1,2,3]`, `['a','b']` &hellip;), `tuple`, `range` &hellip;
2. Un ensemble d'opérations pour manipuler les suites :

	```python
	__contains__ : (list * any) -> bool
               # à partir d'une liste `l` et d'une valeur `x`,
		       # produit un booléen disant si `x` est dans `l`
			   # Notation : `x in l`
    __add__      : (list * list) -> list
		       # à partir de deux listes `l1` et `l2`,
		       # produit une liste contenant les valeurs de `l1`
		       # suivies des valeurs de `l2`
			   # Notation : `l1 + l2`
    __getitem__  : (list * int) -> any
	           # à partir d'une liste `l` et d'un indice `i`,
		       # produit le ième élément de `l`
			   # Notation : `l[i]`
	```

	Cf. https://docs.python.org/3/library/stdtypes.html#sequence-types-list-tuple-range
	<!-- .element: class="x-small" -->

--

## À suivre &hellip;

Les parties suivantes de ce cours explorent plus précisément&nbsp;:

- Deux paradigmes&nbsp;:

	* le paradigme <a href="#/object">objet</a>,

	* et le paradigme <a href="#/functional">fonctionnel</a>.

- Plusieurs types abstraits de données&nbsp;:

	* les <a href="#/sequence">séquences</a> (listes, piles, files),

	* les <a href="#/tree">arbres</a>,

	* les <a href="#/graph">graphes</a>.
