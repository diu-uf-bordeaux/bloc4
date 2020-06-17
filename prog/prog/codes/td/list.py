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

# from cellule import Cellule

# l1 = Cellule.liste_vide  # returns an empty list
# l2 = Cellule(1, Cellule.liste_vide)
# l3 = Cellule(2, l2)

# print(Cellule.est_vide(l1), True) # -> True
# print(Cellule.est_vide(l2), False) # -> False

# print(l3.suite())                # -> returns a list
# print(l3.suite() == l2, True)    # -> True

import func_list as lis

l1 = lis.liste_vide()  # returns an empty list
l2 = lis.cellule(1, lis.liste_vide)
l3 = lis.cellule(2, l2)

print(lis.est_vide(l1), True) # -> True
print(lis.est_vide(l2), False) # -> False

print(lis.suite(l3))                # -> returns a list
print(lis.suite(l3) == l2, True)    # -> True
