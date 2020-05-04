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

![arbre phylogénétique](prog/images/arbres/arbre_phylogenetique_simplifie.svg)<!-- .element: class="stretch" style="max-width: 60%;" -->
<br/>
[Wikimedia Commons](https://commons.wikimedia.org/wiki/File:Arbre_phylogénétique_simplifié-_FR.svg?uselang=fr)<!-- .element: style="font-size: 0.4em;" -->

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

![terminologie](prog/images/arbres/terminologie1.svg)<!-- .element: class="stretch" style="max-width: 50%;" -->

- un **nœud** est caractérisé par : 
  - une donnée (ou étiquette),
  - un nombre fini de fils.
- une **arête** (ou lien) relie deux nœuds.
- l'**arbre vide** n'est pas un nœud.

--

## Terminologie
<!-- .slide: data-transition="fade" -->

![terminologie](prog/images/arbres/terminologie2.svg)<!-- .element: class="stretch" style="max-width: 50%;" -->

- les **fils** sont l'ensemble des nœuds reliés à un même nœud par des arêtes entrantes.
- le **père** (ou parent) est le nœud relié à ses nœuds fils par une arête sortante.
- un **sous-arbre** est l'ensemble des nœuds et arêtes d'un nœud parent et de ses fils.

--

## Terminologie
<!-- .slide: data-transition="fade" -->

![terminologie](prog/images/arbres/terminologie3.svg)<!-- .element: class="stretch" style="max-width: 50%;" -->

- la **racine** est le seul nœud sans père.
- une **feuille** est un nœud sans fils.
- un **nœud interne** est un nœud qui n'est pas une feuille.

--

## Terminologie
<!-- .slide: data-transition="fade" -->

![terminologie](prog/images/arbres/terminologie4.svg)<!-- .element: class="stretch" style="max-width: 50%;" -->

- un **chemin** est une liste de nœuds reliés par des arêtes.
- une **branche** est le chemin le plus court reliant un nœud à la racine.

--

## Quelques mesures sur les arbres
<!-- .slide: data-transition="fade" -->

![terminologie](prog/images/arbres/terminologie5.svg)<!-- .element: class="stretch" style="max-width: 50%;" -->

- la **taille** d'un arbre est le nombre de nœuds de l'arbre.
- la **profondeur** d'un nœud est le nombre d'arêtes sur la branche qui le relie à la racine. 
- la **hauteur** d'un arbre est la profondeur maximale de l'ensemble des nœuds de l'arbre.

--

## Quelques mesures sur les arbres
<!-- .slide: data-transition="fade" -->

![terminologie](prog/images/arbres/terminologie6.svg)<!-- .element: class="stretch" style="max-width: 50%;" -->

- l'**arité ou degré d'un nœud** est le nombre de fils du nœud.
- l'**arité ou degré d'un arbre** est le nombre maximal de fils des nœuds de l'arbre.

<div class="fragment">
<br/>
Un <strong>arbre binaire</strong> est donc un arbre d'<strong>arité deux</strong>.
</div>

--

## Définition récursive

- Un **arbre binaire** c’est :
  - soit un **arbre vide**, noté ∆ ;
  - soit un **triplet** (*e*, *g*, *d*), appelé nœud, avec :
    -  *e* l'étiquette de la racine de l'arbre,
    -  *g* son sous-arbre binaire **gauche**,
    -  *d* son sous-arbre binaire **droit**.
- <!-- .element: class="fragment" -->Définition <strong>récursive</strong> car un arbre binaire est défini par des arbres binaires.
- <!-- .element: class="fragment" -->La première partie de la définition assure l’arrêt et donc la cohérence de la définition.

--

## Pourquoi les arbres binaires ?

Structure pour effectuer des recherches rapides,<br/> ou maintenir efficacement des ensembles triés.

Par exemples, **arbre rouge-noir** :

![arbre rouge-noir](prog/images/arbres/red-black_tree.svg)<!-- .element: class="stretch" style="max-width: 70%;" -->

[Wikimedia Commons](https://commons.wikimedia.org/wiki/File:Red-black_tree_example.svg)<!-- .element: style="font-size: 0.4em;" -->

--

## Pourquoi les arbres binaires ?

Aide à la création de circuits (synthèse logique)<br/> et vérification formelle de programme.

Par exemple, **arbre de décision binaire** :

![arbre rouge-noir](prog/images/arbres/BDD.png)<!-- .element: class="stretch" style="max-width: 50%;" -->

[Wikimedia Commons](https://commons.wikimedia.org/wiki/File:BDD.png)<!-- .element: style="font-size: 0.4em;" -->

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

![arbre1](prog/images/arbres/arbre1.svg)<!-- .element: style="width: 80px;" -->

- taille : 1
- hauteur : 0
- nb feuilles : 1
</div>

<div class='half fragment' style="border-left-style:solid;padding-left:5px">
(3, (1, ∆, (4, (1, ∆, (5, ∆, ∆)), ∆)), ∆)

![arbre2](prog/images/arbres/arbre2.svg)<!-- .element: style="width: 150px;" -->

  - taille : 5
  - hauteur : 4
  - nb feuilles : 1
</div>

--

## Quelques arbres binaires
<!-- .slide: data-transition="fade" -->

<div class='half'>
(3, (1, (1, ∆, ∆), ∆), (4, (5, ∆, ∆), (9, ∆, ∆)))

![arbre3](prog/images/arbres/arbre3.svg)<!-- .element: class="stretch" style="max-width: 70%;" -->

  - taille : 6
  - hauteur : 2
  - nb feuilles : 3
</div>

<div class='half fragment' style="border-left-style:solid;padding-left:5px">
(3, (1, (1, ∆, ∆), (5, ∆, ∆)), (4, (9, ∆, ∆), (2, ∆, ∆)))

![arbre4](prog/images/arbres/arbre4.svg)<!-- .element: class="stretch" style="max-width: 100%;" -->

  - taille : 7
  - hauteur : 2
  - nb feuilles : 4
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

<div class='half fragment' data-fragment-index="1">

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

<div class='half fragment' data-fragment-index="1">

  ![arbre filiforme](prog/images/arbres/complet.svg)<!-- .element: class="stretch" style="max-width: 90%;"-->

</div>

<aside class="notes">
  Suites géométriques de raisons 2
</aside>

--

## Type abstrait ```Arbre Binaire```

1. Constructeurs :

```python
 arbre_vide : () -> Arbre binaire
    # produit l'arbre vide
 noeud : (Etiquette * Arbre binaire * Arbre binaire) -> Arbre binaire
    # à partir d'un étiquette e et des arbres binaires g et d, 
    # produit l'arbre binaire (e, g, d)
```

2. Sélecteurs : <!-- .element: class="fragment" data-fragment-index="1" -->
  
```python
 etiquette : Arbre binaire -> Etiquette
    # à partir de l'arbre binaire (e, g, d), produit l'étiquette e
 gauche : Arbre binaire -> Arbre binaire
    # à partir de l'arbre binaire (e, g, d), produit l'arbre binaire g
 droit : Arbre binaire -> Arbre binaire
    # à partir de l'arbre binaire (e, g, d), produit l'arbre binaire d
```
<!-- .element: class="fragment" data-fragment-index="1" -->

3. Prédicat : <!-- .element: class="fragment" data-fragment-index="2" -->

```python
 est_vide : Arbre binaire -> bool
    # à partir de l'arbre binaire A, produit un booléen 
    # indiquant si A est l'arbre vide
```
<!-- .element: class="fragment" data-fragment-index="2" -->

--

## Mise en oeuvre en <span class="label">Python</span>

Plusieurs implémentations possibles :

1. **Listes de listes** <br/>&#x279E; paradigme fonctionnel

2. **Classe Noeud** <br/>&#x279E; paradigme objet

3. **Liste unique** (méthode d'Eytzinger) <br/>&#x279E; paradigme impératif

--

## Listes de listes

1. Constructeurs : 
 
  ```python 
    def arbre_vide():
      return []

    def noeud(etiquette, gauche, droit):
      return [etiquette, gauche, droit]
  ```

2. Sélecteurs :

  ```python 
    def etiquette(arbre):
      return arbre[0]

    def gauche(arbre):
      return arbre[1]

    def droit(arbre):
      return arbre[2]
  ```

3. Prédicat :

  ```python 
    def est_vide(arbre):
      return arbre == arbre_vide()
  ```

--

## Listes de listes

Exemple d'utilisation :

```python
 
```

--

## Classe Noeud

1. Arbre vide représenté par `None`
2. Nœud représenté par la classe suivante :

  ```python
    class Noeud:
      arbre_vide = None

      def __init__(self, etiquette, gauche, droit):
          self._etiquette = etiquette
          self._gauche = gauche
          self._droit = droit
      
      def etiquette(self):
          return self._etiquette
      
      def gauche(self):
          return self._gauche

      def droit(self):
          return self._droit
      
      @staticmethod
      def est_vide(arbre):
          return arbre is Noeud.arbre_vide
  ```
<!-- .element: class="stretch" -->

--

## Classe Noeud

Exemple d'utilisation :

```python
 
```

--

## Liste unique (méthode d'Eytzinger)

Liste dans laquelle les fils gauche et droit d'un nœud *i* sont rangés respectivement dans les cases 2*i* et 2*i*+1.

![Eytzinger](prog/images/arbres/Eytzinger.svg)<!-- .element: class="stretch" style="max-width: 65%;" -->

Stockage principalement adapté aux **arbres complets**.

--

## Liste unique (méthode d'Eytzinger)

Version simple où la profondeur de l'arbre est fixée *a priori*.

```python
 arbre = [None] * (2**profondeur_max)

 def etiquette(i):
    return arbre[i]

 def gauche(i): 
    return 2 * i + 1
 
 def droit(i): 
    return 2 * i + 2

 def def_racine(etiquette):
    arbre[0] = etiquette

 def def_gauche(etiquette, i):
    arbre[gauche(i)] = etiquette

 def def_droit(etiquette, i):   
    arbre[droit(i)] = etiquette

 def est_vide(i):
    return arbre[i] == -1
```
<!-- .element: class="stretch" -->

--

## Liste unique (méthode d'Eytzinger)

Exemple d'utilisation :

```python
 
```

--

## Exercices en TP

1. Pour chacune des implémentations précédentes, écrire les prédicats suivants :

```python
 est_feuille : Arbre binaire -> bool
    # à partir d'un arbre binaire A, produit un booléen 
    # indiquant si A est une feuille

 taille : Arbre binaire -> int
    # à partir d'un arbre binaire A, produit un entier 
    # indiquant la taille de A

 hauteur : Arbre binaire -> int
    # à partir d'un arbre binaire A, produit un entier 
    # indiquant la hauteur de A
```

2. Représentation visuelle (exemple des expressions arithmétiques)