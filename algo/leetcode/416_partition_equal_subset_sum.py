"""
重要


416. 分割等和子集
给你一个 只包含正整数 的 非空 数组 nums 。请你判断是否可以将这个数组分割成两个子集，使得两个子集的元素和相等。



示例 1：

输入：nums = [1,5,11,5]
输出：true
解释：数组可以分割成 [1, 5, 5] 和 [11] 。
示例 2：

输入：nums = [1,2,3,5]
输出：false
解释：数组不能分割成两个元素和相等的子集。


提示：

1 <= nums.length <= 200
1 <= nums[i] <= 100

"""

from typing import List


class Solution:
    from functools import cache

    # 暴力递归
    @cache
    def recur(self, nums, target, i):
        if target == 0:
            return True

        # 剪枝
        if i == len(nums) or target < 0 or target - nums[i] < 0:
            return False

        return self.recur(nums, target, i + 1) or self.recur(
            nums, target - nums[i], i + 1
        )

    def dp(self, nums, target):
        # dp 数组表示，使用当前位置求和，是否有解
        dp = [False] * (target + 1)
        dp[0] = True
        for num in nums:
            for i in range(target - num, -1, -1):
                # 如果存在 dp[i]，则认为 dp[i + num] 是有解的
                if dp[i]:
                    dp[i + num] = True

                if dp[target]:
                    return True

        return False

    def canPartition(self, nums: List[int]) -> bool:
        if sum(nums) % 2 != 0:
            return False

        # return self.recur(tuple(sorted(nums)), sum(nums) // 2, 0)
        return self.dp(nums, sum(nums) // 2)


import unittest


class TestSolution(unittest.TestCase):
    def setUp(self):
        self.sl = Solution()

    def test_sl(self):
        nums = [3, 3, 3, 4, 5]
        self.assertEqual(self.sl.canPartition(nums), True)

        nums = [1, 2, 3, 5]
        self.assertEqual(self.sl.canPartition(nums), False)

        nums = [1, 2, 3, 4]
        self.assertEqual(self.sl.canPartition(nums), True)

        nums = [1, 5, 11, 5]
        self.assertEqual(self.sl.canPartition(nums), True)

        nums = [1, 2, 5]
        self.assertEqual(self.sl.canPartition(nums), False)

        nums = [
            100,
            100,
            100,
            100,
            100,
            100,
            100,
            100,
            100,
            100,
            100,
            100,
            100,
            100,
            100,
            100,
            100,
            100,
            100,
            100,
            100,
            100,
            100,
            100,
            100,
            100,
            100,
            100,
            100,
            100,
            100,
            100,
            100,
            100,
            100,
            100,
            100,
            100,
            100,
            100,
            100,
            100,
            100,
            100,
            100,
            100,
            100,
            100,
            100,
            100,
            100,
            100,
            100,
            100,
            100,
            100,
            100,
            100,
            100,
            100,
            100,
            100,
            100,
            100,
            100,
            100,
            100,
            100,
            100,
            100,
            100,
            100,
            100,
            100,
            100,
            100,
            100,
            100,
            100,
            100,
            100,
            100,
            100,
            100,
            100,
            100,
            100,
            100,
            100,
            100,
            100,
            100,
            100,
            100,
            100,
            100,
            100,
            100,
            100,
            100,
            100,
            100,
            100,
            100,
            100,
            100,
            100,
            100,
            100,
            100,
            100,
            100,
            100,
            100,
            100,
            100,
            100,
            100,
            100,
            100,
            100,
            100,
            100,
            100,
            100,
            100,
            100,
            100,
            100,
            100,
            100,
            100,
            100,
            100,
            100,
            100,
            100,
            100,
            100,
            100,
            100,
            100,
            100,
            100,
            100,
            100,
            100,
            100,
            100,
            100,
            100,
            100,
            100,
            100,
            100,
            100,
            100,
            100,
            100,
            100,
            100,
            100,
            100,
            100,
            100,
            100,
            100,
            100,
            100,
            100,
            100,
            100,
            100,
            100,
            100,
            100,
            100,
            100,
            100,
            100,
            100,
            100,
            100,
            100,
            100,
            100,
            100,
            100,
            100,
            100,
            100,
            100,
            100,
            100,
            100,
            100,
            100,
            100,
            99,
            97,
        ]
        print(self.sl.canPartition(nums))


if __name__ == "__main__":
    unittest.main()
