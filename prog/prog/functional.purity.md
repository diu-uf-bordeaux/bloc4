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

<div class="half" style="width:46%; margin-top:10px">

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

<div class="half" style="width:53%; margin-top:10px">

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

- Chaque intermédiaire peut être considéré comme constant.


--

## Pureté : un exemple (2/2)

- Transformation de code impératif $\rightarrow$ fonctionnel

<div class="half" style="margin-top:10px">

Avec effet de bord <!-- .element: class="title" -->

```python
global_board = Board() # global state

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
