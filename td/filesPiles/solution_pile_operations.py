from code_pile import *
from code_file import file_vide, pop, file, est_vide

def fileStr(file):
    if est_vide(file):
        return 'x'
    else:
        tmp = pop(file)
        return '[' + str(tmp[0]) + ']-' + fileStr(tmp[1])

def pileStr(pile):
    if est_vide(pile):
        return 'x'
    else:
        tmp = pop(pile)
        return '[' + str(tmp[0]) + ']-' + pileStr(tmp[1])

#### TAILLE ####

def taille(pile):
    if est_vide(pile):
        return 0

    return 1 + taille(pop(pile)[1])

print('== Test taille ==')

P1 = pile(3, pile(6, pile(9, pile_vide())))
print('Pile:', pileStr(P1))
print('Taille:', taille(P1))

print('----')

P1 = pile(10, P1)
print('Pile:', pileStr(P1))
print('Taille:', taille(P1))

print('----')

P1 = pile_vide()
print('Pile:', pileStr(P1))
print('Taille:', taille(P1))

print('=================')

################

#### MAX ####

def max(pile):
    if est_vide(pile):
        return None

    tmp = pop(pile)

    if est_vide(tmp[1]):
        return tmp[0]
    
    resteMax = max(tmp[1])

    if tmp[0] > resteMax:
        return tmp[0]
    else:
        return resteMax

print('== Test max ==')

P1 = pile(3, pile(6, pile(9, pile_vide())))
print('pile:', pileStr(P1))
print('Max:', max(P1))

print('----')

P1 = pile(10, P1)
print('pile:', pileStr(P1))
print('Max:', max(P1))

print('----')

P1 = pile_vide()
print('pile:', pileStr(P1))
print('Max:', max(P1))

print('=================')

#############

#### MIN ####

def min(pile):
    if est_vide(pile):
        return None

    tmp = pop(pile)

    if est_vide(tmp[1]):
        return tmp[0]

    resteMin = min(tmp[1])

    if tmp[0] < resteMin:
        return tmp[0]
    else:
        return resteMin

print('== Test min ==')

P1 = pile(3, pile(6, pile(9, pile_vide())))
print('pile:', pileStr(P1))
print('Min:', min(P1))

print('----')

P1 = pile(-3, P1)
print('pile:', pileStr(P1))
print('Min:', min(P1))

print('----')

P1 = pile_vide()
print('pile:', pileStr(P1))
print('Min:', max(P1))

print('=================')

#############

#### COPIE ####

def copie(pileReste):
    if est_vide(pileReste):
        return pileReste

    tmp = pop(pileReste)

    return pile(
        tmp[0],
        copie(
            tmp[1]
        )
    )

print('== Test copie pile ==')

P1 = pile(3, pile(6, pile(9, pile_vide())))
print('Pile:', pileStr(P1))
print('Copie:', copie(P1), '<=>', pileStr(P1))

print('=====================')

###############

## PARENTHESAGE ##

# Version imperative
def verifierParentheses(fileReste):
    stock = pile_vide()

    while not est_vide(fileReste):
        (teteFile, fileReste) = pop(fileReste)

        if teteFile == ']':
            if est_vide(stock):
                return False
            else:
                (sommetPile, stock) = pop(stock)
                if sommetPile != '[':
                    return False
        elif teteFile == ')':
            if est_vide(stock):
                return False
            else:
                (sommetPile, stock) = pop(stock)
                if sommetPile != '(':
                    return False
        else:
            stock = push(teteFile, stock)

    return True

F1 = file('(', file('[', file(']', file(')', file_vide()))))
print('File:', fileStr(F1))
print('Bien parenthesee:', verifierParentheses(F1))

F1 = file('(', file('[', file(')', file(']', file_vide()))))
print('File:', fileStr(F1))
print('Bien parenthesee:', verifierParentheses(F1))

##################