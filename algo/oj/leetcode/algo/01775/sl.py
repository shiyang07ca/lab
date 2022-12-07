"""

[1775] Equal Sum Arrays With Minimum Number of Operations


You are given two arrays of integers nums1 and nums2, possibly of different lengths. The values in the arrays are between 1 and 6, inclusive.

In one operation, you can change any integer&#39;s value in any of the arrays to any value between 1 and 6, inclusive.

Return the minimum number of operations required to make the sum of values in nums1 equal to the sum of values in nums2. Return -1​​​​​ if it is not possible to make the sum of the two arreq.</p>
&"example">tr/>
<str:</strong> nums1 = [1,2,3,4,5,6], nums2 = [1,1]
<stro:</3
<strong>Ex:</strong> You can make the sums of nums1 and nums2 equal with 3 operations. All indices are 0-indexed.
- Change nums2[0] to 6. nums1 = [1,2,3,4,5,6],utrong></u>,1,2,2,2,2].
- Change nums1[5] to 1. nums1 = [s></strong>], nums2 = [6,1,2,2,2,2].
- Change nums1[2] to 2. nums></strong>,4,5,1], nums2 = [6,1,2]"example">tr/>
<str:</strong> nums1 = [1,1,1,1,1,1,1], nu]
<stro:</s1
<strong>Ex:</strong> There is no way to decrease the sum of nums1 or to increase the sum of nums2 to make thal"example">tr/>
<str:</strong> nums1 = [6,6], nu]
<stro:</3
<strong>Ex:</strong> You can make the sums of nums1 and nums2 equal with 3 operations. All indices are 0-indexed.
- Change nums1[0] to 2.s></strong>,6], nums2 = [1].
- Change nums1[1] to 2. ns></strong>], nums2 = [1].
- Change nums2[0] to 4. nums1 = [2,2],s></>]/pre>
&p><strong>Cotr</<li><code>1 &lt;= nums1.length, nums2.lengt;co<li><code>1 &lt;= nums1[i], nums2[c/li>
</ul>

################################################################

# TODO
# tag: greedy

1775. 通过最少操作次数使数组的和相等
给你两个长度可能不等的整数数组 nums1 和 nums2 。两个数组中的所有值都在 1 到 6 之间（包含 1 和 6）。

每次操作中，你可以选择 任意 数组中的任意一个整数，将它变成 1 到 6 之间 任意 的值（包含 1 和 6）。

请你返回使 nums1 中所有数的和与 nums2 中所有数的和相等的最少操作次数。如果无法使两个数组的和相等，请返回 -1 。


示例 1：

输入：nums1 = [1,2,3,4,5,6], nums2 = [1,1,2,2,2,2]
输出：3
解释：你可以通过 3 次操作使 nums1 中所有数的和与 nums2 中所有数的和相等。以下数组下标都从 0 开始。
- 将 nums2[0] 变为 6 。 nums1 = [1,2,3,4,5,6], nums2 = [6,1,2,2,2,2] 。
- 将 nums1[5] 变为 1 。 nums1 = [1,2,3,4,5,1], nums2 = [6,1,2,2,2,2] 。
- 将 nums1[2] 变为 2 。 nums1 = [1,2,2,4,5,1], nums2 = [6,1,2,2,2,2] 。


示例 2：

输入：nums1 = [1,1,1,1,1,1,1], nums2 = [6]
输出：-1
解释：没有办法减少 nums1 的和或者增加 nums2 的和使二者相等。


示例 3：

输入：nums1 = [6,6], nums2 = [1]
输出：3
解释：你可以通过 3 次操作使 nums1 中所有数的和与 nums2 中所有数的和相等。以下数组下标都从 0 开始。
- 将 nums1[0] 变为 2 。 nums1 = [2,6], nums2 = [1] 。
- 将 nums1[1] 变为 2 。 nums1 = [2,2], nums2 = [1] 。
- 将 nums2[0] 变为 4 。 nums1 = [2,2], nums2 = [4] 。


提示：

1 <= nums1.length, nums2.length <= 105
1 <= nums1[i], nums2[i] <= 6

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
作者：endlesscheng
链接：https://leetcode.cn/problems/equal-sum-arrays-with-minimum-number-of-operations/solution/mei-xiang-ming-bai-yi-ge-dong-hua-miao-d-ocuu/
来源：力扣（LeetCode）
著作权归作者所有。商业转载请联系作者获得授权，非商业转载请注明出处。

"""


class Solution:
    def minOperations(self, nums1: List[int], nums2: List[int]) -> int:
        if 6 * len(nums1) < len(nums2) or 6 * len(nums2) < len(nums1):
            return -1  # 优化
        d = sum(nums2) - sum(nums1)  # 数组元素和的差，我们要让这个差变为 0
        if d < 0:
            d = -d
            nums1, nums2 = nums2, nums1  # 统一让 nums1 的数变大，nums2 的数变小
        ans = 0
        # 统计每个数的最大变化量（nums1 的变成 6，nums2 的变成 1）
        cnt = Counter(6 - x for x in nums1) + Counter(x - 1 for x in nums2)
        for i in range(5, 0, -1):  # 从大到小枚举最大变化量 5 4 3 2 1
            if i * cnt[i] >= d:  # 可以让 d 变为 0
                return ans + (d + i - 1) // i
            ans += cnt[i]  # 需要所有最大变化量为 i 的数
            d -= i * cnt[i]


class TestSolution(unittest.TestCase):
    def setUp(self):
        self.sl = Solution()

    def test_sl(self):
        nums1 = [1,2,3,4,5,6]
        nums2 = [1,1,2,2,2,2]
        self.assertEqual(
            self.sl.minOperations(nums1, nums2),
            3,
        )

        nums1 = [1,1,1,1,1,1,1]
        nums2 = [6]
        self.assertEqual(
            self.sl.minOperations(nums1, nums2),
            -1,
        )

        nums1 = [6, 6]
        nums2 = [1]
        self.assertEqual(
            self.sl.minOperations(nums1, nums2),
            3,
        )


if __name__ == "__main__":
    unittest.main()
