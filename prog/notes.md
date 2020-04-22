# Bloc 4

## Programmation Avancée

[https://sourcesup.renater.fr/www/diu-eil/medias/diu-eil-habilit-2-ppn.pdf](PDF de l'etudiant.fr)

[https://wiki.inria.fr/wikis/sciencinfolycee/images/a/a7/Informatique_et_Sciences_du_Num%25C3%25A9rique_-_Sp%25C3%25A9cialit%25C3%25A9_ISN_en_Terminale_S._version_Python.pdf](Informatique et Sciences du Numérique) par G. Dowek et. al.

## Liste de paradigmes de programmation

- Programmation modulaire      (en +)
- Programmation impérative
- Programmation fonctionnelle
- Programmation objet
- Programmation événementielle (js)
- Programmation parallèle
- Programmation logique

## Liste de structures de données

- Notion de structure de données abstraite
- Listes, piles, files
- Arbres binaires, arbres binaires de recherche
- Graphes (networkx ?)
- Choix d'une structure de données

## Mutabilité

- Programmation fonctionnelle pure
- DDD (value object (immutable))

## Idée : gérer paradigmes et structures de données à double entrée

- pb : certaines cases seront certainement difficiles à gérer
- ex : graphes + prog événementielle ?
- ex : listes + prog parallèle ?
- pb : tous les paradigmes n'ont pas la même granularité (impératif <
  fonctionnel < objet)
- pb : la plupart des paradigmes n'ont pas vraiment de granularité
  pour organiser des TADs (impératif, logique, parallèle,
  événementiel)
- idée : parler de programmation modulaire

Problème de l'extension

## Exercices

Trouver des exercices et des bibliothèques Python pour chaque
paradigme.

- Logic :
  * Pyke (http://pyke.sourceforge.net/, https://github.com/mayask/pyke)

	Vieux, dernier commits datent de 10ans, ne compile pas en Python 3

  * Logpy/Kanren (https://github.com/logpy/logpy)

    Apparemment, il s'agit du portage d'une lib Java/Clojure en
    Python.  Contient un exemple "famille-liens-père-mère", un exemple
    "géometrie-états-d'amérique"

  * Tutoriel sur l'utilisation de Kanren :
  https://www.tutorialspoint.com/artificial_intelligence_with_python/artificial_intelligence_with_python_logic_programming.htm

	Contient un exemple avec un jeu logique où l'allemand fume des
    Marlboro avec son lama.

  * La doc est pas géniale, elle a tendance à se référer à la doc de
    la bibliothèque originale en Clojure. A la limite, on trouve
    cela : https://github.com/logpy/logpy/blob/master/doc/basic.md


- Parallel : la question se pose de quoi présenter. Les threads, les
  process, les mémoires partagées, les envois de message, peut-être le
  plus important c'est l'asynchronisme.

  * multiprocessing (https://docs.python.org/3/library/multiprocessing.html)

	Bibliothèque avec des process, et des pipes pour la communication
    des objets. Parallèlisme multi-processeur.  Existe des
    implémentations raisonnablement simples de map-reduce.

  * threading (https://docs.python.org/3/library/threading.html)

    Bibliothèque avec des threads (même espace mémoire, comparé aux
    processus). Sensible au GIL (global interpreter lock), et donc
    limité au mono-processeur.

  * asyncio (https://docs.python.org/fr/3/library/asyncio.html)

	Bibliothèque avec des async et des await, pour faire des coroutines.

  * exercice comparant les 3 différentes bibliothèques précédentes sur
    un même exemple (https://realpython.com/python-concurrency/)

  * exemples : méthodes numériques d'intégration avec parallèlisme


## Fonctionnement

- pas de présentiel
- synchro
- moodle
- first-class citizenship
