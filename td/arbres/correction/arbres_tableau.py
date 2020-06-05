profondeur_max = 3

def arbre_vide():
  return None

arbre = [arbre_vide()] * (2**(profondeur_max+1)-1)

def noeud(etiquette,i):
  arbre[i] = etiquette

def etiquette(i):
  return arbre[i]

def gauche(i):
  return 2*i+1

def droit(i):
  return 2*i+2

def est_vide(i):
  return arbre[i] == arbre_vide()

def est_feuille(i):
  return est_vide(gauche(i)) and est_vide(droit(i))

def compte_feuille(i):
  if(est_vide(i)):
    return 0
  if est_feuille(i):
    return 1 
  return compte_feuille(gauche(i)) + compte_feuille(droit(i))

def taille (i):
  if(est_vide(i)):
    return 0
  if est_feuille(i):
    return 1 
  return 1 + taille(gauche(i)) + taille(droit(i)) 

def hauteur (i):
  if(est_vide(i)):
    return -1
  if est_feuille(i):
    return 0
  h1 = 1 + hauteur(gauche(i))
  h2 = 1 + hauteur(droit(i))
  return max(h1,h2)

def represente(i, p = 0) :
  if est_vide(i): 
    print('*')
  else:
    print(etiquette(i))
    p += 1
    print('-' * p, end ='')
    represente(gauche(i), p)
    print('-' * p, end ='')
    represente(droit(i), p)

noeud('r',0)
noeud('a',gauche(0))
noeud('b',droit(0))
noeud('c',gauche(droit(0)))
# print(etiquette(gauche(droit(0))))
# print(est_feuille(gauche(droit(0))))
# print(hauteur(1))
represente(0)