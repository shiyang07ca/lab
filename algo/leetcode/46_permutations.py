"""

46. 全排列
给定一个 *不含重复* 数字的数组 nums ，返回其 所有可能的全排列 。你可以 按任意顺序 返回答案。



示例 1：

输入：nums = [1,2,3]
输出：[[1,2,3],[1,3,2],[2,1,3],[2,3,1],[3,1,2],[3,2,1]]
示例 2：

输入：nums = [0,1]
输出：[[0,1],[1,0]]
示例 3：

输入：nums = [1]
输出：[[1]]


提示：

1 <= nums.length <= 6
-10 <= nums[i] <= 10
nums 中的所有整数 互不相同

"""

from typing import List


from copy import deepcopy

class Solution:
    def process(self, nums, i, ans):
        if i == len(nums):
            ans.append(deepcopy(nums))

        for j in range(i, len(nums)):
            nums[i], nums[j] = nums[j], nums[i]
            self.process(nums, i + 1, ans)
            nums[i], nums[j] = nums[j], nums[i]

    def permute(self, nums: List[int]) -> List[List[int]]:
        ans = []
        self.process(nums, 0, ans)
        return sorted(ans)


import unittest


class TestSolution(unittest.TestCase):
    def setUp(self):
        self.sl = Solution()

    def test_sl(self):
        nums = [1, 2, 3]
        # print(tuple(self.sl.permute(nums)))
        self.assertEqual(
            self.sl.permute(nums),
            [[1, 2, 3], [1, 3, 2], [2, 1, 3], [2, 3, 1], [3, 1, 2], [3, 2, 1]],
        )

        nums = [0, 1]
        self.assertEqual(self.sl.permute(nums), [[0, 1], [1, 0]])

        nums = [1]
        self.assertEqual(self.sl.permute(nums), [[1]])


if __name__ == "__main__":
    unittest.main()
