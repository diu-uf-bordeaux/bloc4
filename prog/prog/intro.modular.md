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
