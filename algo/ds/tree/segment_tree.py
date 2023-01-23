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


# 作者：endlesscheng
# 链接：https://leetcode.cn/problems/minimum-cost-to-split-an-array/solution/by-endlesscheng-05s0/
# 来源：力扣（LeetCode）
# 著作权归作者所有。商业转载请联系作者获得授权，非商业转载请注明出处。


# Lazy 线段树模板（区间加，查询区间最小）
n = len(nums)
mn = [0] * (4 * n)
todo = [0] * (4 * n)


def do(o: int, v: int) -> None:
    mn[o] += v
    todo[o] += v


def spread(o: int) -> None:
    v = todo[o]
    if v:
        do(o * 2, v)
        do(o * 2 + 1, v)
        todo[o] = 0


# 区间 [L,R] 内的数都加上 v   o,l,r=1,1,n
def update(o: int, l: int, r: int, L: int, R: int, v: int) -> None:
    if L <= l and r <= R:
        do(o, v)
        return
    spread(o)
    m = (l + r) // 2
    if m >= L:
        update(o * 2, l, m, L, R, v)
    if m < R:
        update(o * 2 + 1, m + 1, r, L, R, v)
    mn[o] = min(mn[o * 2], mn[o * 2 + 1])


# 查询区间 [L,R] 的最小值   o,l,r=1,1,n
def query(o: int, l: int, r: int, L: int, R: int) -> int:
    if L <= l and r <= R:
        return mn[o]
    spread(o)
    m = (l + r) // 2
    if m >= R:
        return query(o * 2, l, m, L, R)
    if m < L:
        return query(o * 2 + 1, m + 1, r, L, R)
    return min(query(o * 2, l, m, L, R), query(o * 2 + 1, m + 1, r, L, R))


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
