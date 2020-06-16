---
layout: page
title: "Foire aux questions"
permalink: /faq/
---

- [Retour à la page principale](../)

- [Quelle est la différence entre `import ..` et `from .. import` ?](./#quelle-est-la-différence-entre-import--et-from--import-)

- [A quoi servent les annotations de types en Python ?](./#a-quoi-servent-les-annotations-de-types-en-python-)

- [Quelle est la différence entre une méthode d'instance et une méthode de classe ?](./#quelle-est-la-différence-entre-une-méthode-dinstance-et-une-méthode-de-classe-)

- [A quoi sert l'annotation `@staticmethod` pour les méthodes des objets ?](./#a-quoi-sert-lannotation-staticmethod-pour-les-méthodes-des-objets-)

## Questions fréquemment posées

### Quelle est la différence entre `import ..` et `from .. import` ?

Lorsque l'on désire utiliser une fonction `function` d'une
bibliothèque `library` en Python, on utilise en fait une fonction
appelée `__import__`,
([documentation](https://docs.python.org/fr/3/library/functions.html#__import__)). Cette
fonction présente (pour simplifier) deux choix possibles :

1. l'import "classique" : `import library` et sa variante nommée
   `import library as lib`

1. l'import "sélectif" : `from library import function` et

Remarques importantes :

- Aucun des deux n'est préférable à l'autre.

- Dans tous les cas, il faut éviter de faire `from library import *`.

La différence notable entre les deux : l'import classique demande de
*préfixer* les noms des fonctions importées (`library.function`),
alors que l'import sélectif permet de les utiliser directement
(`function`).

Les avantages de l'import "classique" :

- On a accès à toutes les fonctions de `library` (utile quand on
  utilise beaucoup de fonctions, comme pour les bibliothèques `sys`, ou
  `matplotlib`)

- Elles ne se mélangent pas avec les autres fonctions du fichier,
  puisqu'elles sont préfixées.

- Elles sont documentées en partie, du fait du préfixe, on sait de
  quelle bibliothèque `function` provient.

Les désavantages de l'import "classique" :

- Il faut à chaque fois préfixer la fonction par le nom de la
  bibliothèque. C'est simplifié si on fait un import classique nommé
  avec un nom court.

Les avantages d'une solution sont les désavantages de
l'autre. D'autres idées de réponses sont données sur le [lien
suivant](https://stackoverflow.com/questions/710551/use-import-module-or-from-module-import).

### A quoi servent les annotations de types en Python ?

Les annotations de types sont un ajout au langage Python depuis la
version 3.5, et utilisables avec la bibliothèque `typing`
([documentation](https://docs.python.org/3/library/typing.html)). Elles
apparaissent de la façon suivante :

```python
from typing import str

def greeting(name: str) -> str:
    return 'Hello ' + name
```

Remarque importante : l'interpréteur Python *n'effectue pas* de
vérification sur les annotations de types, contrairement à ce que
ferait par exemple un compilateur en `C` ou en `OCaml`.

Les intérêts des annotations de type :

- un intérêt de *documentation* : les fonctions annoncent la forme que
  prennent leurs paramètres et les valeurs renvoyées

- un intérêt de *vérification* : des outils externes (comme par
  exemple [mypy](http://mypy-lang.org/) peuvent vérifier l'usage des
  types et aider le programmeur

- un intérêt d'*optimisation* : des compilateurs comme
  [cython](https://cython.org/) peuvent utiliser les annotations de
  type pour générer du code plus efficace (cf. par exemple ce
  [lien](https://cython.readthedocs.io/en/latest/src/quickstart/cythonize.html))

### Quelle est la différence entre une méthode d'instance et une méthode de classe ?

Rappelons vite que dans un objet, on a deux types de méthodes :

1. les *méthodes d'instance* qui s'appliquent à partir d'une instance
   de la classe. Caractéristique : elles prennent un paramètre
   particulier appelée usuellement `self`.

1. les *méthodes de classe* qui s'appliquent *sans* instance,
   uniquement en précisant le nom de la classe. Caractéristique :
   elles ne prennent pas de paramètre `self`.

Par exemple, dans le code suivant :

```python
class Cellule:
    liste_vide = None

    def __init__(self, etiquette, liste):
        self._valeur = etiquette
        self._suivant = liste

    def longueur(self):
        return 1 if (Cellule.est_vide(self._suivant)) else \
			1 + self._suivant.longueur()

    def est_vide(liste):
        return liste is Cellule.liste_vide
```

La méthode `longueur` est une méthode d'instance. Si on possède une
instance `l` de la classe `Cellule`, on peut appeler la méthode
`longueur` dessus en faisant `l.longueur()`.

La méthode `est_vide` est une méthode de classe. On peut l'appeler
simplement en faisant un `Cellule.est_vide(l)`. sur un objet qui n'est
pas une instance.

La distinction se voit dans l'exemple suivant :


```python
from classe_cellule import Cellule
l = Cellule(1, Cellule(2, Cellule.liste_vide))
l.longueur()        # -> 2
Cellule.est_vide(l) # -> False

l = Cellule.liste_vide
l.longueur()        # Error : 'NoneType' object has no attribute 'longueur'
Cellule.est_vide(l) # -> True
```

`Cellule.liste_vide` n'est pas une instance de la classe, on ne peut
pas appeler la méthode `longueur` dessus. Par contre, mais on peut
appeler la méthode `Cellule.est_vide` dessus.

<a id="annot"/>
### A quoi sert l'annotation `@staticmethod` pour les méthodes des objets ?

Il s'agit d'une décoration Python. Elle permet d'utiliser une méthode
de classe sur une instance de la classe. Dans l'exemple précédent, le
fait de rajouter l'annotation devant le code de `est_vide` permet de
rendre l'appel suivant valide :

```python
l.est_vide(l)
```

Nous déconseillons l'utilisation de cette annotation dans le cadre des
cours d'apprentissage de la programmation, car elle floute la
distinction entre méthode de classe et méthode d'instance.
