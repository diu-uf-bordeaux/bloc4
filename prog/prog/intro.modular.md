## Changement de paradigme

Transition avec l'impératif, les procédures, puis les modules.

Programmation structurée

Flot de contrôle

Parler d'architecture quelque part.

--

## Ex. de paradigme : le modulaire

* Brique élémentaire : le **module**

* Idée générale :
  - le code est réparti dans des composants séparés
  - ces modules sont reliés par des liens de dépendance.
  - chaque module peut être remplacé aisément

* Qualités : les dépendances entre modules doivent être **faibles**, les
  dépendances à l'intérieur doivent être **fortes**

* Représentant historique : CLU (1974)

* Exemple actuel : **OCaml** (1996, v4.10 : 2020)

--

Code modulaire : CLU

```clu
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
