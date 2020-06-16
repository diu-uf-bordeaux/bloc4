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
  return 1 + taille(gauche(arbre)) + taille(droit(arbre)) 

def hauteur (arbre):
  if est_vide(arbre):
    return -1
  h1 = 1 + hauteur(gauche(arbre))
  h2 = 1 + hauteur(droit(arbre))
  return max(h1,h2)

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

def affiche(expression):
  if est_feuille(expression):
    print(etiquette(expression), end ='')
  else:
    print('(', end ='')
    affiche(gauche(expression))
    print(etiquette(expression), end ='')
    affiche(droit(expression))
    print(')', end ='')

def evalue(expression, valeurs):
    if est_vide(expression): 
        return 0
    if est_feuille(expression):
        v = etiquette(expression)
        if v in valeurs:
          return valeurs[v]
        return v
    a=evalue(gauche(expression), valeurs)
    b=evalue(droit(expression), valeurs)
    o=etiquette(expression)
    if o=='+':
        return a+b
    if o=='*':
        return a*b
    if o=='-':
        return a-b
    if o=='/':
        return a/b

def affichePolonaise(expression):
  if est_feuille(expression):
    print(etiquette(expression), end =' ')
  else:
    affichePolonaise(gauche(expression))
    affichePolonaise(droit(expression))
    print(etiquette(expression), end =' ')

a = noeud('a', arbre_vide(), arbre_vide())
c = noeud('c', arbre_vide(), arbre_vide())
b = noeud('b', c, arbre_vide())
A3 = noeud('r', a, b)
print(compte_feuille(A3))
# represente(A3)

# expression = noeud('+', noeud('*', noeud(6,arbre_vide(),arbre_vide()), noeud('+', noeud('x',arbre_vide(),arbre_vide()), noeud('y',arbre_vide(),arbre_vide()))), noeud('-', noeud('y',arbre_vide(),arbre_vide()), noeud(14,arbre_vide(),arbre_vide())))

# affiche(expression)
# print(evalue(expression, {'x':5,'y':2}))
# affichePolonaise(expression)