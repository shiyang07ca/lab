"""
6355. Count the Number of Fair Pairs

Given a 0-indexed integer array nums of size n and two integers lower and upper, return the number of fair pairs.

A pair (i, j) is fair if:

0 <= i < j < n, and
lower <= nums[i] + nums[j] <= upper


Example 1:

Input: nums = [0,1,7,4,4,5], lower = 3, upper = 6
Output: 6
Explanation: There are 6 fair pairs: (0,3), (0,4), (0,5), (1,3), (1,4), and (1,5).


Example 2:

Input: nums = [1,7,9,2,5], lower = 11, upper = 11
Output: 1
Explanation: There is a single fair pair: (2,3).


Constraints:

1 <= nums.length <= 105
nums.length == n
-109 <= nums[i] <= 109
-109 <= lower <= upper <= 109



################################################################

https://leetcode.cn/problems/count-the-number-of-fair-pairs

# TODO

6355. 统计公平数对的数目

给你一个下标从 0 开始、长度为 n 的整数数组 nums ，和两个整数 lower 和 upper ，返回 公平数对的数目 。

如果 (i, j) 数对满足以下情况，则认为它是一个 公平数对 ：

0 <= i < j < n，且
lower <= nums[i] + nums[j] <= upper


示例 1：

输入：nums = [0,1,7,4,4,5], lower = 3, upper = 6
输出：6
解释：共计 6 个公平数对：(0,3)、(0,4)、(0,5)、(1,3)、(1,4) 和 (1,5) 。


示例 2：

输入：nums = [1,7,9,2,5], lower = 11, upper = 11
输出：1
解释：只有单个公平数对：(2,3) 。


提示：

1 <= nums.length <= 105
nums.length == n
-109 <= nums[i] <= 109
-109 <= lower <= upper <= 109



"""

from sortedcontainers import SortedList
from bisect import *


# TLE
class Solution:
    def countFairPairs(self, nums: List[int], lower: int, upper: int) -> int:
        ans = 0
        a = SortedList([nums[-1]])
        for i in range(len(nums) - 2, -1, -1):
            n = nums[i]
            ans += bisect_right(a, upper - n) - bisect_left(a, lower - n)
            a.add(n)

        return ans


# NOTE
# 这样写不会超时


class Solution:
    def countFairPairs(self, nums: List[int], lower: int, upper: int) -> int:
        ans = 0
        a = SortedList([nums[-1]])
        for i in range(len(nums) - 2, -1, -1):
            n = nums[i]
            ans += a.bisect_right(upper - n) - a.bisect_left(lower - n)
            a.add(n)
        return ans


"""
作者：endlesscheng
链接：https://leetcode.cn/problems/count-the-number-of-fair-pairs/solution/er-fen-cha-zhao-de-ling-huo-yun-yong-by-wplbj/
来源：力扣（LeetCode）
著作权归作者所有。商业转载请联系作者获得授权，非商业转载请注明出处。



由于排序不会影响数对的个数，为了能够二分，可以先排序。

然后枚举 nums[j]，二分查找符合要求的 nums[i] 的个数。



lo <= nums[i] + nums[j] <= hi

=>

lo - nums[j] <= nums[i] <= hi - nums[j]


"""


class Solution:
    def countFairPairs(self, nums: List[int], lower: int, upper: int) -> int:
        ans = 0
        nums.sort()
        for j, x in enumerate(nums):
            r = bisect_right(nums, upper - x, 0, j)
            l = bisect_left(nums, lower - x, 0, j)
            ans += r - l
        return ans
