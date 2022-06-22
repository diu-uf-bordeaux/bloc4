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
  ## ou :
  # return functools.reduce(operator.add, [ degre(graphe,s) for s in S ]) / len(S)
  ## ou encore : 
  return sum([ degre(graphe,s) for s in S ]) / len(S)

def sont_voisins(graphe, s1, s2):
  return s2 in voisins(graphe, s1)

G = creer_graphe(['a', 'b', 'c', 'd', 'e'])
ajouter_arete(G, 'a', 'b')
ajouter_arete(G, 'a', 'c')
ajouter_arete(G, 'c', 'd')
print('G:', G)

print('== Test degre ==')
print('Degre de `a` :', degre(G,'a'))
print('Degre de `b` :', degre(G,'b'))
print('Degre de `c` :', degre(G,'c'))
print('Degre de `d` :', degre(G,'d'))
print('Degre de `e` :', degre(G,'e'))
print('==============')

print('== Test est_isole ==')
print('`a` est isolé :', est_isole(G,'a'))
print('`e` est isolé :', est_isole(G,'e'))
print('==============')

print('== Test degre_moyen ==')
print('Degre moyen de G :', degre_moyen(G))
print('==============')

print('== Test sont_voisins ==')
print('`a` est voisin de `b` :', sont_voisins(G,'a','b'))
print('`a` est voisin de `d` :', sont_voisins(G,'a','d'))
print('==============')