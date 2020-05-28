## Le Paradigme Objet

Qu'est ce qu'un objet ?

Comment programmer en objet  ?

Architecture Orientée Objet ?

--

## Une entité à part entière


* Propose **plusieurs traitements**
* Possède **ses données (son état)**

=> Un objet existe **à l'exécution**

--

## Définition : Objet

1. Une **identité** unique
2. Des **données** propres
3. Des **traitements** dont il est responsable

![Objet](prog/images/object/object.png)<!-- .element: class="stretch" style="max-width: 50%;" -->

--

## Exemple : La Pile de caractères

1. Identité : Pile_1
2. Données : Une liste de caractères (vide au début)
3. Traitements
   1. Empiler un caractère
   2. Dépiler le dernier caractère
   3. Savoir si la pile est vide

--


## Un objet sans identité ?

1. ~~Identité~~
2. Données
3. Traitements

![Objet](prog/images/object/object.png)<!-- .element: class="stretch" style="max-width: 50%;" -->

--

## Un objet sans données ?

1. Identité
2. ~~Données~~
3. Traitements

![Objet](prog/images/object/object.png)<!-- .element: class="stretch" style="max-width: 50%;" -->

--

## Un objet sans traitements ?

1. Identité
2. Données
3. ~~Traitements~~


![Objet](prog/images/object/object.png)<!-- .element: class="stretch" style="max-width: 50%;" -->

--


## Encapsulation

Un objet **protège ses données**

Un objet **peut laisser d'autres objets lire** ses données

Un objet est **le seul à modifier** ses données

![Encapsulation](prog/images/object/objet_encapsulation.png)<!-- .element: class="stretch" style="max-width: 40%;" -->

--

## Responsabilité

Un objet est **responsable des traitements qu'il propose**

Il a donc toutes les données nécessaires et suffisantes

Il peut utiliser (les traitements) d'autres objets

![Encapsulation](prog/images/object/objet_responsable.png)<!-- .element: class="stretch" style="max-width: 40%;" -->

--

## Cohérence

Un objet propose **peu** de traitements

Les traitements **partagent** des données

=> Couper un objet en deux ne devrait pas avoir de sens


--

## Communication

* Les objets communiquent par **échange de messages**
  * Celui qui envoie le message
  * Celui qui reçoit le message


![Objet](prog/images/object/communication.png)<!-- .element: class="stretch" style="max-width: 70%;" -->

--

## Envoyer un message

* Connaître l'identifiant du destinataire
* Préciser quel traitement il demande
* Fournir les paramètres nécessaires au traitement

## Recevoir un message

* Obligation de réponse
* (Envoyeur inconnu)

--

## Synchrone & MonoThread

Un seul object actif

L'objet actif peut envoyer

L'envoyeur n'est plus actif

Le receveur devient actif

L'envoyeur redevient actif avec la réponse


--

## Couplage

Un objet communique avec **peu** d'autres objets

Chaque traitement fait intervenir **peu** d'autres objets

=> Limiter les chaînes et interdir les boucles !

--

## Création d'objet

Tout **objet peut créer des objets** !

L'objet créateur **connaît l'id** de l'objet créé.

Il peut alors **donner les ids** des objets qu'il a créé

--

## Suppression

Avec un **garbage collector** (ramasse-miettes) : les objets
**inaccessibles** sont supprimés

Sans garbage collector : les objets doivent **se supprimer**

--

## Application OO

Plusieurs objets qui communiquent

Certains objets communiquent avec l'extérieur

=> Une configuration initiale

--

## Conception Objet

Quels objets ?

Quelles cohérence ?

Quels couplage ?

Quelle dynamicité ?

--

## Le Paradigme Objet

~~Qu'est ce qu'un objet ?~~

Comment programmer en objet  ?

Architecture Orientée Objet ?

--

## Programmer des objets

Créer l'objet

Lui donner ses données

Lui donner ses traitements

--

## La Classe

Nom

Définition des données

Définition des traitements

--

## Exemple de Classe

Pile

liste de caractères

empiler, dépiler

--

## Classe et Encapsulation

L'objet doit encapsuler ses données

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

=> Calcul de la moyenne pour une UE

--

## Coherence

Les méthodes **utilisent** les données

Une classe devrait être **insécable**

--

## Le Paradigme Objet

~~Qu'est ce qu'un objet ?~~

~~Comment programmer en objet  ?~~

Architecture Orientée Objet ?

--

## Objectifs

Améliorer la maintenance

Améliorer la performance

Améliorer la sécurité

...

--

## Reuse

**Réutiliser** du code

Coder pour être **réutilisé**

=> Héritage / Interface

--

## Héritage

Une classe hérite d'une autre classe

Les objets sont au moins conformes

=> Ajouter des champs et des méthodes

--

## Quand hériter ?

Réduire la redondance

Étendre une classe

Faire un template

--

## Surcharge et Polymorphisme

Ajouter des paramètres aux méthodes

Changer le body des méthodes

--

## L'interface

Définition d'un contrat d'usage

Limite la dépendance de l'utilisateur

=> Contrat appelant / appelé

--

## Quand passer par une interface

Masquer l'implémentation

Inverser la dépendance


--

## Le Paradigme Objet

Qu'est ce qu'un objet ?

Comment programmer en objet  ?

Architecture Orientée Objet ?

--

## Conclusion

Pensez Object (id, données, traitement)

Coder les classes

Améliorer la conception
