class GenericList:

    def __init__(self):
        pass

    def __str__(self):
        raise "Method must be overriden in subclasses"

    def is_empty(self):
        raise "Method must be overriden in subclasses"

    def cons(self, x):
        return NonEmptyList(x, self)

class EmptyList(GenericList):

    def is_empty(self):   return True
    def __str__(self):    return "[]"

class NonEmptyList(GenericList):

    def __init__(self, x, l):
        self._hd = x
        self._tl = l

    def is_empty(self):  return False
    def hd(self):        return self._hd
    def tl(self):        return self._tl
    def __str__(self):   return "{},{}".format(self._hd, self._tl)

# Factory method
def List(*args):
    if args:
        return NonEmptyList(args[0], List(*args[1:]))
    else:
        return EmptyList()

# Convention : never use the classes GenericList, EmptyList and
# NonEmptyList, and always build the lists using the List() method.

l = List()
print(l)
l = List(1, 2, 3)
print(l)
print(l.cons(4).cons(5))

# Now one can implement functions on lists using a functional
# paradigm.

def length(l):
    if l.is_empty():
        return 0
    else:
        return 1 + length(l.tl())

print(length(l.cons(4).cons(5)))
print(length(List()))
