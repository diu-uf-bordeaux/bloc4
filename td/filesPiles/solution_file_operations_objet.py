class File:
    file_vide = None

    def __init__(self, valeur, file):
        self._valeur = valeur
        self._suite = file

    def push(self, valeur):
        if File.est_vide(self._suite):
            self._suite = File(valeur, File.file_vide)
        else:
            self._suite.push(valeur)
        return self

    def pop(self):
        return (self._valeur, self._suite)

    def taille(self):
        if File.est_vide(self._suite):
            return 1

        return 1 + self._suite.taille()

    def max(self):
        if File.est_vide(self._suite):
            return self._valeur

        maxReste = self._suite.max()

        if maxReste > self._valeur:
            return maxReste
        else:
            return self._valeur

    def min(self):
        if File.est_vide(self._suite):
            return self._valeur

        minReste = self._suite.min()

        if minReste < self._valeur:
            return minReste
        else:
            return self._valeur

    def inverse(self):
        if File.est_vide(self._suite):
            return File(self._valeur, File.file_vide)

        return self._suite.inverse().push(self._valeur)

    def _ignoreValeur(self, valeur):
        if self._valeur == valeur:
            return self._suite

        return File(self._valeur, self._suite._ignoreValeur(valeur))

    def tri(self):
        if File.est_vide(self._suite):
            return File(self._valeur, File.file_vide)

        listeMax = self.max()

        return File(
            listeMax,
            self._ignoreValeur(listeMax).tri()
        )

    def popValeur(self, valeur):
        if self._valeur == valeur:
            if File.est_vide(self._suite):
                return File.file_vide
            else:
                return self._suite.popValeur(valeur)
        else:
            if File.est_vide(self._suite):
                return self
            else:
                self._suite = self._suite.popValeur(valeur)
                return self

    def __str__(self):
        if File.est_vide(self._suite):
            return "[" + str(self._valeur) + "]"
        else:
            return "[" + str(self._valeur) + "]-" + str(self._suite)

    @staticmethod
    def est_vide(file):
        return file is File.file_vide

    @staticmethod
    def fusion(file1, file2):
        if File.est_vide(file1):
            return file2
        elif File.est_vide(file2):
            return file1

        tmpFile1 = file1.pop()
        tmpFile2 = file2.pop()

        if tmpFile1[0] > tmpFile2[0]:
            return File(tmpFile1[0], File.fusion(
                tmpFile1[1],
                file2
            ))
        else:
            return File(tmpFile2[0], File.fusion(
                file1,
                tmpFile2[1]
            ))

#### TAILLE ####

print('== Test taille ==')

F1 = File(3, File(6, File(9, File.file_vide)))
print('Liste:', F1)
print('Taille:', F1.taille())

print('----')

F1 = File(10, F1)
print('Liste:', F1)
print('Taille:', F1.taille())

print('----')

F1 = File.file_vide
print('Liste:', F1)
print('Taille: Impossible d\'utiliser taille sur l\'objet None')

print('=================')

################

#### MAX ####

print('== Test max ==')

F1 = File(3, File(6, File(9, File.file_vide)))
print('File:', F1)
print('Max:', F1.max())

print('----')

F1 = File(10, F1)
print('File:', F1)
print('Max:', F1.max())

print('----')

F1 = File.file_vide
print('File:', F1)
print('Max: Impossible de lancer la fonction max sur l\'objet None')

print('=================')

#############

#### MIN ####

print('== Test min ==')

F1 = File(3, File(6, File(9, File.file_vide)))
print('File:', F1)
print('Min:', F1.min())

print('----')

F1 = File(-3, F1)
print('File:', F1)
print('Min:', F1.min())

print('----')

F1 = File.file_vide
print('File:', F1)
print('Min: Impossible de lancer la fonction min sur l\'objet None')

print('=================')

#############

#### INVERSE ####

print('== Test inverse ==')

F1 = File(3, File(6, File(9, File.file_vide)))
print('File:', F1)
print('Inverse:', F1.inverse())
print('Cette fonction n\'est pas inplace, F1:', F1)

print('==================')

#################

#### TRIER ####

print('== Test tri ==')

F1 = File(3, File(6, File(9, File.file_vide)))
print('File:', F1)
print('File triee:', F1.tri())
print('Cette fonction n\'est pas inplace, F1:', F1)

print('==============')

###############

#### FUSION ####

print('== Test fusion ==')

F1 = File(9, File(6, File(3, File.file_vide)))
F2 = File(15, File(4, File(1, File.file_vide)))
print('File1:', F1)
print('File2:', F2)
print('File fusionnees:', File.fusion(F1, F2))

print('==============')

################

#### POP VALEUR ####

print('== Test pop valeur ==')

F1 = File(6, File(7, File(6, File(4, File(6, File.file_vide)))))
print('File:', F1)
print('Pop valeur 6:', F1.popValeur(6))

print('=====================')

####################