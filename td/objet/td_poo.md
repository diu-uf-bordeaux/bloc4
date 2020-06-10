---
layout: page_ext
title: "Exercices sur les objet"
permalink: /td/poo/
---

[Retour à l'ensemble des exercices](../)

L'objectif est de concevoir des applications en commençant par
identifier les différents objets qui la composent, puis en programmant
leurs classes.

### 1 - Le blackjack

L'application que nous souhaitons développer est celle d'une table de
blackjack. Nous considérons des règles très simples&nbsp;:

- Un donneur distribue des cartes (un paquet de 52 cartes sans les
jokers) aux joueurs, à la hauteur d'une carte par joueur et par tour.

- Le donneur incarne un joueur particulier : la banque.

- A la fin d'un tour, si la somme des valeurs des cartes d'un joueur
dépasse 21, le joueur est éliminé (on considère que les têtes et l'as
valent 10 points, les autres valeurs correspondent à la hauteur de la
carte).

- À la fin d'un tour, si un joueur n'est pas éliminé, il peut décider
de ne plus recevoir de carte. Le donneur ne lui en donnera pas le tour
suivant.

- Si la banque perd, tous les joueurs non éliminés gagnent (on
comptera un point par gain).

- S'il ne reste plus de joueur engagé dans la partie (soit ils sont
éliminés soit ils ont décidé de ne plus recevoir de carte), alors le
joueur dont la somme des valeurs de ses cartes est la plus proche de
21 gagne.

On imagine, qu'il est possible de jouer à plusieurs joueurs (5 au max,
mais a priori 2 pour les besoins de cet exercice).

<span class="label">Vous pouvez adapter ces règles</span>

On ne se soucie pas des aspects d'interface graphique (affichage,
interaction avec les personnes, etc.). L'objectif ici est de concevoir
la partie interne du jeu (définir les objets)

Pour vous aider, voici les données que ceux-ci devront se partager :

* La liste des joueurs
* Le jeu de cartes à distribuer
* Les mains de chaque joueur
* Les scores de chaque joueur

Et voici les traitements qui devront être réalisés:

* démarrer une nouvelle partie
* mélanger le jeu de carte
* donner une carte à un joueur
* calculer la valeur d'une main
* vérifier que la valeur d'une main n'est pas au dessus de 21
* préciser qu'un joueur ne veut plus recevoir de cartes ou confirmer qu'il veut bien recevoir des cartes
* compter le nombre de joueurs engagés et, si personne n'est engagé, calculer qui est le gagnant

1. Une conception qui consisterait à ne faire qu'un seul objet ne serait pas cohérente. Est-il possible de couper en deux types d'objets : donneur et joueurs ? Précisez les données et les traitements pour chaque objet.

2. Expliquez les relations (échange de message) entre ces objets. Déroulez une partie avec deux joueurs. Vous pouvez alors montrer quels messages sont échangés et comment les objets (leurs données) évoluent.

3. Développez la classe `Joueur`

4. Développez la classe `Donneur`

5. Développez un main (script montrant le déroulement d'une application avec deux joueurs)


### 2 - Dessin Vectoriel

Une application que nous souhaitons développer est celle d'un outil de
dessin vectoriel. Nous considérons qu'il est possible de créer un
nouveau dessin vierge. Ensuite, il est possible d'ajouter des formes
vectorielles à ce dessin: des points, des droites, des carrés, des
rectangles et des cercles. Une fois les formes créées, il est possible
de les modifier, de les déplacer et de les supprimer. Enfin, il est
possible de sauvegarder le dessin dans un fichier au [format
`SVG`](https://fr.wikipedia.org/wiki/Scalable_Vector_Graphics) pour
qu'il soit affichable dans un navigateur web.

1. Proposez une conception à l'aide d'objets. Vous préciserez alors
   quels sont les objets qui composent cette application.

2. Proposez un script qui construit un dessin avec deux droites et
   deux carrés puis qui supprime le deuxième carré.

3. Développez la classe `Dessin`

4. Développez plusieurs classes représentant des formes graphiques en
   exploitant l'héritage.


### 3 - Aller plus loin

1. Proposez un mécanisme permettant la sauvegarde d'un dessin
   vectoriel sous forme d'un fichier `SVG`.

2. Faites en sorte que le code de sauvegarde dépende du code métier et
   pas l'inverse.
