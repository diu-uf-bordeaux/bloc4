class Cellule:
    liste_vide = None

    def __init__(self, etiquette, liste):
        self._valeur = etiquette
        self._suivant = liste

    def valeur(self):
        return self._valeur

    def suite(self):
        return self._suivant

    def est_vide(liste):
        return liste is Cellule.liste_vide