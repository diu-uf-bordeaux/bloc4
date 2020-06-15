def pile_vide():
    return []

def pile(valeur, pile):
    return [valeur, pile]

def push(valeur, pile):
    return [valeur, pile]

def pop(pile):
    return (pile[0], pile[1])
    
def est_vide(pile):
    return pile == pile_vide()