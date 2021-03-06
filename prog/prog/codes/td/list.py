def search_rec(l, x):
    if (l == []):
        return False
    elif (l[0] == x):
        return True
    else:
        return search_rec(l[1:], x)

def search_for(l, x):
    for y in l:
        if (x == y):
            return True
    return False

def test_search(search_fun):
    test_values = [
        (([], 1), False),
        (([1], 1), True),
        (([1,2], 1), True),
        (([2,1], 1), True),
        (([2,3], 1), False),
    ]
    for ((l,x), r) in test_values:
        assert(search_fun(l,x) == r)

# test_search(search_rec)
# test_search(search_for)

def count_rec(l, x):
    if (l == []):
        return 0
    elif (l[0] == x):
        return 1 + count_rec(l[1:], x)
    else:
        return count_rec(l[1:], x)

def count_for(l, x):
    res = 0
    for y in l:
        if (y == x):
            res += 1
    return res

def test_count(count_fun):
    test_values = [
        (([], 1), 0),
        (([1], 1), 1),
        (([1,1], 1), 2),
        (([1,2], 1), 1),
        (([2,1], 1), 1),
        (([2,3], 1), 0),
    ]
    for ((l,x), r) in test_values:
        assert(count_fun(l,x) == r)

# test_count(count_rec)
# test_count(count_for)

print("##### Listes Code Objet #####")
from cellule import Cellule

l1 = Cellule.liste_vide  # returns an empty list
l2 = Cellule(1, Cellule.liste_vide)
l3 = Cellule(2, l2)

print(Cellule.est_vide(l1), True) # -> True
print(Cellule.est_vide(l2), False) # -> False

print(l3.suite())                # -> returns a list
print(l3.suite() == l2, True)    # -> True
l3 = Cellule(3, l3)

def str_liste(l):
    if Cellule.est_vide(l):
        return "[]"
    else:
        return "[{},{}]".format(l.valeur(), str_liste(l.suite()))

print(str_liste(l3))

def taille(l):
    if Cellule.est_vide(l):
        return 0
    else:
        return 1 + taille(l.suite())

print(taille(l3), 3)

def max_liste(l):
    if Cellule.est_vide(l):
        raise Exception("No max on an empty list")
    elif Cellule.est_vide(l.suite()):
        return l.valeur()
    else:
        return max(l.valeur(), max_liste(l.suite()))

print(max_liste(l3), 3)

def min_liste(l):
    if Cellule.est_vide(l):
        raise Exception("No min on an empty list")
    elif Cellule.est_vide(l.suite()):
        return l.valeur()
    else:
        return min(l.valeur(), min_liste(l.suite()))

print(min_liste(l3), 1)

def inserer(x, l):
    if Cellule.est_vide(l):
        return Cellule(x, Cellule.liste_vide)
    elif x < l.valeur():
        return Cellule(x, l)
    else:
        return Cellule(l.valeur(), inserer(x, l.suite()))

def trier(l):
    if Cellule.est_vide(l):
        raise Exception("No min on an empty list")
    elif Cellule.est_vide(l.suite()):
        return l
    else:
        return inserer(l.valeur(), trier(l.suite()))

print(str_liste(trier(l3)))

print("##### Listes Code Fonctionnel #####")
import func_list as lis

l1 = lis.liste_vide()  # returns an empty list
l2 = lis.cellule(1, lis.liste_vide())
l3 = lis.cellule(2, l2)

print(lis.est_vide(l1), True) # -> True
print(lis.est_vide(l2), False) # -> False

print(lis.suite(l3))                # -> returns a list
print(lis.suite(l3) == l2, True)    # -> True
l3 = lis.cellule(3, l3)

def str_liste(l):
    if lis.est_vide(l):
        return "[]"
    else:
        return "[{},{}]".format(lis.valeur(l), str_liste(lis.suite(l)))

print(str_liste(l3))

def taille(l):
    if lis.est_vide(l):
        return 0
    else:
        return 1 + taille(lis.suite(l))

print(taille(l3), 3)

def max_liste(l):
    if lis.est_vide(l):
        raise Exception("No max on an empty list")
    elif lis.est_vide(lis.suite(l)):
        return lis.valeur(l)
    else:
        return max(lis.valeur(l), max_liste(lis.suite(l)))

print(max_liste(l3), 3)

def min_liste(l):
    if lis.est_vide(l):
        raise Exception("No min on an empty list")
    elif lis.est_vide(lis.suite(l)):
        return lis.valeur(l)
    else:
        return min(lis.valeur(l), min_liste(lis.suite(l)))

print(min_liste(l3), 1)

def inserer(x, l):
    if lis.est_vide(l):
        return lis.cellule(x, lis.liste_vide())
    elif x < lis.valeur(l):
        return lis.cellule(x, l)
    else:
        return lis.cellule(lis.valeur(l), inserer(x, lis.suite(l)))

def trier(l):
    if lis.est_vide(l):
        raise Exception("No min on an empty list")
    elif lis.est_vide(lis.suite(l)):
        return l
    else:
        return inserer(lis.valeur(l), trier(lis.suite(l)))

print(str_liste(trier(l3)))

print("##### Listes Code Objet + Empty Object #####")
from classe2 import Liste

l1 = Liste.liste_vide  # returns an empty list
l2 = Liste(1, Liste.liste_vide)
l3 = Liste(2, l2)

print(l1.est_vide(), True) # -> True
print(l2.est_vide(), False) # -> False

print(l3.suite())                # -> returns a list
print(l3.suite() == l2, True)    # -> True
l3 = Liste(3, l3)

def str_liste(l):
    if l.est_vide():
        return "[]"
    else:
        return "[{},{}]".format(l.valeur(), str_liste(l.suite()))

print(str_liste(l3))

def taille(l):
    if l.est_vide():
        return 0
    else:
        return 1 + taille(l.suite())

print(taille(l3), 3)

def max_liste(l):
    if l.est_vide():
        raise Exception("No max on an empty list")
    elif l.suite().est_vide():
        return l.valeur()
    else:
        return max(l.valeur(), max_liste(l.suite()))

print(max_liste(l3), 3)

def min_liste(l):
    if l.est_vide():
        raise Exception("No min on an empty list")
    elif l.suite().est_vide():
        return l.valeur()
    else:
        return min(l.valeur(), min_liste(l.suite()))

print(min_liste(l3), 1)

def inserer(x, l):
    if l.est_vide():
        return Liste(x, Liste.liste_vide)
    elif x < l.valeur():
        return Liste(x, l)
    else:
        return Liste(l.valeur(), inserer(x, l.suite()))

def trier(l):
    if l.est_vide():
        raise Exception("No min on an empty list")
    elif l.suite().est_vide():
        return l
    else:
        return inserer(l.valeur(), trier(l.suite()))

print(str_liste(trier(l3)))

print("##### Listes Code Objet + Empty Object + Methods inside class #####")

def str_liste(self):
    if self.est_vide():
        return "[]"
    else:
        return "[{},{}]".format(self.valeur(), str_liste(self.suite()))
Liste.str_liste = str_liste

print(l3.str_liste())

def taille(self):
    if self.est_vide():
        return 0
    else:
        return 1 + taille(self.suite())
Liste.taille = taille

print(l3.taille(), 3)

def max_liste(self):
    if self.est_vide():
        raise Exception("No max on an empty list")
    elif self.suite().est_vide():
        return self.valeur()
    else:
        return max(self.valeur(), max_liste(self.suite()))
Liste.max_liste = max_liste

print(l3.max_liste(), 3)

def min_liste(self):
    if self.est_vide():
        raise Exception("No min on an empty list")
    elif self.suite().est_vide():
        return self.valeur()
    else:
        return min(self.valeur(), min_liste(self.suite()))
Liste.min_liste = min_liste

print(l3.min_liste(), 1)

def inserer(self, x):
    if self.est_vide():
        return Liste(x, Liste.liste_vide)
    elif x < self.valeur():
        return Liste(x, l)
    else:
        return Liste(self.valeur(), self.suite().inserer(x))
Liste.inserer = inserer

def trier(self):
    if self.est_vide():
        raise Exception("No min on an empty list")
    elif self.suite().est_vide():
        return self
    else:
        return trier(self.suite()).inserer(self.valeur())
Liste.trier = trier

print(l3.trier().str_liste())
