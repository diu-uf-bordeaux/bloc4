## Graphes

- Structures de données :
  - **relationnelles**,
  - **séquentielles** et **récursives**.

<br/>

- Utilisées pour représenter une **relation** entre un **ensemble d’objets homogènes** :
  - réseaux routiers, de machines, sociaux, etc.
  - ordre d'exécution

<!-- .element: class="fragment" -->

<br/>

- Utilisées dans de nombreux **algorithmes d'optimisation** :
  - ordonnancement de tâches
  - routage réseau
  - jeux

<!-- .element: class="fragment" -->

--

## Exemple : repas de famille


![internet](prog/images/graphes/repas.jpg)<!-- .element: class="stretch" style="max-width: 60%;" -->
<br/>
[Pixinio](https://pixnio.com/fr/gens-fr/foule-fr/personnes-profiter-a-repas-in-the-refectoire)<!-- .element: style="font-size: 0.4em;" -->

- **Ensemble** : personnes
- **Relation** : cousin

--

## Exemple : internet


![internet](prog/images/graphes/internet.svg)<!-- .element: class="stretch" style="max-width: 60%;" -->
<br/>
[The OPTE project](https://web.archive.org/web/20181228014321/http://www.opte.org/)<!-- .element: style="font-size: 0.4em;" -->

- **Ensemble** : machines
- **Relation** : connexion réseau

--

## Exemple : molécule

![caffeine](prog/images/graphes/caffeine.png)<!-- .element: class="stretch" style="max-width: 40%;" -->
<br/>
[Molécule de caféine](https://pixabay.com/fr/illustrations/caféine-molécule-café-stimulant-854454/)<!-- .element: style="font-size: 0.4em;" -->

- **Ensemble** : atomes
- **Relation** : liaison covalente

<aside class="notes">
Chercher des sous-parties de molécules communes dans certains médicaments
</aside>

--

## Pourquoi les graphes ?

Permettent de représenter différentes situations de la vie courante

- **Problèmes de la vie courante** <br/>&#x279E; questions à résoudre sur les graphes

- **Algorithme sur les graphes** (cf. Bloc 5) <br/>&#x279E; réponse informatique à des problèmes concrets

![caffeine](prog/images/graphes/what-is-math.png)<!-- .element: class="stretch" style="max-width: 60%;" -->
<br/>
[Spiked Math](http://spikedmath.com/382.html)<!-- .element: style="font-size: 0.4em;" -->

--

## Terminologie
<!-- .slide: data-transition="fade" -->

![terminologie](prog/images/graphes/terminologie0.svg)<!-- .element: class="stretch" style="max-width: 50%;" -->

- un **sommet** est caractérisé par une donnée (ou étiquette).
- une **arête** relie deux sommets qui sont alors **voisins**.
- une arête peut porter une **valuation** (un poids, un coût).

--

## Terminologie
<!-- .slide: data-transition="fade" -->

![terminologie](prog/images/graphes/terminologie1.svg)<!-- .element: class="stretch" style="max-width: 50%;" -->

- le **degré** d'un sommet est le nombre d’arêtes qui lui sont incidentes.
- un sommet de degré zéro est dit **isolé**

--

## Terminologie
<!-- .slide: data-transition="fade" -->

![terminologie](prog/images/graphes/terminologie3.svg)<!-- .element: class="stretch" style="max-width: 50%;" -->

- une **boucle** est une arête reliant un sommet à lui-même.
- des **arêtes multiples** relient les mêmes sommets.

--

## Terminologie
<!-- .slide: data-transition="fade" -->

![terminologie](prog/images/graphes/terminologie2.svg)<!-- .element: class="stretch" style="max-width: 50%;" -->

- les arêtes peuvent être **orientées**, on parle alors d'**arcs**.
- auquel cas, on définit l'ensemble des **successeurs** et
  **prédécesseurs** d'un sommet.

--

## Terminologie
<!-- .slide: data-transition="fade" -->

![terminologie](prog/images/graphes/terminologie4.svg)<!-- .element: class="stretch" style="max-width: 50%;" -->

- un graphe **simple** ne contient ni boucles, ni arêtes multiples.

--

## Définition

- Un **graphe simple** est un couple $(S,A)$ formé de :
  - un ensemble $S = \\{ x_1, x_2, \dots, x_n \\} $ de sommets,
  - un ensemble $A = \\{ a_1, a_2, \dots, a_m \\}$ d'arêtes
  <br/>tel que $\forall i, a_i = (x,y) \in S^2 \wedge x \neq y$.

--

## Type abstrait ```Graphe simple```

1. Constructeur :

```python
 creer_graphe : liste de Sommets -> Graphe
    # à partir de la liste des sommets S, produit le graphe (S,∆)
```

2. Opération :

```
 ajouter_arete : (Graphe * Sommet * Sommet) -> Graphe
    # à partir d'un graphe (S,A) et des sommets s1 et s2 appartenant à S,
    # produit le graphe (S,A ∪ {(s1,s2)})
```

3. Sélecteurs : <!-- .element: class="fragment" data-fragment-index="1" -->

```python
 sommets : Graphe -> liste de Sommets
    # à partir d'un graphe (S,A), produit la liste de sommets S
 voisins : (Graphe * Sommet) -> liste de Sommets
    # à partir du graphe (S,A) et du sommet s,
    # produit la liste des voisins de s
```
<!-- .element: class="fragment" data-fragment-index="1" -->

--

## Mise en oeuvre en <span class="label">Python</span>

Plusieurs implémentations possibles :

1. **Matrice d'adjacence** <br/>&#x279E; paradigme impératif ou fonctionnel

2. **Listes de successeurs (ou de prédécesseurs)** <br/>&#x279E; paradigme impératif ou fonctionnel

<br/>

**Remarque** : sommets et/ou arêtes peuvent être représentés par des
classes (paradigme objet), si nécessaire

--

## Matrice d'adjacence

Les arêtes sont représentées par un **tableau 2D** (matrice) :
  - **lignes** (d'indice i) : tous les sommets
  - **colonnes** (d'indice j) : tous les sommets
  - **case(i,j)** :
    - 1 (ou sa valuation) si il existe un arc/une arête entre le sommet i et le sommet j,
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
| **a** | 0 | 0 | 0 | 0 | 0 | 1 | 0 |
| **b** | 1 | 0 | 1 | 0 | 0 | 0 | 0 |
| **c** | 1 | 0 | 0 | 0 | 0 | 1 | 1 |
| **d** | 0 | 0 | 0 | 0 | 0 | 0 | 0 |
| **e** | 0 | 1 | 0 | 0 | 1 | 0 | 0 |
| **f** | 0 | 0 | 0 | 0 | 0 | 0 | 1 |
| **g** | 0 | 0 | 0 | 0 | 0 | 0 | 0 |

</div>

--

## Matrice d'adjacence

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

## Listes de successeurs <br/>(ou de prédécesseurs)

Les arêtes sont représentées par un **dictionnaire** de **listes** :
  - **clés** du dictionnaire : tous les sommets
  - **liste** associée à une clé : successeurs (ou prédécesseurs) de ce sommet

<br/>

**Remarque** : dans le cas non-orienté, listes des **voisins** du sommet

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

## Listes de successeurs

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

|                  | matrice d'adjacence | liste de successeurs |
|------------------|:-------------------:|:--------------------:|
| **mémoire**      |    n<sup>2</sup>    |         n+m          |
| peu d'arêtes     |          <span style="color:red">✗</span>          |          <span style="color:green">✔︎</span>           |
| bcp d'arêtes     |          <span style="color:green">✔</span>︎          |          <span style="color:red">✗</span>           |
| **temps de calcul**                                           |
| x et y voisins ? |          1          |      degré de x      |
| x isolé ?        |          n          |          1           |
| nb arêtes ?      |    n<sup>2</sup>    |  n ou n<sup>2</sup>  |
