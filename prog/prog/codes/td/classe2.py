class Liste:

    def __init__(self, x, l):
        self._hd = x
        self._tl = l

    def valeur(self): return self._hd
    def suite(self): return self._tl

    def est_vide(self):
        return self is Liste.liste_vide

Liste.liste_vide = Liste(None, None)
