## Arbres

- Structures de données :
  - **hiérarchiques**, 
  - **naturellement récursives**.

<br/>

- Utilisées pour représenter des ensembles de **données** :
  - système de fichiers (répertoires et fichiers),
  - bases de données,
  - documents structurés (HTML, XML)

<!-- .element: class="fragment" -->

<br/>

- Utilisées dans les **algorithmes** :
  - arbre de décision
  - compression de textes (Huffman)
  - synthèse d'image (_kd-tree_)

<!-- .element: class="fragment" -->

--

## Exemple : arbre phylogénétique

![arbre phylogénétique](prog/images/arbres/arbre_phylogenetique_simplifie.svg)<!-- .element: class="stretch" style="max-width: 55%;" -->
<br/>
[Wikimedia Commons](https://commons.wikimedia.org/wiki/File:Arbre_phylogénétique_simplifié-_FR.svg?uselang=fr)<!-- .element: style="font-size: 0.4em;" -->

<!-- .element: style="line-height: 1;" -->

- **Quel lien ?**
  - du plus générique au plus spécifique  <!-- .element: class="fragment" -->
  - du plus ancien au plus récent  <!-- .element: class="fragment" -->
  - du plus complexe au plus simple  <!-- .element: class="fragment" -->

--

## Exemple : système de fichiers

![système de fichiers](prog/images/arbres/standard-unix-filesystem-hierarchy.svg)<!-- .element: class="stretch" style="max-width: 80%;" -->

[Wikimedia Commons](https://commons.wikimedia.org/wiki/File:Standard-unix-filesystem-hierarchy.svg)<!-- .element: style="font-size: 0.4em;" -->

--

## Exemple : expressions arithmétiques

![arbre d'expression](prog/images/arbres/expression_Tree.svg)<!-- .element: class="stretch" style="max-width: 50%;" -->

- **Quelle expression ?**
  - 4/2+6x5-3  <!-- .element: class="fragment" -->
  - (((4/2)+6)x(5-3))   <!-- .element: class="fragment" -->

--

## Terminologie
<!-- .slide: data-transition="fade" -->

![terminologie](prog/images/arbres/terminologie1.svg)<!-- .element: class="stretch" style="max-width: 45%; margin: 0" -->

- un **nœud** est caractérisé par une donnée (ou étiquette),
- une **arête** (ou lien) relie deux nœuds.
- l'**arbre vide** n'est pas un nœud.

--

## Terminologie
<!-- .slide: data-transition="fade" -->

![terminologie](prog/images/arbres/terminologie2.svg)<!-- .element: class="stretch" style="max-width: 45%; margin: 0" -->

- les **fils** sont l'ensemble des nœuds reliés à un même nœud par des arêtes entrantes.
- le **père** (ou parent) est le nœud relié à ses nœuds fils par une arête sortante.
- un **sous-arbre** est l'ensemble des nœuds et arêtes d'un nœud parent et de ses fils.

--

## Terminologie
<!-- .slide: data-transition="fade" -->

![terminologie](prog/images/arbres/terminologie3.svg)<!-- .element: class="stretch" style="max-width: 45%; margin: 0" -->

- la **racine** est le seul nœud sans père.
- une **feuille** est un nœud sans fils.
- un **nœud interne** est un nœud qui n'est pas une feuille.

--

## Terminologie
<!-- .slide: data-transition="fade" -->

![terminologie](prog/images/arbres/terminologie4.svg)<!-- .element: class="stretch" style="max-width: 45%; margin: 0" -->

- un **chemin** est une liste de nœuds reliés par des arêtes.
- une **branche** est le chemin le plus court reliant un nœud à la racine.

--

## Quelques mesures sur les arbres
<!-- .slide: data-transition="fade" -->

![terminologie](prog/images/arbres/terminologie5.svg)<!-- .element: class="stretch" style="max-width: 45%; margin: 0" -->

- la **taille** d'un arbre est le nombre de nœuds de l'arbre.
- la **profondeur** d'un nœud est le nombre d'arêtes sur la branche qui le relie à la racine. 
- la **hauteur** d'un arbre est la profondeur maximale de l'ensemble des nœuds de l'arbre.

--

## Quelques mesures sur les arbres
<!-- .slide: data-transition="fade" -->

![terminologie](prog/images/arbres/terminologie6.svg)<!-- .element: class="stretch" style="max-width: 45%; margin: 0" -->

- l'**arité ou degré d'un nœud** est le nombre de fils du nœud.
- l'**arité ou degré d'un arbre** est le nombre maximal de fils des nœuds de l'arbre.

<div class="fragment">
<br/>
Un <strong>arbre binaire</strong> est donc un arbre d'<strong>arité deux</strong>.
</div>
