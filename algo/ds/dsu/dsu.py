"""

# https://oi-wiki.org/ds/dsu/
# https://cp-algorithms.com/data_structures/disjoint_set_union.html

并查集
Disjoint Set Union or DSU. Often it is also called Union Find




"""


# class DSU:
#     def __init__(self):
#         self.pa = {}

#     def find(self, x):
#         if self.pa[x] != x:
#             # 路径压缩
#             self.pa[x] = self.find(self.pa[x])
#         return self.pa[x]

#     def union(self, a, b):
#         self.pa[self.find(a)] = self.find(b)


N = 10**7 + 10
p = list(range(N))
size = [1] * N


def find(x):
    if p[x] != x:
        p[x] = find(p[x])
    return p[x]


def union(a, b):
    pa, pb = find(a), find(b)
    if pa == pb:
        return
    p[pa] = pb
    size[pb] += size[pa]


import unittest


class TestSolution(unittest.TestCase):
    def setUp(self):
        """"""

    def test1(self):
        def is_same_set(a, b):
            sets = ({0, 1, 2}, {3, 4, 5})
            for s in sets:
                if a in s and b in s:
                    return True

        union(0, 1)
        union(1, 2)

        union(3, 4)
        union(3, 5)

        vs = range(0, 6)
        for v0 in vs:
            for v1 in vs:
                if is_same_set(v0, v1):
                    # print(v0, v1)
                    self.assertEqual(find(v0) == find(v1), True)
                else:
                    self.assertEqual(find(v0) != find(v1), True)


if __name__ == "__main__":
    unittest.main()
