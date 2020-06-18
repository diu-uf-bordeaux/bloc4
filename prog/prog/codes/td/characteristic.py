import functools
import math

################################################################
def set_all(x):
    return True

def set_empty(x):
    return False

def set_single(x):
    return lambda y: (x == y)

def belongs(s, x):
    return s(x)

def set_complement(s):
    return lambda y: not(s(y))

def set_union(s1, s2):
    return lambda y: s1(y) or s2(y)

def set_intersection(s1, s2):
    return lambda y: s1(y) and s2(y)

def set_add(s, x):
    return lambda y: s(y) or y == x

def set_diffs(s1, s2):
    return lambda y: s1(y) != s2(y)

################################################################
import numpy as np
import matplotlib.pyplot as mp

def set_display_2d_generic(c1, c2, n, s):
    """ Draw a set s with matplotlib inside a window
        c1 is the lower left point
        c2 is the upper right point
        n is the number of divisions """
    h1 = (c2[0] - c1[0]) / n
    h2 = (c2[1] - c1[1]) / n
    m = np.zeros((n,n))
    for i in range(n):
        for j in range(n):
            m[i,j] = 1 if s((c1[1] + j * h2,
                             c2[0] - i * h1)) else 0
    mp.imshow(m,extent=[c1[0],c2[0],c1[1],c2[1]])
    mp.show()

def set_display_2d(s):
    set_display_2d_generic((0,0), (10,10), 200, s)

def dist(p1, p2):
    return np.sqrt((p1[0] - p2[0])**2 + (p1[1] - p2[1])**2)

def set_circle(c, r):
    return lambda y: dist(y, c) <= r

def set_square(p1, p2):
    return lambda y: y[0] >= p1[0] and y[0] <= p2[0] and \
        y[1] >= p1[1] and y[1] <= p2[1]

def translate(deltax, deltay):
    return lambda p: (p[0] + deltax, p[1] + deltay)

def scale(a, b):
    return lambda p: (p[0] * a, p[1] * b)

def rotate(theta):
    costheta = math.cos(theta)
    sintheta = math.sin(theta)
    return lambda p: (p[0] * costheta - p[1] * sintheta, \
                      p[1] * costheta + p[0] * sintheta)

def set_translate(s, deltax, deltay):
    return lambda p: s(translate(-deltax, -deltay)(p))

def set_scale(s, a, b):
    return lambda p: s(scale(1./a,1./b)(p))

def set_rotate(s, theta):
    return lambda p: s(rotate(-theta)(p))

def set_rotate_rel(s, theta, p):
    cen_x = p[0]
    cen_y = p[1]
    return lambda p: s(translate(cen_x, cen_y)(rotate(theta)(translate(-cen_x,-cen_y)(p))))

def wheel(s, p, n):
    cen_x = p[0]
    cen_y = p[1]
    theta = 2. * 3.1415927 / n
    all_rots = [ set_rotate_rel(s, theta*i, p) for i in range(n) ]
    return functools.reduce(set_diffs, all_rots, set_all)

################################################################
x = 1
assert(belongs(set_all, x))
assert(not(belongs(set_empty, x)))
assert(belongs(set_single(x), x))
assert(not(belongs(set_single(x), x+1)))
assert(dist((1,1),(1,1)) < 0.01)
assert((dist((1,1),(2,1)) - 1) < 0.01)
assert((dist((1,1),(2,2)) - 1.414) < 0.01)

c1 = set_circle((5,5), 3)
c2 = set_complement(set_circle((7.5,3.5), 1))
r  = set_square((4,0),(10,10))
s = set_intersection(set_intersection(c1,c2), r)

# set_display_2d(wheel(s,(5,5),12))

s = set_scale(set_circle((7.5,10), 3), 1, 0.5)
set_display_2d(wheel(s,(5,5),24))

s = set_empty
for i in range(1, 10):
    for j in range(1, 10):
        s = set_add(s, (i,j))

# set_display_2d(s)

################################################################
import random

songs = [ \
{ "title": "Walking on Broken Glass", "artist": "Annie Lennox", "album": "Diva", "track": 2, "genre": "pop rock" },
{ "title": "Roar", "artist": "Katy Perry", "album": "PRISM", "track": 1, "genre": "power pop" },
{ "title": "Don't Wanna Fight", "artist": "Alabama Shakes", "album": "Sound & Color", "track": 2, "genre": "blues rock" },
{ "title": "Grace Kelly", "artist": "Mika", "album": "Life in Cartoon Motion", "track": 1, "genre": "glam rock" },
{ "title": "Don't Stop Me Now", "artist": "Queen", "album": "Jazz", "track": 6, "genre": "pop rock" },
{ "title": "Black Pearls", "artist": "Apollo Brown", "album": "Clouds", "track": 7, "genre": "hip hop underground" },
]

r1 = lambda m: "rock" in m["genre"]
r2 = lambda m: m["title"].startswith("Don't")

def generate_playlist(req, n):
    res = []
    valid_songs = [ s for s in songs if req(s) ]
    if len(valid_songs) == 0:
        return res
    for i in range(n):
        res.append(random.choice(valid_songs))
    return res

# print(generate_playlist(r1, 5))
# print(generate_playlist(r2, 5))
