"""

# https://oi-wiki.org/ds/dsu/
# https://cp-algorithms.com/data_structures/disjoint_set_union.html

并查集
Disjoint Set Union or DSU. Often it is also called Union Find




"""


class DSU:
    def __init__(self):
        self.pa = {}

    def find(self, x):
        if self.pa[x] != x:
            # 路径压缩
            self.pa[x] = self.find(self.pa[x])
        return self.pa[x]

    def union(self, a, b):
        self.pa[self.find(a)] = self.find(b)


import unittest


class TestSolution(unittest.TestCase):
    def setUp(self):
        """"""

    def test1(self):
        d1 = DSU()
        d2 = DSU()

        d1.union(1, 1)
        d2.union(1, 1)


if __name__ == "__main__":
    unittest.main()
