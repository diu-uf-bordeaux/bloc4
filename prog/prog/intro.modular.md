## Exemple de paradigme : le modulaire

* Brique élémentaire : le **module**

* Idée générale :
  - le code est réparti dans des composants séparés
  - ces modules sont reliés par des liens de dépendance.
  - chaque module peut être remplacé aisément

* Qualités : les dépendances entre modules doivent être **faibles**, les
  dépendances à l'intérieur doivent être **fortes**

* Représentant historique : CLU (1974)

* Exemple emblématique : **OCaml** (1996, v4.10 : 2020)

--

## Exemple de décomposition modulaire

* Partons du code calculant la suite de Fibonacci.

* Ce code peut être **étendu** de diverses manières :

  - en ajoutant le code d'autres suites connues

  - en ajoutant des tests de validation pour chaque suite

  - en ajoutant un afficheur générique de suites &hellip;

* Considérons une décomposition du code classifiant les objets selon
  leur nature.

--

![Décomposition modulaire](prog/images/intro/modules.svg)<!-- .element: class="stretch" style="max-width: 80%;" -->


--

## Code modulaire : CLU

Module pour les nombres complexes en CLU <!-- .element: class="title" -->

```
complex_number = cluster is add, subtract, multiply, ...
	rep = record [ real_part: real, imag_part: real ]
	add = proc ... end add;
	subtract = proc ... end subtract;
	multiply = proc ... end multiply;
	...
end complex_number;
```

--

## Autres paradigmes

Paradigme logique (cf. logpy)

Paradigme parallèle

Paradigme événementiel
