"""
"""
"""
"""


"""

线段树

线段树是一棵二叉树，线段树上每个结点对应的是序列的一段区间，每一个叶子结点对应的
是序列的一个元素。

树上的每个节点都维护一个区间，根维护的是整个区间，每个节点维护的是父亲的区间二等
分后的其中一个子区间。

当有 n 个元素时，对区间的操作可以在 O(logn) 复杂度时间内完成。

另外，从二叉树结构上，可以看出线段树是一棵完美二叉树（Perfect Binary Tree），即
所有叶子的深度都相同，

并且每个节点要么是叶子，要么有 2 个子树。


ref:
https://www.desgard.com/algo/docs/part3/ch02/1-segment-tree-rmq/




lazy 线段树

问题：一个数组，更新一个子数组的值（都加上一个数、把子数组内的元素取反，...）
                查询一个子数组的值（求和，求最大值, ...）


两大思想
1. 挑选 O(n) 个特殊区间，使得任意一个区间可以拆分为 O(log n) 个特殊区间


"""


def build(o: int, l: int, r: int) -> None:
    if l == r:
        return
    m = (l + r) // 2
    build(o * 2, l, m)
    build(o * 2 + 1, m + 1, r)
    # maintain


# 更新 [L, R]
def update(o: int, l: int, r: int, L: int, R: int) -> None:
    if L <= l and r <= R:
        return
