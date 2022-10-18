"""

线段树

线段树是一棵二叉树，线段树上每个结点对应的是序列的一段区间，每一个叶子结点对应的是序列的一个元素。
树上的每个节点都维护一个区间，根维护的是整个区间，每个节点维护的是父亲的区间二等分后的其中一个子区间。
当有 n 个元素时，对区间的操作可以在 O(logn) 复杂度时间内完成。
另外，从二叉树结构上，可以看出线段树是一棵完美二叉树（Perfect Binary Tree），即所有叶子的深度都相同，
并且每个节点要么是叶子，要么有 2 个子树。

ref:
https://www.desgard.com/algo/docs/part3/ch02/1-segment-tree-rmq/

"""

import math


class SegmentTree:
    def __init__(self, arr):
        self.N = len(arr)
        self.arr = [None] + arr
        self.tree = [None] * 4 * self.N  # NOTE 节点空间为 arr 长度的 4 倍
        print(self.arr)
        self.build(1, self.N, 1)
        print(self.tree)

    def push_up(self, idx):
        self.tree[idx] = self.tree[idx * 2] + self.tree[idx * 2 + 1]

    def build(self, l, r, idx):
        """
        @param      l 当前节点描述范围的左边界
        @param      r 当前节点左边界
        @param      idx 当前节点下标，tree[idx] 代表当前节点
        """
        if l == r:
            self.tree[idx] = self.arr[l]
        else:
            m = (l + r) // 2
            self.build(l, m, idx * 2)
            self.build(m + 1, r, idx * 2 + 1)
            self.push_up(idx)

    def query(self, L, R):
        """
        @param      L 待查询区间左边界
        @param      R 待查询区间右边界
        @param      idx 当前节点下标，tree[idx] 代表当前节点
        """
        # print(self.N)
        return self._query_recur(L, R, 1, self.N, 1)

    def _query_recur(self, L, R, l, r, idx):
        """
        @param      L 待查询区间左边界
        @param      R 待查询区间右边界
        @param      l 当前节点描述范围的左边界
        @param      r 当前节点描述范围的右边界
        @param      idx 当前节点下标，tree[idx] 代表当前节点
        """
        if L <= l and r <= R:
            return self.tree[idx]
        # elif L > l or R < r:
        #     return -math.inf
        else:
            m = (l + r) // 2
            ret = 0
            if L <= m:
                ret += self._query_recur(L, R, l, m, idx * 2)
            if R > m:
                ret += self._query_recur(L, R, m + 1, r, idx * 2 + 1)

            return ret

    def update(self, p, val):
        """
        @param      p 要更新的节点下标
        @param      val 代表要更新的值
        """
        return self._update_recur(1, self.N, p, val, 1)

    def _update_recur(self, l, r, p, val, idx):
        """
        @param      l 当前节点描述范围的左边界
        @param      r 当前节点描述范围的右边界
        @param      idx 下标，tree[idx] 代表当前节点
        @param      p 要更新的节点下标
        @param      val 代表要更新的值
        """
        if l == r:
            self.tree[idx] = val
            return
        else:
            m = (l + r) // 2
            if p <= m:
                self._update_recur(l, m, p, val, idx * 2)
            else:
                self._update_recur(m + 1, r, p, val, idx * 2 + 1)
            self.push_up(idx)


import unittest


class TestSegmentTree(unittest.TestCase):
    def setUp(self):
        """
                         32
             16                     16
          9       7              8       8
        1   8   3   4          7   1   6   2
        1   2   3   4          5   6   7   8
        """

        arr = [1, 8, 3, 4, 7, 1, 6, 2]
        self.segt = SegmentTree(arr)

    def test1(self):
        print(self.segt.query(1, 3))  # 1 + 8 + 3 = 12
        print(self.segt.query(3, 8))  # 3 + 4 + 7 + 1 + 6 + 2 = 23

        self.segt.update(3, 10)  # [1, 8, 10, 4, 7, 1, 6, 2]
        print(self.segt.query(1, 3))  # 1 + 8 + 10 = 19
        print(self.segt.tree)


if __name__ == "__main__":

    unittest.main()
