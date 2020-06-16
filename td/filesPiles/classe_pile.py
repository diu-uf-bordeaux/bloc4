class Pile:
    pile_vide = None

    def __init__(self, valeur, pile):
        self._valeur = valeur
        self._suite = pile
    
    def push(self, valeur):
        return Pile(valeur, self)
    
    def pop(self):
        return (self._valeur, self._suite)
    
    def est_vide(pile):
        return pile is Pile.pile_vide