"""

# TODO
# tag: array

31. 下一个排列
整数数组的一个 排列  就是将其所有成员以序列或线性顺序排列。

例如，arr = [1,2,3] ，以下这些都可以视作 arr 的排列：[1,2,3]、[1,3,2]、[3,1,2]、[2,3,1] 。
整数数组的 下一个排列 是指其整数的下一个字典序更大的排列。更正式地，如果数组的所有排列根据其字典顺序从小到大排列在一个容器中，那么数组的 下一个排列 就是在这个有序容器中排在它后面的那个排列。如果不存在下一个更大的排列，那么这个数组必须重排为字典序最小的排列（即，其元素按升序排列）。

例如，arr = [1,2,3] 的下一个排列是 [1,3,2] 。
类似地，arr = [2,3,1] 的下一个排列是 [3,1,2] 。
而 arr = [3,2,1] 的下一个排列是 [1,2,3] ，因为 [3,2,1] 不存在一个字典序更大的排列。
给你一个整数数组 nums ，找出 nums 的下一个排列。

必须 原地 修改，只允许使用额外常数空间。



示例 1：

输入：nums = [1,2,3]
输出：[1,3,2]


示例 2：

输入：nums = [3,2,1]
输出：[1,2,3]


示例 3：

输入：nums = [1,1,5]
输出：[1,5,1]


提示：

1 <= nums.length <= 100
0 <= nums[i] <= 100


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
# print(sys.path)


from algo.tree.builder import *

"""

# 算法推导

如何得到这样的排列顺序？这是本文的重点。我们可以这样来分析：

1. 我们希望下一个数比当前数大，这样才满足“下一个排列”的定义。因此只需要将后面的「大数」与前面的「小数」交换，就能得到一个更大的数。比如 123456，将 5 和 6 交换就能得到一个更大的数 123465。

2. 我们还希望下一个数增加的幅度尽可能的小，这样才满足“下一个排列与当前排列紧邻“的要求。为了满足这个要求，我们需要：
    1. 在尽可能靠右的低位进行交换，需要从后向前查找
    2. 将一个 尽可能小的「大数」 与前面的「小数」交换。比如 123465，下一个排列应该把
       5 和 4 交换而不是把 6 和 4 交换
    3. 将「大数」换到前面后，需要将「大数」后面的所有数重置为升序，升序排列就是最小的排列。
       以 123465 为例：首先按照上一步，交换 5 和 4，得到 123564；然后需要将 5 之后的数重置为升序，
       得到 123546。显然 123546 比 123564 更小，123546 就是 123465 的下一个排列

以上就是求“下一个排列”的分析过程。


# 算法过程

标准的“下一个排列”算法可以描述为：

1. 从后向前查找第一个相邻升序的元素对 (i,j)，满足 A[i] < A[j]。此时 [j,end) 必然是降序
2. 在 [j,end) 从后向前查找第一个满足 A[i] < A[k] 的 k。A[i]、A[k] 分别就是上文所说的「小数」、「大数」
3. 将 A[i] 与 A[k] 交换
4. 可以断定这时 [j,end) 必然是降序，逆置 [j,end)，使其升序
5. 如果在步骤 1 找不到符合的相邻元素对，说明当前 [begin,end) 为一个降序顺序，则直接跳到步骤 4


作者：imageslr
链接：https://leetcode.cn/problems/next-permutation/solution/xia-yi-ge-pai-lie-suan-fa-xiang-jie-si-lu-tui-dao-/
来源：力扣（LeetCode）
著作权归作者所有。商业转载请联系作者获得授权，非商业转载请注明出处。

"""


class Solution:
    def nextPermutation(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        if len(nums) <= 1:
            return

        i, j = len(nums) - 2, len(nums) - 1
        # find: A[i] < A[j]
        while i >= 0 and nums[i] >= nums[j]:
            i -= 1
            j -= 1

        k = len(nums) - 1
        if i >= 0:  # 找到了第一个升序对
            # 从后向前查找第一个大于 A[i] 的下标
            # find: A[i] < A[k]
            while nums[i] >= nums[k]:
                k -= 1
            # swap A[i], A[k]
            nums[i], nums[k] = nums[k], nums[i]

        # reverse A[j:end]
        l, r = j, len(nums) - 1
        while l < r:
            nums[l], nums[r] = nums[r], nums[l]
            l += 1
            r -= 1


class TestSolution(unittest.TestCase):
    def setUp(self):
        self.sl = Solution()

    def test_sl(self):
        nums = [1, 2, 3]
        self.sl.nextPermutation(nums),
        self.assertEqual(
            nums,
            [1, 3, 2],
        )

        nums = [3, 2, 1]
        self.sl.nextPermutation(nums),
        self.assertEqual(
            nums,
            [1, 2, 3],
        )
        nums = [1, 1, 5]
        self.sl.nextPermutation(nums),
        self.assertEqual(
            nums,
            [1, 5, 1],
        )

        nums = [1, 1]
        self.sl.nextPermutation(nums),
        self.assertEqual(
            nums,
            [1, 1],
        )


if __name__ == "__main__":
    unittest.main()
