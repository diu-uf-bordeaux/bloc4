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

  @staticmethod
  def est_vide(arbre):
    return arbre is Noeud.arbre_vide

  def est_feuille(self):
    return Noeud.est_vide(self.gauche()) and Noeud.est_vide(self.droit())

  def compte_feuille (self):
    if Noeud.est_vide(self):
      return 0
    if self.est_feuille():
      return 1 
    return self.gauche().compte_feuille() + self.droit().compte_feuille()

  def taille (self):
    if Noeud.est_vide(self):
      return 0
    if self.est_feuille():
      return 1 
    return 1 + self.gauche().taille() + self.droit().taille()

  def hauteur (self):
    if Noeud.est_vide(self):
      return -1
    if self.est_feuille():
      return 0
    h1 = 1 + self.gauche().hauteur()
    h2 = 1 + self.droit().hauteur()
    return max(h1,h2)

  @staticmethod
  def represente (arbre, p=0):
    if Noeud.est_vide(arbre):
      print('*')
    else :
        print(arbre.etiquette())
        p += 1
        print('-' * p, end ='')
        Noeud.represente(arbre.gauche())
        print('-' * p, end ='')
        Noeud.represente(arbre.droit())


a = Noeud('a', Noeud.arbre_vide, Noeud.arbre_vide)
b = Noeud('b', Noeud.arbre_vide, Noeud.arbre_vide)
A2 = Noeud('r', a, b)
# print(a.est_feuille())
# print(A2.hauteur())
Noeud.represente(A2)