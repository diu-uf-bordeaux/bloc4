from code_file import file, file_vide, pop, est_vide

def fileStr(file):
    if est_vide(file):
        return 'x'
    else:
        tmp = pop(file)
        return '[' + str(tmp[0]) + ']-' + fileStr(tmp[1])

class Pile:
    pile_vide = None

    def __init__(self, valeur, pile):
        self._valeur = valeur
        self._suite = pile
    
    def push(self, valeur):
        return Pile(valeur, self)
    
    def pop(self):
        return (self._valeur, self._suite)

    def taille(self):
        if Pile.est_vide(self._suite):
            return 1

        return 1 + self._suite.taille()

    def max(self):
        if Pile.est_vide(self._suite):
            return self._valeur

        maxReste = self._suite.max()

        if maxReste > self._valeur:
            return maxReste
        else:
            return self._valeur

    def min(self):
        if Pile.est_vide(self._suite):
            return self._valeur

        minReste = self._suite.min()

        if minReste < self._valeur:
            return minReste
        else:
            return self._valeur

    def copie(self):
        if Pile.est_vide(self._suite):
            return Pile(self._valeur, Pile.pile_vide)

        return Pile(self._valeur, self._suite.copie())

    def __str__(self):
        if Pile.est_vide(self._suite):
            return "[" + str(self._valeur) + "]"
        else:
            return "[" + str(self._valeur) + "]-" + str(self._suite)
    
    @staticmethod
    def est_vide(pile):
        return pile is Pile.pile_vide

#### TAILLE ####

print('== Test taille ==')

P1 = Pile(3, Pile(6, Pile(9, Pile.pile_vide)))
print('Liste:', P1)
print('Taille:', P1.taille())

print('----')

P1 = Pile(10, P1)
print('Liste:', P1)
print('Taille:', P1.taille())

print('----')

P1 = Pile.pile_vide
print('Liste:', P1)
print('Taille: Impossible d\'utiliser taille sur l\'objet None')

print('=================')

################

#### MAX ####

print('== Test max ==')

P1 = Pile(3, Pile(6, Pile(9, Pile.pile_vide)))
print('Pile:', P1)
print('Max:', P1.max())

print('----')

P1 = Pile(10, P1)
print('Pile:', P1)
print('Max:', P1.max())

print('----')

P1 = Pile.pile_vide
print('Pile:', P1)
print('Max: Impossible de lancer la fonction max sur l\'objet None')

print('=================')

#############

#### MIN ####

print('== Test min ==')

P1 = Pile(3, Pile(6, Pile(9, Pile.pile_vide)))
print('Pile:', P1)
print('Min:', P1.min())

print('----')

P1 = Pile(-3, P1)
print('Pile:', P1)
print('Min:', P1.min())

print('----')

P1 = Pile.pile_vide
print('Pile:', P1)
print('Min: Impossible de lancer la fonction min sur l\'objet None')

print('=================')

#############

#### COPIE ####

print('== Test copie ==')

P1 = Pile(3, Pile(6, Pile(9, Pile.pile_vide)))
print('Pile:', P1)
P2 = P1.copie()
print('Copie P2:', P2)

print('================')

###############

#### PAREN ####

# Version impérative également mais en utilisant une pile objet
def verifierParentheses(fileReste):
    if est_vide(fileReste):
        return True

    (teteFile, fileReste) = pop(fileReste)
    stock = Pile(teteFile, Pile.pile_vide)

    while not est_vide(fileReste):
        (teteFile, fileReste) = pop(fileReste)

        if teteFile == ']':
            if Pile.est_vide(stock):
                return False
            else:
                (sommetPile, stock) = stock.pop()
                if sommetPile != '[':
                    return False
        elif teteFile == ')':
            if Pile.est_vide(stock):
                return False
            else:
                (sommetPile, stock) = stock.pop()
                if sommetPile != '(':
                    return False
        else:
            stock = stock.push(teteFile)

    return True

F1 = file('(', file('[', file(']', file(')', file_vide()))))
print('File:', fileStr(F1))
print('Bien parenthesee:', verifierParentheses(F1))

F1 = file('(', file('[', file(')', file(']', file_vide()))))
print('File:', fileStr(F1))
print('Bien parenthesee:', verifierParentheses(F1))

###############