## Files

- Les files sont largement utilisées lorsque l'on veut modéliser une file d'attente.
- Par exemple :
  - Les impressions sont gérées par une file.
  - Dans une simulation de guichet, on modélisera généralement l'arrivée des clients par une file.

--

## Type abstrait `File`

1. Constructeurs :

```python
 file_vide : () -> File
    # produit la file vide
 file : (Valeur * File) -> File
    # produit une file à partir d'une valeur et d'une autre file
```

2. Fonctions : <!-- .element: class="fragment" data-fragment-index="1" -->

```python
 push : (Valeur * File) -> File
    # ajoute une valeur dans la file
 pop : File -> (Valeur * File)
    # extrait la valeur de la tête de la file
    # puis renvoi la file sans cette valeur
    # Attention: La file ne doit pas être vide
```

<!-- .element: class="fragment" data-fragment-index="1" -->

3. Prédicat : <!-- .element: class="fragment" data-fragment-index="2" -->

```python
 est_vide : File -> bool
    # indique si la file est vide
```

<!-- .element: class="fragment" data-fragment-index="2" -->

--

## Mise en oeuvre en <span class="label">Python</span>

Plusieurs implémentations possibles :

1. **Récursive** <br/>&#x279E; paradigme fonctionnel

--

## Récursive

1. Constructeurs :

```python 
  def file_vide():
    return []

  def file(valeur, file):
    return [valeur, file]
```

2. Sélecteurs : <!-- .element: class="fragment" data-fragment-index="1" -->

```python
  def push(valeur, file):
    if est_vide(file):
      return [valeur, file_vide()]
    return [file[0], push(valeur, file[1])]

  def pop(file):
    return (file[0], file[1])
```

<!-- .element: class="fragment" data-fragment-index="1" -->

3. Prédicat : <!-- .element: class="fragment" data-fragment-index="2" -->

```python 
  def est_vide(file):
    return file == file_vide()
```

<!-- .element: class="fragment" data-fragment-index="2" -->

--

## Récursive
<!-- .slide: data-transition="fade" -->

Exemple d'utilisation :

```python
  1. F1 = file_vide()
  2. F1 = push(3, F1)
  3. print(F1) # [3, []]
  4.
  5. F1 = push(6, F1)
  6. print(F1) # [3, [6, []]]
  7.
  8. resultat = pop(push(9, F1))
  9. print(resultat) # (3, [6, [9, []]])
 10.
 11. # Nous pouvons copier une file en la défilant dans une autre file
 11. F2 = file_vide()
 12. while not est_vide(F1):
 13.   res = pop(F1)  # res[0] contient la valeur, res[1] contient la file restante
 14.   F2 = push(res[0], F2)
 15.   F1 = res[1]
 16. print(F2)  # [6, [9, []]]
```

--

## Mise en oeuvre en <span class="label">Python</span>

Plusieurs implémentations possibles :

1. **Récursive** <br/>&#x279E; paradigme fonctionnel

<br/>

2. **Classe File** <br/>&#x279E; paradigme objet

--

## Classe File
<!-- .slide: data-transition="fade" -->

La classe file est implémentée à l'aide d'un tableau :

```python
  class File:
    file_vide = None

    def __init__(self, valeur, file):
      self._valeur = valeur
      self._suite = file
    
    def push(self, valeur):
      if File.est_vide(self._suite):
        self._suite = File(valeur, File.file_vide)
      else:
        self._suite.push(valeur)
      return self
    
    def pop(self):
      return (self._valeur, self._suite)
    
    def est_vide(file):
      return file is File.file_vide
```

<!-- .element: class="stretch" -->

--

## Classe File
<!-- .slide: data-transition="fade" -->

Exemple d'utilisation :

```python
   1. F1 = File(3, File.file_vide)
   3. print(F1.pop()) # (3, None)
   4.
   5. F2 = File(3, File.file_vide)
   6. F2.push(6).push(9)
   7. # F2: <--[3]<--[6]<--[9]<--
   8.
   9. (val, F2) = F2.pop()
  10. F3 = File(val, File.file_vide)
  11. while not File.est_vide(F2):
  12.   (val, F2) = F2.pop()
  13.   F3.push(val)
  14. # F3: <--[3]<--[6]<--[9]<--
```

--

## Mise en oeuvre en <span class="label">Python</span>

Plusieurs implémentations possibles :

1. **Récursive** <br/>&#x279E; paradigme fonctionnel

<br/>

2. **Classe Cellule** <br/>&#x279E; paradigme objet

<br/>

3. **Tableau** <br/>&#x279E; paradigme impératif

--

## Tableau
<!-- .slide: data-transition="fade" -->

File stockée dans un tableau.

```python 
  def file_vide():
    return []

  def file(valeur, file):
    return file + [valeur]

  def push(valeur, file):
    return file + [valeur]

  def pop(file):
    return (file[0], file[1:])

  def est_vide(file):
    return file == file_vide()
```

--

## Tableau
<!-- .slide: data-transition="fade" -->

Exemple d'utilisation :

```python
   1. file = file_vide()
   2. file = push(3, file)
   3. print(pop(file)) # (3, [])
   4.
   5. file = file_vide()
   6. file = push(3, file)
   7. file = push(6, file)
   8. file = push(9, file)
   9. copie = file_vide()
  10.
  11. while not est_vide(file):
  12.   (val, file) = pop(file)
  12.   copie = push(val, copie)
  13. print(copie) # [3, 6, 9]
```