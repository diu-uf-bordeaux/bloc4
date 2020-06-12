def creer_graphe(sommets):
  dimension = len(sommets)
  adjacence = [[0 for i in range(dimension)] for j in range(dimension)]
  return (sommets,adjacence)

def ajouter_arete(graphe, s1, s2):
  i = graphe[0].index(s1)
  j = graphe[0].index(s2)
  graphe[1][i][j] = 1
  graphe[1][j][i] = 1 # non-orienté
  return graphe

def sommets(graphe):
  return graphe[0]

def voisins(graphe, sommet):
  i = sommets(graphe).index(sommet)
  return [sommets(graphe)[j] for j in range (len(sommets(graphe))) if graphe[1][i][j]==1]

def degre(graphe, sommet):
  i = sommets(graphe).index(sommet)
  c = 0
  for j in range(len(sommets(graphe))):
    c += graphe[1][i][j]
  return len(voisins(graphe, sommet))

def est_isole(graphe, sommet):
  return degre(graphe, sommet) == 0

def degre_moyen(graphe):
  c = 0
  for s in sommets(graphe):    
        c += degre(graphe,s)
  return c/len(sommets(graphe))

def sont_voisins(graphe, s1, s2):
  i = sommets(graphe).index(s1)
  j = sommets(graphe).index(s2)
  return graphe[1][i][j] == 1

# G = creer_graphe(['a', 'b', 'c', 'd'])
# ajouter_arete(G, 'a', 'b')
# ajouter_arete(G, 'a', 'c')
# ajouter_arete(G, 'c', 'd')
# print(voisins(G, 'c'))
# print(G)
# print(degre(G,'a'))
# print(est_isole(G,'d'))
# print(degre_moyen(G))
# print(sont_voisins(G,'a','b'))