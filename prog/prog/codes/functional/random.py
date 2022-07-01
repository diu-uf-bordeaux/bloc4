seed = 12345
M = 65537
A = 75

def rand():
    global seed
    seed = (A * seed) % M
    return seed

for i in range(6):
    print(rand())
# -> [ 8357, 36942, 18096, 46460, 11039, 41481 ]


def make_rand():
    int_seed = 12345
    int_M = 65537
    int_A = 75
    def int_rand():
        nonlocal int_seed
        int_seed = (int_A * int_seed) % int_M
        return int_seed
    return int_rand

new_rand = make_rand()
for i in range(6):
    print(new_rand())
# -> [ 8357, 36942, 18096, 46460, 11039, 41481 ]
