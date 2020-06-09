---
layout: page_ext
title: "Réflexion sur les objets"
permalink: /td/poo/objet/
---

[Retour aux exercices sur la programmation orientée objet](../)

L'objectif de cet exercice est de concevoir une application en identifiant les différents objets qui la composent. La programmation de cette application (avec des classes) se fera par la suite.

### Le blackjack

L'application que nous souhaitons développer est celle d'une table de blackjack. Nous considérons des règles très simples. Le donneur distribue des cartes (un paquer de 52 cartes sans les joker) aux joueurs (une carte par joueur et par tour). A la fin d'un tour, si la somme des valeurs des cartes d'un joueur dépasse 21, le joueur est éliminé (on considère que les têtes et l'as valent 10 points, les autres valeurs correspondent à la hauteur de la carte).
Toujours à la fin d'un tour, si un joueur n'est pas éliminé, il peut décider de ne plus recevoir de carte. Le donneur ne lui en donnera pas le tour suivant.
On considère que le donneur incarne un joueur particulier: la banque.

Si la banque perd, tous les joueurs non éliminés gagnent (on comptera un point par gain).
S'il ne reste plus de joueur engagé dans la partie (soit ils sont éliminés soit ils ont décidé de ne plus recevoir de carte), alors le joueur dont la somme des valeurs de ses cartes est la plus proche de 21 gagne.

On imagine, qu'il est possible de jouer à plusieurs joueurs (5 au max).

__vous pouvez adapter ces règles__

### Conception 

On ne se soucie pas des aspects d'interface graphique (affichage, interaction avec les personnes, etc.).
L'objectif est de concevoir la partie interne du jeu (définir les objets)

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


2. Expliquer les relations (échange de message) entre ces objets ?

Déroulez une partie avec deux joueurs. Vous pouvez alors montrer quels messages sont échangés et comment les objets (leurs données) évoluent.

