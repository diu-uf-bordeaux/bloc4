import collections
import itertools
import multiprocessing
import requests

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
    with multiprocessing.Pool(num_workers) as pool:
        results = pool.map(scrape, all_urls)
        print(results)

map_reduce2()
