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

Liste.liste_vide = Liste(None, None)
