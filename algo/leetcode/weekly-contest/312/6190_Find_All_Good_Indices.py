"""

给你一个大小为 n 下标从 0 开始的整数数组 nums 和一个正整数 k 。

对于 k <= i < n - k 之间的一个下标 i ，如果它满足以下条件，我们就称它为一个 好 下标：

下标 i 之前 的 k 个元素是 非递增的 。
下标 i 之后 的 k 个元素是 非递减的 。
按 升序 返回所有好下标。



示例 1：

输入：nums = [2,1,1,1,3,4,1], k = 2
输出：[2,3]
解释：数组中有两个好下标：
- 下标 2 。子数组 [2,1] 是非递增的，子数组 [1,3] 是非递减的。
- 下标 3 。子数组 [1,1] 是非递增的，子数组 [3,4] 是非递减的。
注意，下标 4 不是好下标，因为 [4,1] 不是非递减的。


示例 2：

输入：nums = [2,1,1,2], k = 2
输出：[]
解释：数组中没有好下标。


提示：

n == nums.length
3 <= n <= 105
1 <= nums[i] <= 106
1 <= k <= n / 2

"""
from typing import *

"""

作者：endlesscheng
链接：https://leetcode.cn/problems/find-all-good-indices/solution/d-by-endlesscheng-kya3/
来源：力扣（LeetCode）
著作权归作者所有。商业转载请联系作者获得授权，非商业转载请注明出处。



先倒着遍历，得到从每个位置向后的最长连续非降序列的长度，
然后正着遍历，得到每个位置向前的最长连续非增序列的长度，同时统计答案。

"""


class Solution:
    def goodIndices(self, nums: List[int], k: int) -> List[int]:
        n = len(nums)
        ans = []
        dec = [1] * n
        for i in range(n - 2, k, -1):
            if nums[i] <= nums[i + 1]:
                dec[i] = dec[i + 1] + 1  # 递推
        inc = 1
        for i in range(1, n - k):
            if inc >= k and dec[i + 1] >= k:
                ans.append(i)
            if nums[i - 1] >= nums[i]:
                inc += 1  # 递推
            else:
                inc = 1
        return ans


import unittest


class TestSolution(unittest.TestCase):
    def setUp(self):
        self.sl = Solution()

    def test_sl(self):
        nums = [2, 1, 1, 1, 3, 4, 1]
        k = 2
        self.assertEqual(
            self.sl.goodIndices(nums, k),
            [2, 3],
        )

        nums = [2, 1, 1, 2]
        k = 2
        self.assertEqual(
            self.sl.goodIndices(nums, k),
            [],
        )

        nums = [440043, 276285, 336957]
        k = 1
        self.assertEqual(
            self.sl.goodIndices(nums, k),
            [1],
        )

        nums = [
            878724,
            201541,
            179099,
            98437,
            35765,
            327555,
            475851,
            598885,
            849470,
            943442,
        ]
        k = 4
        self.assertEqual(
            self.sl.goodIndices(nums, k),
            [4, 5],
        )

        nums = [
            433,
            639679,
            267108,
            15179,
            14818,
            10492,
            8478,
            3160,
            2340,
            1506,
            1168,
            1167,
            600,
            523,
            152,
            132,
            111,
            51,
            736058,
            237085,
            943608,
            997519,
            997796,
            998643,
            999914,
            999922,
            999947,
            999971,
            999993,
            999997,
        ]
        k = 10
        self.assertEqual(
            self.sl.goodIndices(nums, k),
            [18],
        )


10


if __name__ == "__main__":
    unittest.main()
