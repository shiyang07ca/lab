"""

[982] Triples with Bitwise AND Equal To Zero


Given an integer array nums, return the number of AND triples.

An AND triple is a triple of indices (i, j, k) such that:


	0 <= i < nums.length
	0 <= j < nums.length
	0 <= k < nums.length
	nums[i] & nums[j] & nums[k] == 0, where & represents the bitwise-AND operator.



Example 1:


Input: nums = [2,1,3]
Output: 12
Explanation: We could choose the following i, j, k triples:
(i=0, j=0, k=1) : 2 & 2 & 1
(i=0, j=1, k=0) : 2 & 1 & 2
(i=0, j=1, k=1) : 2 & 1 & 1
(i=0, j=1, k=2) : 2 & 1 & 3
(i=0, j=2, k=1) : 2 & 3 & 1
(i=1, j=0, k=0) : 1 & 2 & 2
(i=1, j=0, k=1) : 1 & 2 & 1
(i=1, j=0, k=2) : 1 & 2 & 3
(i=1, j=1, k=0) : 1 & 1 & 2
(i=1, j=2, k=0) : 1 & 3 & 2
(i=2, j=0, k=1) : 3 & 2 & 1
(i=2, j=1, k=0) : 3 & 1 & 2


Example 2:


Input: nums = [0,0,0]
Output: 27



Constraints:


	1 <= nums.length <= 1000
	0 <= nums[i] < 2¹⁶


################################################################

# TODO

982. 按位与为零的三元组

给你一个整数数组 nums ，返回其中 按位与三元组 的数目。

按位与三元组 是由下标 (i, j, k) 组成的三元组，并满足下述全部条件：

0 <= i < nums.length
0 <= j < nums.length
0 <= k < nums.length
nums[i] & nums[j] & nums[k] == 0 ，其中 & 表示按位与运算符。

示例 1：

输入：nums = [2,1,3]
输出：12
解释：可以选出如下 i, j, k 三元组：
(i=0, j=0, k=1) : 2 & 2 & 1
(i=0, j=1, k=0) : 2 & 1 & 2
(i=0, j=1, k=1) : 2 & 1 & 1
(i=0, j=1, k=2) : 2 & 1 & 3
(i=0, j=2, k=1) : 2 & 3 & 1
(i=1, j=0, k=0) : 1 & 2 & 2
(i=1, j=0, k=1) : 1 & 2 & 1
(i=1, j=0, k=2) : 1 & 2 & 3
(i=1, j=1, k=0) : 1 & 1 & 2
(i=1, j=2, k=0) : 1 & 3 & 2
(i=2, j=0, k=1) : 3 & 2 & 1
(i=2, j=1, k=0) : 3 & 1 & 2


示例 2：

输入：nums = [0,0,0]
输出：27


提示：

1 <= nums.length <= 1000
0 <= nums[i] < 216

"""

import sys
import inspect
import os
import unittest

from itertools import *
from collections import *
from copy import *
from typing import *
from math import *

from os.path import abspath, join, dirname

currentdir = os.path.dirname(os.path.abspath(inspect.getfile(inspect.currentframe())))
parentdir = os.path.dirname(currentdir)
parentdir = os.path.dirname(parentdir)  # algo
parentdir = os.path.dirname(parentdir)  # leetcode
parentdir = os.path.dirname(parentdir)  # oj
parentdir = os.path.dirname(parentdir)  # algo
sys.path.insert(0, parentdir)
# print(sys.path)


from algo.tree.builder import *

"""

https://leetcode.cn/problems/triples-with-bitwise-and-equal-to-zero/solution/you-ji-qiao-de-mei-ju-chang-shu-you-hua-daxit/

暴力枚举 i，j，k 的话，时间复杂度O(n^3)

对于 nums[k] 来说，只需要知道它 AND 一个数的结果是否等于 0，至于这个数是由哪些
nums[i] AND nums[j] 得到的，并不重要

因此，可以先写一个 O(n^2) 的枚举，预处理所有 nums[i] AND nums[j] 的出现次数，存
到哈希表 cnt 中。然后枚举 nums[k] 和 x，如果 nums[k] AND x 等于 0，那就把 cnt[x]
加到答案中

"""


class Solution:
    def countTriplets(self, nums: List[int]) -> int:
        cnt = Counter(x & y for x in nums for y in nums)
        return sum(c for x, c in cnt.items() for y in nums if x & y == 0)


# 注：这一技巧经常用于子集状压 DP 中
# TODO
"""

如果把二进制数看成集合的话，二进制从低到高第 i 位为 1 表示 i 在集合中，为 0 表示
i 不在集合中，例如 a=1101(2) 表示集合 A={0,2,3}。

那么 a AND b=0 相当于集合
A 和集合 B 没有交集，也可以理解成 B 是 CuA 的子集，这里 U={0,1,2,⋯,15}，对应的数
字就是 0xffff。一个数异或 0xffff 就可以得到这个数的补集了。

因此，上面的代码可以优化成枚举 m=nums[k]⊕0xffff 的子集。

怎么枚举m 的子集 s 呢？可以从 m 不断减一，直到 0，如果s AND m=s 就表示s 是 m 的
子集。

更高效的做法是直接「跳到」下一个子集，即 s 更新为 (s−1) AND m。这样做的正确性在
于，s−1 仅仅把 s 最低位的 1 改成了 0，比这个 1 更低的 0 全部改成了 1，因此下一个
子集一定是s−1 的子集，直接 AND m，就能得到下一个子集了。

最后，当 s=0 时，由于 −1 的二进制全为 1，所以 (s−1) AND m=m，因此我们可以通过判
断下一个子集是否又回到 m，来判断是否要退出循环。

注：这一技巧经常用于子集状压 DP 中。

"""


class Solution:
    def countTriplets(self, nums: List[int]) -> int:
        cnt = [0] * (1 << 16)
        for x in nums:
            for y in nums:
                cnt[x & y] += 1
        ans = 0
        for m in nums:
            m ^= 0xFFFF
            s = m
            while True:  # 枚举 m 的子集（包括空集）
                ans += cnt[s]
                s = (s - 1) & m
                if s == m:
                    break
        return ans


class TestSolution(unittest.TestCase):
    def setUp(self):
        self.sl = Solution()

    def test_sl(self):
        self.assertEqual(
            self.sl,
            None,
        )


if __name__ == "__main__":
    unittest.main()
