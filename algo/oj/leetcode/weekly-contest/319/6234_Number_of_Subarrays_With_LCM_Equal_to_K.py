"""

6234. Number of Subarrays With LCM Equal to K

Given an integer array nums and an integer k, return the number of subarrays of nums where the least common multiple of the subarray's elements is k.

A subarray is a contiguous non-empty sequence of elements within an array.

The least common multiple of an array is the smallest positive integer that is divisible by all the array elements.



Example 1:

Input: nums = [3,6,2,7,1], k = 6
Output: 4
Explanation: The subarrays of nums where 6 is the least common multiple of all the subarray's elements are:
- [3,6,2,7,1]
- [3,6,2,7,1]
- [3,6,2,7,1]
- [3,6,2,7,1]


Example 2:

Input: nums = [3], k = 2
Output: 0
Explanation: There are no subarrays of nums where 2 is the least common multiple of all the subarray's elements.


Constraints:

1 <= nums.length <= 1000
1 <= nums[i], k <= 1000

################################################################

# TODO

6234. 最小公倍数为 K 的子数组数目

给你一个整数数组 nums 和一个整数 k ，请你统计并返回 nums 的 子数组 中满足 元素最小公倍数为 k 的子数组数目。

子数组 是数组中一个连续非空的元素序列。

数组的最小公倍数 是可被所有数组元素整除的最小正整数。

示例 1 ：

输入：nums = [3,6,2,7,1], k = 6
输出：4
解释：以 6 为最小公倍数的子数组是：
- [3,6,2,7,1]
- [3,6,2,7,1]
- [3,6,2,7,1]
- [3,6,2,7,1]

示例 2 ：

输入：nums = [3], k = 2
输出：0
解释：不存在以 2 为最小公倍数的子数组。


提示：

1 <= nums.length <= 1000
1 <= nums[i], k <= 1000

"""

"""

作者：endlesscheng
链接：https://leetcode.cn/problems/number-of-subarrays-with-lcm-equal-to-k/solution/by-endlesscheng-3qnt/
来源：力扣（LeetCode）
著作权归作者所有。商业转载请联系作者获得授权，非商业转载请注明出处。

"""


class Solution:
    def subarrayLCM(self, nums: List[int], k: int) -> int:
        ans, n = 0, len(nums)
        for i in range(n):
            res = 1
            for j in range(i, n):
                res = lcm(res, nums[j])
                if k % res:
                    break  # 剪枝：LCM 必须是 k 的因子
                if res == k:
                    ans += 1
        return ans
