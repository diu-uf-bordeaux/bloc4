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

    def calcul(self, x):
        if Cellule.est_vide(self._suivant):
            return self._valeur
        else:
            return self._valeur * (x ** (self.taille() - 1)) + self._suivant.calcul(x)

    def _setSuivant(self, liste):
        self._suivant = liste

    def add(self, liste):

        if self.taille() > liste.taille():
            self._suivant.add(liste)
        elif self.taille() < liste.taille():
            # Probleme incoming
            # Nous sommes obligés de créer un nouvel objet en amont de celui-ci
            nouveau = Cellule(liste.valeur(), Cellule.liste_vide)
            
            nouveau._setSuivant(
                self.add(liste.suite())
            )

            return nouveau
        else:
            self._valeur += liste.valeur()
            if not Cellule.est_vide(self._suivant):
                self._suivant.add(liste.suite())

        return self

    def sub(self, liste):
        if self.taille() > liste.taille():
            self._suivant.sub(liste)
        elif self.taille() < liste.taille():
            # Probleme incoming
            # Nous sommes obligés de créer un nouvel objet en amont de celui-ci
            nouveau = Cellule(-liste.valeur(), Cellule.liste_vide)
            
            nouveau._setSuivant(
                self.sub(liste.suite())
            )

            return nouveau
        else:
            self._valeur -= liste.valeur()
            if not Cellule.est_vide(self._suivant):
                self._suivant.sub(liste.suite())

        return self

    def __str__(self):
        if Cellule.est_vide(self._suivant):
            return "[" + str(self._valeur) + "]"
        else:
            return "[" + str(self._valeur) + "]-" + str(self._suivant)

    # Méthodes de classe
    @staticmethod
    def est_vide(liste):
        return liste is Cellule.liste_vide

#### VALEUR ####

print('== Test valeur polynome ==')

L1 = Cellule(3, Cellule(0, Cellule(1, Cellule(6, Cellule.liste_vide))))
print('Liste:', L1)

for x in [2, 4, 6]:
    print('Valeur pour x =', x, ':', L1.calcul(x))

print('=================')

################

#### ADDITION ####

L1 = Cellule(3, Cellule(0, Cellule(1, Cellule(6, Cellule.liste_vide))))
L2 = Cellule(9, Cellule(5, Cellule.liste_vide))

print('== Test addition polynome ==')

print('Polynome 1:', L1)
print('Polynome 2:', L2)

print('Polynome 1 + Polynome 2:', L1.add(L2))
print('Polynome 1 après:', L1)

# Nous devons réinitialiser L1 comme il a été modifié
L1 = Cellule(3, Cellule(0, Cellule(1, Cellule(6, Cellule.liste_vide))))

print('Polynome 2 + Polynome 1:', L2.add(L1))
print('Polynome 1 après:', L1)

print('============================')

##################

#### SOUSTRACTION ####

print('== Test soustraction polynome ==')

L1 = Cellule(3, Cellule(0, Cellule(1, Cellule(6, Cellule.liste_vide))))
L2 = Cellule(9, Cellule(5, Cellule.liste_vide))

print('Polynome 1:', L1)
print('Polynome 2:', L2)

print('Polynome 1 - Polynome 2:', L1.sub(L2))

# Nous devons réinitialiser L1 comme il a été modifié
L1 = Cellule(3, Cellule(0, Cellule(1, Cellule(6, Cellule.liste_vide))))

print('Polynome 2 - Polynome 1:', L2.sub(L1))

print('================================')

######################

#### MULTIPLICATION ET DIVISION ####

# Les multiplications et divisions inplace pour des listes chaînées sont très difficiles
# et n'apporteront que des difficultés. Je préfère donc ne pas vous les présenter dans ce paradigme.

####################################