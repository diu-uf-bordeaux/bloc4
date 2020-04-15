### Introduction

![Tiobe'18](prog/images/tiobe2018.png) <!-- .element: class="stretch" style="max-width: 70%;" -->

Ceci n'est pas un cours de Python <!-- .element: class="strong" -->


--

## Paradigme de programmation

A **paradigm** is a global and general model for decomposing problems
and composing solutions. It is a way for designing mechanisms into
manageable and composable parts, and thinking about them.

Each paradigm is therefore assumed to be based on a few simple and
elementary kind of **building blocks**. Paradigms can be therefore
understood and analyzed from the properties of their composable parts,
which in turn allows to identify associated programming constructs,
techniques and ways of thinking. As a matter of fact, a paradigm also
shapes the way one gets to specific solutions.

--

|Paradigme       | Bloc de base           |
|----------------|------------------------|
|Impératif       | Instruction            |
|Fonctionnel     | Expression, Fonction   |
|Objet           | Objet, Message         |
|Modulaire       | Module                 |
|Logique         | Formule logique        |
|Parallèle       | Algorithmes parallèles |
|Événementiel    | Événement, Cible       |
|||

--

## Type abstrait de données

Un **type abstrait de données** (aussi appelé TAD) consiste en :

1. un **ensemble de valeurs** possibles (aussi appelé type)

2. un **ensemble d'opérations** agissant sur ces valeurs

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
	read  : (book * number) -> string
	      # à partir d'un livre ouvert et d'un numéro de page
		  # produit le texte sur une page
	```

	NB : la notation "&rarr;" ainsi que le verbe "produit" permettent de
    dénoter à la fois un paradigme impératif et fonctionnel, selon que
    l'on estime que l'on a un état avant / après ou un passage
    paramètre / retour

--

## Exemple de TAD : `sequence`  en <span class="label">Python</span>


1. L'ensemble des suites possibles : `list` (`[]`, `[1,2,3]`, `['a','b']` &hellip;), `tuple`, `range` &hellip;
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


--

## Qualités de génie logiciel

Abstraction

Modularité

&hellip;

--

## Paradigme impératif

Description

Notion d'état, de mémoire.

Historique ? (Fortran, Algol)

Exemple (genre exemple récurrent, ou sur un thème proche)

Exemple classique (genre en C)

--

## Paradigme modulaire

Transition avec l'impératif, les procédures, puis les modules.

Parler d'architecture quelque part.

--

## Paradigme fonctionnel

Description, propriétés

Programmation pure, effets de bords, mutabilité

Historique ? (Lisp, Scheme)

Exemple (genre exemple récurrent)

Exemple classique (pas trop effrayant, genre OCaml)

--

## Paradigme logique

Cf. logpy

--

## Parallèle, événementiel
