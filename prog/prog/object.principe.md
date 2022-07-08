## Le Paradigme Objet

- Brique élémentaire : l'**objet** qui répond à des **messages**

- Idée générale :

	* un objet est une entité rassemblant des données et les traitements sur ces données;

	* les objets échangent entre eux à travers des messages;

	* la décomposition en objets/classes structure le code.

* Représentants historiques : **Simula** (1967), **Smalltalk** (1971)

* Exemple emblématique : **Java** (1996, Java SE 18 date de 2022)

Note:
On peut citer C++, python, javascript, ...

--

## Qu'est ce qu'un objet ?

Une entité à part entière :

- Possède une **identité** unique\
  (`id()`, opérateur `is`)
- A des données propres  (`vars`) \
  appelées **attributs** (des fois _propriétés_, ou _champs_)
- Propose des traitements (`dir()`) \
  appelés **méthodes**

> Un objet existe **à l'exécution**

--

## Encapsulation

- Un objet **protège ses données**

  - Un objet est **le seul à modifier** ses données (dans l'idéal)
  - Un objet **peut laisser d'autres objets lire** ses données (cf. visibilité)

- Un object **expose des traitements** dont il est responsable
   - Il a donc toutes les données nécessaires et suffisantes
   - Il peut utiliser (les traitements) d'autres objets

--

## Envoi de message

- Les objets communiquent par **échange de messages**

- Celui qui envoie le message doit:
  * Connaître l'identifiant du destinataire
  * Préciser quel traitement il demande
  * Fournir les paramètres nécessaires au traitement

- Celui qui reçoit le message (**receveur**)
  * Obligation de réponse
  * (Envoyeur inconnu)

```
  print(mon_texte.capitalize())
```

--

## Création d'objet

Tout objet peut créer des objets, c'est l'**instanciation** (ou la construction)

- Le créateur **connaît l'id** de l'objet créé
- Il peut donc envoyer des messages à cet objet
- et peut aussi éventuellement publier son identité

La suppression d'un objet peut être:

- manuelle, par exemple en C++ (ce n'est pas `del` en Python)
- automatique par utilisation de ramasse-miettes (_garbage collector_)

---

## Les langages à classes

Dérivé de la tradition aristotélicienne, on regroupe les objets en classes,
possédant des propriétés communes :

> Socrate est homme, les hommes sont mortels, socrate est mortel.

- Socrate est un **instance** de la **classe** des _hommes_.
- _Mortel_ est une propriété (appartient à l'_extension_) de la classe _homme_.
- Socrate hérite de l'union des extensions de sa.es classe.s

--

### La classe

- La classe est un élément statique qui nous aide à structurer le programme,
- l'objet est l'élément dynamique, celui qui est présent en mémoire lors de l'exécution.

En python, une classe défini les **méthodes** qui seront invoqués (appelées) à
la réception d'un message.

Le premier paramètre est le receveur, par convention `self` (`this` en JavaScript)

Note:
La classe n'est pas centrale au modèle objet, cf. les prototypes en
JavaScript.

--


### Instanciation d'un objet

- allocation : préparation de la mémoire
- initialisation : appel au constructeur (`__init__`)

> Exemples : `list()`, `int("10", 2)`, `date(1789, 7, 14)`

Remarque: A la fin de la vie d'un objet, il est détruit avec `__del__`; que
vous ne contrôlez pas.

--

## Ma première classe
### Une Pile quelconque

- Données
  - Une liste
- Traitements
  - Empiler un élément
  - Dépiler le dernier élément
  - Savoir si la pile est vide

--

<div class='half'>

### Définition d'une classe

```
class Stack:

  def __init__(self):
    self.values = []

  def push(self, value):
    self.values.append(value)

  def pop(self):
    return self.values.pop()

  def is_empty(self):
    return len(self.values) == 0
```

</div>
<div class='half'>

### Utilisation de cette classe

```
some_stack = Stack()

print(stack.is_empty())
stack.push("World")
stack.push("Hello")
print(stack.is_empty())

print(stack.pop())
print(stack.pop())
```

</div>

--

### La spécialisation

Une classe peut **spécialiser** une autre classe (appelé **super-classe**).

- Elle hérite des propriétés de sa.es super-classe.s
- Elle peut redéfinir des propriétés
- Elle peut introduire de nouvelles propriétés

A l'exécution, l'objet répond a un message en sélectionnant :
- la propriété (méthode) la plus spécifique.

C'est aussi un moyen de factoriser du code.

--

### Mise en œuvre su syllogisme

<div class='half'>

```
class Mortal():
    def __init__(self):
        self.is_alive = True

    def die(self):
        self.is_alive = False

    def is_alive(self):
      return self.is_alive

```

</div>
<div class='half'>

```
class Human(Mortal):
  pass

class Greek(Human):
  pass
```

</div>

```
socrate = Greek()
socrate.die()
print(socrate.is_alive())
```

--

## Redéfinition

- Ajout du chant du signe aux humains (`final_blow`), i.e., annonce sa mort dans sa langue

```
class Human:

  def die(self):
    self.is_alive = false
    self.final_blow()

  def final_blow(self):
    pass

class Greek(Human):
  def final_blow(self):
    print(f"Πεθαίνω ! ({self})")

class French(Human):
  def final_blow(self):
    print(f"Je meurs ! ({self})")
```

--

### Appel à une super méthode

> `super(klass, self)`

ou `klass` est la classe courante.

peut s'abrége rdans les cas simples par

> `super()`

- Exercice: Création de la classe `Cat` qui a neuf vies

--

## Les exceptions

Sont des objets particuliers, ils spécialisent la classe `Exception`, qui peuvent être **levés** (`raise`).

Ces objets sont **rattrapées** par des blocs particuliers (`try:`, `execpt Exception:`, `finally:`).
- Lorsqu'une exception est levée, la pile d'exécution est déroulée jusqu'au premier bloc `except` qui déclare un sous-type compatible avec l'exception.
- les blocs `finally` sont appelés inconditionnellement, qu'il y ai eu exception, ou pas.

```
class AlreadyDeadException(Exception):
    pass
```

> Exercice: Lever l'exception AlreadyDeadException si le mortel est déjà mort.

--

### Identité vs Égalité

- Ne faut pas confondre l'identité (`is`), est-ce le même objet
- avec l'égalité (`==`), l'envoi du message `__eq__` à un objet

```
[] == []            ### True
[] is []            ### False

Stack() is Stack()  ### False
Stack() == Stack()  ### False
```

pour que le dernier cas soit vrai, il faudrait définir la méthode `__eq__`

```
def __eq__(self, other):
  return other isinstance Stack and self.values == other.values
```

--

## Conseils

Bien programmer en objet est dur (cf. la littérature)

- Couplage faible/Cohérence forte
- S.O.L.I.D.
- Design Pattern, elements of reuse (GoF)
- Évitez l'_over-engineering_
- D.R.Y. (*Dont Répeat Yourself*)
  - Copier/Coller c'est mal, le couper/coller c'est bien !

--

### Quand spécialiser/hériter ?

- Réduire la redondance de son code
- Étendre une classe pour la réutiliser
- Faire un _template_ pour un autre développeur

### Comment spécialiser

- B est il sous-classe de A
- A est il sous-classe de B
- A et B, sont sous-classe d'un ancêtre commun C

> Si vous hésitez vraiment trop, la dernière solution est probablement la bonne

--

### SOLID

- Single responsability principle (SRP)
- Open/Closed
  - Définissez clairement les interfaces et les `@abstractmethod`
- (L) Substituabilité
  - Évitez de récupérer du code pour récupérer du code.
- (I) Ségrégation des interfaces
  - Évitez les _god_classes, minimisez le couplage.
- (D) Inversion des Dépendances
  - Utilisez des types abstraits

--

### Couplage

Un objet communique avec **peu** d'autres objets

Chaque traitement fait intervenir **peu** d'autres objets

$\Rightarrow$ Limiter les chaînes et interdir les boucles !

### Cohérence

Un objet propose peu de traitements (liés entre eux)

Les traitements partagent des données

$\Rightarrow$ Couper un objet en deux ne devrait pas avoir de sens

---

## Application OO

Plusieurs objets qui communiquent

Certains objets communiquent avec l'extérieur

$\Rightarrow$ Une configuration initiale

--

## Conception Objet

Quels objets ?

Quelles cohérence ?

Quels couplage ?

Quelle dynamicité ?

--


## Un objet sans identité ?

1. ~~Identité~~
2. Données
3. Traitements

![Objet](prog/images/object/object.png)<!-- .element: class="stretch" style="max-width: 50%;" -->

C'est possible, objet **autonome** et **anonyme**

--

## Un objet sans données ?

1. Identité
2. ~~Données~~
3. Traitements

![Objet](prog/images/object/object.png)<!-- .element: class="stretch" style="max-width: 50%;" -->

C'est possible, objet **stateless** (sans état)

--

## Un objet sans traitements ?

1. Identité
2. Données
3. ~~Traitements~~

![Objet](prog/images/object/object.png)<!-- .element: class="stretch" style="max-width: 50%;" -->

Plus rare (**objet données**), pas très cohérent avec le modèle.

--

## Couplage

Un objet communique avec **peu** d'autres objets

Chaque traitement fait intervenir **peu** d'autres objets

$\Rightarrow$ Limiter les chaînes et interdir les boucles !


--


## Cohérence

Un objet propose **peu** de traitements (liés entre eux)

Les traitements **partagent** des données

$\Rightarrow$ Couper un objet en deux ne devrait pas avoir de sens


