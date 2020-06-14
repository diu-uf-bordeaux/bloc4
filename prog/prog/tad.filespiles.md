## Files et piles

- Les files et piles sont comme des sacs.

<!-- .element: class="fragment" -->

- Une file est dite `First-In First-Out` (FIFO):
  - On insère un élément par la queue de la file
  - On prend un élément par le devant de la file

<!-- .element: class="fragment" -->

- Une pile est dite `Last-In First-Out` (LIFO):
  - On insère un élément sur le dessus de la pile
  - On prend un élément sur le dessus de la pile

<!-- .element: class="fragment" -->

--

## Files et piles

- Ces types abstraits de données nous permettent de:
  - Savoir si la structure est **vide**
  - **Récupérer** un élément
  - **Insérer** un élément

<!-- .element: class="fragment" -->

- Dans la majorité des cas:
  - **Empiler/Enfiler** un élément se dit `push`
  - **Dépiler/Défiler** un élément se dit `pop`

<!-- .element: class="fragment" -->

- `Attention`: Le fait de récupérer un élément l'enlève de la pile/file. Il faudra donc le réinsérer si on souhaite le garder.

<!-- .element: class="fragment" -->

--

## Terminologie

![Terminologie](prog/images/pilesfiles/terminologie.svg)<!-- .element: class="stretch" style="width: 45%;" -->

- Une file `pop` un élément de la **tête** et `push` un élément dans la **queue**
- Une pile `pop` et `push` les éléments sur le **sommet de la pile** uniquement

--

## Exemple de file et pile: `Push`

On peut représenter une file/pile (nommée **s**) comme suit:

![Représentation](prog/images/pilesfiles/filesPilesRepresentation.svg)<!-- .element: class="stretch" style="max-width: 80%;" -->

Ces structures sont le résultat du code suivant:

```python
1. s.push(3)
2. s.push(6)
3. s.push(9)
```

--

## Exemple de file et pile: `Pop`

En reprenant les structures de la slide précédente:

![Représentation](prog/images/pilesfiles/filesPilesRepresentation.svg)<!-- .element: class="stretch" style="max-width: 80%;" -->

L'opération `Pop` produit différents résultats:

```python
1. file.pop() -> 3  # Premier élément inséré (FIFO)
2. 
3. pile.pop() -> 9  # Dernier élément inséré (LIFO)
```
