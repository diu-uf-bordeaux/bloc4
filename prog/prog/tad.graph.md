## Graphes

- Structures de données :
  - **relationnelles**,
  - **séquentielles** et **récursives**.

<br/>

- Utilisées pour représenter une **relation** entre un **ensemble de données** :
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

--

## Terminologie
<!-- .slide: data-transition="fade" -->

![terminologie](prog/images/graphes/terminologie0.svg)<!-- .element: class="stretch" style="max-width: 50%;" -->

- un **sommet** est caractérisé par une donnée (ou étiquette).
- une **arête** relie deux sommets.
- le **degré** d'un sommet est le nombre d’arêtes incidente au sommet.

--

## Terminologie
<!-- .slide: data-transition="fade" -->

![terminologie](prog/images/graphes/terminologie3.svg)<!-- .element: class="stretch" style="max-width: 50%;" -->

- les arêtes peuvent être **orientées**, on parle alors d'**arcs**.
- auquel cas, on définit l'ensemble des **successeurs** et **prédécesseurs** d'un sommet.

--

## Terminologie
<!-- .slide: data-transition="fade" -->

![terminologie](prog/images/graphes/terminologie1.svg)<!-- .element: class="stretch" style="max-width: 50%;" -->

- une **boucle** est une arête reliant un sommet à lui-même.
- des **arêtes multiples** relient les mêmes sommets.

--

## Terminologie
<!-- .slide: data-transition="fade" -->

![terminologie](prog/images/graphes/terminologie2.svg)<!-- .element: class="stretch" style="max-width: 50%;" -->

- un graphe **simple** ne contient ni boucles, ni arêtes multiples.


--

## Type abstrait ```Graphe```

Graphes **simples non orientés**

1. Constructeurs :

```python
 faire_graphe : liste de Sommets -> Graphe
    # à partir de la liste des sommets S, produit le graphe (S,∆)
 ajouter_arete : (Graphe * Sommet * Sommet) -> Graphe
    # à partir d'un graphe (S,A) et des sommets s1 et s2 appartenant à S, 
    # produit le graphe (S,A∪{(s1,s2)})
```

2. Sélecteurs : <!-- .element: class="fragment" data-fragment-index="1" -->
  
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

1. **Matrice d'adjacence** <br/>&#x279E; paradigme impératif

2. **Listes de successeurs/prédécesseurs** <br/>&#x279E; paradigme fonctionnel 

3. **Classe Noeud** <br/>&#x279E; paradigme objet
