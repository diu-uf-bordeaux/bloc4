## Type abstrait ```Graphe simple```

1. Constructeur :

```python
 creer_graphe : liste de Sommets -> Graphe
    # à partir de la liste des sommets S, produit le graphe (S,∆)
```

2. Opération : <!-- .element: class="fragment" data-fragment-index="1" -->

```
 ajouter_arete : (Graphe * Sommet * Sommet) -> Graphe
    # à partir d'un graphe (S,A) et des sommets s1 et s2 appartenant à S,
    # produit le graphe (S,A ∪ {(s1,s2)})
```
<!-- .element: class="fragment" data-fragment-index="1" -->

3. Sélecteurs : <!-- .element: class="fragment" data-fragment-index="2" -->

```python
 sommets : Graphe -> liste de Sommets
    # à partir d'un graphe (S,A), produit la liste de sommets S
 voisins : (Graphe * Sommet) -> liste de Sommets
    # à partir du graphe (S,A) et du sommet s,
    # produit la liste des voisins de s
```
<!-- .element: class="fragment" data-fragment-index="2" -->

--

## Mise en oeuvre en <span class="label">Python</span>

Plusieurs implémentations possibles :

1. **Matrice d'adjacence** <br/>&#x279E; paradigme impératif ou fonctionnel

--

## Matrice d'adjacence
<!-- .slide: data-transition="fade" -->

Les arêtes sont représentées par un **tableau 2D** (matrice) :
  - **lignes** (d'indice i) : tous les sommets
  - **colonnes** (d'indice j) : tous les sommets
  - **case(i,j)** :
    - 1 (ou sa valuation) si il existe un arc/une arête <br/>entre le sommet i et le sommet j,
    - 0 sinon.

<br/>

**Remarque** : dans le cas non-orienté, le tableau est **symétrique** <br/>&#x279E; ```case(i,j) = case(j,i)```

--

## Matrice d'adjacence
<!-- .slide: data-transition="fade" class="graph" -->

<div class='half'>

![graphe orienté simple](prog/images/graphes/oriented_simple_graphe.svg)<!-- .element: class="stretch" style="max-width: 90%;"-->

</div>

<div class='half'>

|   |   |   |   |   |   |   |   |
|:-:|:-:|:-:|:-:|:-:|:-:|:-:|:-:|
|   | **a** | **b** | **c** | **d** | **e** | **f** | **g** |
| **a** |  |  |  |  |  |  |  |
| **b** |  |  |  |  |  |  |  |
| **c** |  |  |  |  |  |  |  |
| **d** |  |  |  |  |  |  |  |
| **e** |  |  |  |  |  |  |  |
| **f** |  |  |  |  |  |  |  |
| **g** |  |  |  |  |  |  |  |

</div>

--

## Matrice d'adjacence
<!-- .slide: data-transition="fade" class="graph" -->

<div class='half'>

![graphe orienté simple](prog/images/graphes/oriented_simple_graphe.svg)<!-- .element: class="stretch" style="max-width: 90%;"-->

</div>

<div class='half'>

|   |   |   |   |   |   |   |   |
|:-:|:-:|:-:|:-:|:-:|:-:|:-:|:-:|
|   | **a** | **b** | **c** | **d** | **e** | **f** | **g** |
| **a** | 0 | 0 | 0 | 0 | 0 | `1` | 0 |
| **b** | `1` | 0 | `1` | 0 | 0 | 0 | 0 |
| **c** | `1` | 0 | 0 | 0 | 0 | `1` | `1` |
| **d** | 0 | 0 | 0 | 0 | 0 | 0 | 0 |
| **e** | 0 | `1` | 0 | 0 | `1` | 0 | 0 |
| **f** | 0 | 0 | 0 | 0 | 0 | 0 | `1` |
| **g** | 0 | 0 | 0 | 0 | 0 | 0 | 0 |

</div>

--

## Matrice d'adjacence
<!-- .slide: data-transition="fade" -->

```python
 def creer_graphe(sommets):
  dimension = len(sommets)
  adjacence = [[0 for i in range(dimension)] for j in range(dimension)]
  return (sommets,adjacence)

 def ajouter_arete(graphe, s1, s2):
  i = graphe[0].index(s1)
  j = graphe[0].index(s2)
  graphe[1][i][j] = 1
  return graphe

 def sommets(graphe):
  return graphe[0]

 def voisins(graphe, sommet):
  i = self.sommets.index(sommet)
  return [graphe[0][j] for j in range (len(graphe[0])) if graphe[1][i][j]==1]
```
<!-- .element: style="width:95%" -->

--
## Matrice d'adjacence
<!-- .slide: data-transition="fade" -->

Exemple d'utilisation :

```python
 G = creer_graphe(['a', 'b', 'c', 'd'])
 G.ajouter_arete('a', 'b')
 G.ajouter_arete('a', 'c')
 G.ajouter_arete('c', 'd')
 print(G.voisins('c'))
 print(graphe[1])
```

--

## Mise en oeuvre en <span class="label">Python</span>

Plusieurs implémentations possibles :

1. **Matrice d'adjacence** <br/>&#x279E; paradigme impératif ou fonctionnel

2. **Listes de successeurs (ou de prédécesseurs)** <br/>&#x279E; paradigme impératif ou fonctionnel

<br/>

**Remarque** : sommets et/ou arêtes peuvent être représentés par des
classes (paradigme objet), si nécessaire
<!-- .element: class="fragment" -->

--

## Listes de successeurs <br/>(ou de prédécesseurs)

Les arêtes sont représentées par un **dictionnaire** de **listes** :
  - **clés** du dictionnaire : tous les sommets
  - **liste** associée à une clé : successeurs (ou prédécesseurs) de ce sommet

<br/>

**Remarques** : 
1. dans le cas non-orienté, listes des **voisins** du sommet
2. pour les arcs/arêtes valués, dictionnaire de dictionnaires

--

## Listes de successeurs
<!-- .slide: data-transition="fade" class="graph" -->

<div class='half'>

![graphe orienté simple](prog/images/graphes/oriented_simple_graphe.svg)<!-- .element: class="stretch" style="max-width: 90%;"-->

</div>

<div class='half'>

- **a** :
- **b** :
- **c** :
- **d** :
- **e** :
- **f** :
- **g** :

</div>

--

## Listes de successeurs
<!-- .slide: data-transition="fade" class="graph" -->

<div class='half'>

![graphe orienté simple](prog/images/graphes/oriented_simple_graphe.svg)<!-- .element: class="stretch" style="max-width: 90%;"-->

</div>

<div class='half'>

- **a** : [f]
- **b** : [a,c]
- **c** : [a,f,g]
- **d** : []
- **e** : [b,e]
- **f** : [g]
- **g** : []

</div>

--

## Listes de prédécesseurs
<!-- .slide: data-transition="fade" class="graph" -->

<div class='half'>

![graphe orienté simple](prog/images/graphes/oriented_simple_graphe.svg)<!-- .element: class="stretch" style="max-width: 90%;"-->

</div>

<div class='half'>

- **a** :
- **b** :
- **c** :
- **d** :
- **e** :
- **f** :
- **g** :

</div>

--

## Listes de prédécesseurs
<!-- .slide: data-transition="fade" class="graph" -->

<div class='half'>

![graphe orienté simple](prog/images/graphes/oriented_simple_graphe.svg)<!-- .element: class="stretch" style="max-width: 90%;"-->

</div>

<div class='half'>

- **a** : [b,c]
- **b** : [e]
- **c** : [b]
- **d** : []
- **e** : [e]
- **f** : [a,c]
- **g** : [c,f]

</div>

--

## Listes de successeurs
<!-- .slide: data-transition="fade" -->

```python
  def creer_graphe(sommets):
    return (sommets, dict())

  def ajouter_arete (graphe, x, y):
    if x in graphe[1]:
        graphe[1][x].add(y)
    else:
        graphe[1][x]={y}

  def sommets (graphe):
    return graphe[0]

  def voisins (graphe, sommet):
    return list(graphe[1][sommet])
```

--

## Listes de successeurs
<!-- .slide: data-transition="fade" -->

Exemple d'utilisation :

```python
  G = creer_graphe(['a', 'b', 'c', 'd'])
  G.ajouter_arete('a', 'b')
  G.ajouter_arete('a', 'c')
  G.ajouter_arete('c', 'd')
  print(G.voisins('c'))
  print(graphe[1])
```

--

## Comparaison
<!-- .slide: data-transition="fade" -->

|                  | matrice d'adjacence | liste de successeurs |
|------------------|:-------------------:|:--------------------:|
| **mémoire**      |                     |                      |
| peu d'arêtes     |                     |                      |
| bcp d'arêtes     |                     |                      |
| **temps de calcul**                                           |
| $x$ et $y$ voisins ? |                 |                      |
| $x$ isolé ?      |                     |                      |
| nb arêtes ?      |                     |                      |

avec $n$ le nombre de sommets et $m$ le nombre d'arêtes.

--

## Comparaison
<!-- .slide: data-transition="fade" -->

|                  | matrice d'adjacence | liste de successeurs |
|------------------|:-------------------:|:--------------------:|
| **mémoire**      |        $n^2$        |         $n+m$        |
| peu d'arêtes     |<span style="color:red">✗</span>|<span style="color:green">✔︎</span>|
| bcp d'arêtes     |<span style="color:green">✔︎</span>|<span style="color:red">✗</span>|
| **temps de calcul**                                           |
| $x$ et $y$ voisins ? |                 |                      |
| $x$ isolé ?      |                     |                      |
| nb arêtes ?      |                     |                      |

avec $n$ le nombre de sommets et $m$ le nombre d'arêtes.

--

## Comparaison
<!-- .slide: data-transition="fade" -->

|                  | matrice d'adjacence | liste de successeurs |
|------------------|:-------------------:|:--------------------:|
| **mémoire**      |    $n^2$    |         $n+m$          |
| peu d'arêtes     |          <span style="color:red">✗</span>          |          <span style="color:green">✔︎</span>           |
| bcp d'arêtes     |          <span style="color:green">✔︎</span>          |          <span style="color:red">✗</span>           |
| **temps de calcul**                                           |
| $x$ et $y$ voisins ? |          $1$          |      degré de $x$      |
| $x$ isolé ?        |          $n$          |          $1$           |
| nb arêtes ?      |    $n^2$    |  $n$ ou $n^2$  |

avec $n$ le nombre de sommets et $m$ le nombre d'arêtes.