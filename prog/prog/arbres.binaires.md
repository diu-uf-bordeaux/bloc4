## Pourquoi les arbres binaires ?

Structure pour effectuer des recherches rapides,<br/> ou maintenir efficacement des ensembles triés.

Par exemples, **arbre rouge-noir** :

![arbre rouge-noir](prog/images/arbres/red-black_tree.svg)<!-- .element: class="stretch" style="max-width: 70%;" -->
<br/>
[Wikimedia Commons](https://commons.wikimedia.org/wiki/File:Red-black_tree_example.svg)<!-- .element: style="font-size: 0.4em;" -->

<!-- .element: style="line-height: 1;" -->

--

## Pourquoi les arbres binaires ?

Aide à la création de circuits (synthèse logique)<br/> et vérification formelle de programme.

Par exemple, **arbre binaire de décision** :

![arbre de decision](prog/images/arbres/BDD.svg)<!-- .element: style="width: 55%;" -->
![diagramme de decision](prog/images/arbres/BDD_simple.svg)<!-- .element: class="fragment" style="width: 24%;" -->
<br/>
[Wikimedia Commons](https://commons.wikimedia.org/wiki/File:BDD.png)<!-- .element: style="font-size: 0.4em;" -->

<!-- .element: style="line-height: 1;" -->

--

## Pourquoi les arbres binaires ?

Permet de représenter un arbre quelconque.

<div class='half'>

Arbre **n-aire**
![arbre n-aire](prog/images/arbres/arbre-naire.svg)<!-- .element: class="stretch" style="max-width: 100%;" -->

</div>

<div class='half'>

Arbre **binaire** équivalent
![arbre binaire](prog/images/arbres/arbre-binaire.svg)<!-- .element: class="stretch" style="max-width: 75%;" -->

</div>

--

## Définition récursive

- Un **arbre binaire** c'est :
  - soit un **arbre vide**, noté ∆ ;
  - soit un **triplet** (*e*, *g*, *d*), appelé nœud, avec :
    -  *e* son étiquette,
    -  *g* son sous-arbre binaire **gauche**,
    -  *d* son sous-arbre binaire **droit**.
- <!-- .element: class="fragment" -->Définition <strong>récursive</strong> car un arbre binaire est défini par des arbres binaires.
- <!-- .element: class="fragment" -->La première partie de la définition assure l'arrêt et donc la cohérence de la définition.

--

## Quelques arbres binaires
<!-- .slide: data-transition="fade" -->

- Dessinez chacun des arbres ci-dessous :

  - (1, ∆, ∆)
  - (3, (1, ∆, (4, (1, ∆, (5, ∆, ∆)), ∆)), ∆)
  - (3, (1, (1, ∆, ∆), ∆), (4, (5, ∆, ∆), (9, ∆, ∆)))
  - (3, (1, (1, ∆, ∆), (5, ∆, ∆)), (4, (9, ∆, ∆), (2, ∆, ∆)))

- Donnez sa taille et sa hauteur, le nombre de feuilles, le nombre de nœuds à chaque profondeur.

--

## Quelques arbres binaires
<!-- .slide: data-transition="fade" -->

<div class='half'>
(1, ∆, ∆)

![arbre1](prog/images/arbres/arbre1.svg)<!-- .element: class="fragment" style="width: 80px; margin:0" -->

- taille : 1
- hauteur : 0
- nb feuilles : 1

<!-- .element: class="fragment" -->
</div>

<div class='half fragment' style="border-left-style:solid;padding-left:5px">
(3, (1, ∆, (4, (1, ∆, (5, ∆, ∆)), ∆)), ∆)

![arbre2](prog/images/arbres/arbre2.svg)<!-- .element: class="fragment" style="width: 150px; margin:0" -->

- taille : 5
- hauteur : 4
- nb feuilles : 1

<!-- .element: class="fragment" -->
</div>

--

## Quelques arbres binaires
<!-- .slide: data-transition="fade" -->

<div class='half'>
(3, (1, (1, ∆, ∆), ∆), (4, (5, ∆, ∆), (9, ∆, ∆)))

![arbre3](prog/images/arbres/arbre3.svg)<!-- .element: class="fragment stretch" style="max-width: 70%; margin:0" -->

- taille : 6
- hauteur : 2
- nb feuilles : 3

<!-- .element: class="fragment" -->
</div>

<div class='half fragment' style="border-left-style:solid;padding-left:5px">
(3, (1, (1, ∆, ∆), (5, ∆, ∆)), (4, (9, ∆, ∆), (2, ∆, ∆)))

![arbre4](prog/images/arbres/arbre4.svg)<!-- .element: class="fragment stretch" style="max-width: 100%; margin:0" -->

- taille : 7
- hauteur : 2
- nb feuilles : 4

<!-- .element: class="fragment" -->
</div>

--

## Arbre binaire de hauteur ```h``` 
<!-- .slide: data-transition="fade" -->

Combien de **feuilles** et de **nœuds** comporte-il :

<div class='half'>

1. Au minimum ?
  - <!-- .element: class="fragment" data-fragment-index="1" -->1 feuille et h+1 nœuds d'arité 1.
  - <!-- .element: class="fragment" data-fragment-index="1" -->On parle alors d'arbre <strong>filiforme</strong>.
   
</div>

<div class='half fragment' data-fragment-index="2">

  ![arbre filiforme](prog/images/arbres/filiforme.svg)<!-- .element: style="width: 180px;"-->

</div>

--

## Arbre binaire de hauteur ```h```  
<!-- .slide: data-transition="fade" -->

Combien de **feuilles** et de **nœuds** comporte-il :

<div class='half'>

1. Au minimum ?
  - 1 feuille et h+1 nœuds d'arité 1.
  - On parle alors d'arbre <strong>filiforme</strong>.
2. Au maximum ?
  - <!-- .element: class="fragment" data-fragment-index="1" -->2<sup>h</sup> feuilles et 2<sup>h+1</sup>-1 nœuds.
  - <!-- .element: class="fragment" data-fragment-index="1" -->On parle alors d'arbre <strong>complet</strong>.

</div>

<div class='half fragment' data-fragment-index="2" style="vertical-align:bottom">

  ![arbre filiforme](prog/images/arbres/complet.svg)<!-- .element: class="stretch" style="max-width: 90%;"-->

</div>

<aside class="notes">
  Suites géométriques de raisons 2
</aside>