import functools
import operator

def creer_graphe(sommets):
  return {key: [] for key in sommets}

def ajouter_arete (graphe, x, y):
  if x in graphe and y in graphe:
    graphe[x].append(y)
    graphe[y].append(x) # non-orienté

def sommets(graphe):
  return list(graphe.keys())

def voisins(graphe, sommet):
  return list(graphe[sommet])

def degre(graphe, sommet):
  return len(voisins(graphe, sommet))
  
def est_isole(graphe, sommet):
  return degre(graphe, sommet) == 0

def degre_moyen(graphe):
  S = sommets(graphe)
  # c = 0
  # for s in S:
  #   c += degre(graphe, s)
  # return c / len(S)
  return functools.reduce(operator.add, [ degre(graphe,s) for s in S ]) / len(S)

def sont_voisins(graphe, s1, s2):
  return s2 in voisins(graphe, s1)

G = creer_graphe(['a', 'b', 'c', 'd'])
ajouter_arete(G, 'a', 'b')
ajouter_arete(G, 'a', 'c')
ajouter_arete(G, 'c', 'd')
print(G)
print(voisins(G, 'c'))
print(degre(G,'c'))
print(est_isole(G,'d'))
print(degre_moyen(G))
print(sont_voisins(G,'a','b'))