from code_file import *

def fileStr(file):
    if est_vide(file):
        return 'x'
    else:
        tmp = pop(file)
        return '[' + str(tmp[0]) + ']-' + fileStr(tmp[1])

#### TAILLE ####

def taille(file):
    if est_vide(file):
        return 0

    return 1 + taille(pop(file)[1])

print('== Test taille ==')

F1 = file(3, file(6, file(9, file_vide())))
print('File:', fileStr(F1))
print('Taille:', taille(F1))

print('----')

F1 = file(10, F1)
print('File:', fileStr(F1))
print('Taille:', taille(F1))

print('----')

F1 = file_vide()
print('File:', fileStr(F1))
print('Taille:', taille(F1))

print('=================')

################

#### MAX ####

def max(file):
    if est_vide(file):
        return None

    tmp = pop(file)

    if est_vide(tmp[1]):
        return tmp[0]
    
    resteMax = max(tmp[1])

    if tmp[0] > resteMax:
        return tmp[0]
    else:
        return resteMax

print('== Test max ==')

F1 = file(3, file(6, file(9, file_vide())))
print('File:', fileStr(F1))
print('Max:', max(F1))

print('----')

F1 = file(10, F1)
print('File:', fileStr(F1))
print('Max:', max(F1))

print('----')

F1 = file_vide()
print('File:', fileStr(F1))
print('Max:', max(F1))

print('=================')

#############

#### MIN ####

def min(file):
    if est_vide(file):
        return None

    tmp = pop(file)

    if est_vide(tmp[1]):
        return tmp[0]

    resteMin = min(tmp[1])

    if tmp[0] < resteMin:
        return tmp[0]
    else:
        return resteMin

print('== Test min ==')

F1 = file(3, file(6, file(9, file_vide())))
print('File:', fileStr(F1))
print('Min:', min(F1))

print('----')

F1 = file(-3, F1)
print('File:', fileStr(F1))
print('Min:', min(F1))

print('----')

F1 = file_vide()
print('File:', fileStr(F1))
print('Min:', max(F1))

print('=================')

#############

#### INVERSE ####

def inverse(file):
    if est_vide(file):
        return file_vide()

    tmp = pop(file)

    return push(tmp[0], inverse(tmp[1]))

print('== Test inverse ==')

F1 = file(3, file(6, file(9, file_vide())))
print('File:', fileStr(F1))
print('Inverse:', fileStr(inverse(F1)))

print('==================')

#################

#### TRIER ####

def enleverValeur(valeur, resteFile):
    if est_vide(resteFile):
        return file_vide()

    tmp = pop(resteFile)

    if tmp[0] == valeur:
        return tmp[1]
    else:
        return file(tmp[0], enleverValeur(valeur, tmp[1]))

def tri(resteFile):
    if est_vide(resteFile):
        return file_vide()

    fileMax = max(resteFile)

    return file(
        fileMax,
        tri(
            enleverValeur(
                fileMax,
                resteFile
            )
        )
    )

print('== Test tri ==')

F1 = file(3, file(6, file(9, file_vide())))
print('File:', fileStr(F1))
print('File triee:', fileStr(tri(F1)))

print('==============')

###############

#### FUSION ####

def fusion(file1, file2):
    if taille(file1) == 0:
        return file2
    elif taille(file2) == 0:
        return file1

    tmpFile1 = pop(file1)
    tmpFile2 = pop(file2)

    if tmpFile1[0] > tmpFile2[0]:
        return file(tmpFile1[0], fusion(
            tmpFile1[1],
            file2
        ))
    else:
        return file(tmpFile2[0], fusion(
            file1,
            tmpFile2[1]
        ))

print('== Test fusion ==')

F1 = file(9, file(6, file(3, file_vide())))
F2 = file(15, file(4, file(1, file_vide())))
print('File1:', fileStr(F1))
print('File2:', fileStr(F2))
print('File fusionnees:', fileStr(fusion(F1, F2)))

print('==============')

################

#### POP VALEUR ####

def popValeur(valeur, fileReste):
    if est_vide(fileReste):
        return file_vide()

    tmp = pop(fileReste)

    if tmp[0] == valeur:
        return popValeur(valeur, tmp[1])
    else:
        return file(tmp[0], popValeur(valeur, tmp[1]))

print('== Test pop valeur ==')

F1 = file(6, file(7, file(6, file(4, file(6, file_vide())))))
print('File:', fileStr(F1))
print('Pop valeur 6:', fileStr(popValeur(6, F1)))

print('=====================')

####################