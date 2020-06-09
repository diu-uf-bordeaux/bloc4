## Pureté (1/2)

- Idée : le résultat de l'évaluation d'une fonction ne dépend que de
  la valeur de ses paramètres, sans aucun facteur externe.

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

f() - f() # (1 - 2) or (2 - 1) ?
```
</div>
<!-- .element: style="margin-top:-10px; background-color: #3f3f3f" -->

<div class="half">

- En <span class="label">Python</span> : `-1`

- En <span class="label">C</span> : `1` ou `-1`

- En <span class="label">OCaml</span> : `1` ou `-1`

</div>
<!-- .element: style="margin-top:-10px;" -->

Note:
- une application est telle qu'à un élément d'origine on associe un
unique élément d'arrivée.
- en C, la chose est plus facile à vérifier parce qu'il existe
plusieurs compilateurs. en OCaml, il y a deux compilateurs mais tous
les deux développés ensemble (bytecode et natif), et les versions
récentes ont unifié le comportement, mais il est l'opposé de Python.


--

## Pureté (2/2)

- Une fonction "impure" produisant ou dépendant de facteurs externes
  est dite réaliser des **effets de bords**.


- La présence de **variables** ou de **boucles**, et plus généralement
  la notion d'**état** (<a href="#/intro.imperative">impératif</a>)
  sont propices aux effets de bords.

  $\Rightarrow$ Idée : manipuler et transformer des objets **constants**

- Exemples d'effets de bord&nbsp;:
	* lecture/écriture dans un fichier, une base de données
<!-- .element: style="margin-top:-10px;" -->
	* dépendance à un générateur aléatoire,
	* dépendance à une mesure externe (heure, lieu &hellip;)

- Il n'est pas toujours simple d'écrire des fonctions pures, il faut
  parfois transiger.


--

## Pureté : un exemple (1/2)

- Transformation de code impératif $\rightarrow$ fonctionnel

<div class="half" style="width:46%; margin-top:10px">

Avec effet de bord (imp)<!-- .element: class="title" -->

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

Sans effet de bord (fonc)<!-- .element: class="title" -->

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

Avec effet de bord (imp)<!-- .element: class="title" -->

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

Sans effet de bord (fonc)<!-- .element: class="title" -->

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

--

## Coder sans effets de bords

- Comment organiser un calcul (non trivial) sans variables ?

```python
play(                                    \
	play(                                \
		play(                            \
			play(board,                  \
				 Color.WHITE),           \
			Color.BLACK),                \
		Color.WHITE),                    \
	Color.BLACK)
```

- Solution possible : écrire des fonctions récursives.

```python
def play_rec(board, n):
    if (n == 0):
        return board
    else:
        next_board = play(play(board, Color.WHITE), Color.BLACK)
        return play_rec(next_board, n-1)
```
