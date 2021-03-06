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


![internet](prog/images/graphes/repas.jpg)<!-- .element: class="stretch" style="max-width: 55%; margin:0 0 0 0" -->
<br/>
[Pixinio](https://pixnio.com/fr/gens-fr/foule-fr/personnes-profiter-a-repas-in-the-refectoire)<!-- .element: style="font-size: 0.4em;" -->

<!-- .element: style="line-height: 1;" -->

- **Ensemble** : personnes
- **Relation** : cousin

--

## Exemple : internet


![internet](prog/images/graphes/internet.svg)<!-- .element: class="stretch" style="max-width: 55%; margin:0 0 0 0" -->
<br/>
[The OPTE project](https://web.archive.org/web/20181228014321/http://www.opte.org/)<!-- .element: style="font-size: 0.4em;" -->

<!-- .element: style="line-height: 1;" -->

- **Ensemble** : machines
- **Relation** : connexion réseau

--

## Exemple : molécule

![caffeine](prog/images/graphes/caffeine.png)<!-- .element: class="stretch" style="max-width: 35%;" -->
<br/>
[Molécule de caféine](https://pixabay.com/fr/illustrations/caféine-molécule-café-stimulant-854454/)<!-- .element: style="font-size: 0.4em;" -->

<!-- .element: style="line-height: 1;" -->

- **Ensemble** : atomes
- **Relation** : liaison covalente

<aside class="notes">
Chercher des sous-parties de molécules communes dans certains médicaments
</aside>

--

## Pourquoi les graphes ?

Permettent de représenter différentes situations de la vie courante

- **Problèmes de la vie courante** <br/>&#x279E; questions à résoudre sur les graphes

<!-- .element: class="fragment" -->

- **Algorithme sur les graphes** (cf. Bloc 5) <br/>&#x279E; réponse informatique à des problèmes concrets

<!-- .element: class="fragment" -->

![caffeine](prog/images/graphes/what-is-math.png)<!-- .element: class="stretch" style="max-width: 60%; margin:0" -->
<br/>
[Spiked Math](http://spikedmath.com/382.html)<!-- .element: style="font-size: 0.4em;" -->

<!-- .element: style="line-height: 1;" -->

--

## Exemple : examens de spécialité
<!-- .slide: data-transition="fade" -->

- Les élèves d'une classe de terminal passent leurs examens de spécialité, à choisir parmi : Maths (M), Humanité (H), NSI (N), Physique-Chimie (P), SVT (S) et Langues (L).
- Certains passent M, H, N, d'autres N, P, S et d'autres S, L, P.
- Tous les examens sont d'une durée de 2h.

- **Question :** Quelle est la durée la plus courte pour organiser ces examens ?

--

## Exemple : examens de spécialité
<!-- .slide: data-transition="fade" -->

- **Ensemble** : examens {M, H, N, P, S, L}
- **Relation** : incompatibilité entre deux examens <br/>&#x279E; si un élèves doit passer deux des examens, les épreuves ne peuvent avoir lieu en même temps

![examens](prog/images/graphes/examens1.svg)<!-- .element: class="fragment" style="max-width: 50%; margin:0" -->

--

## Exemple : examens de spécialité
<!-- .slide: data-transition="fade" -->

- On cherche à attribuer à chaque examen un créneau horaire <br/>&#x279E; on veut **colorier** les sommets adjacents avec des couleurs différentes en utilisant un **minimum** de couleurs.

![examens](prog/images/graphes/examens2.svg)<!-- .element: class="fragment" style="max-width: 50%; margin:0" -->

**Solution :** 3 couleurs &#x279E; on peut organiser les examens en 3 x 2h.
<!-- .element: class="fragment" -->

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

![terminologie](prog/images/graphes/terminologie3.svg)<!-- .element: class="stretch" style="max-width: 50%;" -->

- une **boucle** est une arête reliant un sommet à lui-même.
- des **arêtes multiples** relient les mêmes sommets.

--

## Terminologie
<!-- .slide: data-transition="fade" -->

![terminologie](prog/images/graphes/terminologie1.svg)<!-- .element: class="stretch" style="max-width: 50%;" -->

- le **degré** d'un sommet est le nombre d’arêtes qui lui sont incidentes.
- un sommet de degré zéro est dit **isolé**

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

un graphe **simple** ne contient ni boucles, ni arêtes multiples.

--

## Définition

- Un **graphe simple** est un couple $(S,A)$ formé de :
  - un ensemble $S = \\{ x_1, x_2, \dots, x_n \\}$ de sommets,
  - un ensemble $A = \\{ a_1, a_2, \dots, a_m \\}$ d'arêtes
  <br/>tel que $\forall i, a_i = (x,y) \in S^2 \wedge x \neq y$.

- **Remarque :** pour un graphe orienté, l'arête $(x,y)$ _part_ du sommet $x$ et _arrive_ au sommet $y$.

--

## Exemple

![terminologie](prog/images/graphes/terminologie4.svg)<!-- .element: style="max-width: 50%;" -->

- Graphe $(S,A)$ avec :
  - $S = \\{ a, b, c, d, e, f, g \\}$
  - $A = \\{ (e,b), (b,a), (b,c), (c,a), (c,f), (c,g), (a,f), (f,g) \\}$