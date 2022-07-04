def arbre_vide():
  return []

def noeud(etiquette, gauche, droit):
  return [etiquette,gauche,droit]

def etiquette(arbre):
  return arbre[0]

def gauche(arbre):
  return arbre[1]

def droit(arbre):
  return arbre[2]

def est_vide(arbre):
  return arbre == arbre_vide()

def est_feuille(arbre):
  if est_vide(arbre):
    return False
  return est_vide(gauche(arbre)) and est_vide(droit(arbre))

def compte_feuille (arbre):
  if est_vide(arbre):
    return 0
  if est_feuille(arbre):
    return 1
  return compte_feuille(gauche(arbre)) + compte_feuille(droit(arbre))

def taille (arbre):
  if est_vide(arbre):
    return 0
  else:
    return 1 + taille(gauche(arbre)) + taille(droit(arbre))

def hauteur (arbre):
  if est_vide(arbre):
    return -1
  else:
    h1 = hauteur(gauche(arbre))
    h2 = hauteur(droit(arbre))
    return 1 + max(h1,h2)

def represente(arbre, p = 0) :
  if est_vide(arbre):
    print('*')
  else:
    print(etiquette(arbre))
    p += 1
    print('-' * p, end ='')
    represente(gauche(arbre), p)
    print('-' * p, end ='')
    represente(droit(arbre), p)

a = noeud('a', arbre_vide(), arbre_vide())
c = noeud('c', arbre_vide(), arbre_vide())
b = noeud('b', c, arbre_vide())
d = noeud('d', a, b)

print('== Test est_feuille ==')

print('est_feuille:', est_feuille(a))
print('est_feuille:', est_feuille(b))
print('est_feuille:', est_feuille(d))

print('==============')

print('== Test compte_feuille ==')

print('compte_feuille:', compte_feuille(a))
print('compte_feuille:', compte_feuille(b))
print('compte_feuille:', compte_feuille(d))

print('==============')

print('== Test taille ==')

print('taille:', taille(a))
print('taille:', taille(b))
print('taille:', taille(d))

print('==============')

print('== Test hauteur ==')

print('hauteur:', hauteur(a))
print('hauteur:', hauteur(b))
print('hauteur:', hauteur(d))

print('==============')

print('== Test represente ==')

represente(a)
print()
represente(b)
print()
represente(d)

print('==============')
