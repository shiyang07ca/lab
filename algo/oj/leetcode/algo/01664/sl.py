"""

[1664] Ways to Make a Fair Array


You are given an integer array nums. You can choose exactly one index (0-indexed) and remove the element. Notice that the index of the elements may change after the removal.

For example, if nums = [6,1,7,4,1]:


	Choosing to remove index 1 results in nums = [6,7,4,1].
	Choosing to remove index 2 results in nums = [6,1,4,1].
	Choosing to remove index 4 results in nums = [6,1,7,4].


An array is fair if the sum of the odd-indexed values equals the sum of the even-indexed values.

Return the number of indices that you could choose such that after the removal, nums is fair.


Example 1:


Input: nums = [2,1,6,4]
Output: 1
Explanation:
Remove index 0: [1,6,4] -> Even sum: 1 + 4 = 5. Odd sum: 6. Not fair.
Remove index 1: [2,6,4] -> Even sum: 2 + 4 = 6. Odd sum: 6. Fair.
Remove index 2: [2,1,4] -> Even sum: 2 + 4 = 6. Odd sum: 1. Not fair.
Remove index 3: [2,1,6] -> Even sum: 2 + 6 = 8. Odd sum: 1. Not fair.
There is 1 index that you can remove to make nums fair.


Example 2:


Input: nums = [1,1,1]
Output: 3
Explanation: You can remove any index and the remaining array is fair.


Example 3:


Input: nums = [1,2,3]
Output: 0
Explanation: You cannot make a fair array after removing any index.



Constraints:


	1 <= nums.length <= 10⁵
	1 <= nums[i] <= 10⁴

################################################################

1664. 生成平衡数组的方案数

给你一个整数数组 nums 。你需要选择 恰好 一个下标（下标从 0 开始）并删除对应的元素。请注意剩下元素的下标可能会因为删除操作而发生改变。

比方说，如果 nums = [6,1,7,4,1] ，那么：

选择删除下标 1 ，剩下的数组为 nums = [6,7,4,1] 。
选择删除下标 2 ，剩下的数组为 nums = [6,1,4,1] 。
选择删除下标 4 ，剩下的数组为 nums = [6,1,7,4] 。
如果一个数组满足奇数下标元素的和与偶数下标元素的和相等，该数组就是一个 平衡数组 。

请你返回删除操作后，剩下的数组 nums 是 平衡数组 的 方案数 。



示例 1：

输入：nums = [2,1,6,4]
输出：1
解释：
删除下标 0 ：[1,6,4] -> 偶数元素下标为：1 + 4 = 5 。奇数元素下标为：6 。不平衡。
删除下标 1 ：[2,6,4] -> 偶数元素下标为：2 + 4 = 6 。奇数元素下标为：6 。平衡。
删除下标 2 ：[2,1,4] -> 偶数元素下标为：2 + 4 = 6 。奇数元素下标为：1 。不平衡。
删除下标 3 ：[2,1,6] -> 偶数元素下标为：2 + 6 = 8 。奇数元素下标为：1 。不平衡。
只有一种让剩余数组成为平衡数组的方案。


示例 2：

输入：nums = [1,1,1]
输出：3
解释：你可以删除任意元素，剩余数组都是平衡数组。


示例 3：

输入：nums = [1,2,3]
输出：0
解释：不管删除哪个元素，剩下数组都不是平衡数组。


提示：

1 <= nums.length <= 105
1 <= nums[i] <= 104

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


class Solution:
    def waysToMakeFair(self, nums: List[int]) -> int:
        ans, N = 0, len(nums)
        even, odd = [0] * (N + 2), [0] * (N + 2)
        for i in range(N - 1, -1, -1):
            if i % 2 == 0:
                even[i] = nums[i] + even[i + 2]
            else:
                odd[i] = nums[i] + odd[i + 2]
        #       i
        # 0 1   2   3 4 5
        # even(0:i) + odd(i+1:) == odd(0:i) + even(i+1:)

        for i, n in enumerate(nums):
            if i % 2 == 0:
                if even[0] - even[i] + odd[i + 1] == odd[1] - odd[i + 1] + even[i + 2]:
                    ans += 1
            else:
                if even[0] - even[i + 1] + odd[i + 2] == odd[1] - odd[i] + even[i + 1]:
                    ans += 1

        return ans


"""
作者：lcbin
链接：https://leetcode.cn/problems/ways-to-make-a-fair-array/solution/by-lcbin-3jl3/
来源：力扣（LeetCode）
著作权归作者所有。商业转载请联系作者获得授权，非商业转载请注明出处。


方法一：预处理 + 枚举

我们先预处理得到数组 nums 的偶数下标元素之和 s1 以及奇数下标元素之和 s2

然后从前往后枚举数组 nums 的每个元素 v, 用变量 t1 和 t2 分别记录已遍历的偶数下标
元素之和以及奇数下标元素之和。

我们观察发现，对于当前遍历到的元素 v，如果删除了，那么该元素之后的奇偶下标元素之
和会发生交换。此时，我们先判断该位置下标 i 是奇数还是偶数。

* 如果是偶数下标，删除该元素后，数组的奇数下标元素之和为 t2 + s1 - t1 − v，而偶
数下标元素之和为 t1 + s2 - t2 ，如果这两个和相等，那么就是一个平衡数组，答案加一。

* 如果是奇数下标，删除该元素后，数组的偶数下标元素之和为t1 + s2 - t2 − v，而奇数
下标元素之和为 t2 + s1 - t1 ，如果这两个和相等，那么就是一个平衡数组，答案加一。

然后我们根据下标的奇偶性更新 t1 或 t2，继续遍历下一个元素。遍历完数组后，即可得
到答案。

"""


class Solution:
    def waysToMakeFair(self, nums: List[int]) -> int:
        s1, s2 = sum(nums[::2]), sum(nums[1::2])
        ans = t1 = t2 = 0
        for i, v in enumerate(nums):
            ans += i % 2 == 0 and t2 + s1 - t1 - v == t1 + s2 - t2
            ans += i % 2 == 1 and t2 + s1 - t1 == t1 + s2 - t2 - v
            t1 += v if i % 2 == 0 else 0
            t2 += v if i % 2 == 1 else 0
        return ans


class TestSolution(unittest.TestCase):
    def setUp(self):
        self.sl = Solution()

    def test_sl(self):
        nums = [2, 1, 6, 4]
        self.assertEqual(
            self.sl.waysToMakeFair(nums),
            1,
        )

        nums = [1, 1, 1]
        self.assertEqual(
            self.sl.waysToMakeFair(nums),
            3,
        )

        nums = [1, 2, 3]
        self.assertEqual(
            self.sl.waysToMakeFair(nums),
            0,
        )


if __name__ == "__main__":
    unittest.main()
