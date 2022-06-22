class Liste:

    def __init__(self, etiquette, liste):
        self._valeur = etiquette
        self._suivant = liste

    def valeur(self): 
        return self._valeur
    
    def suite(self): 
        return self._suivant

    def est_vide(self):
        return self is Liste.liste_vide

    def __str__(self):
        if self.est_vide():
            return "[]"
        else:
            return "[{},{}]".format(self.valeur(), str(self.suite()))

    def taille(self):
        if self.est_vide():
            return 0
        else:
            return 1 + self.suite().taille()

    def max(self):
        if self.est_vide():
            raise Exception("No max on an empty list")
        elif self.suite().est_vide():
            return self.valeur()
        else:
            return max(self.valeur(), self.suite().max())

    def min(self):
        if self.est_vide():
            raise Exception("No min on an empty list")
        elif self.suite().est_vide():
            return self.valeur()
        else:
            return min(self.valeur(), self.suite().min())

    def inserer(self, x):
        if self.est_vide():
            return Liste(x, Liste.liste_vide)
        elif x < self.valeur():
            return Liste(x, self)
        else:
            return Liste(self.valeur(), self.suite().inserer(x))

    def trier(self):
        if self.est_vide():
            raise Exception("No min on an empty list")
        elif self.suite().est_vide():
            return self
        else:
            return self.suite().trier().inserer(self.valeur())

Liste.liste_vide = Liste(None, None)

print('== Test taille ==')

L1 = Liste(3, Liste(6, Liste(9, Liste.liste_vide)))
print('Liste:', L1)
print('Taille:', L1.taille())

print('----')

L1 = Liste(10, L1)
print('Liste:', L1)
print('Taille:', L1.taille())

print('----')

L1 = Liste.liste_vide
print('Liste:', L1)
print('Taille: ', L1.taille())

print('=================')

print('== Test max ==')

L1 = Liste(3, Liste(6, Liste(9, Liste.liste_vide)))
print('Liste:', L1)
print('Max:', L1.max())

print('----')

L1 = Liste(10, L1)
print('Liste:', L1)
print('Max:', L1.max())

print('----')

L1 = Liste.liste_vide
print('Liste:', L1)
try:
    print('Max:', L1.max())
except Exception as error:
    print(error)

print('==============')

print('== Test min ==')

L1 = Liste(3, Liste(6, Liste(9, Liste.liste_vide)))
print('Liste:', L1)
print('Min:', L1.min())

print('----')

L1 = Liste(-3, L1)
print('Liste:', L1)
print('Min:', L1.min())

print('----')

L1 = Liste.liste_vide
print('Liste:', L1)
try:
    print('Min:', L1.min())
except Exception as error:
    print(error)

print('==============')

print('== Test tri ==')

L1 = Liste(9, Liste(6, Liste(3, Liste.liste_vide)))
print('Liste:', L1)
print('Résultat:', L1.trier())

print('========================')