"""

# TODO
# tag: BIT
# template

剑指 Offer 51. 数组中的逆序对


在数组中的两个数字，如果前面一个数字大于后面的数字，则这两个数字组成一个逆序对。输入一个数组，求出这个数组中的逆序对的总数。



示例 1:

输入: [7,5,6,4]
输出: 5


限制：

0 <= 数组长度 <= 50000

"""


import sys
import inspect
import os
import unittest
from os.path import abspath, join, dirname
from typing import *

currentdir = os.path.dirname(os.path.abspath(inspect.getfile(inspect.currentframe())))
parentdir = os.path.dirname(currentdir)
parentdir = os.path.dirname(parentdir)  # algo
parentdir = os.path.dirname(parentdir)  # leetcode
parentdir = os.path.dirname(parentdir)  # algo
sys.path.insert(0, parentdir)

import bisect


"""

作者：LeetCode-Solution
链接：https://leetcode.cn/problems/shu-zu-zhong-de-ni-xu-dui-lcof/solution/shu-zu-zhong-de-ni-xu-dui-by-leetcode-solution/
来源：力扣（LeetCode）
著作权归作者所有。商业转载请联系作者获得授权，非商业转载请注明出处。


思路

记题目给定的序列为 a，我们规定 ai 的取值集合为 a 的「值域」。我们用桶来表示值域中的每一个数，
桶中记录这些数字出现的次数。假设 a = {5,5,2,3,6}，那么遍历这个序列得到的桶是这样的：

index  ->  1 2 3 4 5 6 7 8 9
value  ->  0 1 1 0 2 1 0 0 0

我们可以看出它第 i - 1 位的前缀和表示「有多少个数比 i 小」。
那么我们可以从后往前遍历序列 a，记当前遍历到的元素为 ai ，我们把 ai 对应的桶的值自增 1，
把 i - 1 位置的前缀和加入到答案中算贡献。为什么这么做是对的呢，因为我们在循环的过程中，
我们把原序列分成了两部分，后半部部分已经遍历过（已入桶），前半部分是待遍历的（未入桶），
那么我们求到的 i - 1 位置的前缀和就是「已入桶」的元素中比 ai大的元素的总和，
而这些元素在原序列中排在 ai 的后面，但它们本应该排在 ai 的前面，这样就形成了逆序对。

我们显然可以用数组来实现这个桶，可问题是如果 ai 中有很大的元素，比如 10^9 ，我们就要开一个大小为 10^9
 的桶，内存中是存不下的。这个桶数组中很多位置是 0，有效位置是稀疏的，
我们要想一个办法让有效的位置全聚集到一起，减少无效位置的出现，这个时候我们就需要用到一个方法——离散化。

离散化一个序列的前提是我们只关心这个序列里面元素的相对大小，而不关心绝对大小（即只关心元素在序列中的排名）；
离散化的目的是让原来分布零散的值聚集到一起，减少空间浪费。那么如何获得元素排名呢，
我们可以对原序列排序后去重，对于每一个 ai 通过二分查找的方式计算排名作为离散化之后的值。
当然这里也可以不去重，不影响排名。


"""


class BIT:
    def __init__(self, n):
        self.n = n
        self.tree = [0] * (n + 1)

    @staticmethod
    def lowbit(x):
        return x & (-x)

    def query(self, x):
        ans = 0
        while x > 0:
            ans += self.tree[x]
            x -= BIT.lowbit(x)

        return ans

    def update(self, x):
        while x <= self.n:
            self.tree[x] += 1
            x += BIT.lowbit(x)


class Solution1:
    def reversePairs(self, nums: List[int]) -> int:
        n = len(nums)
        # 离散化
        tmp = sorted(nums)
        for i in range(n):
            nums[i] = bisect.bisect_left(tmp, nums[i]) + 1
        # print(f"nums: {nums}")
        # 树状数组统计逆序对
        bit = BIT(n)
        ans = 0
        for i in range(n - 1, -1, -1):
            ans += bit.query(nums[i] - 1)
            bit.update(nums[i])
        return ans


class Solution1a:
    def reversePairs(self, nums: List[int]) -> int:
        self.count = 0

        self.merge_count(nums)

        return self.count

    def merge_count(self, a):
        N = len(a)
        if N <= 1:
            return a
        mid = N // 2
        left, right = self.merge_count(a[:mid]), self.merge_count(a[mid:])
        self.merge(left, right, a)

        return a

    def merge(self, left, right, merged):
        l, r = 0, 0
        while l < len(left) and r < len(right):
            if left[l] <= right[r]:
                merged[l + r] = left[l]
                l += 1
            else:
                # print(
                #     f"count: {self.count}, left: {left}, right: {right}, mid:{mid}, l:{l}, {mid-l+1}"
                # )
                # 右数组元素放入排序数组时，统计逆序数
                # len(left) - 1 - l + 1 为当前 l 指向元素的逆序数
                self.count += len(left) - 1 - l + 1
                merged[l + r] = right[r]
                r += 1

        for l in range(l, len(left)):
            merged[l + r] = left[l]
        for r in range(r, len(right)):
            merged[l + r] = right[r]


# lc 315 计算右侧小于当前元素的个数
class Solution2:
    def reversePairs(self, nums: List[int]) -> int:
        n = len(nums)
        # 离散化
        tmp = sorted(nums)
        for i in range(n):
            nums[i] = bisect.bisect_left(tmp, nums[i]) + 1
        # print(f"nums: {nums}")
        # 树状数组统计逆序对
        bit = BIT(n)
        ans = []
        for i in range(n - 1, -1, -1):
            ans.insert(0, bit.query(nums[i] - 1))
            bit.update(nums[i])
        return ans


import unittest


class TestSolution(unittest.TestCase):
    def setUp(self):
        self.sl = Solution1()

        self.sl1a = Solution1a()

        self.sl2 = Solution2()

    def test_sl(self):
        n = [7, 5, 6, 4]
        # print(n)
        self.assertEqual(self.sl.reversePairs(n), 5)

    def test_sl1a(self):
        n = [7, 5, 6, 4]
        print(f"pre: {n}")
        ans = self.sl1a.reversePairs(n)
        print(f"after: {n}")
        self.assertEqual(ans, 5)

        n = [1,3,2,3,1]
        print(f"pre: {n}")
        ans = self.sl1a.reversePairs(n)
        print(f"after: {n}")
        self.assertEqual(ans, 4)


    def test_sl2(self):
        n = [5, 2, 6, 1]
        self.assertEqual(self.sl2.reversePairs(n), [2, 1, 1, 0])

        n = [-1]
        self.assertEqual(self.sl2.reversePairs(n), [0])

        n = [-1, -1]
        self.assertEqual(self.sl2.reversePairs(n), [0, 0])


if __name__ == "__main__":
    unittest.main()
