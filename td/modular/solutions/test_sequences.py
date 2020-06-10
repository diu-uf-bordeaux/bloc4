import sequences as seq
import unittest

class TestSequences(unittest.TestCase):

    def test_fibo(self) -> None:
        tab = [0, 1, 1, 2, 3, 5, 8, 13, 21, 34]
        for i in range(10):
            assert(seq.fibo_imp(i) == tab[i])
            assert(seq.fibo_rec_double(i) == tab[i])
            assert(seq.fibo_tail_rec(i) == tab[i])

    def test_rowland(self) -> None:
        tab = [7, 7, 8, 9, 10, 15, 18, 19, 20, 21]
        for i in range(10):
            assert(seq.rowland(i) == tab[i])

    def test_catalan(self) -> None:
        tab = [1, 1, 2, 5, 14, 42, 132, 429, 1430, 4862]
        for i in range(10):
            assert(seq.catalan(i) == tab[i])

    def test_log2(self) -> None:
        tab = [0, 0, 1, 1, 2, 2, 2, 2, 3, 3]
        for i in range(10):
            assert(seq.log_2(i) == tab[i])

if __name__ == '__main__':
    unittest.main()
