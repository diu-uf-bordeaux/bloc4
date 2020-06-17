import collections
import itertools
import multiprocessing
import requests
import time

################################################################
def map_imp(f, l):
    res = []
    for x in l:
        res.append(f(x))
    return res

def map_rec(f, l):
    if (len(l) == 0):
        return []
    else:
        return [f(l[0])] + map_rec(f, l[1:])

print(map_imp(lambda x: x+2, range(10)))
print(map_rec(lambda x: x+2, range(10)))

def filter_imp(f, l):
    res = []
    for x in l:
        if (f(x)):
            res.append(x)
    return res

def filter_rec(f, l):
    if (len(l) == 0):
        return []
    elif f(l[0]):
        return [l[0]] + filter_rec(f, l[1:])
    else:
        return filter_rec(f, l[1:])

print(filter_imp(lambda x: x % 2 == 0, range(10)))
print(filter_rec(lambda x: x % 2 == 0, range(10)))

def sum_imp(f, l):
    res = 0
    for x in l:
        res += f(x)
    return res

def sum_rec(f, l):
    if (len(l) == 0):
        return 0
    else:
        return f(l[0]) + sum_rec(f, l[1:])

print(sum_imp(lambda x: x*x, range(10)))
print(sum_rec(lambda x: x*x, range(10)))

def reduce_imp(f, acc, l):
    res = acc
    for x in l:
        res = f(res, x)
    return res

def reduce_rec(f, acc, l):
    if (len(l) == 0):
        return acc
    else:
        return reduce_rec(f, f(acc, l[0]), l[1:])

print(reduce_imp(lambda acc, x: acc-x, 0, range(10)))
print(reduce_rec(lambda acc, x: acc-x, 0, range(10)))
print(reduce_imp(lambda acc, x: acc+x, 0, range(10)))
print(reduce_rec(lambda acc, x: acc+x, 0, range(10)))

def reverse_reduce(l):
    return reduce_rec(lambda acc, x: [x] + acc, [], l)

print(reverse_reduce(range(10)))

################################################################
sages = [
{ "name": "Thalès", "birth": -625, "death": -547 },
{ "name": "Anaximandre", "birth": -600, "death": -546 },
{ "name": "Héraclite", "birth": -544, "death": -480 },
{ "name": "Empédocle", "birth": -490, "death": -430 },
{ "name": "Aristote", "birth": -384, "death": -322 },
{ "name": "Archimède", "birth": -287, "death": -212 },
{ "name": "Ératosthène", "birth": -276, "death": -194 },
{ "name": "Ptolémée", "birth": 100, "death": 170 },
{ "name": "Pétrone", "birth": 27, "death": 66 },
{ "name": "Leucippe", "birth": -460, "death": -370 },
{ "name": "Démocrite", "birth": -460, "death": -370 },
{ "name": "Protagoras", "birth": -490, "death": -420 },
{ "name": "Antiphon", "birth": -480, "death": -410 },
{ "name": "Gorgias", "birth": -480, "death": -375 },
{ "name": "Aristippe", "birth": -435, "death": -356 },
{ "name": "Antisthène", "birth": -444, "death": -365 },
{ "name": "Diogène de Sinope", "birth": -413, "death": -327 },
{ "name": "Prodicos", "birth": -470, "death": -399 },
{ "name": "Eudoxe", "birth": -408, "death": -355 },
{ "name": "Épicure", "birth": -331, "death": -270 },
{ "name": "Philodème de Gadara", "birth": -110, "death": -40 },
{ "name": "Lucrèce", "birth": -94, "death": -55 },
{ "name": "Xénophane", "birth": -570, "death": -475 },
{ "name": "Zénon", "birth": -490, "death": -430 },
{ "name": "Pythagore", "birth": -580, "death": -495 },
{ "name": "Socrate", "birth": -470, "death": -399 },
{ "name": "Platon", "birth": -428, "death": -347 },
{ "name": "Xénophon", "birth": -445, "death": -354 },
{ "name": "Zénon de Cition", "birth": -335, "death": -263 },
{ "name": "Cléanthe", "birth": -330, "death": -232 },
{ "name": "Chrysippe", "birth": -280, "death": -206 },
{ "name": "Cicéron", "birth": -106, "death": -43 },
{ "name": "Sénèque", "birth": 4, "death": 65 },
{ "name": "Épictète", "birth": 50, "death": 130 },
{ "name": "Marc Aurèle", "birth": 121, "death": 180 },
{ "name": "Catulle", "birth": -84, "death": -54 },
{ "name": "Properce", "birth": -47, "death": 15 },
{ "name": "Tibulle", "birth": -54, "death": -19 },
{ "name": "Alexandre le Grand", "birth": -356, "death": -323 },
{ "name": "Jules César", "birth": -100, "death": -44 },
]

age = lambda s: s["death"] - s["birth"]

# names = sorted(map_rec(lambda s: s["name"], sages))
# names = sorted([s["name"] for s in sages])
# print(names)

# most_ancient = sorted(sages, key=lambda s: s["birth"])[0]
# print(most_ancient)

# most_longlived = sorted(sages, key=age, reverse=True)[0]
# print(most_longlived)

# mean_age = sum(map_rec(age, sages)) / len(sages)
# print(mean_age)

################################################################
def map_func(x):
    return [ (x%2, x) ]

def reduce_func(x):
    word, occurances = x
    return (word, sum(occurances))

def map_reduce1():
    num_workers = 5
    inputs = range(10)
    with multiprocessing.Pool(num_workers) as pool:
        map_responses = pool.map(map_func, inputs)
        print(map_responses) # results of maps
        mapped_values = itertools.chain(*map_responses) # concat
        partitioned_data = collections.defaultdict(list)
        for a_value in mapped_values:
            partitioned_data[a_value[0]].append(a_value[1])
        print(partitioned_data.items()) # first step of reduce
        reduced_values = pool.map(reduce_func, partitioned_data.items())
        print(reduced_values)

def scrape(url):
    print("Scraping '{}'".format(url))
    res = requests.get(url)
    print("Returned {} ({})".format(res.url, res.status_code))
    return res

def map_reduce2():
    num_workers = 5
    all_urls = [
        "https://www.labri.fr/perso/renault",
        "https://www.labri.fr/perso/borgne",
        "https://www.labri.fr/perso/rollet",
        ]
    all_urls = [ 1, 2, 3 ]
    with multiprocessing.Pool(num_workers) as pool:
        results = pool.map(time.sleep, all_urls)
        print(results)

map_reduce2()
