"""
2541. Minimum Operations to Make Array Equal II

You are given two integer arrays nums1 and nums2 of equal length n and an integer k. You can perform the following operation on nums1:

Choose two indexes i and j and increment nums1[i] by k and decrement nums1[j] by k. In other words, nums1[i] = nums1[i] + k and nums1[j] = nums1[j] - k.
nums1 is said to be equal to nums2 if for all indices i such that 0 <= i < n, nums1[i] == nums2[i].

Return the minimum number of operations required to make nums1 equal to nums2. If it is impossible to make them equal, return -1.



Example 1:

Input: nums1 = [4,3,1,4], nums2 = [1,3,7,1], k = 3
Output: 2
Explanation: In 2 operations, we can transform nums1 to nums2.
1st operation: i = 2, j = 0. After applying the operation, nums1 = [1,3,4,4].
2nd operation: i = 2, j = 3. After applying the operation, nums1 = [1,3,7,1].
One can prove that it is impossible to make arrays equal in fewer operations.

Example 2:

Input: nums1 = [3,8,5,2], nums2 = [2,4,1,6], k = 1
Output: -1
Explanation: It can be proved that it is impossible to make the two arrays equal.

Constraints:

n == nums1.length == nums2.length
2 <= n <= 105
0 <= nums1[i], nums2[j] <= 109
0 <= k <= 105

"""

"""

2541. 使数组中所有元素相等的最小操作数 II

给你两个整数数组 nums1 和 nums2 ，两个数组长度都是 n ，再给你一个整数 k 。你可以对数组 nums1 进行以下操作：

选择两个下标 i 和 j ，将 nums1[i] 增加 k ，将 nums1[j] 减少 k 。换言之，nums1[i] = nums1[i] + k 且 nums1[j] = nums1[j] - k 。
如果对于所有满足 0 <= i < n 都有 num1[i] == nums2[i] ，那么我们称 nums1 等于 nums2 。

请你返回使 nums1 等于 nums2 的 最少 操作数。如果没办法让它们相等，请你返回 -1 。



示例 1：

输入：nums1 = [4,3,1,4], nums2 = [1,3,7,1], k = 3
输出：2
解释：我们可以通过 2 个操作将 nums1 变成 nums2 。
第 1 个操作：i = 2 ，j = 0 。操作后得到 nums1 = [1,3,4,4] 。
第 2 个操作：i = 2 ，j = 3 。操作后得到 nums1 = [1,3,7,1] 。
无法用更少操作使两个数组相等。


示例 2：

输入：nums1 = [3,8,5,2], nums2 = [2,4,1,6], k = 1
输出：-1
解释：无法使两个数组相等。


提示：

n == nums1.length == nums2.length
2 <= n <= 105
0 <= nums1[i], nums2[j] <= 109
0 <= k <= 105
"""

"""

https://leetcode.cn/circle/discuss/33ZnsL/

我们考虑每一个位置，差距只能减少 k 的倍数。同时，每次操作都不会改变 nums1 的和，
如果两个数组和不相等，则无法达成目标。接下来我们只需要计算减少某个位置的操作的个
数即可。

注意！要看数据范围！这题 kk 可以取 0，可能带来 modmod 0 之类的错误。
"""


class Solution:
    def minOperations(self, nums1: List[int], nums2: List[int], k: int) -> int:
        if sum(nums1) != sum(nums2):
            return -1
        cnt = 0
        for x, y in zip(nums1, nums2):
            tmp = x - y
            if tmp != 0:
                if k == 0:
                    return -1
                if tmp % k:
                    return -1
                if tmp > 0:
                    cnt += tmp // k
        return cnt
