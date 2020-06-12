import functools
import operator

def creer_graphe(sommets):
  return {key: [] for key in sommets}

def ajouter_arete (graphe, x, y):
  if x in graphe and y in graphe:
    if not y in graphe[x]:
      graphe[x].append(y)
    if not x in graphe[y]:
      graphe[y].append(x) # non-orienté

def sommets(graphe):
  return list(graphe.keys())

def voisins(graphe, sommet):
  return list(graphe[sommet])
