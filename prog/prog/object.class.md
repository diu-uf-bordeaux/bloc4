## Le Paradigme Objet

~~Qu'est ce qu'un objet ?~~

Comment programmer en objet  ?

~~Architecture Orientée Objet ?~~

--

## Peut-on programmer des objets ?

Le programme crée l'objet

Lui donne ses données

Lui donne ses traitements

$\Rightarrow$ Programmer plusieurs objets : programmer des classes !

--

## La Classe : Définition

Une classe a un **nom** unique dans le programme.

Elle définit les données associées à ses objets: les **propriétés**

Elle définit les traitements des objets: les **méthodes**

$\Rightarrow$ Un objet est instance d'une classe !

--

## Exemple de Classe

nom: Pile

données: liste de caractères

méthodes: empiler, dépiler

$\Rightarrow$ Une pile: p = Pile()

--

## Classe et Encapsulation

(Rappel: l'objet doit encapsuler ses données)

La classe précise les règles d'accès aux champs

**public** : accès total

**private** : accès interdit

--

## Valeurs et Getter / Setter

Affectation à la création

Lecture (get_field)

Écriture (set_field)

--

## Couplage et Classe

Relations entre classes

Durée de vie

Lien avec les traitements

--

## Exemple : UE, Etudiant et Examen

Une UE a deux examens

Un étudiant est inscrit à plusieurs UE

$\Rightarrow$ Calcul de la moyenne pour une UE

--

## Cohérence

Les méthodes **utilisent** les données

Une classe devrait être **insécable**
