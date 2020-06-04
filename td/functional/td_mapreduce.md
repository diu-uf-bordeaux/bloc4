---
layout: page_ext
title: "Map &amp; Reduce"
---

[Retour aux exercices de programmation fonctionnelle](./td_functional.md)

Cette page contient un ensemble d'exemples montrant comment utiliser
des fonctions d'ordre supérieur (des fonctions prenant en paramètre
d'autrs fonction, comme `filter`, `map`, `reduce` &hellip;) pour
manipuler des ensembles de données. La seconde partie montre comment,
dans des conditions où les transformations sont pures (i.e ne font pas
d'effet de bord), le calcul peut être parallèlisé.

### 1ère partie : les fonctions d'ordre supérieur

Un exemple très simple de fonction d'ordre supérieur est la fonction
appelée `map`, qui prend en paramètre une liste $l$ et une fonction
$f$, applique la fonction à tous les éléments de $l$ et renvoie la
liste des résultats&nbsp;:

$$
\begin{cases}
\mathrm{map} : (A \to B, List[A]) & \to List[B] \\
\mathrm{map}(f, [l_1, \dots, l_n]) & = [f(l_1), \dots, f(l_n)]
\end{cases}$$

Cette fonction existe en Python et possède sa propre
[documentation](https://docs.python.org/3/library/functions.html#map),
et en voici un cas d'usage&nbsp;:

```python
>>> numbers = [1, 2, 3, 4, 5]
>>> sqrList = map(lambda x: x*x, numbers)
>>> sqrList
<map object at 0x7fd20e91ad50>
>>> list(sqrList)  # must convert back to list to see contents
[1, 4, 9, 16, 25]
```

Le Python complique un peu les choses, parce qu'il permet de faire les
opérations précédentes en utilisant la syntaxe des compréhensions de
liste&nbsp;:

```python
>>> numbers = [1, 2, 3, 4, 5]
>>> sqrList = [ x*x for x in numbers]
>>> sqrList
[1, 4, 9, 16, 25]
```

Écrire la fonction `map` comme une fonction Python. Écrire la fonction
`filter` qui prend en paramètre une fonction de filtre $f$ et une
liste $l$, et renvoie la liste des éléments de $l$ pour lesquels $f$
renvoie `True`. Écrire la fonction `sum` qui prend en paramètre une
fonction $f$ et une liste $l$, et qui renvoie la somme des $f(l_i)$.

Écrire une fonction `reduce` qui suit la spécification suivante (une
écriture récursive est la manière la plus simple de faire)&nbsp;:

$$
\begin{cases}
\mathrm{reduce} :: ((A,B) \to A), A, List[B]) & \to A \\
\mathrm{reduce}(f, acc, []) & = acc \\
\mathrm{reduce}(f, acc, [l_1,l_2,\dots,l_n]) & = reduce(f, f(acc, l_1), [l_2,\dots,l_n])
\end{cases}
$$

En pratique, cette fonction calcule la chose suivante&nbsp;:

$$ \mathrm{reduce}(f, acc, [l_1,l_2,\dots,l_n]) =  f (\dots (f (f(acc, l_1), l_2) \dots), l_n) $$

Noter que cette fonction existe dans le module `functools` et possède
une
[documentation](https://docs.python.org/fr/3/library/functools.html#functools.reduce).

Réécrire la fonction `sum` à partir de la fonction `reduce`. Écrire à
partir de la fonction `reduce` une fonction `any` qui teste si une
liste de booléens contient un élément valant `True`. <span
class="label">Difficile</span> Utiliser la fonction `reduce` pour
écrire une fonction `reverse` qui prend une liste et renvoie la liste
symétrique.

### 2ème partie : Sagesse de l'Antiquité

Les fonctions évoquées précédemment servent en quelque sorte de
"couteau-suisse" pour effectuer des transformations sur des ensembles
de données. Un usage courant de ces fonctions est la manipulation de
données héritées d'une base de données. Pour simuler la chose ici, on
propose de construire une petite base de données comme la liste
suivante&nbsp;:

```python
[
{ "name": "Thalès", "birth": -625, "death": -547 },
{ "name": "Anaximandre", "birth": -600, "death": -546 },
{ "name": "Héraclite", "birth": -544, "death": -480 },
{ "name": "Empédocle", "birth": -490, "death": -430 },
]
```

[Lien direct](higher.txt)

Utiliser à bon escient les fonctions `map`, `filter`, `sort` et
`reduce` pour effectuer les calculs suivants&nbsp;:

- extraire de cette base la liste des noms dans l'ordre alphabétique;

- extraire de cette base la personne née le plus tôt dans l'ordre chronologique;

- extraire de cette base la personne dont la durée de vie a été la plus longue;

- extraire de cette base la somme de toutes les durées de vies de ces sages.

### 3ème partie <span class="label">Pour aller plus loin ...</span> : questions de parallélisation

Hormis la possibilité de pouvoir manipuler des données, les fonctions
comme `map` permettent de mettre en place du parallélisme de manière
(plus ou moins) automatique. Le module `processing` permet ainsi de
distribuer des calculs sur des ensembles (pools) de processeurs. Par
exemple&nbsp;:

```python
import multiprocessing
import requests

def scrape(url):
    print("Scraping '{}'".format(url))
    res = requests.get(url)
    print("Returned {} ({})".format(res.url, res.status_code))
    return res

def parallel_scrape():
    num_workers = 5
    all_urls = [
		# insert here list of URLs
        ]
    with multiprocessing.Pool(num_workers) as pool:
        results = pool.map(scrape, all_urls)
        print(results)
```

Le choix d'une fonction comme `requests.get` permet d'assurer que les
temps de retours des différents serveurs soient non triviaux et
dépendant de suffisamment de conditions extérieures pour paraître
aléatoires.

Tester le code précedent avec une liste d'URLs choisie avec
délicatesse pour ne pas surcharger les serveurs. Considérer le fait
que la parallélisation ne fonctionne bien uniquement parce que les
fonctions comme `scrape` ne font pas d'effets de bords (i.e leurs
appels sont indépendants).
