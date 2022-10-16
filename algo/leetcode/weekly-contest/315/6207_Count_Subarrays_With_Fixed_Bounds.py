"""

6207. Count Subarrays With Fixed Bounds
You are given an integer array nums and two integers minK and maxK.

A fixed-bound subarray of nums is a subarray that satisfies the following conditions:

The minimum value in the subarray is equal to minK.
The maximum value in the subarray is equal to maxK.
Return the number of fixed-bound subarrays.

A subarray is a contiguous part of an array.



Example 1:

Input: nums = [1,3,5,2,7,5], minK = 1, maxK = 5
Output: 2
Explanation: The fixed-bound subarrays are [1,3,5] and [1,3,5,2].


Example 2:

Input: nums = [1,1,1,1], minK = 1, maxK = 1
Output: 10
Explanation: Every subarray of nums is a fixed-bound subarray. There are 10 possible subarrays.


Constraints:

2 <= nums.length <= 105
1 <= nums[i], minK, maxK <= 106


################################################################

# TODO
# tag: two pointer

6207. 统计定界子数组的数目

给你一个整数数组 nums 和两个整数 minK 以及 maxK 。

nums 的定界子数组是满足下述条件的一个子数组：

子数组中的 最小值 等于 minK 。
子数组中的 最大值 等于 maxK 。
返回定界子数组的数目。

子数组是数组中的一个连续部分。

示例 1：

输入：nums = [1,3,5,2,7,5], minK = 1, maxK = 5
输出：2
解释：定界子数组是 [1,3,5] 和 [1,3,5,2] 。

示例 2：

输入：nums = [1,1,1,1], minK = 1, maxK = 1
输出：10
解释：nums 的每个子数组都是一个定界子数组。共有 10 个子数组。


提示：

2 <= nums.length <= 105
1 <= nums[i], minK, maxK <= 106

"""

"""
作者：endlesscheng
链接：https://leetcode.cn/problems/count-subarrays-with-fixed-bounds/solution/jian-ji-xie-fa-pythonjavacgo-by-endlessc-gag2/
来源：力扣（LeetCode）
著作权归作者所有。商业转载请联系作者获得授权，非商业转载请注明出处。


提示 1
首先考虑一个简单的情况，nums 的所有元素都在 [minK, maxK] 范围内。

在这种情况下，相当于要统计同时包含 minK 和 maxK 的子数组的个数。

我们可以枚举子数组的右端点。遍历 nums，记录 minK 上一次出现的位置 minI 和 maxK 上一次出现的位置 maxI，
当遍历到 nums[i] 时，如果 minK 和 maxK 之前出现过，则左端点 ≤ min(minI,maxI) 的子数组都是合法的，
合法子数组的个数为 min(minI, maxI) + 1。

提示 2
回到原问题，由于子数组不能包含在 [minK, maxK] 范围之外的元素，因此我们还需要记录上一个在 [minK, maxK] 范围之外的 nums[i]
的下标，记作 i0。此时合法子数组的个数为 min(minI, maxI) − i0 。

代码实现时：

为方便计算，可以初始化 minI, maxI, i0 均为 −1。
如果 min(minI, maxI) − i0 < 0，则表示在 i_0 右侧 minK 和 maxK 没有同时出现，此时合法子数组的个数为 0。

"""
from typing import *


class Solution:
    def countSubarrays(self, nums: List[int], min_k: int, max_k: int) -> int:
        ans = 0
        min_i = max_i = i0 = -1
        for i, x in enumerate(nums):
            if x == min_k:
                min_i = i
            if x == max_k:
                max_i = i
            if not min_k <= x <= max_k:
                i0 = i  # 子数组不能包含 nums[i0]
            ans += max(min(min_i, max_i) - i0, 0)
            # 注：上面这行代码，改为手动算 min max 会更快
            # j = min_i if min_i < max_i else max_i
            # if j > i0: ans += j - i0
        return ans


def main():
    sl = Solution()
    nums = [1, 3, 5, 2, 7, 5]
    min_k = 1
    max_k = 5
    assert sl.countSubarrays(nums, min_k, max_k) == 2

    nums = [1, 1, 1, 1]
    min_k = 1
    max_k = 1
    assert sl.countSubarrays(nums, min_k, max_k) == 10


if __name__ == "__main__":
    main()
