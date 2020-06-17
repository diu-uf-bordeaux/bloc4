from code_liste import *

def listeSTR(liste):
    if est_vide(liste):
        return '.'
    else:
        return '[' + str(valeur(liste)) + ']-' + listeSTR(suite(liste))

#### VALEUR ####
def taille(liste):
    if est_vide(liste):
        return 0
    else:
        return 1 + taille(suite(liste))

def valeurPolynome(x, liste):
    if est_vide(liste):
        return 0
    else:
        degreeMax = taille(liste) - 1
        
        return valeur(liste) * (x**degreeMax) + valeurPolynome(
            x, 
            suite(liste)
        )

print('== Test valeur polynome ==')

L1 = cellule(3, cellule(0, cellule(1, cellule(6, liste_vide()))))
print('Liste:', listeSTR(L1))

for x in [2, 4, 6]:
    print('Valeur pour x =', x, ':', valeurPolynome(x, L1))

print('=================')

################

#### ADDITION ####

def addPolynome(poly1, poly2):
    taillePoly1 = taille(poly1)
    taillePoly2 = taille(poly2)

    if taillePoly1 == 0 and taillePoly2 == 0:
        return liste_vide()

    if taillePoly1 > taillePoly2:
        return cellule(
            valeur(poly1),
            addPolynome(
                suite(poly1),
                poly2
            )
        )
    elif taillePoly2 > taillePoly1:
        return cellule(
            valeur(poly2),
            addPolynome(
                poly1,
                suite(poly2)
            )
        )
    else:
        return cellule(
            valeur(poly1) + valeur(poly2),
            addPolynome(
                suite(poly1),
                suite(poly2)
            )
        )

L1 = cellule(3, cellule(0, cellule(1, cellule(6, liste_vide()))))
L2 = cellule(9, cellule(5, liste_vide()))

print('== Test addition polynome ==')

print('Polynome 1:', L1)
print('Polynome 2:', L2)

print('Polynome 1 + Polynome 2:', addPolynome(L1, L2))
print('Polynome 2 + Polynome 1:', addPolynome(L2, L1))

print('============================')

##################

#### SOUSTRACTION ####

def subPolynome(poly1, poly2):
    taillePoly1 = taille(poly1)
    taillePoly2 = taille(poly2)

    if taillePoly1 == 0 and taillePoly2 == 0:
        return liste_vide()

    if taillePoly1 > taillePoly2:
        return cellule(
            valeur(poly1),
            subPolynome(
                suite(poly1),
                poly2
            )
        )
    elif taillePoly2 > taillePoly1:
        return cellule(
            -valeur(poly2),
            subPolynome(
                poly1,
                suite(poly2)
            )
        )
    else:
        return cellule(
            valeur(poly1) - valeur(poly2),
            subPolynome(
                suite(poly1),
                suite(poly2)
            )
        )

L1 = cellule(3, cellule(0, cellule(1, cellule(6, liste_vide()))))
L2 = cellule(9, cellule(5, liste_vide()))

print('== Test soustraction polynome ==')

print('Polynome 1:', L1)
print('Polynome 2:', L2)

print('Polynome 1 - Polynome 2:', subPolynome(L1, L2))
print('Polynome 2 - Polynome 1:', subPolynome(L2, L1))

print('================================')

######################

#### MULTIPLICATION ####

# Multiplication d'un degree par un polynome
# 5x² * (9x + 3)
def mulElemPolynome(tuple, poly):
    if taille(poly) == 0:
        return liste_vide()
    
    # Le but ici est de multiplier le degree par le premier element du polynome (9x + 3)
    degreeMax = taille(poly) - 1 # Degree max du polynome (1)
    valeurPoly = valeur(poly)    # Valeur du premier element du polynome (9)

    degreeFinal = degreeMax + tuple[1]  # Degree final: 3
    valeurFinale = valeurPoly * tuple[0] # Valeur finale: 45

    # Générer le polynome à retourner, chainage de 0 jusqu'au degree max - 1
    resultat = liste_vide()
    degreeCourant = 0
    while degreeCourant < degreeFinal:
        resultat = cellule(0, resultat)
        degreeCourant += 1

    return addPolynome(
        cellule(valeurFinale, resultat),    # On rajoute la valeur finale au polynome
        mulElemPolynome(                    # Puis on rappelle cette fonction sur le reste du polynome
            tuple,
            suite(poly)
        )
    )

def mulPolynome(poly1, poly2):
    # Si un des polynomes est nul, arreter
    if taille(poly1) == 0 or taille(poly2) == 0:
        return liste_vide()

    # Le but de cette multiplication est de multiplier le premier degree de poly1 avec poly2
    # Puis d'ajouter le reste de la multiplication, i.e. enlever le degree que l'on vient d'utiliser de poly1
    # et rappeler la fonction.

    # Prendre le premier élément et l'extraire, i.e. [5]-[6]-[3] -> (5, 2) représentant 5x²
    tmp = (valeur(poly1), taille(poly1) - 1) # (5, 2) par exemple

    return addPolynome(
        mulElemPolynome(tmp, poly2),    # Multiplication entre le degree (5x²) et poly2
        mulPolynome(                    # Reste de la multiplication, i.e. (poly1 - 5x²) * poly2
            suite(poly1),
            poly2
        )
    )

print('== Test multiplication polynome ==')

L1 = cellule(5, cellule(2, liste_vide()))
L2 = cellule(3, cellule(6, cellule(2, liste_vide())))
print('L1:', listeSTR(L1))
print('L2:', listeSTR(L2))
print('Multiplication des deux:',
    mulPolynome(
        L1,
        L2
    ),
    '<=>', listeSTR(
        mulPolynome(
            L1,
            L2
        )
    )
)

print('==================================')

########################

#### Division ####

def divisionPoly(poly1, poly2):
    # Vider les leading 0 de poly 1
    while valeur(poly1) == 0:
        poly1 = suite(poly1)

    degreePoly1 = taille(poly1)
    degreePoly2 = taille(poly2)

    if degreePoly1 < degreePoly2:
        return liste_vide()

    valeurPoly1 = valeur(poly1)
    valeurPoly2 = valeur(poly2)

    degreeFinal = degreePoly1 - degreePoly2

    # Créer le polynome correspondant
    nouveauPoly = liste_vide()
    degreeCourant = 0
    while degreeCourant < degreeFinal:
        nouveauPoly = cellule(0, nouveauPoly)
        degreeCourant += 1
    nouveauPoly = cellule(valeurPoly1 / valeurPoly2, nouveauPoly)

    return addPolynome(
        nouveauPoly,
        divisionPoly(
            subPolynome(
                poly1,
                mulPolynome(
                    nouveauPoly,
                    poly2
                )
            ),
            poly2
        )
    )

L1 = cellule(4, cellule(0, cellule(-5, cellule(7, cellule(8, liste_vide())))))
L2 = cellule(1, cellule(2, cellule(-3, liste_vide())))

print('Polynome 1:', L1, '<=>', listeSTR(L1))
print('Polynome 2:', L2, '<=>', listeSTR(L2))
print('Resultat de la division:', divisionPoly(L1, L2), '<=>', listeSTR(divisionPoly(L1, L2)))
print('Reste de la division:', subPolynome(
    L1,
    mulPolynome(
        divisionPoly(L1, L2),
        L2
    )
))

##################