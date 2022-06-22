class Cellule:
    liste_vide = None

    def __init__(self, etiquette, liste):
        self._valeur = etiquette
        self._suivant = liste

    # Méthode d'objets
    def valeur(self):
        return self._valeur

    def suite(self):
        return self._suivant

    def taille(self):
        if Cellule.est_vide(self._suivant):
            return 1
    
        return 1 + self._suivant.taille()

    def min(self):
        if Cellule.est_vide(self._suivant):
            return self._valeur
        else:
            prochainMin = self._suivant.min()
            if prochainMin < self._valeur:
                return prochainMin
            else:
                return self._valeur

    def max(self):
        if Cellule.est_vide(self._suivant):
            return self._valeur
        else:
            prochainMax = self._suivant.max()
            if prochainMax < self._valeur:
                return self._valeur
            else:
                return prochainMax

    def _swap(self, cible, nouvelleValeur):
        if self._valeur == cible:
            self._valeur = nouvelleValeur
        else:
            self._suivant._swap(cible, nouvelleValeur)

    def triDecroissant(self):
        maxListe = self.max()

        # Remonter le max en en haut de la liste puis lancer tri sur le reste de la liste
        if self._valeur != maxListe:
            self._swap(maxListe, self._valeur)
            self._valeur = maxListe
        
        if not Cellule.est_vide(self._suivant):
            self._suivant.triDecroissant()

        return self

    def triCroissant(self):
        minListe = self.min()

        # Remonter le min en en haut de la liste puis lancer tri sur le reste de la liste
        if self._valeur != minListe:
            self._swap(minListe, self._valeur)
            self._valeur = minListe
        
        if not Cellule.est_vide(self._suivant):
            self._suivant.triCroissant()

        return self

    def __str__(self):
        if Cellule.est_vide(self._suivant):
            return "[" + str(self._valeur) + "]"
        else:
            return "[" + str(self._valeur) + "]-" + str(self._suivant)

    @staticmethod
    def est_vide(liste):
        return liste is Cellule.liste_vide

    @staticmethod
    def tailleStatic(liste):
        if Cellule.est_vide(liste):
            return 0
        else:
            return liste.taille()

print('== Test taille ==')

L1 = Cellule(3, Cellule(6, Cellule(9, Cellule.liste_vide)))
print('Liste:', L1)
print('Taille:', L1.taille())

print('----')

L1 = Cellule(10, L1)
print('Liste:', L1)
print('Taille:', L1.taille())

print('----')

L1 = Cellule.liste_vide
print('Liste:', L1)
print('Impossible de calculer la taille de la liste vide via la méthode objet: None.taille()')
print('Taille via méthode statique (Cellule.taille(L1)): ', Cellule.tailleStatic(L1))

print('=================')

print('== Test max ==')

L1 = Cellule(3, Cellule(6, Cellule(9, Cellule.liste_vide)))
print('Liste:', L1)
print('Max:', L1.max())

print('----')

L1 = Cellule(10, L1)
print('Liste:', L1)
print('Max:', L1.max())

print('----')

L1 = Cellule.liste_vide
print('Liste:', L1)
print('Impossible de calculer la taille de la liste vide via la méthode objet: None.max()')

print('==============')

print('== Test min ==')

L1 = Cellule(3, Cellule(6, Cellule(9, Cellule.liste_vide)))
print('Liste:', L1)
print('Min:', L1.min())

print('----')

L1 = Cellule(-3, L1)
print('Liste:', L1)
print('Min:', L1.min())

print('----')

L1 = Cellule.liste_vide
print('Liste:', L1)
print('Impossible de calculer la taille de la liste vide via la méthode objet: None.min()')

print('==============')

print('== Test tri decroissant ==')

L1 = Cellule(3, Cellule(6, Cellule(9, Cellule.liste_vide)))
print('Liste:', L1)
print('Résultat:', L1.triDecroissant())

print('==========================')

print('== Test tri croissant ==')

print('Liste:', L1)
print('Résultat:', L1.triCroissant())

print('========================')