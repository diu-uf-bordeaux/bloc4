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
