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

def est_vide(arbre):
  return arbre == arbre_vide()

def est_feuille(arbre):
  return est_vide(gauche(arbre)) and est_vide(droit(arbre))

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

expression = noeud('+', 
                   noeud('*', 
                         noeud(6,arbre_vide(),arbre_vide()), 
                         noeud('+', 
                              noeud('x',arbre_vide(),arbre_vide()), 
                              noeud('y',arbre_vide(),arbre_vide()))), 
                   noeud('-', 
                         noeud('y',arbre_vide(),arbre_vide()), 
                         noeud(14,arbre_vide(),arbre_vide())))

print('== Test affiche ==')

affiche(expression)

print()
print('==============')

print('== Test evalue ==')

print('Avec x = 5, y = 2:', evalue(expression, {'x': 5, 'y': 2}))

print('==============')

print('== Test affichePolonaise ==')

affichePolonaise(expression)

print()
print('==============')
