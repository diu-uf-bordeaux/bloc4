---
layout: page_ext
title: "Programmation paresseuse"
---

- [Retour aux exercices de programmation fonctionnelle](./td_functional.md)

- [Accès aux solutions](./td_laziness.solutions.md)

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

### 2ème partie : les expressions congelées

Une manière très simple de contrôler la réalisation d'un calcul
consiste à l'encapsuler dans une fonction sans paramètre. Le calcul
sera effectué uniquement lorsque la fonction sera exécutée. Par
exemple, la fonction suivante transforme une valeur en une valeur
encapsulée à l'intérieur d'une fonction.

```python
def make_value(x):
    return lambda : x

f = make_value(666)
print(f)    # <function make_value.<locals>.<lambda> at 0x7fb1899b6e60>
print(f())  # 666
```

On dit que cette valeur est gelée (frozen en anglais). Bien sûr, cela
ne semble pas avoir beaucoup d'intérêt, si on ne fait que geler des
valeurs déjà calculées. L'intérêt devient plus grand lorsque l'on
commence à geler des calculs&nbsp;:

```python
def make_addition(a, b):
    return lambda : a() + b()

f = make_addition(make_value(42), make_value(58))
print(f)    # <function make_addition.<locals>.<lambda> at 0x7fb1899cf200>
print(f())  # 100
```

La finesse de ce que l'on obtient ainsi, c'est de pouvoir construire
des expressions arbitrairement complexes, sans jamais évaluer les
morceaux. Il devient alors envisageable de construire tout un calcul,
tout en repoussant le moment où le calcul est réellement effectué. En
pratique, toute fonction est une manière de congeler un calcul.

### 3ème partie : le contrôle de l'évaluation

Pour l'instant, les expressions congelées ne semblent pas
particulièrement utiles. Cette partie montre un exemple dans lequel le
contrôle de l'évaluation permet de décomposer un calcul en la somme de
ses étapes, que l'on peut ensuite faire avancer à la demande : une
forme primitive de débuggueur.

Considérons la fonction `pgcd` construite dans l'exercice [sur la
récursivité](/td/functional/td_recursivity.html)&nbsp;:

```python
def pgcd(a, b):
    if a == 0:
        return b
    elif a == b:
        return b
    elif a > b:
        return pgcd(b, a)
    else:
        return pgcd(b % a, a)
```

Cette fonction a le bon goût de faire une suite de calculs qui sont
tous des appels à elle-même. Considérons geler tous ces calculs, en la
transformrmant de la manière suivante&nbsp;:

```python
def pgcd_lazy(a, b):
    if a == 0:
        return lambda: b
    elif a == b:
        return lambda: b
    elif a > b:
        return lambda: pgcd_lazy(b, a)
    else:
        return lambda: pgcd_lazy(b % a, a)
```

Extraire de `pgcd_lazy(7, 5)` la valeur finale `1`. Comment faire
cela&nbsp;? Combien d'appels de fonctions sont-il nécessaires&nbsp;?

En ajoutant les `lambda`, on a bloqué le calcul à chaque étape, mais
le résultat ne donne pas beaucoup d'informations sur l'état
intermédiaire du calcul. Considérons la version suivante de la même
fonction&nbsp;:

```python
def pgcd_dbg(a, b):
    dic = {"a":a, "b":b }
    if a == 0:
        return lambda: (b, dic)
    elif a == b:
        return lambda: (b, dic)
    elif a > b:
        return lambda: (pgcd_dbg(b, a), dic)
    else:
        return lambda: (pgcd_dbg(b % a, a), dic)
```

Afficher les différentes étapes du calcul de `pgcd_dbg(7,5)`. De
quelles informations supplémentaires dispose-t'on ? En quoi cette
manière de faire permet-elle d'implémenter à peu de frais une sorte de
débuggueur&nbsp;?
