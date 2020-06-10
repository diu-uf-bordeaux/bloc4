## Qualités de génie logiciel

Quels sont les objectifs que l'on vise lorsqu'on écrit du code ?

1. des qualités de **fonctionnalité**&nbsp;: le code produit-il les
   comportements attendus ? avec quel degré de certitude ?

2. des qualités d'**évolutivité**&nbsp;: peut-on faire évoluer le code
   dans le temps et ainsi l'ensemble des comportements attendus ?

--

## Qualités de fonctionnalité

### Correction

- Qualité du code consistant à vérifier une spécification :

	* le code réalise t'il les calculs demandés ?

	* le code termine t'il ses calculs sans erreur ?

	* le code utilise t'il une quantité de ressources (temps, mémoire)
      raisonnables ?

- Concepts : fiabilité, sûreté, validation, efficacité &hellip;

- Outils : spécifications, types, tests, modèles logiques &hellip;

--

## Qualités d'évolutivité

### Modularité

- Qualité de découpage du code en composants distincts ayant des
  dépendances réduites entre eux

- Concepts : cohésion, couplage

## Abstraction
<!-- .element: style="margin-top: 5%;" -->

- Qualité d'un composant à n'exposer qu'une interface minimale pour
  interagir avec d'autres composants

- Concepts : encapsulation, distinction public/privé
  &hellip;

--

## Pour quelques qualités de plus&hellip;

- Combinées, les deux dernières propriétés permettent d'envisager de
  nombreuses techniques&nbsp;:

	* construire des composants fortement réutilisables
   (bibliothèques, frameworks &hellip;)

	* construire des composants fortement indépendants

	* remplacer des composants par d'autres proposant la même
      interface (résolution de bugs, améliorations &hellip;)

- Concepts : généricité, réutilisabilité, séparation des
  responsabilités &hellip;
