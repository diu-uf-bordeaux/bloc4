---
layout: page_ext
title: "Programmation paresseuse"
---

[Retour aux exercices de programmation fonctionnelle](./td_functional.md)

Cette page donne des exemples de contrôle de l'évaluation sous la
forme d'une technique de programmation faisant appel à de
l'[évaluation
paresseuse](https://en.wikipedia.org/wiki/Lazy_evaluation). Cette
technique permet en particulier de restreindre les calculs pour ne
réaliser **que** ceux qui sont nécessaires à la complétion d'un
programme.

### 1ère partie : les itérateurs Python

Un premier exemple de contrôle de l'évaluation apparaît dans des
objets que l'on manipule très vite en Python lorsque l'on manipule des
listes. Considérons pour commencer la fonction suivante très simple
qui fait un affichage et un calcul&nbsp;:

```python
def f(x):
	print("Using {}".format(x))
	return x+1
```

L'intérêt de cette fonction, c'est d'afficher un message au moment de
son exécution. Ainsi, il est possible d'appliquer cette fonction à
plusieurs valeurs de la manière suivante&nbsp;:

```
>> [f(x) for x in range(3)]
Using 0
Using 1
Using 2
[1, 2, 3]
```

Très naturellement, le calcul de la liste d'arrivée entraîne
l'application de la fonction `f` sur les valeurs de la liste. Les
affichages sont réalisés pendant les calculs, et la liste obtenue est
renvoyée à la fin.

Maintenant, réalisons le même calcul à l'aide de la fonction
`map`. Cette fonction ne renvoie pas une liste, mais un
itérateur&nbsp;:


```python
>> it = map(f, range(3))      # returns <map object at 0x7fd20e91aed0>
>> it.__next__()              # prints "Using 0", returns 1
>> it.__next__()              # prints "Using 1", returns 2
>> it.__next__()              # prints "Using 2", returns 3
>> it.__next__()              # raises an error : StopIteration
```

L'application de la méthode `__next__` entraîne à chaque fois une
application de la fonction `f`. L'itérateur (dans ce cas le `<map
object>`) permet de produire pas à pas les éléments dans la liste
finale.  Il s'agit d'un exemple de contrôle de l'évaluation : les
calculs sur la liste sont effectués à la demande,

Construire un itérateur avec la fonction `filter`, et extraire les
éléments de la liste un par un.

<span class="label">Difficile</span>. Une fois que l'on a compris
qu'on pouvait extraire les éléments d'une liste en les demandant un
par un, rien n'empêche plus de construire des listes infinies (au sens
où : desquelles on peut extraire autant d'éléments qu'on veut). Dans
l'exemple suivant, estimer combien d'entiers on peut tirer de cet
itérateur&nbsp;:

```python
def make_f():           # creates a 0-parameter function that
    x = [0]             # returns a new integer each time it is called
    def f():
        x[0] = x[0]+1
        return x[0]
    return f

it = iter(make_f(), -1) # -1 acts as a sentinel indicating the end of the list
for x in it: print(x)
```

Ces exemples peuvent paraître un peu futiles, mais correspondent en
fait à des fonctions apparaissant dans le module `itertools`
(cf. [documentation](https://docs.python.org/3/library/itertools.html)).

### 2ème partie : le contrôle de l'évaluation

Une manière très simple de contrôler la réalisation d'un calcul
consiste à l'encapsuler dans une fonction sans paramètre. Le calcul
sera effectué uniquement lorsque la fonction sera exécutée.
