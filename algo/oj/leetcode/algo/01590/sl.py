"""

[1590] Make Sum Divisible by P


Given an array of positive integers nums, remove the smallest subarray (possibly empty) such that the sum of the remaining elements is divisible by p. It is not allowed to remove the whole array.

Return the length of the smallest subarray that you need to remove, or -1 if it's impossible.

A subarray is defined as a contiguous block of elements in the array.


Example 1:


Input: nums = [3,1,4,2], p = 6
Output: 1
Explanation: The sum of the elements in nums is 10, which is not divisible by 6. We can remove the subarray [4], and the sum of the remaining elements is 6, which is divisible by 6.


Example 2:


Input: nums = [6,3,5,2], p = 9
Output: 2
Explanation: We cannot remove a single element to get a sum divisible by 9. The best way is to remove the subarray [5,2], leaving us with [6,3] with sum 9.


Example 3:


Input: nums = [1,2,3], p = 3
Output: 0
Explanation: Here the sum is 6. which is already divisible by 3. Thus we do not need to remove anything.



Constraints:


	1 <= nums.length <= 10⁵
	1 <= nums[i] <= 10⁹
	1 <= p <= 10⁹

################################################################

# TODO

1590. 使数组和能被 P 整除

给你一个正整数数组 nums，请你移除 最短 子数组（可以为 空），使得剩余元素的 和 能被 p 整除。 不允许 将整个数组都移除。

请你返回你需要移除的最短子数组的长度，如果无法满足题目要求，返回 -1 。

子数组 定义为原数组中连续的一组元素。



示例 1：

输入：nums = [3,1,4,2], p = 6
输出：1
解释：nums 中元素和为 10，不能被 p 整除。我们可以移除子数组 [4] ，剩余元素的和为 6 。


示例 2：

输入：nums = [6,3,5,2], p = 9
输出：2
解释：我们无法移除任何一个元素使得和被 9 整除，最优方案是移除子数组 [5,2] ，剩余元素为 [6,3]，和为 9 。


示例 3：

输入：nums = [1,2,3], p = 3
输出：0
解释：和恰好为 6 ，已经能被 3 整除了。所以我们不需要移除任何元素。


示例  4：

输入：nums = [1,2,3], p = 7
输出：-1
解释：没有任何方案使得移除子数组后剩余元素的和被 7 整除。


示例 5：

输入：nums = [1000000000,1000000000,1000000000], p = 3
输出：0


提示：

1 <= nums.length <= 105
1 <= nums[i] <= 109
1 <= p <= 109

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

https://leetcode.cn/problems/make-sum-divisible-by-p/solution/tao-lu-qian-zhui-he-ha-xi-biao-pythonjav-rzl0/

相似题目（前缀和+哈希表）
推荐按照顺序完成。

LC560. 和为 K 的子数组 https://leetcode.cn/problems/subarray-sum-equals-k/
LC974. 和可被 K 整除的子数组 https://leetcode.cn/problems/subarray-sums-divisible-by-k/
LC523. 连续的子数组和 https://leetcode.cn/problems/continuous-subarray-sum/
LC525. 连续数组 https://leetcode.cn/problems/contiguous-array/


"""


class Solution:
    def minSubarray(self, nums: List[int], p: int) -> int:
        s = list(accumulate(nums, initial=0))
        x = s[-1] % p
        if x == 0:
            return 0  # 移除空子数组（这行可以不要）

        ans = n = len(nums)
        last = {}
        for i, v in enumerate(s):
            last[v % p] = i
            j = last.get((v - x) % p, -n)  # 如果不存在，-n 可以保证 i-j >= n
            ans = min(ans, i - j)
        return ans if ans < n else -1


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
