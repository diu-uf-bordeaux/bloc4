def liste_vide():
    return []

def cellule(etiquette, liste):
    return [etiquette, liste]

def valeur(liste):
    return liste[0]

def suite(liste):
    return liste[1]

def est_vide(liste):
    return liste == liste_vide()