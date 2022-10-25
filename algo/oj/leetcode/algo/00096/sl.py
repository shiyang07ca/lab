"""

[96] Unique Binary Search Trees


Given an integer n, return the number of structurally unique BST's (binary search trees) which has exactly n nodes of unique values from 1 to n.


--------------------------------------------------

Example 1:


Input: n = 3
Output: 5


--------------------------------------------------

Example 2:


Input: n = 1
Output: 1



Constraints:


	1 <= n <= 19


################################################################

96. 不同的二叉搜索树
给你一个整数 n ，求恰由 n 个节点组成且节点值从 1 到 n 互不相同的 二叉搜索树 有多少种？返回满足题意的二叉搜索树的种数。




示例 1：

   1               1
     3              2
   2                 3
================================================================
   2               3
  1 3             2
                 1
================================================================
   3
  1 2


输入：n = 3
输出：5


示例 2：

输入：n = 1
输出：1


提示：

1 <= n <= 19

"""

from typing import *


class Solution:

    from functools import cache

    # 计算从 [l, r] 每个元素作为根节点，所有二叉搜索树的种数
    # 对于每一个节点 i， 计算 [l, i-1] 的 BST 种数，即 i 的左子树可能性
    # 以及 [i+1, r] 的 BST 种数，即 i 的右子树可能性。
    # 二者相乘，也就是节点 i 作为根节点的 BST 种数
    @cache
    def recurPerms(self, l, r):
        if l > r:
            return 1

        ans = 0
        for i in range(l, r + 1):
            ans += self.recurPerms(l, i - 1) * self.recurPerms(i + 1, r)

        return ans

    def numTrees(self, n: int) -> int:
        return self.recurPerms(1, n)


import unittest


class TestSolution(unittest.TestCase):
    def setUp(self):
        self.sl = Solution()

    def test_sl(self):
        n = 3
        self.assertEqual(
            self.sl.numTrees(n),
            5,
        )

        n = 1
        self.assertEqual(
            self.sl.numTrees(n),
            1,
        )

        n = 20
        print(self.sl.numTrees(n))


if __name__ == "__main__":
    unittest.main()
