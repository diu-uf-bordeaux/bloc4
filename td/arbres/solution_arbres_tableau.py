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
  if est_vide(i):
    return False
  return est_vide(gauche(i)) and est_vide(droit(i))

def compte_feuille(i):
  if(est_vide(i)):
    return 0
  elif est_feuille(i):
    return 1
  else:
    return compte_feuille(gauche(i)) + compte_feuille(droit(i))

def taille (i):
  if(est_vide(i)):
    return 0
  elif est_feuille(i):
    return 1
  else:
    return 1 + taille(gauche(i)) + taille(droit(i))

def hauteur (i):
  if(est_vide(i)):
    return -1
  elif est_feuille(i):
    return 0
  else:
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

noeud('d',0)
noeud('a',gauche(0))
noeud('b',droit(0))
noeud('c',gauche(droit(0)))

print('== Test est_feuille ==')

print('est_feuille:', est_feuille(1))
print('est_feuille:', est_feuille(2))
print('est_feuille:', est_feuille(0))

print('==============')

print('== Test compte_feuille ==')

print('compte_feuille:', compte_feuille(1))
print('compte_feuille:', compte_feuille(2))
print('compte_feuille:', compte_feuille(0))

print('==============')

print('== Test taille ==')

print('taille:', taille(1))
print('taille:', taille(2))
print('taille:', taille(0))

print('==============')

print('== Test hauteur ==')

print('hauteur:', hauteur(1))
print('hauteur:', hauteur(2))
print('hauteur:', hauteur(0))

print('==============')

print('== Test represente ==')

represente(1)
print()
represente(2)
print()
represente(0)

print('==============')
