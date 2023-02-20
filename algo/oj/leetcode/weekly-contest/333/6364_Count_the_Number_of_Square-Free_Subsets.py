"""

6364. Count the Number of Square-Free Subsets

You are given a positive integer 0-indexed array nums.

A subset of the array nums is square-free if the product of its elements is a square-free integer.

A square-free integer is an integer that is divisible by no square number other than 1.

Return the number of square-free non-empty subsets of the array nums. Since the answer may be too large, return it modulo 109 + 7.

A non-empty subset of nums is an array that can be obtained by deleting some (possibly none but not all) elements from nums. Two subsets are different if and only if the chosen indices to delete are different.



Example 1:

Input: nums = [3,4,4,5]
Output: 3
Explanation: There are 3 square-free subsets in this example:
- The subset consisting of the 0th element [3]. The product of its elements is 3, which is a square-free integer.
- The subset consisting of the 3rd element [5]. The product of its elements is 5, which is a square-free integer.
- The subset consisting of 0th and 3rd elements [3,5]. The product of its elements is 15, which is a square-free integer.
It can be proven that there are no more than 3 square-free subsets in the given array.


Example 2:

Input: nums = [1]
Output: 1
Explanation: There is 1 square-free subset in this example:
- The subset consisting of the 0th element [1]. The product of its elements is 1, which is a square-free integer.
It can be proven that there is no more than 1 square-free subset in the given array.


Constraints:

1 <= nums.length <= 1000
1 <= nums[i] <= 30


################################################################

# TODO
# tag: dp

6364. 无平方子集计数

给你一个正整数数组 nums 。

如果数组 nums 的子集中的元素乘积是一个 无平方因子数 ，则认为该子集是一个 无平方 子集。

无平方因子数 是无法被除 1 之外任何平方数整除的数字。

返回数组 nums 中 无平方 且 非空 的子集数目。因为答案可能很大，返回对 109 + 7 取余的结果。

nums 的 非空子集 是可以由删除 nums 中一些元素（可以不删除，但不能全部删除）得到的一个数组。如果构成两个子集时选择删除的下标不同，则认为这两个子集不同。



示例 1：

输入：nums = [3,4,4,5]
输出：3
解释：示例中有 3 个无平方子集：
- 由第 0 个元素 [3] 组成的子集。其元素的乘积是 3 ，这是一个无平方因子数。
- 由第 3 个元素 [5] 组成的子集。其元素的乘积是 5 ，这是一个无平方因子数。
- 由第 0 个和第 3 个元素 [3,5] 组成的子集。其元素的乘积是 15 ，这是一个无平方因子数。
可以证明给定数组中不存在超过 3 个无平方子集。


示例 2：

输入：nums = [1]
输出：1
解释：示例中有 1 个无平方子集：
- 由第 0 个元素 [1] 组成的子集。其元素的乘积是 1 ，这是一个无平方因子数。
可以证明给定数组中不存在超过 1 个无平方子集。


提示：

1 <= nums.length <= 1000
1 <= nums[i] <= 30


"""

"""
"""

"""

作者：endlesscheng
链接：https://leetcode.cn/problems/count-the-number-of-square-free-subsets/solution/liang-chong-xie-fa-01bei-bao-zi-ji-zhuan-3ooi/
来源：力扣（LeetCode）
著作权归作者所有。商业转载请联系作者获得授权，非商业转载请注明出处。

1. 背包

把每个无平方因字数 NSQ，对应的质因子集合，表示成一个二进制数

枚举子集的元素乘积，把乘积看成是一个背包
它去装能够组成这个乘积的 NSQ


2. 状压的做法

"""


PRIMES = 2, 3, 5, 7, 11, 13, 17, 19, 23, 29
NSQ_TO_MASK = [0] * 31  # NSQ_TO_MASK[i] 为 i 对应的质数集合（用二进制表示）
for i in range(2, 31):
    for j, p in enumerate(PRIMES):
        if i % p == 0:
            if i % (p * p) == 0:  # 有平方因子
                NSQ_TO_MASK[i] = -1
                break
            NSQ_TO_MASK[i] |= 1 << j  # 把 j 加到集合中

class Solution:
    def squareFreeSubsets(self, nums: List[int]) -> int:
        MOD = 10 ** 9 + 7
        M = 1 << len(PRIMES)
        f = [0] * M  # f[j] 表示恰好组成集合 j 的方案数
        f[0] = 1  # 空集的方案数为 1
        for x in nums:
            mask = NSQ_TO_MASK[x]
            if mask >= 0:  # x 是 NSQ
                for j in range(M - 1, mask - 1, -1):
                    if (j | mask) == j:  # mask 是 j 的子集
                        f[j] = (f[j] + f[j ^ mask]) % MOD  # 不选 mask + 选 mask
        return (sum(f) - 1) % MOD  # -1 去掉空集
