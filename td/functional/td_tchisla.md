---
layout: page_ext
title: "Tchisla"
---

- [Retour aux exercices de programmation fonctionnelle](./td_functional.md)

- [Accès aux solutions](./td_tchisla.solutions.md)

Le jeu de Tchisla, présenté dans le
[cours](https://dept-info.labri.fr/~gavoille/UE-TAP/cours.pdf) de
C. Gavoille, est un jeu dont le but consiste à "trouver une expression
arithmétique égale à un entier $n > 0$ mais utilisant uniquement un
chiffre $c \in \\{1, . . . , 9\\}$ donné". L’expression ne peut
comporter qu'un nombre limité de symboles. Il s'agit d'une variante du
jeu de chiffres "Le compte est bon" apparaissant dans l'émission ["Des
chiffres et des
lettres"](https://fr.wikipedia.org/wiki/Des_chiffres_et_des_lettres). Cet
exercice propose de construire une technique de résolution.

### 1ère partie : les expressions

Les expressions mathématiques considérées sont composées :

- de nombres ($c$, $cc$, $ccc$ $\dots$),

- d'opérations unaires ($\sqrt{}$, $!$ $\dots$),

- d'opérations binaires ($+$, $-$, $\times$, $/$, $\mathrm{pow}$ $\dots$).

Les points de suspension sont intentionnels, puisque le problème peut
être vu comme paramétré par les composants possibles. On pourrait par
exemple ne rechercher que les expressions qui constituent des sommes,
ou ajouter de nouvelles opérations mathématiques comme le modulo.

Le point important à remarquer ici : toutes ces expressions sont des
arbres, et leur composants sont des feuilles (nombres), des noeuds
internes à 1 fils (opérations unaires) et des noeuds internes à
deux fils (opérations binaires).

Écrire une classe `Expr` et trois classes qui en héritent :

- `Value` pour les expressions qui sont directement des nombres,

- `UnaryOp` pour les expressions dont la racine est une opération
  unaire,

- `BinaryOp` pour les expressions dont la racine est une opérations
  binaire.

Chacune de ces classes doit avoir une méthode `eval` qui permet de
récupérer la valeur de l'expression. Pour aider, on fournit le code
suivant à compléter (typiquement, les endroits avec `pass`). La classe
`Value` est déjà terminée. Lorsqu'un constructeur prend en paramètre
un argument `op_name`, il s'agit de fournir une chaîne de caractères
pour afficher l'expression.

```python
class Expr:
    def eval(self):
        raise Exception("Cannot evaluate abstract expression")

class Value(Expr):
    def __init__(self, v):
        self.value = v
    def __repr__(self):
        return "{}".format(self.value)
    def eval(self):
        return self.value

class UnaryOp(Expr):
    def __init__(self, op, op_name, arg):
		pass
    def __repr__(self):
		pass
    def eval(self):
		pass

class BinaryOp(Expr):
    def __init__(self, op, op_name, arg1, arg2):
		pass
    def __repr__(self):
		pass
    def eval(self):
		pass
```

L'idée est à la fin de pouvoir construire des expressions de la
manière suivante :

```python
# This expression represents "1 + 2"
one_plus_two = BinaryOp(lambda a,b: a+b, "plus", Value(1), Value(2))
one_plus_two        # displays 'plus(1,2)'
one_plus_two.eval() # returns 3
```

### 2ème partie : un peu de programmation fonctionnelle

Pour simplifier la suite, nous allons construire des fonctions qui
permettent de construire facilement les expressions qui nous
intéressent. Par exemple, la fonction suivante prend en paramètre un
nombre et renvoie une expression contenant ce nombre :

```python
def make_value(e): return Value(e)
```

Plus intéressant, la fonction suivante prend en paramètre un nombre et
produit une expression qui construit la racine carrée de ce nombre :

```python
def make_sqrt_op(e): return UnaryOp(sqrt, "sqrt", e)
```

Construire les fonctions permettant de construire toutes les
expressions qui vous intéressent dans le jeu, et les placer dans les
listes suivantes :

```python
unary_ops = [
    make_sqrt_op,
	# à compléter
    ]

binary_ops = [
	# à compléter
    ]
```

### 3ème partie : un algorithme d'énumération

Résoudre le problème complètement général de Tchisla est difficile,
mais on peut résoudre un problème plus simple : énumérer toutes les
expressions (ici des arbres) avec $n$ noeuds internes. Pour cela, on
applique un algorithme récursif :

- si $n == 0$, alors notre arbre est juste une feuille valant $c = 1$ (on
  pourra raffiner dans un second temps si on veut ajouter d'autres
  valeurs $cc$ $\dots),

- sinon, on engendre récursivement tous les arbres contenant $m$
  opérations pour $m$ compris entre $0$ et $n-1$ (mémoïser les
  résultats serait sympathique). Et on renvoie :

  * d'une part, pour toute opération unaire $u$ dans `unary_ops` un
  arbre de racine $u$ dont le fils est un arbre de taille $n-1$,

  * et pour toute opération binaire $b$ dans `binary_ops` et tout
  entier $x$ compris entre $0$ et $n-1$, un arbre de racine $b$ avec
  deux fils, l'un de taille $x$ et l'autre de taille $n-x-1$.

Écrire une fonction `find_solution_of_size` qui, étant donné un nombre
$n$, une valeur de $c$ et un but $goal$, renvoie tous les arbres avec
$n$ noeuds internes dont l'évaluation renvoie $goal$.

### 4ème partie : des optimisations possibles

Le code récursif produit dans la partie précédente est inefficace. Il
a tendance à refaire des calculs déjà faits. Mettre en place un
système de cache pour ne pas recalculer à chaque étape les arbres déjà
calculés précédemment.

Même comme cela, le code produit trop d'expressions dès que le nombre
de noeuds internes augmente. Découper les opérations binaires en
celles qui sont commutatives et celles qui ne le sont pas. Adapter
l'algorithme d'énumération pour ne pas générer les expressions
$2+(2+2)$ et $(2+2)+2$.
