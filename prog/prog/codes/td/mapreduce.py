import collections
import itertools
import multiprocessing

def map_func(x):
    return [ (x%2, x) ]

def reduce_func(x):
    word, occurances = x
    return (word, sum(occurances))

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
