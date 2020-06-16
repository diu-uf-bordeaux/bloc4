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