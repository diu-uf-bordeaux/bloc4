## Programmation modulaire

* Brique élémentaire : le **module**

* Idée générale :
  - le code est réparti dans des composants séparés,
  - ces modules sont reliés par des liens de dépendance,
  - chaque module peut être remplacé aisément.

* Qualités : les dépendances entre modules doivent être **faibles**, les
  dépendances à l'intérieur peuvent être **fortes**

* Représentant historique : CLU (1974)

* Exemple emblématique : **OCaml** (1996, v4.10 : 2020)

Note: la programmation modulaire n'est pas un paradigme, en tout cas
n'a jamais été présentée en tant que tel historiquement.

--

## Exemple de décomposition modulaire

* Partons du code calculant la suite de Fibonacci.

* Ce code peut être **étendu** de diverses manières :

  - en ajoutant le code d'autres suites connues&nbsp;:<br/>
	`catalan`, `rowland` &hellip;

  - en ajoutant des tests de validation pour chaque suite&nbsp;:<br/>
	`test_fibo`, `test_catalan` &hellip;

  - en ajoutant un afficheur générique de suites&nbsp;:<br/>
	`plot_a_sequence`, `plot_all_sequences` &hellip;

* Réfléchissons à une décomposition du code arrangeant ces ajouts
  selon leur nature.

--

## Exemple de décomposition modulaire
<!-- .element: style="display:none" -->

![Décomposition modulaire](prog/images/intro/modules.svg)<!-- .element: class="stretch" style="max-width: 80%;" -->


--

## Code modulaire : Python

<div class="half" style="width:46%">

sequences.py <!-- .element: class="title" -->
```
import math

def fibo(n: int) -> int:
    fibPr = 0
    fib = 1
    for num in range(1, n+1):
        fibPr, fib = fib, fib+fibPr
    return fibPr

def catalan(n: int) -> int:
    ...
def rowland(n: int) -> int:
    ...
```

</div>
<div class="half" style="width:52%">

sequences_test.py <!-- .element: class="title" -->
```
import unittest

def test_fibo() -> None: ...
def test_catalan() -> None: ...
def test_rowland() -> None: ...

```

sequences_plot.py <!-- .element: class="title" -->
```
import matplotlib

def plot_a_sequence(f: Callable[[int],
                                int],
                    n: int) -> None: ..

def plot_all_sequences() -> None: ...
```

</div>

<span style="font-size:large">Remarque : les indications de type sont
  optionnelles en <span class="label">Python</span> et disponibles
  uniquement depuis la version 3.5 </span>


--

## Code modulaire : OCaml

<div class="half" style="width:45%">

sequences.ml <!-- .element: class="title" -->
```ocaml
module type SEQUENCE = sig
    val fibo : int -> int
    val catalan : int -> int
	val rowland : int -> int
end

module S : SEQUENCE = struct
	let fibo(n) =
	  let fibP = ref (0,1) in
	  for i = 1 to n do
		let (u,v) = !fibP in
		fibP := (v, u+v)
	  done;
	  fst !fibPr
end
```

</div>
<div class="half" style="width:53%; padding-top:1%">

sequences_test.ml <!-- .element: class="title" -->
```ocaml
module type SEQUENCE_TEST = sig
    val test_fibo : unit -> bool
    val test_catalan : unit -> bool
    val test_rowland : unit -> bool
end
```

sequences_plot.ml <!-- .element: class="title" -->
```ocaml
module type SEQUENCE_PLOT = sig
	val plot_a_sequence : (int -> int)
	                    -> int -> unit
    val plot_all_seqs : unit -> unit
end
```

</div>

* Distinction est faite entre l'**interface** et l'**implémentation**.

Note: Les modules sont liés entre eux à la compilation en <span
class="label">OCaml</span>


--

## Quelques remarques ...

* Chaque module met ainsi à disposition une **interface**&nbsp;:

	- la liste des éléments à l'intérieur (fonctions, valeurs&hellip;),

	- le cas échéant une forme de spécification plus précise (types,
      documentation&hellip;).

* Et contient une **implémentation** de ces éléments&nbsp;:

	- le code de chacun des éléments dans le modules,

	- le cas échéant, des éléments internes servant à implémenter les
      autres.

--

## Alors, c'est quoi un module ?

* La forme que prennent les modules varie selon les langages&nbsp;:

	- en <span class="label">Python</span>, un module s'appelle bien un module,

	https://docs.python.org/fr/3/tutorial/modules.html
	 <!-- .element: class="small" -->

	- en <span class="label">C</span>, les modules n'existent pas
      concrètement, mais sont simulables avec des séparations par
      fichiers,

	- en <span class="label">Java</span>, plusieurs niveaux de modules
      coexistent, à travers les paquetages et les classes,

	- en <span class="label">JavaScript</span>, une technique
      (obsolète) consiste à encapsuler les modules à l'aide de
      fonctions.
