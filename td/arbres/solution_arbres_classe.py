class Noeud:
  arbre_vide = None

  def __init__(self, etiquette, gauche, droit):
    self._etiquette = etiquette
    self._gauche = gauche
    self._droit = droit

  def etiquette(self):
    return self._etiquette

  def gauche(self):
    return self._gauche

  def droit(self):
    return self._droit

  def est_vide(arbre):
    return arbre is Noeud.arbre_vide

  def est_feuille(self):
    if Noeud.est_vide(self):
      return False
    return Noeud.est_vide(self.gauche()) and Noeud.est_vide(self.droit())

  def compte_feuille (self):
    if self.est_feuille():
      return 1
    n = 0
    if not Noeud.est_vide(self.gauche()):
      n += self.gauche().compte_feuille()
    if not Noeud.est_vide(self.droit()):
      n += self.droit().compte_feuille()
    return n

  def taille (self):
    if self.est_feuille():
      return 1
    n = 1
    if not Noeud.est_vide(self.gauche()):
      n += self.gauche().taille()
    if not Noeud.est_vide(self.droit()):
      n += self.droit().taille()
    return n

  def hauteur (self):
    if self.est_feuille():
      return 0
    h1 = 0
    h2 = 0
    if not Noeud.est_vide(self.gauche()):
      h1 = 1 + self.gauche().hauteur()
    if not Noeud.est_vide(self.droit()):
      h2 = 1 + self.droit().hauteur()
    return max(h1,h2)

  def represente (arbre, p=0):
    if Noeud.est_vide(arbre):
      print('*')
    else :
        print(arbre.etiquette())
        p += 1
        print('-' * p, end ='')
        Noeud.represente(arbre.gauche(),p)
        print('-' * p, end ='')
        Noeud.represente(arbre.droit(),p)


a = Noeud('a', Noeud.arbre_vide, Noeud.arbre_vide)
c = Noeud('c', Noeud.arbre_vide, Noeud.arbre_vide)
b = Noeud('b', Noeud.arbre_vide, c)
d = Noeud('d', a, b)

print('== Test est_feuille ==')

print('est_feuille:', a.est_feuille())
print('est_feuille:', b.est_feuille())
print('est_feuille:', d.est_feuille())

print('==============')

print('== Test compte_feuille ==')

print('compte_feuille:', a.compte_feuille())
print('compte_feuille:', b.compte_feuille())
print('compte_feuille:', d.compte_feuille())

print('==============')

print('== Test taille ==')

print('taille:', a.taille())
print('taille:', b.taille())
print('taille:', d.taille())

print('==============')

print('== Test hauteur ==')

print('hauteur:', a.hauteur())
print('hauteur:', b.hauteur())
print('hauteur:', d.hauteur())

print('==============')

print('== Test represente ==')

a.represente()
print()
b.represente()
print()
d.represente()

print('==============')