import graphe_listes as gl
import graphe_matrice as gm

def gl2gm(graphe_listes):
  graphe_matrice = gm.creer_graphe(gl.sommets(graphe_listes))
  for s1 in gl.sommets(graphe_listes):
    for s2 in gl.voisins(graphe_listes, s1):
      gm.ajouter_arete(graphe_matrice, s1, s2)
  return graphe_matrice

def gm2gl(graphe_matrice):
  graphe_listes = gl.creer_graphe(gm.sommets(graphe_matrice))
  for s1 in gm.sommets(graphe_matrice):
    print(gm.voisins(graphe_matrice, s1))
    for s2 in gm.voisins(graphe_matrice, s1):
      gl.ajouter_arete(graphe_listes, s1, s2)
  return graphe_listes

G_listes = gl.creer_graphe(['a', 'b', 'c', 'd'])
gl.ajouter_arete(G_listes, 'a', 'b')
gl.ajouter_arete(G_listes, 'a', 'c')
gl.ajouter_arete(G_listes, 'c', 'd')
print(G_listes)
G_matrice = gl2gm(G_listes)
print(G_matrice)
print(gm2gl(G_matrice))