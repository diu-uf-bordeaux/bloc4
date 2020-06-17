from code_liste import *

def listeSTR(liste):
    if est_vide(liste):
        return 'x'
    else:
        return '[' + str(valeur(liste)) + ']-' + listeSTR(suite(liste))

##### TAILLE ####
def taille(liste):
    if est_vide(liste):
        return 0
    else:
        return 1 + taille(suite(liste))

print('== Test taille ==')

L1 = cellule(3, cellule(6, cellule(9, liste_vide())))
print('Liste:', listeSTR(L1))
print('Taille:', taille(L1))

print('----')

L1 = cellule(10, L1)
print('Liste:', listeSTR(L1))
print('Taille:', taille(L1))

print('----')

L1 = liste_vide()
print('Liste:', listeSTR(L1))
print('Taille:', taille(L1))

print('=================')

#################

##### MAX ####
def max(a, b):
    if a > b:
        return a
    else:
        return b

def maxListe(liste):
    if est_vide(liste):
        return None        # Pas de résultat possible
    elif est_vide(suite(liste)):
        return valeur(liste)
    else:
        return max(
            valeur(liste), 
            maxListe(suite(liste))
        )

print('== Test max ==')

L1 = cellule(3, cellule(6, cellule(9, liste_vide())))
print('Liste:', listeSTR(L1))
print('Max:', maxListe(L1))

print('----')

L1 = cellule(10, L1)
print('Liste:', listeSTR(L1))
print('Max:', maxListe(L1))

print('----')

L1 = liste_vide()
print('Liste:', listeSTR(L1))
print('Max:', maxListe(L1))

print('==============')

#################

##### MIN ####

def min(a, b):
    if a < b:
        return a
    else:
        return b

def minListe(liste):
    if est_vide(liste):
        return None        # Pas de résultat possible
    elif est_vide(suite(liste)):
        return valeur(liste)
    else:
        return min(
            valeur(liste), 
            minListe(suite(liste))
        )

print('== Test min ==')

L1 = cellule(3, cellule(6, cellule(9, liste_vide())))
print('Liste:', listeSTR(L1))
print('Min:', minListe(L1))

print('----')

L1 = cellule(-3, L1)
print('Liste:', listeSTR(L1))
print('Min:', minListe(L1))

print('----')

L1 = liste_vide()
print('Liste:', listeSTR(L1))
print('Min:', minListe(L1))

print('==============')

##### TRI ####

def enleverValeur(val, liste):
    if est_vide(liste):
        return liste
    elif valeur(liste) == val:
        return suite(liste)
    else:
        return cellule(
            valeur(liste),
            enleverValeur(
                val, 
                suite(liste)
            )
        )

def triListeDecroissant(liste):
    if est_vide(liste):
        return liste
    else:
        return cellule(
            maxListe(liste),
            triListeDecroissant(
                enleverValeur(
                    maxListe(liste),
                    liste
                )
            )
        )

def triListeCroissant(liste):
    if est_vide(liste):
        return liste
    else:
        return cellule(
            minListe(liste),
            triListeCroissant(
                enleverValeur(
                    minListe(liste),
                    liste
                )
            )
        )

print('== Test enlever valeur ==')

L1 = cellule(3, cellule(6, cellule(9, liste_vide())))
print('Liste:', listeSTR(L1))
print('Résultat:', enleverValeur(6, L1), "<=>", listeSTR(enleverValeur(6, L1)))

print('=========================')

print('== Test tri decroissant ==')

L1 = cellule(3, cellule(6, cellule(9, liste_vide())))
print('Liste:', listeSTR(L1))
print('Résultat:', triListeDecroissant(L1), "<=>", listeSTR(triListeDecroissant(L1)))

L1 = triListeDecroissant(L1)

print('==========================')

print('== Test tri croissant ==')

print(triListeCroissant(L1))
print('Liste:', listeSTR(L1))
print('Résultat:', triListeCroissant(L1), "<=>", listeSTR(triListeCroissant(L1)))

print('========================')