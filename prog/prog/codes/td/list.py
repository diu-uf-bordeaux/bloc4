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

test_search(search_rec)
test_search(search_for)

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

test_count(count_rec)
test_count(count_for)
